#Runs an evalution of the given policy
#Adapted from
#[Christianos et al., 2020] Filippos Christianos, Lukas697
#Sch ̈afer, and Stefano V Albrecht. Shared experience698
#actor-critic for multi-agent reinforcement learning. In699
#Thirty-fourth Conference on Neural Information Process-700
#ing Systems, pages 10707–10717. Curran Associates Inc,701
#2020
#Orginal code location: https://github.com/semitable/seac

import torch
import robotic_warehouse
import gym
import os
import RWARE_convertStates

from a2c import A2C
from wrappers import RecordEpisodeStatistics, TimeLimit

import RWARE_convertStates
import time

holdingshelfs = ""
n_holdingshelfs = ""
deliveredshelfs = ""
n_deliveredshelfs = ""

TargetStates = {"deliver_shelf4":[],"deliver_shelf3":[],"deliver_shelf2":[],"deliver_shelf1":[],
"pickup_shelf4":[],"pickup_shelf3":[],"pickup_shelf2":[],"pickup_shelf1":[]}

def convertToHighLevel(obs, n_obs, actions, shelfs,numAgents,env_name,numTasks,newStateNumber):
    numVariables = 0
    global holdingshelfs
    global deliveredshelfs
    global TargetStates

    oldStateNumber, newStateNumber, failedAction, holdingshelfs, deliveredshelfs, TargetStates = RWARE_convertStates.generateTransitions(obs,n_obs,numVariables,numTasks,numAgents,env_name,shelfs,actions,holdingshelfs, deliveredshelfs, TargetStates,newStateNumber)

    return oldStateNumber, newStateNumber, failedAction, n_holdingshelfs, n_deliveredshelfs, TargetStates

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

def updateHighToLow(newStateNumber, oldStateNumber,obs,n_obs,highToLowConversions, numberOfAgents):
    if (newStateNumber,oldStateNumber) not in highToLowConversions.keys():
        newState = []
        for i in range(0,numberOfAgents):
            newState = newState + list(n_obs[i])
        highToLowConversions[(newStateNumber,oldStateNumber)] = str(newState) + '*' + str(oldStateNumber)
    return highToLowConversions


def main():
    start = time.time()
    stateList = []
    transitionList = {}
    highToLowConversions = {}

    path = "results/trained_models/479/u213000"
    env_name = "rware-tiny-2ag-easy-v1"
    numAgents = 2
    numTasks = 4
    numVariables = 0
    time_limit = 500 # 25 for LBF

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

    #EDIT HERE
    modelStartState = [0.0, 4.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 6.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    newStateNumber = [False] * (numAgents * numTasks + numAgents * numTasks + numAgents + numTasks + numTasks*numAgents)
    if os.path.exists("currentStartStateRWARE.txt"):
        os.remove("currentStartStateRWARE.txt")
        f = open("currentStartStateRWARE.txt", "w")
        f.write(str(modelStartState) + "*" + str(newStateNumber))
        f.close()

    obs = env.reset()
    if numAgents == 2:
        modelStartState = list(obs[0]) + list(obs[1])
    if numAgents == 3:
        modelStartState = list(obs[0]) + list(obs[1]) + list(obs[2])
    if numAgents == 4:
        modelStartState = list(obs[0]) + list(obs[1]) + list(obs[2]) + list(obs[3])
    actions = [0] * numAgents

    f = open("request_queue.txt", "r")
    shelfs = f.read()
    shelfs = shelfs.split("-")
    f.close()

    oldStateNumber, newStateNumber, failedAction, holdingshelfs, deliveredshelfs, TargetStates = convertToHighLevel(obs,obs,actions,shelfs,numAgents,env_name,numTasks,newStateNumber)
    highToLowConversions[(newStateNumber,oldStateNumber)] = modelStartState


    for i in range(RUN_STEPS):
        obs = [torch.from_numpy(o) for o in obs]
        _, actions, _ , _ = zip(*[agent.model.act(obs[agent.agent_id], None, None) for agent in agents])  #Make sure to change the model File
        actions = [a.item() for a in actions]
        n_obs, reward, done, info = env.step(actions)
        oldStateNumber, newStateNumber, failedAction, holdingshelfs, deliveredshelfs, TargetStates = convertToHighLevel(obs, n_obs, actions, shelfs, numAgents, env_name ,numTasks,newStateNumber)
        stateList, transitionList = addToLists(stateList, transitionList, newStateNumber, oldStateNumber)
        highToLowConversions = updateHighToLow(newStateNumber, oldStateNumber,obs,n_obs,highToLowConversions,numAgents)
        obs = n_obs
        if all(done):
            print(i)
            print("ALL DONE")
            obs = env.reset()
            print("--- Episode Finished ---")
            print(f"Episode rewards: {sum(info['episode_reward'])}")
            print(info)
            print(" --- ")
    f = open("RWARE_conrollStates.py", "w")
    f.write("stateList=")
    f.write(str(stateList))
    f.close()
    f = open("RWARE_conrollTrans.py", "w")
    f.write("transitions=")
    f.write(str(transitionList))
    f.close()
    f = open("RWARE_conrollHighLow.py", "w")
    f.write("highToLow=")
    f.write(str(highToLowConversions))
    f.close()
            #Write or copy/paste to correct files if hooking directly to pipeline


main()
