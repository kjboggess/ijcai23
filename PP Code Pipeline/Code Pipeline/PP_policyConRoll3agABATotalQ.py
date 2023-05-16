from re import L
from sys import maxsize
from xmlrpc.client import Unmarshaller
import torch
import gym

from a2c import A2C
from wrappers import RecordEpisodeStatistics, TimeLimit

import PP_conrollStates
import PP_conrollTrans
import PP_conrollHighLow
import PP_abstractToPrism
import PP_generateExplanations
import queue
import itertools
import os
import time
import random
import math
import numpy
import PP_generateNotPossExp_3agTotalQ
import PP_convertStates
import pressureplate

#GLOBAL VARIABLES
stateList = []
transitions = {}
UMNumber = {}
currentStart = []
currentOldState = ["[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]",1]
userPlan = []

nonTargetStates = {"plate1":[], "plate2":[], "plate3":[], "plate4":[], "goal":[]}
TargetStates = {"plate1":[], "plate2":[], "plate3":[], "plate4":[], "goal":[]}


def convertToHighLevel(obs, n_obs, actions,numTasks,numAgents,env_name,plates,currentStart):
    numVariables = 0
    global nonTargetStates
    global TargetStates

    oldStateNumber, newStateNumber, failedAction, nonTargetStates, TargetStates = PP_convertStates.generateTransitions(obs,n_obs,numVariables,numTasks,numAgents,env_name,plates,actions, nonTargetStates, TargetStates, currentStart)

    return oldStateNumber.replace(" "," "), newStateNumber.replace(" "," "), failedAction, nonTargetStates, TargetStates

def isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions):
    oldStateNumberSplit = oldStateNumber.split(",")
    newStateNumberSplit = newStateNumber.split(",")

    newUMNumber = 0
    completedNextTasks = [False] * numberOfAgents
    if newStateNumber != oldStateNumber:
        oldUMNumber = UMNumber[oldStateNumber]
        if oldUMNumber == float("-inf"):
            UMNumber[newStateNumber] = float("-inf")
            return float("-inf"), UMNumber
        tasksToDo = []

        for i in range(1,numberOfAgents+1):
            tasksToDo = tasksToDo + userQuery["agent"+str(i)][oldUMNumber:]

        if tasksToDo != []:
            for i in range(1,numberOfAgents+1):
                nextAgentTask = userQuery["agent"+str(i)][oldUMNumber]
                if numberOfAgents == 9:
                    if nextAgentTask == "*":
                        completedNextTasks[i-1] = True
                        tasksToDo.remove("*")
                    if nextAgentTask == 'plate1':
                        if("True" in newStateNumberSplit[0+i-1]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("plate1")
                    if nextAgentTask == 'plate2':
                        if("True" in newStateNumberSplit[9+i-1]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("plate2")
                    if nextAgentTask == 'plate3':
                        if("True" in newStateNumberSplit[18+i-1]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("plate3")
                    if nextAgentTask == 'plate4':
                        if("True" in newStateNumberSplit[27+i-1]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("plate4")
                    if nextAgentTask == 'goal':
                        if("True" in newStateNumberSplit[36+i-1]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("goal")

        if newUMNumber != float("-inf"):
            if False not in completedNextTasks:
                newUMNumber = oldUMNumber + 1
            else:
                newUMNumber = oldUMNumber
        if numberOfAgents == 9:
            if ("True" in newStateNumberSplit[0] or "True" in newStateNumberSplit[1] or "True" in newStateNumberSplit[2] or "True" in newStateNumberSplit[3] or "True" in newStateNumberSplit[4] or "True" in newStateNumberSplit[5] or "True" in newStateNumberSplit[6] or "True" in newStateNumberSplit[7] or "True" in newStateNumberSplit[8]) and "plate1" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[9] or "True" in newStateNumberSplit[10] or "True" in newStateNumberSplit[11] or "True" in newStateNumberSplit[12] or "True" in newStateNumberSplit[13] or "True" in newStateNumberSplit[14] or "True" in newStateNumberSplit[15] or "True" in newStateNumberSplit[16] or "True" in newStateNumberSplit[17]) and "plate2" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[18] or "True" in newStateNumberSplit[19] or "True" in newStateNumberSplit[20] or "True" in newStateNumberSplit[21] or "True" in newStateNumberSplit[22] or "True" in newStateNumberSplit[23] or "True" in newStateNumberSplit[24] or "True" in newStateNumberSplit[25] or "True" in newStateNumberSplit[26]) and "plate3" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[27] or "True" in newStateNumberSplit[28] or "True" in newStateNumberSplit[29] or "True" in newStateNumberSplit[30] or "True" in newStateNumberSplit[31] or "True" in newStateNumberSplit[32] or "True" in newStateNumberSplit[33] or "True" in newStateNumberSplit[34] or "True" in newStateNumberSplit[35]) and "plate4" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[36] or "True" in newStateNumberSplit[37] or "True" in newStateNumberSplit[38] or "True" in newStateNumberSplit[39] or "True" in newStateNumberSplit[40] or "True" in newStateNumberSplit[41] or "True" in newStateNumberSplit[42] or "True" in newStateNumberSplit[43] or "True" in newStateNumberSplit[44]) and "goal" in tasksToDo:
                newUMNumber = float("-inf")
    else:
        newUMNumber = UMNumber[newStateNumber]

    if newStateNumber in UMNumber.keys():
        if UMNumber[newStateNumber] <= newUMNumber:
            UMNumber[newStateNumber] = newUMNumber
    else:
        UMNumber[newStateNumber] = newUMNumber

    return newUMNumber, UMNumber


def addHighLevelStates(newStateNumber, oldStateNumber, stateList, transitions, highLevelStates, currentStep, actions, UMNumber, userQuery, numberOfAgents):
    global currentOldState
    global userPlan

    transitionValue = float('inf')


    newUMNumber, UMNumber = isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions)

    if(oldStateNumber not in stateList):
        stateList.append(oldStateNumber)
    if(newStateNumber not in stateList):
        stateList.append(newStateNumber)

    if newStateNumber != currentOldState[0]:
        if currentStep == -1:
            transitionValue = 1
        else:
            transitionValue = (currentStep+1) - currentOldState[1]
            currentOldState[0] = newStateNumber
            currentOldState[1] = currentStep
            userPlan.append(newStateNumber)

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


def generateComboActions(lowCurrentStart, env, agents,highToLowConver,currentStart):
    if os.path.exists("currentStartStatePP.txt"):
        os.remove("currentStartStatePP.txt")
    f = open("currentStartStatePP.txt", "w")
    max_value = max(UMNumber.values())
    f.write(str(lowCurrentStart) + str(max_value))
    f.close()

    obs = env.reset()

    obs = [torch.from_numpy(o) for o in obs]
    a, actions, b , c, newProbsIndex = zip(*[agent.model.act(obs[agent.agent_id], None, None) for agent in agents])
    for i in range(0,len(agents)):
        if 0 in newProbsIndex[i]:
            newProbsIndex[i].remove(4)  #Don't allow the agents to stop moving

    return newProbsIndex

def jointlowLevelScore(state, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks):
    agent_locations = []
    task_distance = 0
    query_distance = 0


    if currentTaskNumber == float("-inf"):
        return float("-inf")

    if len(state)>5:
        if numberOfAgents == 9:
            state = [state[0:102],state[102:204],state[204:306],state[306:408],state[408:510],state[510:612],state[612:714],state[714:816],state[816:918]]

    for i in range(1,numberOfAgents+1):
        agent_locations.append((state[i-1][-2],state[i-1][-1]))
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
                        task_x_loc = state[i-1][-2]
                        task_y_loc = state[i-1][-1]
                else:
                    task_x_loc = task_locations[nextAgentTask][0]
                    task_y_loc = task_locations[nextAgentTask][1]
                nextTaskDistance = abs(state[i-1][-2] - float(task_x_loc)) + abs(state[i-1][-1] - float(task_y_loc))
            query_distance = query_distance + nextTaskDistance

    for j in range(0,len(agent_locations)):
        if "agent"+str(2-j+1) in userQuery.keys():
            agentAssignedTasks = userQuery["agent"+str(2-j+1)]
            for i in task_locations.keys():
                if i not in freeTasks and i not in agentAssignedTasks:
                    current_distance = 10 - (abs(agent_locations[j][-2] - float(task_locations[i][-1])) + abs(agent_locations[j][-2] - float(task_locations[i][-1])))
                else:
                    current_distance = abs(agent_locations[j][-2] - float(task_locations[i][0])) + abs(agent_locations[j][-1] - float(task_locations[i][1]))
                task_distance = task_distance + current_distance



    score = task_distance + query_distance
    return score

def updateHighToLowConver(highToLowConver, oldStateNumber, newStateNumber, n_obs, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks):
    if (newStateNumber, oldStateNumber) in highToLowConver.keys():
        currentLowLevelStateScore = jointlowLevelScore(highToLowConver[(newStateNumber,oldStateNumber)], currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks)
        newStateScore = jointlowLevelScore(n_obs, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks)
        if newStateScore > currentLowLevelStateScore:
            if numberOfAgents == 9:
                highToLowConver[(newStateNumber,oldStateNumber)] = list(n_obs[0]) + list(n_obs[1]) + list(n_obs[2]) + list(n_obs[3] + list(n_obs[4]) + list(n_obs[5]) + list(n_obs[6]) + list(n_obs[7]) + list(n_obs[8]))
    else:
        if numberOfAgents == 9:
            highToLowConver[(newStateNumber,oldStateNumber)] = list(n_obs[0]) + list(n_obs[1]) + list(n_obs[2]) + list(n_obs[3] + list(n_obs[4]) + list(n_obs[5]) + list(n_obs[6]) + list(n_obs[7]) + list(n_obs[8]))

    if numberOfAgents == 9:
        newLowLevel = list(n_obs[0]) + list(n_obs[1]) + list(n_obs[2]) + list(n_obs[3] + list(n_obs[4]) + list(n_obs[5]) + list(n_obs[6]) + list(n_obs[7]) + list(n_obs[8]))

    return highToLowConver, numberOfAgents


def generateIntialUM(userQuery,transitions,numberOfAgents,startState,numTasks,numAgents,plates):
    global nonTargetStates
    global TargetStates
    UMNumber = {}
    UMNumber[str(startState)] = 0
    keyQueue = queue.Queue()
    keyQueue.put(str(startState))
    while keyQueue.empty() != True:
        i = keyQueue.get()
        if i in transitions.keys():
            for j in transitions[i]:#
                if j[0] not in UMNumber.keys():
                    keyQueue.put(j[0])
                oldStateNumber = i
                oldStateNumberSplit = oldStateNumber.split(",")
                newStateNumber = j[0]
                newStateNumberSplit = newStateNumber.split(",")
                actions = [0] * numAgents

                newUMNumber, UMNumber = isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions)

                if numAgents == 9:
                    breakNumbers = [0,9,18,27,36,45]


                onPlate = 0
                for k in range(breakNumbers[0],breakNumbers[1]):
                    if "True" in newStateNumberSplit[k]:
                        onPlate = onPlate + 1
                if onPlate == 2 and newStateNumber not in TargetStates["plate1"]:
                    TargetStates["plate1"].append(str(newStateNumber).replace(" ",""))
                elif onPlate == 1 and newStateNumber not in nonTargetStates["plate1"]:
                    nonTargetStates["plate1"].append(str(newStateNumber).replace(" ",""))

                onPlate = 0
                for k in range(breakNumbers[1],breakNumbers[2]):
                    if "True" in newStateNumberSplit[k]:
                        onPlate = onPlate + 1
                if onPlate == 2 and newStateNumber not in TargetStates["plate2"]:
                    TargetStates["plate2"].append(str(newStateNumber).replace(" ",""))
                elif onPlate == 1 and newStateNumber not in nonTargetStates["plate1"]:
                    nonTargetStates["plate2"].append(str(newStateNumber).replace(" ",""))

                if numberOfAgents >= 7:
                    onPlate = 0
                    for k in range(breakNumbers[2],breakNumbers[3]):
                        if "True" in newStateNumberSplit[k]:
                            onPlate = onPlate + 1
                    if onPlate == 2 and newStateNumber not in TargetStates["plate3"]:
                        TargetStates["plate3"].append(str(newStateNumber).replace(" ",""))
                    elif onPlate == 1 and newStateNumber not in nonTargetStates["plate3"]:
                        nonTargetStates["plate3"].append(str(newStateNumber).replace(" ",""))

                if numberOfAgents >= 9:
                    onPlate = 0
                    for k in range(breakNumbers[3],breakNumbers[4]):
                        if "True" in newStateNumberSplit[k]:
                            onPlate = onPlate + 1
                    if onPlate == 2 and newStateNumber not in TargetStates["plate4"]:
                        TargetStates["plate4"].append(str(newStateNumber).replace(" ",""))
                    elif onPlate == 1 and newStateNumber not in nonTargetStates["plate4"]:
                        nonTargetStates["plate4"].append(str(newStateNumber).replace(" ",""))

                onPlate = 0
                for k in range(breakNumbers[-2],breakNumbers[-1]):
                    if "True" in newStateNumberSplit[k] and newStateNumber not in TargetStates["goal"]:
                        onPlate = onPlate + 1
                if onPlate == 1 and newStateNumber not in nonTargetStates["goal"]:
                    TargetStates["goal"].append(str(newStateNumber).replace(" ",""))

    return UMNumber

def findBestActionRandom(possibleActions,lowCurrentStart,env,userQuery,numberOfAgents,stateList,transitions,highLevelStates,UMNumber,numTasks,numAgents,env_name,plates):
    comboActions = list(itertools.product(*possibleActions))
    choice = random.choice(comboActions)
    obs = env.reset()
    n_obs, reward, done, info = env.step(choice)
    newStateNumber, oldStateNumber, failedAction,nonTargetStates, TargetState = convertToHighLevel(obs, n_obs, choice,numTasks,numAgents,env_name,plates,currentStart)
    stateList, transitions, highLevelStates, newStateNumber, oldStateNumber, newUMNumber, UMNumber = addHighLevelStates(newStateNumber, oldStateNumber, stateList, transitions, highLevelStates, 0, choice, UMNumber, userQuery, numberOfAgents)
    return choice, UMNumber, stateList, transitions


def main():
    #todo
        #Generate Not Possible Explanation
        #Generate Original Files from Evalution
    #---Make Enviroment---
    path = "results/trained_models/462/u1000"
    env_name = "pressureplate-linear-4p-v0"

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
    global currentOldState
    global userPlan
    global UMNumber
    global currentStart
    global nonTargetStates
    global TargetStates

    #---BackGround Info---
    numberOfAgents = 9
    numberOfTasks = 5


    #---Define Plans and Queries---
    stateList = PP_conrollStates.stateList
    transitions = PP_conrollTrans.transitions
    highToLowConver = PP_conrollHighLow.highToLow

    plates = [[2, 13],[7, 13],[2, 9],[7, 9],[7, 5],[2, 5],[8, 6],[1, 6],[3, 1]]
    startState = [False] * 45

    userQuery = {"agent1": ["*","plate2","*"], #Possible
    "agent2": ["*","*","*"],
    "agent3": ["*","*","plate3"],
    "agent4": ["*","*","*"],
    "agent5": ["plate1","*","*"],
    "agent6": ["*","*","*"],
    "agent7": ["*","*","*"],
    "agent8": ["*","*","*"],
    "agent9": ["*","*","*"],
    }

    userQuery = {"agent1": ["*","plate2","*"], #Not Possible
    "agent2": ["*","*","*"],
    "agent3": ["*","*","*"],
    "agent4": ["*","*","*"],
    "agent5": ["plate1","*","plate3"],
    "agent6": ["*","*","*"],
    "agent7": ["*","*","*"],
    "agent8": ["*","*","*"],
    "agent9": ["*","*","*"],
    }


    freeTasks = []


    RUN_STEPS = 1500
    HIGH_SEARCH_DEPTH = 100
    LOW_SEARCH_DEPTH = 50
    ROLLOUT_AMOUNT = 0
    query_episodes = 3
    episodes = 10
    lossbase = 100
    query_possible = False

    #---Check if rho in G---
    while query_episodes != 0 and query_possible != True:
        print("USER QUERY:",userQuery)
        query_episodes -= 1

        UMNumber = generateIntialUM(userQuery,transitions,numberOfAgents,startState,numberOfTasks,numberOfAgents,plates)
        UMNumber[str(startState).replace(" ","")] = 0

        if userQuery == []:
            print("No user query given")
        else:
            print("SEARCHING...")
            PP_abstractToPrism.createPrismModel(numberOfAgents, numberOfTasks, transitions, startState)
            PP_abstractToPrism.createProperty(userQuery, numberOfAgents)
            os.system("sh ../../prism-4.7-linux64/bin/prism checkableModel.prism checkablepropertiesFile.pctl -exportresults resultsLogPP.txt")
            f = open("resultsLogPP.txt", "r")
            for line in f:
                if line != "Result\n":
                    if 0.0 < float(line):
                        print("FOIL IS POSSIBLE")
                        query_possible = True
                        holdPlan = [k for k,v in UMNumber.items() if v == max(UMNumber.values())]
                        holdPlan = [holdPlan[-1]]
                        print("Your current query is possible.")
                        return

        #---Begin Rollout---
            print("SEARCHING FOR FOIL")
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
                holdPlan = []
                max_value = max(UMNumber.values())
                print("Scenario Number: ",counter,"Max U-Value Found: ", max_value)
                counter = counter + 1
                startingNode = startStatesQueue.get()
                currentStart = startingNode[2]
                currentStartParent = startingNode[3]
                newStateNumber = startingNode[2]
                oldStateNumber = startingNode[3]
                lowCurrentStart = highToLowConver[(currentStart,currentStartParent)]
                if os.path.exists("currentStartStatePP.txt"):
                    os.remove("currentStartStatePP.txt")
                f = open("currentStartStatePP.txt", "w")
                f.write(str(lowCurrentStart) + str(max_value))
                f.close()
                obs = env.reset()

                task_locations = {"plate1":plates[0], "plate2":plates[2], "plate3":plates[4], "plate4":plates[6], "goal":plates[8]}


                holdPlan.append(currentStart)
                startStatesQueue.put(startingNode) #Continue to fill queue for search until episode run out
                highLevelCounter = 0
                lowLevelCounter = 0
                new_UMNumber = 0
                while highLevelCounter != HIGH_SEARCH_DEPTH and lowLevelCounter != LOW_SEARCH_DEPTH:
                    highLevelStates = {}
                    possibleActions = generateComboActions(lowCurrentStart, env, agents,highToLowConver,currentStart) #Find only the actions allowed in the policy
                    bestAction,UMNumber, stateList, transitions = findBestActionRandom(possibleActions,lowCurrentStart,env,userQuery, numberOfAgents,stateList,transitions,highLevelStates,UMNumber,numberOfTasks,numberOfAgents,env_name,plates)
                    if os.path.exists("currentStartStatePP.txt"):
                        os.remove("currentStartStatePP.txt")
                    f = open("currentStartStatePP.txt", "w")
                    max_value = max(UMNumber.values())
                    f.write(str(lowCurrentStart) + str(max_value))
                    f.close()
                    obs = env.reset()
                    n_obs, reward, done, info = env.step(bestAction)
                    oldStateNumber, newStateNumber, failedAction, nonTargetStates, TargetStates = convertToHighLevel(obs, n_obs, bestAction,numberOfTasks,numberOfAgents,env_name,plates,currentStart)
                    stateList, transitions, highLevelStates, newStateNumber, oldStateNumber, new_UMNumber, UMNumber = addHighLevelStates(newStateNumber, oldStateNumber, stateList, transitions, highLevelStates, lowLevelCounter, bestAction, UMNumber, userQuery, numberOfAgents)
                    if new_UMNumber == float("-inf") or failedAction == True:
                        break
                    if newStateNumber != oldStateNumber:
                        holdPlan.append(newStateNumber)
                        highToLowConver, newLowCurrentState = updateHighToLowConver(highToLowConver, oldStateNumber, newStateNumber, n_obs, new_UMNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks)
                        highLevelCounter = highLevelCounter + 1
                        for l in transitions[oldStateNumber]:
                            if l[0] == newStateNumber:
                                observations = l[1]
                        startStatesQueue.put([-1*new_UMNumber,observations,newStateNumber,oldStateNumber])
                    currentStart = newStateNumber
                    lowCurrentStart = list(n_obs[0]) + list(n_obs[1]) + list(n_obs[2]) + list(n_obs[3]) + list(n_obs[4]) + list(n_obs[5]) + list(n_obs[6]) + list(n_obs[7]) + list(n_obs[8])
                    lowLevelCounter = lowLevelCounter + 1

                if new_UMNumber == len(userQuery["agent1"]) and done:  #Check if rho in G
                    PP_abstractToPrism.createPrismModel(numberOfAgents, numberOfTasks, transitions, startState)
                    os.system("sh ../../prism-4.7-linux64/bin/prism checkableModel.prism checkablepropertiesFile.pctl -exportresults resultsLogPP.txt")
                    f = open("resultsLogPP.txt", "r")
                    for line in f:
                        if line != "Result\n":
                            if 0.0 < float(line):
                                print("FOIL IS POSSIBLE!")
                                end = time.time()
                                query_possible = True
                                print("Your current query is possible.")
                                return


            print("FOIL IS NOT POSSIBLE!")
            PP_generateExplanations.generateNotPossibleExplanation(UMNumber,transitions,nonTargetStates,TargetStates,userQuery,numberOfAgents)
            userQuery = PP_generateNotPossExp_3agTotalQ.genNotPossExp(userQuery, numberOfAgents)
            print("NEW USER QUERY: ", userQuery, "\n")

main()
