from re import L
from sys import maxsize
from xmlrpc.client import Unmarshaller
import torch
import lbforaging
import gym

from a2c import A2C
from wrappers import RecordEpisodeStatistics, TimeLimit

import RE_conrollStates
import RE_conrollTrans
import RE_conrollHighLow
import RE_abstractToPrism
import RE_generateExplanations
import queue
import itertools
import os
import time
import random
import math
import numpy
import RE_generateNotPossExp_3agTotalQ

#GLOBAL VARIABLES
stateList = []
transitions = {}
UMNumber = {}
currentStart = []

TargetStates = {"apple1":[],"apple3":[],"apple2":[]}

def convertToHighLevel(obs, n_obs, actions,oldStateNumberStr):
    #Rules defined to convery low-level states to states with highlevel features
    global TargetStates
    numberOfAgents = 3
    numberOfVariables = 9

    oldStateNumber = []
    oldStateNumberStr = oldStateNumberStr.split(",")
    for i in oldStateNumberStr:
        if "True" in  i:
            oldStateNumber.append(True)
        else:
            oldStateNumber.append(False)
    newStateNumber = [False] * numberOfVariables

    #Grid labels
    Apple1Row = 2
    Apple1Col = 0
    Apple2Row = 3
    Apple2Col = 5
    Apple3Row = 4
    Apple3Col = 1

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

    #Apple2 - Agent 1
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent1Row+1) == Apple2Row and n_obsAgent1Col == Apple2Col and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoSouth) or ((n_obsAgent1Row-1) == Apple2Row and n_obsAgent1Col == Apple2Col and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoNorth) or ((n_obsAgent1Col+1) == Apple2Col and n_obsAgent1Row == Apple2Row and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoEast) or ((n_obsAgent1Col-1) == Apple2Col and n_obsAgent1Row == Apple2Row and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoWest):
        if actions[0] == 5:
            if((obs[0] == Apple2Row and obs[1] == Apple2Col) or (obs[3] == Apple2Row and obs[4] == Apple2Col) or (obs[6] == Apple2Row and obs[7] == Apple2Col)):
                if((n_obs[0] != Apple2Row or n_obs[1] != Apple2Col) and (n_obs[3] != Apple2Row or n_obs[4] != Apple2Col) and (n_obs[6] != Apple2Row or n_obs[7] != Apple2Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Rubble - Agent 1
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent1Row+1) == Apple3Row and n_obsAgent1Col == Apple3Col and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoSouth) or ((n_obsAgent1Row-1) == Apple3Row and n_obsAgent1Col == Apple3Col and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoNorth) or ((n_obsAgent1Col+1) == Apple3Col and n_obsAgent1Row == Apple3Row and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoEast) or ((n_obsAgent1Col-1) == Apple3Col and n_obsAgent1Row == Apple3Row and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoWest):
        if actions[0] == 5:
            if((obs[0] == Apple3Row and obs[1] == Apple3Col) or (obs[3] == Apple3Row and obs[4] == Apple3Col) or (obs[6] == Apple3Row and obs[7] == Apple3Col)):
                if((n_obs[0] != Apple3Row or n_obs[1] != Apple3Col) and (n_obs[3] != Apple3Row or n_obs[4] != Apple3Col) and (n_obs[6] != Apple3Row or n_obs[7] != Apple3Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Vic  - Agent 1
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent1Row+1) == Apple1Row and n_obsAgent1Col == Apple1Col and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoSouth) or ((n_obsAgent1Row-1) == Apple1Row and n_obsAgent1Col == Apple1Col and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoNorth) or ((n_obsAgent1Col+1) == Apple1Col and n_obsAgent1Row == Apple1Row and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoEast) or ((n_obsAgent1Col-1) == Apple1Col and n_obsAgent1Row == Apple1Row and (n_obsAgent1Row,n_obsAgent1Col) not in wallsNoWest):
        if actions[0] == 5:
            if((obs[0] == Apple1Row and obs[1] == Apple1Col) or (n_obs[3] == Apple1Row and obs[4] == Apple1Col) or (obs[6] == Apple1Row and obs[7] == Apple1Col)):
                if((n_obs[0] != Apple1Row or n_obs[1] != Apple1Col) and (n_obs[3] != Apple1Row or n_obs[4] != Apple1Col) and (n_obs[6] != Apple1Row or n_obs[7] != Apple1Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Apple2 - Agent 2
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent2Row+1) == Apple2Row and n_obsAgent2Col == Apple2Col and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoSouth) or ((n_obsAgent2Row-1) == Apple2Row and n_obsAgent2Col == Apple2Col and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoNorth) or ((n_obsAgent2Col+1) == Apple2Col and n_obsAgent2Row == Apple2Row and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoEast) or ((n_obsAgent2Col-1) == Apple2Col and n_obsAgent2Row == Apple2Row and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoWest):
       if actions[1] == 5:
        if((obs[0] == Apple2Row and obs[1] == Apple2Col) or (obs[3] == Apple2Row and obs[4] == Apple2Col) or (obs[6] == Apple2Row and obs[7] == Apple2Col)):
            if((n_obs[0] != Apple2Row or n_obs[1] != Apple2Col) and (n_obs[3] != Apple2Row or n_obs[4] != Apple2Col) and (n_obs[6] != Apple2Row or n_obs[7] != Apple2Col)):
                newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Rubble - Agent 2
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent2Row+1) == Apple3Row and n_obsAgent2Col == Apple3Col and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoSouth) or ((n_obsAgent2Row-1) == Apple3Row and n_obsAgent2Col == Apple3Col and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoNorth) or ((n_obsAgent2Col+1) == Apple3Col and n_obsAgent2Row == Apple3Row and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoEast) or ((n_obsAgent2Col-1) == Apple3Col and n_obsAgent2Row == Apple3Row and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoWest):
        if actions[1] == 5:
            if((obs[0] == Apple3Row and obs[1] == Apple3Col) or (obs[3] == Apple3Row and obs[4] == Apple3Col) or (obs[6] == Apple3Row and obs[7] == Apple3Col)):
                if((n_obs[0] != Apple3Row or n_obs[1] != Apple3Col) and (n_obs[3] != Apple3Row or n_obs[4] != Apple3Col) and (n_obs[6] != Apple3Row or n_obs[7] != Apple3Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Vic  - Agent 2
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent2Row+1) == Apple1Row and n_obsAgent2Col == Apple1Col and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoSouth) or ((n_obsAgent2Row-1) == Apple1Row and n_obsAgent2Col == Apple1Col and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoNorth) or ((n_obsAgent2Col+1) == Apple1Col and n_obsAgent2Row == Apple1Row and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoEast) or ((n_obsAgent2Col-1) == Apple1Col and n_obsAgent2Row == Apple1Row and (n_obsAgent2Row,n_obsAgent2Col) not in wallsNoWest):
        if actions[1] == 5:
            if((obs[0] == Apple1Row and obs[1] == Apple1Col) or (n_obs[3] == Apple1Row and obs[4] == Apple1Col) or (obs[6] == Apple1Row and obs[7] == Apple1Col)):
                if((n_obs[0] != Apple1Row or n_obs[1] != Apple1Col) and (n_obs[3] != Apple1Row or n_obs[4] != Apple1Col) and (n_obs[6] != Apple1Row or n_obs[7] != Apple1Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Apple2 - Agent 3
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent3Row+1) == Apple2Row and n_obsAgent3Col == Apple2Col and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoSouth) or ((n_obsAgent3Row-1) == Apple2Row and n_obsAgent3Col == Apple2Col and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoNorth) or ((n_obsAgent3Col+1) == Apple2Col and n_obsAgent3Row == Apple2Row and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoEast) or ((n_obsAgent3Col-1) == Apple2Col and n_obsAgent3Row == Apple2Row and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoWest):
        if actions[2] == 5:
            if((obs[0] == Apple2Row and obs[1] == Apple2Col) or (obs[3] == Apple2Row and obs[4] == Apple2Col) or (obs[6] == Apple2Row and obs[7] == Apple2Col)):
                if((n_obs[0] != Apple2Row or n_obs[1] != Apple2Col) and (n_obs[3] != Apple2Row or n_obs[4] != Apple2Col) and (n_obs[6] != Apple2Row or n_obs[7] != Apple2Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Rubble - Agent 3
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent3Row+1) == Apple3Row and n_obsAgent3Col == Apple3Col and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoSouth) or ((n_obsAgent3Row-1) == Apple3Row and n_obsAgent3Col == Apple3Col and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoNorth) or ((n_obsAgent3Col+1) == Apple3Col and n_obsAgent3Row == Apple3Row and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoEast) or ((n_obsAgent3Col-1) == Apple3Col and n_obsAgent3Row == Apple3Row and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoWest):
        if actions[2] == 5:
            if((obs[0] == Apple3Row and obs[1] == Apple3Col) or (obs[3] == Apple3Row and obs[4] == Apple3Col) or (obs[6] == Apple3Row and obs[7] == Apple3Col)):
                if((n_obs[0] != Apple3Row or n_obs[1] != Apple3Col) and (n_obs[3] != Apple3Row or n_obs[4] != Apple3Col) and (n_obs[6] != Apple3Row or n_obs[7] != Apple3Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Vic  - Agent 3
    if oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif((n_obsAgent3Row+1) == Apple1Row and n_obsAgent3Col == Apple1Col and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoSouth) or ((n_obsAgent3Row-1) == Apple1Row and n_obsAgent3Col == Apple1Col and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoNorth) or ((n_obsAgent3Col+1) == Apple1Col and n_obsAgent3Row == Apple1Row and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoEast) or ((n_obsAgent3Col-1) == Apple1Col and n_obsAgent3Row == Apple1Row and (n_obsAgent3Row,n_obsAgent3Col) not in wallsNoWest):
        if actions[2] == 5:
            if((obs[0] == Apple1Row and obs[1] == Apple1Col) or (n_obs[3] == Apple1Row and obs[4] == Apple1Col) or (obs[6] == Apple1Row and obs[7] == Apple1Col)):
                if((n_obs[0] != Apple1Row or n_obs[1] != Apple1Col) and (n_obs[3] != Apple1Row or n_obs[4] != Apple1Col) and (n_obs[6] != Apple1Row or n_obs[7] != Apple1Col)):
                    newStateNumber[counter] = True
    else: newStateNumber[counter] = False
    counter = counter + 1

    #Apple2 Complete
    if numberOfAgents == 3:
        if (newStateNumber[0] == True) or (newStateNumber[3] == True) or (newStateNumber[6] == True):
            if str(newStateNumber).replace(" ","") not in TargetStates["apple2"]:
                TargetStates["apple2"].append(str(newStateNumber).replace(" ",""))

    #Apple3 Complete
    if numberOfAgents == 3:
        if (newStateNumber[1] == True) or (newStateNumber[4] == True) or (newStateNumber[7] == True):
            if str(newStateNumber).replace(" ","") not in TargetStates["apple3"]:
                TargetStates["apple3"].append(str(newStateNumber).replace(" ",""))

    #Apple1 Complete
    if numberOfAgents == 3:
        if (newStateNumber[2] == True) or (newStateNumber[5] == True) or (newStateNumber[8] == True):
            if str(newStateNumber).replace(" ","") not in TargetStates["apple1"]:
                TargetStates["apple1"].append(str(newStateNumber).replace(" ",""))

    oldStateNumber =  str(oldStateNumber).replace(" ","")
    newStateNumber = str(newStateNumber).replace(" ","")

    return newStateNumber, oldStateNumber

def isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions):
    oldStateNumberSplit = oldStateNumber.split(",")
    newStateNumberSplit = newStateNumber.split(",")

    newUMNumber = 0
    completedNextTasks = [False] * numberOfAgents
    if newStateNumber != oldStateNumber:
        oldUMNumber = UMNumber[oldStateNumber]
        if oldUMNumber == float("-inf"):
            if newStateNumber in UMNumber.keys():
                return UMNumber[newStateNumber], UMNumber
            else:
                UMNumber[newStateNumber] = float("-inf")
                return float("-inf"), UMNumber

        tasksToDo = []
        for i in range(1,numberOfAgents+1):
            tasksToDo = tasksToDo + userQuery["agent"+str(i)][oldUMNumber:]

        for i in range(1,numberOfAgents+1):
            nextAgentTask = userQuery["agent"+str(i)][oldUMNumber]
            if numberOfAgents == 3:
                if nextAgentTask == "*":
                    if("False" in oldStateNumberSplit[3*i-3] and "True" in newStateNumberSplit[3*i-3]) or ("False" in oldStateNumberSplit[3*i-2] and "True" in newStateNumberSplit[3*i-2]) or ("False" in oldStateNumberSplit[3*i-1] and "True" in newStateNumberSplit[3*i-1]):
                        newUMNumber = float("-inf")
                    completedNextTasks[i-1] = True
                    tasksToDo.remove("*")

                if nextAgentTask == "apple2":
                    if("False" in oldStateNumberSplit[3*i-3] and "True" in newStateNumberSplit[3*i-3]):
                        completedNextTasks[i-1] = True
                        tasksToDo.remove("apple2")
                    elif("False" in oldStateNumberSplit[3*i-2] and "True" in newStateNumberSplit[3*i-2]) or ("False" in oldStateNumberSplit[3*i-1] and "True" in newStateNumberSplit[3*i-1]):
                        newUMNumber = float("-inf")

                elif nextAgentTask == "apple3":
                    if("False" in oldStateNumberSplit[3*i-2] and "True" in newStateNumberSplit[3*i-2]):
                        completedNextTasks[i-1] = True
                        tasksToDo.remove("apple3")
                    elif("False" in oldStateNumberSplit[3*i-3] and "True" in newStateNumberSplit[3*i-3]) or ("False" in oldStateNumberSplit[3*i-1] and "True" in newStateNumberSplit[3*i-1]):
                        newUMNumber = float("-inf")

                elif nextAgentTask == "apple1":
                    if("False" in oldStateNumberSplit[3*i-1] and "True" in newStateNumberSplit[3*i-1]):
                        completedNextTasks[i-1] = True
                        tasksToDo.remove("apple1")
                    elif("False" in oldStateNumberSplit[3*i-2] and "True" in newStateNumberSplit[3*i-2]) or ("False" in oldStateNumberSplit[3*i-3] and "True" in newStateNumberSplit[3*i-3]):
                        newUMNumber = float("-inf")

        if newUMNumber != float("-inf"):
            if False not in completedNextTasks:
                newUMNumber = oldUMNumber + 1
            else:
                newUMNumber = oldUMNumber

        if numberOfAgents == 3:
            if ("True" in newStateNumberSplit[0] or "True" in newStateNumberSplit[3] or "True" in newStateNumberSplit[6])  and "apple2" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[1] or "True" in newStateNumberSplit[4] or "True" in newStateNumberSplit[7]) and "apple3" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[2] or "True" in newStateNumberSplit[5] or "True" in newStateNumberSplit[8]) and "apple1" in tasksToDo:
                newUMNumber = float("-inf")
    else:
        newUMNumber = UMNumber[oldStateNumber]

    if newStateNumber in UMNumber.keys():
        if UMNumber[newStateNumber] <= newUMNumber:
            UMNumber[newStateNumber] = newUMNumber
    else:
        UMNumber[newStateNumber] = newUMNumber

    return newUMNumber, UMNumber


def addHighLevelStates(newStateNumber, oldStateNumber, stateList, transitions, highLevelStates, currentStep, actions, UMNumber, userQuery, numberOfAgents):
    transitionValue = float('inf')

    newUMNumber, UMNumber = isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions)

    if(oldStateNumber not in stateList):
        stateList.append(oldStateNumber)
    if(newStateNumber not in stateList):
        stateList.append(newStateNumber)

    if oldStateNumber in transitions.keys():
        foundTrans = False
        totalTrans = 0
        for new in transitions[oldStateNumber]:
            new[2] = new[2] + 1
            if new[0] == newStateNumber:
                new[1] = new[1] + 1
                foundTrans = True
                if transitionValue < new[3]:
                    new[3] = transitionValue
        if foundTrans == False:
            totalTrans = transitions[oldStateNumber][0][2]
            transitions[oldStateNumber].append([newStateNumber,1,totalTrans,transitionValue])
    else:
        transitions[oldStateNumber]=[[newStateNumber,1,1,transitionValue]]

    highLevelStates[oldStateNumber] = transitions[oldStateNumber]

    return(stateList, transitions, highLevelStates, newStateNumber, oldStateNumber, newUMNumber, UMNumber)


def generateComboActions(lowCurrentStart, env, agents):
    if os.path.exists("currentStartState.txt"):
        os.remove("currentStartState.txt")
    f = open("currentStartState.txt", "w")
    f.write(str(lowCurrentStart))
    f.close()

    obs = env.reset()
    obs = [torch.from_numpy(o) for o in obs]
    a, actions, b , c, newProbsIndex = zip(*[agent.model.act(obs[agent.agent_id], None, None) for agent in agents])
    for i in range(0,len(agents)):
        if 0 in newProbsIndex[i]:
            newProbsIndex[i].remove(0)  #Don't allow the agents to stop moving

    return newProbsIndex


def jointlowLevelScore(state, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks):
    agent_locations = []
    task_distance = 0
    query_distance = 0

    if currentTaskNumber == float("-inf"):
        return float("-inf")

    for i in range(1,numberOfAgents+1):
        agent_locations.append((state[-3*i],state[(-3*i)+1]))
        if "agent"+str(i) in userQuery.keys():
            if currentTaskNumber >= len(userQuery["agent"+str(i)]):
                nextTaskDistance = 0
            else:
                nextAgentTask = userQuery["agent"+str(i)][currentTaskNumber]
                if nextAgentTask == "*":
                    for j in range(currentTaskNumber, len(userQuery["agent"+str(i)])):
                        if userQuery["agent"+str(i)][j] != '*':
                            task_x_loc = task_locations[userQuery["agent"+str(i)][j]][0]
                            task_y_loc = task_locations[userQuery["agent"+str(i)][j]][1]
                            break
                        task_x_loc = state[-3*i]
                        task_y_loc = state[(-3*i)+1]
                else:
                    task_x_loc = task_locations[nextAgentTask][0]
                    task_y_loc = task_locations[nextAgentTask][1]
                nextTaskDistance = abs(state[-3*i] - task_x_loc) + abs(state[(-3*i)+1] - task_y_loc)
            query_distance = query_distance + nextTaskDistance

    for i in range(1,numberOfTasks+1):
            task_x_loc = state[(3*i)-3]
            task_y_loc = state[(3*i)-2]
            taskName = [i for i in task_locations.keys() if task_locations[i] == (task_x_loc,task_y_loc)]
            if state[(3*i)-1] != 0:
                for j in range(0,len(agent_locations)):
                    if "agent"+str(2-j+1) in userQuery.keys():
                        agentAssignedTasks = userQuery["agent"+str(2-j+1)]
                        if taskName[0] not in freeTasks and taskName[0] not in agentAssignedTasks:
                            current_distance = 10 - (abs(agent_locations[j][0] - task_x_loc) + abs(agent_locations[j][1] - task_y_loc))
                        else:
                            current_distance = abs(agent_locations[j][0] - task_x_loc) + abs(agent_locations[j][1] - task_y_loc)
                        task_distance = task_distance + current_distance

    score = task_distance + query_distance
    return score


def updateHighToLowConver(highToLowConver, oldStateNumber, newStateNumber, n_obs, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks):
    if (newStateNumber, oldStateNumber) in highToLowConver.keys():
        currentLowLevelStateScore = jointlowLevelScore(highToLowConver[(newStateNumber,oldStateNumber)], currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks)
        newStateScore = jointlowLevelScore(n_obs, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks)
        if newStateScore > currentLowLevelStateScore:
             highToLowConver[(newStateNumber,oldStateNumber)] = n_obs
    else:
        highToLowConver[(newStateNumber,oldStateNumber)] = n_obs

    return highToLowConver

def generateIntialUM(userQuery,transitions,numberOfAgents,startState):
    global TargetStates
    UMNumber = {}
    UMNumber[str(startState).replace(" ","")] = 0
    keyQueue = queue.Queue()
    keyQueue.put(str(startState).replace(" ",""))
    while keyQueue.empty() != True:
        i = keyQueue.get()
        if i in transitions.keys():
            for j in transitions[i]:
                if j[0] not in UMNumber.keys():
                    keyQueue.put(j[0])
                oldStateNumber = i
                oldStateNumberSplit = oldStateNumber.split(",")
                newStateNumber = j[0]
                newStateNumberSplit = newStateNumber.split(",")
                if numberOfAgents == 3:
                    actions = [0,0,0]
                    if oldStateNumberSplit != newStateNumberSplit:
                        if ("False" in oldStateNumberSplit[0] and "True" in newStateNumberSplit[0]) or ("False" in oldStateNumberSplit[1] and "True" in newStateNumberSplit[1]) or ("False" in oldStateNumberSplit[2] and "True" in newStateNumberSplit[2]):
                            actions[0] = 5
                        if ("False" in oldStateNumberSplit[3] and "True" in newStateNumberSplit[3]) or ("False" in oldStateNumberSplit[4] and "True" in newStateNumberSplit[4]) or ("False" in oldStateNumberSplit[5] and "True" in newStateNumberSplit[5]):
                            actions[1] = 5
                        if ("False" in oldStateNumberSplit[6] and "True" in newStateNumberSplit[6]) or ("False" in oldStateNumberSplit[7] and "True" in newStateNumberSplit[7]) or ("False" in oldStateNumberSplit[8] and "True" in newStateNumberSplit[8]):
                            actions[2] = 5
                newUMNumber, UMNumber = isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions)
                #Apple2 Complete
                if numberOfAgents == 3:
                    if ("False" in oldStateNumberSplit[0] and "True" in newStateNumberSplit[0]) or ("False" in oldStateNumberSplit[3] and "True" in newStateNumberSplit[3]) or ("False" in oldStateNumberSplit[6] and "True" in newStateNumberSplit[6]):
                        if str(newStateNumber).replace(" ","") not in TargetStates["apple2"]:
                            TargetStates["apple2"].append(str(newStateNumber).replace(" ",""))

                #Apple3 Complete
                if numberOfAgents == 3:
                    if ("False" in oldStateNumberSplit[1] and "True" in newStateNumberSplit[1]) or ("False" in oldStateNumberSplit[4] and "True" in newStateNumberSplit[4]) or ("False" in oldStateNumberSplit[7] and "True" in newStateNumberSplit[7]):
                        if str(newStateNumber).replace(" ","") not in TargetStates["apple3"]:
                            TargetStates["apple3"].append(str(newStateNumber).replace(" ",""))

                #Apple1 Complete
                if numberOfAgents == 3:
                    if ("False" in oldStateNumberSplit[2] and "True" in newStateNumberSplit[2]) or ("False" in oldStateNumberSplit[5] and "True" in newStateNumberSplit[5]) or ("False" in oldStateNumberSplit[8] and "True" in newStateNumberSplit[8]):
                        if str(newStateNumber).replace(" ","") not in TargetStates["apple1"]:
                            TargetStates["apple1"].append(str(newStateNumber).replace(" ",""))

    return UMNumber

def findBestActionRandom(possibleActions,lowCurrentStart,env,userQuery,numberOfAgents,stateList,transitions,highLevelStates,UMNumber):
    comboActions = list(itertools.product(*possibleActions))
    choice = random.choice(comboActions)
    obs = env.reset()
    n_obs, reward, done, info = env.step(choice)
    newStateNumber, oldStateNumber = convertToHighLevel(obs[0], n_obs[0], choice,currentStart)
    stateList, transitions, highLevelStates, newStateNumber, oldStateNumber, newUMNumber, UMNumber = addHighLevelStates(newStateNumber, oldStateNumber, stateList, transitions, highLevelStates, 0, choice, UMNumber, userQuery, numberOfAgents)
    return choice, UMNumber, stateList, transitions




def main():
    #---Make Enviroment---
    path = path = "results/trained_models/465/u15000"
    env_name = "Foraging-6x6-3p-3f-v2"

    time_limit = 500

    env = gym.make(env_name)
    env = TimeLimit(env, time_limit)
    env = RecordEpisodeStatistics(env)

    agents = [
        A2C(i, osp, asp, 0.1, 0.1, False, 1, 1, "cpu")
        for i, (osp, asp) in enumerate(zip(env.observation_space, env.action_space))
        ]

    for agent in agents:
        agent.restore(path + f"/agent{agent.agent_id}")

    #---Global Variables---
    global stateList
    global transitions
    global UMNumber
    global currentStart

    #---BackGround Info---
    numberOfAgents = 3
    numberOfTasks = 3
    task_locations = {"apple2":(3,5), "apple3":(4,1), "apple1":(2,0)} #1


    #---Define Plans and Queries---
    stateList = RE_conrollStates.stateList
    transitions = RE_conrollTrans.transitions
    highToLowConver = RE_conrollHighLow.highToLow

    startState = [False] * (numberOfTasks * numberOfAgents)

    #userQuery = {"agent1": ["*","apple1","apple2"],   #Possible Query
    #"agent2":["apple3","*","apple2"],
    #"agent3":["apple3","apple1","*"]}

    userQuery = {"agent1": ["*","*","apple2"],   #Not Possible Query
    "agent2":["apple3","*","apple2"],
    "agent3":["apple3","apple1","*"]}

    freeTasks = []

    HIGH_SEARCH_DEPTH = 100 #based on length of query
    LOW_SEARCH_DEPTH = 50  #based on time_limit for domain
    query_episodes = 2 #Number of times query should be adapted based on returned explantion
    episodes = 10 #based on resources
    query_possible = False  #Is query possibility already know?

    #---Check if rho in G---
    print("USER QUERY: ", userQuery, "\n")

    while query_episodes != 0 and query_possible != True:
        query_episodes -= 1

        UMNumber = generateIntialUM(userQuery,transitions,numberOfAgents,startState)
        #for i in UMNumber: #View U-values
            #print(i,UMNumber[i])


        if userQuery == []:
            print("No user query given.")
        else:
            RE_abstractToPrism.createPrismModel(numberOfAgents, numberOfTasks, transitions, startState)
            RE_abstractToPrism.createProperty(userQuery, numberOfAgents)
            os.system("sh ../../prism-4.7-linux64/bin/prism checkableModel.prism checkablepropertiesFile.pctl -exportresults resultsLog.txt")
            f = open("resultsLog.txt", "r")
            for line in f:
                if line != "Result\n":
                    max_value = max(UMNumber.values())
                    if 0.0 < float(line) and max_value == len(userQuery["agent1"]):
                        print("FOIL IS POSSIBLE!")
                        query_possible = True
                        print("Your current query is possible, but less probable than the current plan.")
                        return

        #---Begin Rollout---
            print("SEARCHING FOR FOIL....")
            startStatesQueue = queue.PriorityQueue()
            startStates = []
            for i in transitions.keys():
                for j in transitions[i]:
                    if j[0] in UMNumber.keys():
                        for l in transitions[i]:
                            if l[0] == j[0]:
                                observations = l[1]
                        if UMNumber[j[0]] != float("-inf"):
                            startStates.append([(-1*UMNumber[j[0]]),observations,j[0],i])

            for s in startStates:
                startStatesQueue.put(s)
            counter = 0

            while startStatesQueue.empty() != True and counter != episodes:
                max_value = max(UMNumber.values())
                print("Scenario Number: ",counter,"Max U-Value Found: ", max_value)
                counter = counter + 1
                startingNode = startStatesQueue.get()
                currentStart = startingNode[2]
                currentStartParent = startingNode[3]
                newStateNumber = startingNode[2]
                oldStateNumber = startingNode[3]
                lowCurrentStart = highToLowConver[(currentStart,currentStartParent)]
                startStatesQueue.put(startingNode) #Continue to fill queue for search until episode run out
                highLevelCounter = 0
                lowLevelCounter = 0
                new_UMNumber = 0
                while highLevelCounter != HIGH_SEARCH_DEPTH and lowLevelCounter != LOW_SEARCH_DEPTH:
                    highLevelStates = {}
                    possibleActions = generateComboActions(lowCurrentStart, env, agents) #Find only the actions allowed in the policy
                    bestAction,UMNumber, stateList, transitions = findBestActionRandom(possibleActions,lowCurrentStart,env,userQuery, numberOfAgents,stateList,transitions,highLevelStates,UMNumber)
                    if os.path.exists("currentStartState.txt"):
                        os.remove("currentStartState.txt")
                    f = open("currentStartState.txt", "w")
                    f.write(str(lowCurrentStart))
                    f.close()
                    obs = env.reset()
                    n_obs, reward, done, info = env.step(bestAction)
                    newStateNumber, oldStateNumber = convertToHighLevel(obs[0], n_obs[0], bestAction,oldStateNumber)
                    stateList, transitions, highLevelStates, newStateNumber, oldStateNumber, new_UMNumber, UMNumber = addHighLevelStates(newStateNumber, oldStateNumber, stateList, transitions, highLevelStates, lowLevelCounter, bestAction, UMNumber, userQuery, numberOfAgents)
                    highToLowConver = updateHighToLowConver(highToLowConver, oldStateNumber, newStateNumber, n_obs[0], new_UMNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks)
                    if new_UMNumber == float("-inf"):
                        break
                    highLevelCounter = highLevelCounter + 1
                    for l in transitions[oldStateNumber]:
                        if l[0] == newStateNumber:
                            observations = l[1]
                    startStatesQueue.put([-1*new_UMNumber,observations,newStateNumber,oldStateNumber])
                    currentStart = newStateNumber
                    lowCurrentStart = n_obs[0]
                    lowLevelCounter = lowLevelCounter + 1
                    oldStateNumber = newStateNumber


                if new_UMNumber == len(userQuery["agent1"]) and done:  #Check if rho in G
                    RE_abstractToPrism.createPrismModel(numberOfAgents, numberOfTasks, transitions, startState)
                    os.system("sh ../../prism-4.7-linux64/bin/prism checkableModel.prism checkablepropertiesFile.pctl -exportresults resultsLog.txt")
                    f = open("resultsLog.txt", "r")
                    for line in f:
                        if line != "Result\n":
                            if 0.0 < float(line):
                                print("FOIL IS POSSIBLE!")
                                query_possible = True
                                print("Your current query is possible, but less probable than the current plan.")
                                return


            print("FOIL IS NOT POSSIBLE!")
            global TargetStates
            RE_generateExplanations.generateNotPossibleExplanation(UMNumber,transitions,TargetStates,userQuery,numberOfAgents)
            userQuery = RE_generateNotPossExp_3agTotalQ.genNotPossExp(userQuery, numberOfAgents)
            print("NEW USER QUERY: ", userQuery, "\n")

main()
