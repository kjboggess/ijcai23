from re import L
from sys import maxsize
from xmlrpc.client import Unmarshaller
import torch
import robotic_warehouse
import gym

from a2c import A2C
from wrappers import RecordEpisodeStatistics, TimeLimit

import RWARE_conrollStates
import RWARE_conrollTrans
import RWARE_conrollHighLow
import RWARE_abstractToPrism
import RWARE_generateExplanations
import queue
import itertools
import os
import time
import random
import math
import numpy
import RWARE_generateNotPossExp_3agTotalQ
import RWARE_convertStates

#GLOBAL VARIABLES
stateList = []
transitions = {}
UMNumber = {}
currentStart = []

TargetStates = {"deliver_shelf4":[],"deliver_shelf3":[],"deliver_shelf2":[],"deliver_shelf1":[],
"pickup_shelf4":[],"pickup_shelf3":[],"pickup_shelf2":[],"pickup_shelf1":[]}

holdingshelfs = ""
n_holdingshelfs = ""
deliveredshelfs = ""
n_deliveredshelfs = ""

def convertToHighLevel(obs, n_obs, actions,numTasks,numAgents,env_name,shelfs,currentStart):
    numVariables = 0
    global holdingshelfs
    global deliveredshelfs
    global TargetStates

    oldStateNumber, newStateNumber, failedAction, holdingshelfs, deliveredshelfs, TargetStates = RWARE_convertStates.generateTransitions(obs,n_obs,numVariables,numTasks,numAgents,env_name,shelfs,actions,holdingshelfs, deliveredshelfs, TargetStates, currentStart)

    return oldStateNumber, newStateNumber, failedAction, n_holdingshelfs, n_deliveredshelfs, TargetStates

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
                if nextAgentTask == "*":
                    completedNextTasks[i-1] = True
                    tasksToDo.remove("*")

                if numberOfAgents == 2:
                    if nextAgentTask == "deliver_shelf1":
                        if(oldUMNumber != float("-inf") and "True" in newStateNumberSplit[2*12-(3-i)]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("deliver_shelf1")
                        elif "True" in newStateNumberSplit[22] or "True" in newStateNumberSplit[23]:
                            newUMNumber = float("-inf")
                    if nextAgentTask == "deliver_shelf2":
                        if(oldUMNumber != float("-inf") and "True" in newStateNumberSplit[2*13-(3-i)]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("deliver_shelf2")
                        elif "True" in newStateNumberSplit[24] or "True" in newStateNumberSplit[25]:
                            newUMNumber = float("-inf")
                    if nextAgentTask == "deliver_shelf3":
                        if(oldUMNumber != float("-inf") and "True" in newStateNumberSplit[2*14-(3-i)]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("deliver_shelf3")
                        elif "True" in newStateNumberSplit[26] or "True" in newStateNumberSplit[27]:
                            newUMNumber = float("-inf")
                    if nextAgentTask == "deliver_shelf4":
                        if(oldUMNumber != float("-inf") and "True" in newStateNumberSplit[2*15-(3-i)]):
                            completedNextTasks[i-1] = True
                            tasksToDo.remove("deliver_shelf4")
                        elif "True" in newStateNumberSplit[28] or "True" in newStateNumberSplit[29]:
                            newUMNumber = float("-inf")
        if newUMNumber != float("-inf"):
            if False not in completedNextTasks:
                newUMNumber = oldUMNumber + 1
            else:
                newUMNumber = oldUMNumber

        if numberOfAgents == 2:
            if ("True" in newStateNumberSplit[22] or "True" in newStateNumberSplit[23]) and "deliver_shelf1" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[24] or "True" in newStateNumberSplit[25]) and "deliver_shelf2" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[26] or "True" in newStateNumberSplit[27]) and "deliver_shelf3" in tasksToDo:
                newUMNumber = float("-inf")
            if ("True" in newStateNumberSplit[28] or "True" in newStateNumberSplit[29]) and "deliver_shelf4" in tasksToDo:
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


def generateComboActions(lowCurrentStart, env, agents,highToLowConver,currentStart):
    if os.path.exists("currentStartStateRWARE.txt"):
        os.remove("currentStartStateRWARE.txt")
    f = open("currentStartStateRWARE.txt", "w")
    f.write(str(lowCurrentStart)+ "*" + str(currentStart))
    f.close()

    obs = env.reset()

    obs = [torch.from_numpy(o) for o in obs]
    a, actions, b , c, newProbsIndex = zip(*[agent.model.act(obs[agent.agent_id], None, None) for agent in agents])

    for i in range(0,len(agents)):
        if 0 in newProbsIndex[i]:
            newProbsIndex[i].remove(0)  #Don't allow the agents to stop moving

    return newProbsIndex

def jointlowLevelScore(state, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks,oldStateNumber):
    agent_locations = []
    task_distance = 0
    query_distance = 0


    if currentTaskNumber == float("-inf"):
        return float("-inf")

    if len(state)>4:
        if type(state) == str:
            state = state.replace("[","")
            state = state.replace("]","")
            state = state.replace(" ","")
            state=state.split(",")
        if numberOfAgents == 2:
            state = [state[0:119],state[119:238]]


    for i in range(1,numberOfAgents+1):
        agent_locations.append((state[i-1][0],state[i-1][1]))
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
                        task_x_loc = state[i-1][0]
                        task_y_loc = state[i-1][1]
                else:
                    shelfNumber = int(nextAgentTask[-1])
                    oldStateNumberSplit = oldStateNumber.split(",")
                    task_x_loc = task_locations[nextAgentTask][0]
                    task_y_loc = task_locations[nextAgentTask][1]
                nextTaskDistance = abs(float(state[i-1][0]) - float(task_x_loc)) + abs(float(state[i-1][1]) - float(task_y_loc))
            query_distance = query_distance + nextTaskDistance

    for j in range(0,len(agent_locations)):
        if "agent"+str(2-j+1) in userQuery.keys():
            agentAssignedTasks = userQuery["agent"+str(2-j+1)]
            for i in task_locations.keys():
                if i not in freeTasks and i not in agentAssignedTasks:
                    current_distance = 10 - (abs(float(agent_locations[j][0]) - float(task_locations[i][0])) + abs(float(agent_locations[j][1]) - float(task_locations[i][1])))
                else:
                    current_distance = abs(float(agent_locations[j][0]) - float(task_locations[i][0])) + abs(float(agent_locations[j][1]) - float(task_locations[i][1]))
                task_distance = task_distance + current_distance



    score = task_distance + query_distance
    return score


def updateHighToLowConver(highToLowConver, oldStateNumber, newStateNumber, n_obs, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks):
    if (newStateNumber, oldStateNumber) in highToLowConver.keys():
        currentLowLevelStateScore = jointlowLevelScore(highToLowConver[(newStateNumber,oldStateNumber)], currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks,oldStateNumber)
        newStateScore = jointlowLevelScore(n_obs, currentTaskNumber, userQuery, numberOfAgents, numberOfTasks, task_locations, freeTasks,oldStateNumber)
        if newStateScore > currentLowLevelStateScore:
            if numberOfAgents == 2:
                highToLowConver[(newStateNumber,oldStateNumber)] = list(n_obs[0]) + list(n_obs[1])
    else:
        if numberOfAgents == 2:
            highToLowConver[(newStateNumber,oldStateNumber)] = list(n_obs[0]) + list(n_obs[1])

    if numberOfAgents == 2:
        newLowLevel = list(n_obs[0]) + list(n_obs[1])

    return highToLowConver, newLowLevel

def generateIntialUM(userQuery,transitions,numberOfAgents,startState,numTasks,numAgents,shelfs):  #EDIT HERE
    global TargetStates
    UMNumber = {}
    UMNumber[str(startState).replace(" "," ")] = 0
    keyQueue = queue.Queue()
    keyQueue.put(str(startState).replace(" "," "))
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
                actions = [0] * numberOfAgents

                newUMNumber, UMNumber = isUMNumberViolated(newStateNumber, oldStateNumber, UMNumber, numberOfAgents, userQuery, actions)

                #---------------------------------------------------------------------------------------------------------------------------
                #--------------------------------------------------------------------------------------------------------------------------
                #---------------------------------------------------------------------------------------------------------------------------
                #Pick up SHELF Failure - If an agent is present at the shelf, but they do not load the shelf
                nonfailedAction1 = False
                nonfailedAction2 = False
                nonfailedAction3 = False
                nonfailedAction4 = False

                if numberOfAgents == 2:
                    startCompleteCounter = 8
                #Shelf 1

                if(numTasks >= 1 and numAgents >= 1):
                    if("True" in oldStateNumberSplit[0*(numTasks-numberOfAgents)] and "True" in newStateNumberSplit[0*(numTasks-numberOfAgents)+startCompleteCounter]):
                        nonfailedAction1 = True
                if(numTasks >= 1 and numAgents >= 2):
                    if("True" in oldStateNumberSplit[0*(numTasks-numberOfAgents)+1] and "True" in newStateNumberSplit[0*(numTasks-numberOfAgents)+startCompleteCounter+1]):
                        nonfailedAction1 = True
                if(numTasks >= 1 and numAgents >= 3):
                    if("True" in oldStateNumberSplit[0*(numTasks-numberOfAgents)+2] and "True" in newStateNumberSplit[0*(numTasks-numberOfAgents)+startCompleteCounter+2]):
                        nonfailedAction1 = True
                if(numTasks >= 1 and numAgents >= 4):
                    if("True" in oldStateNumberSplit[0*(numTasks-numberOfAgents)+3] and "True" in newStateNumberSplit[0*(numTasks-numberOfAgents)+startCompleteCounter+3]):
                        nonfailedAction1 = True
                if nonfailedAction1 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf1"]:
                        TargetStates["pickup_shelf1"].append(str(oldStateNumber).replace(" ",""))

                #Shelf 2

                if(numTasks >= 2 and numAgents >= 1):
                    if("True" in oldStateNumberSplit[1*(numTasks-numberOfAgents)] and "True" in newStateNumberSplit[1*(numTasks-numberOfAgents)+startCompleteCounter]):
                        nonfailedAction2 = True
                if(numTasks >= 2 and numAgents >= 2):
                    if("True" in oldStateNumberSplit[1*(numTasks-numberOfAgents)+1] and "True" in newStateNumberSplit[1*(numTasks-numberOfAgents)+startCompleteCounter+1]):
                        nonfailedAction2 = True
                if(numTasks >= 2 and numAgents >= 3):
                    if("True" in oldStateNumberSplit[1*(numTasks-numberOfAgents)+2] and "True" in newStateNumberSplit[1*(numTasks-numberOfAgents)+startCompleteCounter+2]):
                        nonfailedAction2 = True
                if(numTasks >= 2 and numAgents >= 4):
                    if("True" in oldStateNumberSplit[1*(numTasks-numberOfAgents)+3] and "True" in newStateNumberSplit[1*(numTasks-numberOfAgents)+startCompleteCounter+3]):
                        nonfailedAction2 = True
                if nonfailedAction2 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf2"]:
                        TargetStates["pickup_shelf2"].append(str(oldStateNumber).replace(" ",""))

                #Shelf 3

                if(numTasks >= 3 and numAgents >= 1):
                    if("True" in oldStateNumberSplit[2*(numTasks-numberOfAgents)] and "True" in newStateNumberSplit[2*(numTasks-numberOfAgents)+startCompleteCounter]):
                        nonfailedAction3 = True
                if(numTasks >= 3 and numAgents >= 2):
                    if("True" in oldStateNumberSplit[2*(numTasks-numberOfAgents)+1] and "True" in newStateNumberSplit[2*(numTasks-numberOfAgents)+startCompleteCounter+1]):
                        nonfailedAction3 = True
                if(numTasks >= 3 and numAgents >= 3):
                    if("True" in oldStateNumberSplit[2*(numTasks-numberOfAgents)+2] and "True" in newStateNumberSplit[2*(numTasks-numberOfAgents)+startCompleteCounter+2]):
                        nonfailedAction3 = True
                if(numTasks >= 3 and numAgents >= 4):
                    if("True" in oldStateNumberSplit[2*(numTasks-numberOfAgents)+3] and "True" in newStateNumberSplit[2*(numTasks-numberOfAgents)+startCompleteCounter+3]):
                        nonfailedAction3 = True
                if failedAction3 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf3"]:
                        TargetStates["pickup_shelf3"].append(str(oldStateNumber).replace(" ",""))

                #Shelf 4

                if(numTasks >= 4 and numAgents >= 1):
                    if("True" in oldStateNumberSplit[3*(numTasks-numberOfAgents)] and "True" in newStateNumberSplit[3*(numTasks-numberOfAgents)+startCompleteCounter]):
                        nonfailedAction4 = True
                if(numTasks >= 4 and numAgents >= 2):
                    if("True" in oldStateNumberSplit[3*(numTasks-numberOfAgents)+1] and "True" in newStateNumberSplit[3*(numTasks-numberOfAgents)+startCompleteCounter+1]):
                        nonfailedAction4 = True
                if(numTasks >= 4 and numAgents >= 3):
                    if("True" in oldStateNumberSplit[3*(numTasks-numberOfAgents)+2] and "True" in newStateNumberSplit[3*(numTasks-numberOfAgents)+startCompleteCounter+2]):
                        nonfailedAction4 = True
                if(numTasks >= 4 and numAgents >= 4):
                    if("True" in oldStateNumberSplit[3*(numTasks-numberOfAgents)+3] and "True" in newStateNumberSplit[3*(numTasks-numberOfAgents)+startCompleteCounter+3]):
                        nonfailedAction4 = True
                if failedAction4 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf4"]:
                        TargetStates["pickup_shelf4"].append(str(oldStateNumber).replace(" ",""))

                #---------------------------------------------------------------------------------------------------------------------------
                #--------------------------------------------------------------------------------------------------------------------------
                #---------------------------------------------------------------------------------------------------------------------------
                #Deliver Shelf Failure - If an agent has the shelf but the do not offload it into the goal
                nonfailedAction1 = False
                nonfailedAction2 = False
                nonfailedAction3 = False
                nonfailedAction4 = False

                if numberOfAgents == 2:
                    #Shelf 1

                    if(numTasks >= 1 and numAgents >= 1):
                        if("True" in newStateNumberSplit[22] and "False" in oldStateNumberSplit[22]):
                            nonfailedAction1 = True
                    if(numTasks >= 1 and numAgents >= 2):
                        if("True" in newStateNumberSplit[23] and "False" in oldStateNumberSplit[23]):
                            nonfailedAction1 = True
                    if nonfailedAction1 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf1"]:
                            TargetStates["deliver_shelf1"].append(str(newStateNumber).replace(" ",""))

                    #Shelf 2

                    if(numTasks >= 2 and numAgents >= 1):
                        if("True" in newStateNumberSplit[24] and "False" in oldStateNumberSplit[24]):
                            nonfailedAction2 = True
                    if(numTasks >= 2 and numAgents >= 2):
                        if("True" in newStateNumberSplit[25] and "False" in oldStateNumberSplit[25]):
                            nonfailedAction2 = True
                    if nonfailedAction2 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf2"]:
                            TargetStates["deliver_shelf2"].append(str(newStateNumber).replace(" ",""))

                    #Shelf 3

                    if(numTasks >= 3 and numAgents >= 1):
                        if("True" in newStateNumberSplit[26] and "False" in oldStateNumberSplit[26]):
                            nonfailedAction3 = True
                    if(numTasks >= 3 and numAgents >= 2):
                        if("True" in newStateNumberSplit[27] and "False" in oldStateNumberSplit[27]):
                            nonfailedAction3 = True
                    if nonfailedAction3 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf3"]:
                            TargetStates["deliver_shelf3"].append(str(newStateNumber).replace(" ",""))

                    #Shelf 4

                    if(numTasks >= 4 and numAgents >= 1):
                        if("True" in newStateNumberSplit[28] and "False" in oldStateNumberSplit[28]):
                            nonfailedAction4 = True
                    if(numTasks >= 4 and numAgents >= 2):
                        if("True" in newStateNumberSplit[29] and "False" in oldStateNumberSplit[29]):
                            nonfailedAction4 = True
                    if nonfailedAction4 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf4"]:
                            TargetStates["deliver_shelf4"].append(str(newStateNumber).replace(" ",""))

    return UMNumber

def findBestActionRandom(possibleActions,lowCurrentStart,env,userQuery,numberOfAgents,stateList,transitions,highLevelStates,UMNumber,numTasks,numAgents,env_name,shelfs,):
    comboActions = list(itertools.product(*possibleActions))
    choice = random.choice(comboActions)
    obs = env.reset()
    n_obs, reward, done, info = env.step(choice)
    oldStateNumber, newStateNumber, failedAction, n_holdingshelfs, n_deliveredshelfs, TargetStates = convertToHighLevel(obs, n_obs, choice,numTasks,numAgents,env_name,shelfs,currentStart)
    stateList, transitions, highLevelStates, newStateNumber, oldStateNumber, newUMNumber, UMNumber = addHighLevelStates(newStateNumber, currentStart, stateList, transitions, highLevelStates, 0, choice, UMNumber, userQuery, numberOfAgents)
    return choice, UMNumber, stateList, transitions




def main():
    #todo
        #Generate Not Possible Explanation
        #Generate Original Files from Evalution
    #---Make Enviroment---
    start = time.time()
    path = "results/trained_models/479/u213000"
    env_name = "rware-tiny-2ag-easy-v1"

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
    global TargetStates

    #---BackGround Info---
    numberOfAgents = 2
    numberOfTasks = 4


    #---Define Plans and Queries---
    stateList = RWARE_conrollStates.stateList
    transitions = RWARE_conrollTrans.transitions
    highToLowConver = RWARE_conrollHighLow.highToLow

    shelfs = [2,8,30,7,3,11,1,2,5,7,4,15]
    shelfsLIST = [29,10,4,14]

    startState = [False] * (numberOfAgents * numberOfTasks + numberOfAgents * numberOfTasks + numberOfAgents + numberOfTasks + numberOfTasks*numberOfAgents)

    userQuery = {"agent1": ["deliver_shelf4","*","*"],   #Possible Query
    "agent2":["*","deliver_shelf2","deliver_shelf1"]}

    userQuery = {"agent1": ["*","*","*"],   #Not Possible Query
    "agent2":["deliver_shelf4","deliver_shelf2","deliver_shelf1"]}

    freeTasks = []


    RUN_STEPS = 1500
    HIGH_SEARCH_DEPTH = 100
    LOW_SEARCH_DEPTH = 50
    ROLLOUT_AMOUNT = 0
    query_episodes = 3
    episodes = 10
    lossbase = 100
    query_possible = False


    #---Check if rho in G---  ##Don't forget to load gcc module before running
    while query_episodes != 0 and query_possible != True:
        print("THIS IS THE USER QUERY",userQuery)
        query_episodes -= 1

        UMNumber = generateIntialUM(userQuery,transitions,numberOfAgents,startState,numberOfTasks,numberOfAgents,shelfs)


        if userQuery == []:
            print("No user query given")
        else:
            print("SEARCHING...")
            RWARE_abstractToPrism.createPrismModel(numberOfAgents, numberOfTasks, transitions, startState)
            RWARE_abstractToPrism.createProperty(userQuery, numberOfAgents)
            os.system("sh ../../prism-4.7-linux64/bin/prism checkableModel.prism checkablepropertiesFile.pctl -exportresults resultsLogRWARE.txt")
            f = open("resultsLogRWARE.txt", "r")
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
            print("SEARCHING FOR FOIL...")
            startStatesQueue = queue.PriorityQueue()
            startStates = []
            for i in transitions.keys():
                for j in transitions[i]:
                    if j[0] in UMNumber.keys():
                        if UMNumber[j[0]] != float("-inf"):
                            for l in transitions[i]:
                                if l[0] == j[0]:
                                    observations = l[1]
                            startStates.append([-1*UMNumber[j[0]],observations,j[0],i])

            for s in startStates:
                startStatesQueue.put(s)
            counter = 0

            while startStatesQueue.empty() != True and counter != episodes:
                current = time.time()
                if current-start > 3600:
                        return
                holdPlan = []
                max_value = max(UMNumber.values())
                print("Scenario Number: ",counter,"Max U-Value Found: ", max_value)s
                counter = counter + 1
                startingNode = startStatesQueue.get()
                currentStart = startingNode[2]
                currentStartParent = startingNode[3]
                newStateNumber = startingNode[2]
                oldStateNumber = startingNode[3]
                lowCurrentStart = highToLowConver[(currentStart,currentStartParent)]
                if os.path.exists("currentStartStateRWARE.txt"):
                    os.remove("currentStartStateRWARE.txt")
                f = open("currentStartStateRWARE.txt", "w")
                f.write(str(lowCurrentStart) + "*" + str(currentStart))
                f.close()
                obs = env.reset()

                task_locations = {"deliver_shelf1":(shelfs[0],shelfs[1]), "deliver_shelf2":(shelfs[3],shelfs[4]), "deliver_shelf3":(shelfs[6],shelfs[7]),
                "deliver_shelf4":(shelfs[9],shelfs[10])}

                holdPlan.append(currentStart)
                startStatesQueue.put(startingNode) #Continue to fill queue for search until episode run out
                highLevelCounter = 0
                lowLevelCounter = 0
                new_UMNumber = 0
                while highLevelCounter != HIGH_SEARCH_DEPTH and lowLevelCounter != LOW_SEARCH_DEPTH:
                    highLevelStates = {}
                    possibleActions = generateComboActions(lowCurrentStart, env, agents,highToLowConver,currentStart) #Find only the actions allowed in the policy
                    bestAction,UMNumber, stateList, transitions = findBestActionRandom(possibleActions,lowCurrentStart,env,userQuery, numberOfAgents,stateList,transitions,highLevelStates,UMNumber,numberOfTasks,numberOfAgents,env_name,shelfs,)
                    if os.path.exists("currentStartStateRWARE.txt"):
                        os.remove("currentStartStateRWARE.txt")
                    f = open("currentStartStateRWARE.txt", "w")
                    f.write(str(lowCurrentStart) + "*" + str(currentStart))
                    f.close()
                    obs = env.reset()
                    n_obs, reward, done, info = env.step(bestAction)
                    oldStateNumber, newStateNumber, failedAction, n_holdingshelfs, n_deliveredshelfs, TargetStates = convertToHighLevel(obs, n_obs, bestAction,numberOfTasks,numberOfAgents,env_name,shelfs,currentStart)
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
                    lowCurrentStart = list(n_obs[0]) + list(n_obs[1]) #DONT FORGET TO EDIT THIS FOR NUMAGENTS
                    lowLevelCounter = lowLevelCounter + 1

                if new_UMNumber == len(userQuery["agent1"]) and done:  #Check if rho in G
                    RWARE_abstractToPrism.createPrismModel(numberOfAgents, numberOfTasks, transitions, startState)
                    os.system("sh ../../prism-4.7-linux64/bin/prism checkableModel.prism checkablepropertiesFile.pctl -exportresults resultsLogRWARE.txt")
                    f = open("resultsLogRWARE.txt", "r")
                    for line in f:
                        if line != "Result\n":
                            if 0.0 < float(line):
                                print("FOIL IS POSSIBLE")
                                end = time.time()
                                query_possible = True
                                print("Your current query is possible.")
                                return


            print("FOIL IS NOT POSSIBLE!")
            RWARE_generateExplanations.generateNotPossibleExplanation(UMNumber,transitions, TargetStates,userQuery,numberOfAgents)
            userQuery = RWARE_generateNotPossExp_3agTotalQ.genNotPossExp(userQuery, numberOfAgents)
            print("NEW USER QUERY: ", userQuery, "\n")



main()
