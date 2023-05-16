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
import lbforaging
import gym
import os

from a2c import A2C
from wrappers import RecordEpisodeStatistics, TimeLimit
import time

def convertToHighLevel(obs, n_obs, actions,oldStateNumberStr):
    #Rules defined to convery low-level states to states with highlevel featuress
    numberOfAgents = 3
    numberOfVariables = 9
    failedAction = False

    oldStateNumber = []
    oldStateNumberStr = oldStateNumberStr.split(",")
    for i in oldStateNumberStr:
        if "True" in  i:
            oldStateNumber.append(True)
        else:
            oldStateNumber.append(False)
    newStateNumber = [False] * numberOfVariables

    VictimRow = 1
    VictimCol = 4
    FireRow = 4
    FireCol = 0
    RubbleRow = 3
    RubbleCol = 4

    wallsNoNorth = []
    wallsNoSouth = []
    wallsNoEast = []
    wallsNoWest = []

    if numberOfAgents == 3:
        #Agent Labels
        n_obsAgent1Row = n_obs[9]
        n_obsAgent1Col = n_obs[10]
        n_obsAgent2Row = n_obs[12]
        n_obsAgent2Col = n_obs[13]
        n_obsAgent3Row = n_obs[15]
        n_obsAgent3Col = n_obs[16]

    counter = 0

    #Fire - Agent 1
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent1Row+1) == FireRow and n_obsAgent1Col == FireCol and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoSouth) or ((n_obsAgent1Row-1) == FireRow and n_obsAgent1Col == FireCol and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoNorth) or ((n_obsAgent1Col+1) == FireCol and n_obsAgent1Row == FireRow and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoEast) or ((n_obsAgent1Col-1) == FireCol and n_obsAgent1Row == FireRow and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoWest):
        if actions[0] == 5:
            if((obs[0] == FireRow and obs[1] == FireCol) or (obs[3] == FireRow and obs[4] == FireCol) or (obs[6] == FireRow and obs[7] == FireCol)):
                if((n_obs[0] != FireRow or n_obs[1] != FireCol) and (n_obs[3] != FireRow or n_obs[4] != FireCol) and (n_obs[6] != FireRow or n_obs[7] != FireCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Rubble - Agent 1
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent1Row+1) == RubbleRow and n_obsAgent1Col == RubbleCol and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoSouth) or ((n_obsAgent1Row-1) == RubbleRow and n_obsAgent1Col == RubbleCol and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoNorth) or ((n_obsAgent1Col+1) == RubbleCol and n_obsAgent1Row == RubbleRow and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoEast) or ((n_obsAgent1Col-1) == RubbleCol and n_obsAgent1Row == RubbleRow and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoWest):
        if actions[0] == 5:
            if((obs[0] == RubbleRow and obs[1] == RubbleCol) or (obs[3] == RubbleRow and obs[4] == RubbleCol) or (obs[6] == RubbleRow and obs[7] == RubbleCol)):
                if((n_obs[0] != RubbleRow or n_obs[1] != RubbleCol) and (n_obs[3] != RubbleRow or n_obs[4] != RubbleCol) and (n_obs[6] != RubbleRow or n_obs[7] != RubbleCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Vic  - Agent 1
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent1Row+1) == VictimRow and n_obsAgent1Col == VictimCol and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoSouth) or ((n_obsAgent1Row-1) == VictimRow and n_obsAgent1Col == VictimCol and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoNorth) or ((n_obsAgent1Col+1) == VictimCol and n_obsAgent1Row == VictimRow and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoEast) or ((n_obsAgent1Col-1) == VictimCol and n_obsAgent1Row == VictimRow and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoWest):
        if actions[0] == 5:
            if((obs[0] == VictimRow and obs[1] == VictimCol) or (n_obs[3] == VictimRow and obs[4] == VictimCol) or (obs[6] == VictimRow and obs[7] == VictimCol)):
                if((n_obs[0] != VictimRow or n_obs[1] != VictimCol) and (n_obs[3] != VictimRow or n_obs[4] != VictimCol) and (n_obs[6] != VictimRow or n_obs[7] != VictimCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Fire - Agent 2
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent2Row+1) == FireRow and n_obsAgent2Col == FireCol and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoSouth) or ((n_obsAgent2Row-1) == FireRow and n_obsAgent2Col == FireCol and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoNorth) or ((n_obsAgent2Col+1) == FireCol and n_obsAgent2Row == FireRow and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoEast) or ((n_obsAgent2Col-1) == FireCol and n_obsAgent2Row == FireRow and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoWest):
       if actions[1] == 5:
        if((obs[0] == FireRow and obs[1] == FireCol) or (obs[3] == FireRow and obs[4] == FireCol) or (obs[6] == FireRow and obs[7] == FireCol)):
            if((n_obs[0] != FireRow or n_obs[1] != FireCol) and (n_obs[3] != FireRow or n_obs[4] != FireCol) and (n_obs[6] != FireRow or n_obs[7] != FireCol)):
                newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Rubble - Agent 2
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent2Row+1) == RubbleRow and n_obsAgent2Col == RubbleCol and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoSouth) or ((n_obsAgent2Row-1) == RubbleRow and n_obsAgent2Col == RubbleCol and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoNorth) or ((n_obsAgent2Col+1) == RubbleCol and n_obsAgent2Row == RubbleRow and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoEast) or ((n_obsAgent2Col-1) == RubbleCol and n_obsAgent2Row == RubbleRow and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoWest):
        if actions[1] == 5:
            if((obs[0] == RubbleRow and obs[1] == RubbleCol) or (obs[3] == RubbleRow and obs[4] == RubbleCol) or (obs[6] == RubbleRow and obs[7] == RubbleCol)):
                if((n_obs[0] != RubbleRow or n_obs[1] != RubbleCol) and (n_obs[3] != RubbleRow or n_obs[4] != RubbleCol) and (n_obs[6] != RubbleRow or n_obs[7] != RubbleCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Vic  - Agent 2
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent2Row+1) == VictimRow and n_obsAgent2Col == VictimCol and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoSouth) or ((n_obsAgent2Row-1) == VictimRow and n_obsAgent2Col == VictimCol and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoNorth) or ((n_obsAgent2Col+1) == VictimCol and n_obsAgent2Row == VictimRow and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoEast) or ((n_obsAgent2Col-1) == VictimCol and n_obsAgent2Row == VictimRow and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoWest):
        if actions[1] == 5:
            if((obs[0] == VictimRow and obs[1] == VictimCol) or (n_obs[3] == VictimRow and obs[4] == VictimCol) or (obs[6] == VictimRow and obs[7] == VictimCol)):
                if((n_obs[0] != VictimRow or n_obs[1] != VictimCol) and (n_obs[3] != VictimRow or n_obs[4] != VictimCol) and (n_obs[6] != VictimRow or n_obs[7] != VictimCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Fire - Agent 3
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent3Row+1) == FireRow and n_obsAgent3Col == FireCol and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoSouth) or ((n_obsAgent3Row-1) == FireRow and n_obsAgent3Col == FireCol and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoNorth) or ((n_obsAgent3Col+1) == FireCol and n_obsAgent3Row == FireRow and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoEast) or ((n_obsAgent3Col-1) == FireCol and n_obsAgent3Row == FireRow and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoWest):
        if actions[2] == 5:
            if((obs[0] == FireRow and obs[1] == FireCol) or (obs[3] == FireRow and obs[4] == FireCol) or (obs[6] == FireRow and obs[7] == FireCol)):
                if((n_obs[0] != FireRow or n_obs[1] != FireCol) and (n_obs[3] != FireRow or n_obs[4] != FireCol) and (n_obs[6] != FireRow or n_obs[7] != FireCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Rubble - Agent 3
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent3Row+1) == RubbleRow and n_obsAgent3Col == RubbleCol and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoSouth) or ((n_obsAgent3Row-1) == RubbleRow and n_obsAgent3Col == RubbleCol and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoNorth) or ((n_obsAgent3Col+1) == RubbleCol and n_obsAgent3Row == RubbleRow and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoEast) or ((n_obsAgent3Col-1) == RubbleCol and n_obsAgent3Row == RubbleRow and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoWest):
        if actions[2] == 5:
            if((obs[0] == RubbleRow and obs[1] == RubbleCol) or (obs[3] == RubbleRow and obs[4] == RubbleCol) or (obs[6] == RubbleRow and obs[7] == RubbleCol)):
                if((n_obs[0] != RubbleRow or n_obs[1] != RubbleCol) and (n_obs[3] != RubbleRow or n_obs[4] != RubbleCol) and (n_obs[6] != RubbleRow or n_obs[7] != RubbleCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Vic  - Agent 3
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent3Row+1) == VictimRow and n_obsAgent3Col == VictimCol and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoSouth) or ((n_obsAgent3Row-1) == VictimRow and n_obsAgent3Col == VictimCol and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoNorth) or ((n_obsAgent3Col+1) == VictimCol and n_obsAgent3Row == VictimRow and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoEast) or ((n_obsAgent3Col-1) == VictimCol and n_obsAgent3Row == VictimRow and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoWest):
        if actions[2] == 5:
            if((obs[0] == VictimRow and obs[1] == VictimCol) or (n_obs[3] == VictimRow and obs[4] == VictimCol) or (obs[6] == VictimRow and obs[7] == VictimCol)):
                if((n_obs[0] != VictimRow or n_obs[1] != VictimCol) and (n_obs[3] != VictimRow or n_obs[4] != VictimCol) and (n_obs[6] != VictimRow or n_obs[7] != VictimCol)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1


    oldStateNumber =  str(oldStateNumber).replace(" ","")
    newStateNumber = str(newStateNumber).replace(" ","")

    return newStateNumber, oldStateNumber, failedAction

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

def updateHighToLow(newStateNumber, oldStateNumber,obs,n_obs,highToLowConversions):
    if (newStateNumber,oldStateNumber) not in highToLowConversions.keys():
        highToLowConversions[(newStateNumber,oldStateNumber)] = list(n_obs)
    return highToLowConversions


def main():
    stateList = []
    transitionList = {}
    highToLowConversions = {}

    path = "results/trained_models/398/u66000"
    env_name = "Foraging-6x6-3p-3f-v2"
    time_limit = 500 #Based on domain

    RUN_STEPS = 100 #Based on domain

    env = gym.make(env_name)
    env = TimeLimit(env, time_limit)
    env = RecordEpisodeStatistics(env)

    agents = [
        A2C(i, osp, asp, 0.1, 0.1, False, 1, 1, "cpu")
        for i, (osp, asp) in enumerate(zip(env.observation_space, env.action_space))
    ]

    for agent in agents:
        agent.restore(path + f"/agent{agent.agent_id}")

    modelStartState = [4,0,2,1,4,2,3,4,2,0,3,1,0,4,1,0,5,1]  #x,y,level
    actions = [0,0,0]
    oldStateNumber = str([False]*9)
    newStateNumber = str([False]*9)
    highToLowConversions[(newStateNumber,oldStateNumber)] = modelStartState

    if os.path.exists("currentStartState.txt"):
        os.remove("currentStartState.txt")
        f = open("currentStartState.txt", "w")
        f.write(str(modelStartState))
        f.close()
    obs = env.reset()


    for i in range(RUN_STEPS):
        obs = [torch.from_numpy(o) for o in obs]
        _, actions, _ , _ = zip(*[agent.model.act(obs[agent.agent_id], None, None) for agent in agents])  #Make sure to change the model,distribution,and enviroment file if needed
        actions = [a.item() for a in actions]
        n_obs, reward, done, info = env.step(actions)
        newStateNumber, oldStateNumber, _ = convertToHighLevel(obs[0],n_obs[0],actions,oldStateNumber)
        stateList, transitionList = addToLists(stateList, transitionList, newStateNumber, oldStateNumber)
        highToLowConversions = updateHighToLow(newStateNumber, oldStateNumber,obs[0],n_obs[0],highToLowConversions)
        obs = n_obs
        oldStateNumber = newStateNumber
        if all(done):
            obs = env.reset()
            oldStateNumber = str([False]*9)
            newStateNumber = str([False]*9)
            print("--- Episode Finished ---")
            print(f"Episode rewards: {sum(info['episode_reward'])}")
            print(info)
            print(" --- ")

        #Write or copy/paste to correct files if hooking directly to pipeline
        f = open("RE_conrollStates.py", "w") #States collected for abstract model
        f.write("stateList=")
        f.write(str(stateList))
        f.close()
        f = open("RE_conrollTrans.py", "w") #Transitions collected for abstract model
        f.write("transitions=")
        f.write(str(transitionList))
        f.close()
        f = open("RE_conrollHighLow.py", "w") #Conversions collect for abstract model
        f.write("highToLow=")
        f.write(str(highToLowConversions))
        f.close()


main()
