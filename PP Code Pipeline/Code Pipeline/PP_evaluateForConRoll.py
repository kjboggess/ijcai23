#Runs an evalution of the given policy
#Adapted from
#[Christianos et al., 2020] Filippos Christianos, Lukas
#Sch ̈afer, and Stefano V Albrecht. Shared experience
#actor-critic for multi-agent reinforcement learning. In
#Thirty-fourth Conference on Neural Information Process-
#ing Systems, pages 10707–10717. Curran Associates Inc,
#2020
#Orginal code location: https://github.com/semitable/seac

import torch
import gym
import os

from a2c import A2C
from wrappers import RecordEpisodeStatistics, TimeLimit

import PP_convertStates
import pressureplate

import time

nonTargetStates = {"plate1":[], "plate2":[], "plate3":[], "plate4":[],"goal":[]}
TargetStates = {"plate1":[], "plate2":[], "plate3":[], "plate4":[], "goal":[]}

def convertToHighLevel(obs, n_obs, actions, plates,numAgents,env_name,numTasks,newStateNumber):
    numVariables = 0
    global nonTargetStates
    global TargetStates

    oldStateNumber, newStateNumber, failedAction, nonTargetStates, TargetStates = PP_convertStates.generateTransitions(obs,n_obs,numVariables,numTasks,numAgents,env_name,plates,actions, nonTargetStates, TargetStates,newStateNumber)

    return oldStateNumber, newStateNumber, failedAction, nonTargetStates, TargetStates

def addToLists(stateList, transitionList, newStateNumber, oldStateNumber):
    if newStateNumber not in stateList:
        stateList.append(newStateNumber)
    if oldStateNumber not in stateList:
        stateList.append(oldStateNumber)

    if oldStateNumber not in transitionList.keys():
        transitionList[oldStateNumber] = [[newStateNumber,1,1,1]]
    else:
        foundTransition = False
        currentTransitions = transitionList[oldStateNumber]
        for i in currentTransitions:
            i[2] = i[2] + 1
            if i[0] == newStateNumber:
                i[1] = i[1] + 1
                foundTransition = True
        if foundTransition == False:
            totalTrans = transitionList[oldStateNumber][0][2]
            transitionList[oldStateNumber].append([newStateNumber,1,totalTrans,1])

    return stateList, transitionList

def updateHighToLow(newStateNumber, oldStateNumber,obs,n_obs,highToLowConversions,numAgents):
    if (newStateNumber,oldStateNumber) not in highToLowConversions.keys():
        newState = []
        for i in range(0,numAgents):
            newState = newState + list(n_obs[i])
        highToLowConversions[(newStateNumber,oldStateNumber)] = newState
    return highToLowConversions


def main():
    start = time.time()
    stateList = []
    transitionList = {}
    highToLowConversions = {}

    path = "results/trained_models/462/u1000"
    env_name = "pressureplate-linear-4p-v0"
    numAgents = 9
    numTasks = 5
    numVariables = 0
    time_limit = 500 # 25 for LBF

    plates = [[2, 13],[7, 13],[2, 9],[7, 9],[7, 5],[2, 5],[8, 6],[1, 6],[3, 1]]

    RUN_STEPS = 10000

    env = gym.make(env_name)
    env = TimeLimit(env, time_limit)
    env = RecordEpisodeStatistics(env)

    agents = [
        A2C(i, osp, asp, 0.1, 0.1, False, 1, 1, "cpu")
        for i, (osp, asp) in enumerate(zip(env.observation_space, env.action_space))
    ]

    for agent in agents:
        agent.restore(path + f"/agent{agent.agent_id}")


    obs = env.reset()
    newStateNumber = [False] * numAgents * numTasks
    if numAgents == 9:
         modelStartState = list(obs[0]) + list(obs[1]) + list(obs[2]) + list(obs[3]) + list(obs[4]) + list(obs[5]) + list(obs[6]) + list(obs[7]) + list(obs[8])
    actions = [0] * numAgents

    if os.path.exists("currentStartStatePP.txt"):
        os.remove("currentStartStatePP.txt")
        f = open("currentStartStatePP.txt", "w")
        f.write(str(modelStartState))
        f.close()


    oldStateNumber, newStateNumber, failedAction, nonTargetStates, TargetStates = convertToHighLevel(obs,obs,actions,plates,numAgents,env_name,numTasks,newStateNumber)
    highToLowConversions[(newStateNumber,oldStateNumber)] = modelStartState


    for i in range(RUN_STEPS):
        obs = [torch.from_numpy(o) for o in obs]
        _, actions, _ , _ = zip(*[agent.model.act(obs[agent.agent_id], None, None) for agent in agents])  #Make sure to change the model File
        actions = [a.item() for a in actions]
        n_obs, reward, done, info = env.step(actions)
        oldStateNumber, newStateNumber, failedAction, nonTargetStates, TargetStates = convertToHighLevel(obs, n_obs, actions, plates, numAgents, env_name ,numTasks,newStateNumber)
        if newStateNumber != [False] * numAgents * numTasks:
            stateList, transitionList = addToLists(stateList, transitionList, newStateNumber, oldStateNumber)
        if newStateNumber != oldStateNumber:
            highToLowConversions = updateHighToLow(newStateNumber, oldStateNumber,obs,n_obs,highToLowConversions, numAgents)
        obs = n_obs

        if all(done):
            print("ALL DONE")
            obs = env.reset()
            newStateNumber = [False] * numAgents * numTasks
            print("--- Episode Finished ---")
            print(f"Episode rewards: {sum(info['episode_reward'])}")
            print(info)
            print(" --- ")
            RUN_STEPS = 0

    f = open("PP_conrollStates.py", "w")
    f.write("stateList=")
    f.write(str(stateList))
    f.close()
    f = open("PP_conrollTrans.py", "w")
    f.write("transitions=")
    f.write(str(transitionList))
    f.close()
    f = open("PP_conrollHighLow.py", "w")
    f.write("highToLow=")
    f.write(str(highToLowConversions))
    f.close()
    end = time.time()


            #Write or copy/paste to correct files if hooking directly to pipeline


main()
