# Adapted from:
#Author: Thomas Wagenaar (t.wagenaar@student.tue.nl)
#
# Implementation of the algorithms desribed in the paper "Improving Robot
# Controller Transparency Through Autonomous Policy Explanation" by B. Hayes and
# J.A. Shah.
#Original Code Location: https://gitlab.tue.nl/ha800-hri/hayes-shah


# Import libraries
import json
import hayes_shah.hs
import time
import UMNumber
import importlib
import operator

def generatePredicates(failedTask,numberOfAgents):
    isAgent1Fire = {
        'true': 'Agent 1 fought the fire',
        'false': 'Agent 1 did not fight the fire',
        'verify': lambda s : s['Agent1Fire'] == '1'}

    isAgent1Obs = {
        'true': 'Agent 1 is removed the obstacle',
        'false': 'Agent 1 did not remove the obstacle',
        'verify': lambda s : s['Agent1Obs'] == '1'}

    isAgent1Vic = {
        'true': 'Agent 1 rescused the victim',
        'false': 'Agent 1 did not rescue the victim',
        'verify': lambda s : s['Agent1Vic'] == '1'}


    isAgent2Fire = {
        'true': 'Agent 2 fought the fire',
        'false': 'Agent 2 did not fight the fire',
        'verify': lambda s : s['Agent2Fire'] == '1'}

    isAgent2Obs = {
        'true': 'Agent 2 removed the obstacle',
        'false': 'Agent 2 did not remove the obstacle',
        'verify': lambda s : s['Agent2Obs'] == '1'}

    isAgent2Vic = {
        'true': 'Agent 2 rescused the victim',
        'false': 'Agent 2 did not rescue the victim',
        'verify': lambda s : s['Agent2Vic'] == '1'}


    isAgent3Fire = {
        'true': 'Agent 3 fought the fire',
        'false': 'Agent 3 did not fight the fire',
        'verify': lambda s : s['Agent3Fire'] == '1'}

    isAgent3Obs = {
        'true': 'Agent 3 removed the obstacle',
        'false': 'Agent 3 did not remove the obstacle',
        'verify': lambda s : s['Agent3Obs'] == '1'}

    isAgent3Vic = {
        'true': 'Agent 3 rescused the victim',
        'false': 'Agent 3 did not rescue the victim',
        'verify': lambda s : s['Agent3Vic'] == '1'}


    if numberOfAgents == 3:
            predicates = [isAgent1Fire,isAgent2Fire,isAgent3Fire,isAgent1Obs,isAgent2Obs,isAgent3Obs,isAgent1Vic,isAgent2Vic,isAgent3Vic]

    return predicates

def taskFailure(targetState,numberOfAgents,failedTask):
    states = []
    actions = []
    one = []
    for i in UMNumber.UMNumberKeys:
        state = i.split(",")
        if numberOfAgents == 3:
            holdState = {'Agent1Fire': '0', 'Agent2Fire': '0', 'Agent3Fire': '0','Agent1Obs': '0', 'Agent2Obs': '0', 'Agent3Obs': '0','Agent1Vic': '0', 'Agent2Vic': '0', 'Agent3Vic': '0'}
            if "True" in state[0]:
                holdState['Agent1Fire'] = '1'
            if "True" in state[3]:
                holdState['Agent2Fire'] = '1'
            if "True" in state[6]:
                holdState['Agent3Fire'] = '1'
            if "True" in state[1]:
                holdState['Agent1Obs'] = '1'
            if "True" in state[4]:
                holdState['Agent2Obs'] = '1'
            if "True" in state[7]:
                holdState['Agent3Obs'] = '1'
            if "True" in state[2]:
                holdState['Agent1Vic'] = '1'
            if "True" in state[5]:
                holdState['Agent2Vic'] = '1'
            if "True" in state[8]:
                holdState['Agent3Vic'] = '1'
        states.append(holdState)
        actions.append({'go': 1.0})
    predicates = generatePredicates("obstacle",numberOfAgents)
    explainer = hayes_shah.hs.Explainer(states, actions, predicates);

    for s in targetState[failedTask]:
        state = s.split(",")
        if numberOfAgents == 3:
            holdState = {'Agent1Fire': '0', 'Agent2Fire': '0', 'Agent3Fire': '0','Agent1Obs': '0', 'Agent2Obs': '0', 'Agent3Obs': '0','Agent1Vic': '0', 'Agent2Vic': '0', 'Agent3Vic': '0'}
            if "True" in state[0]:
                holdState['Agent1Fire'] = '1'
            if "True" in state[3]:
                holdState['Agent2Fire'] = '1'
            if "True" in state[6]:
                holdState['Agent3Fire'] = '1'
            if "True" in state[1]:
                holdState['Agent1Obs'] = '1'
            if "True" in state[4]:
                holdState['Agent2Obs'] = '1'
            if "True" in state[7]:
                holdState['Agent3Obs'] = '1'
            if "True" in state[2]:
                holdState['Agent1Vic'] = '1'
            if "True" in state[5]:
                holdState['Agent2Vic'] = '1'
            if "True" in state[8]:
                holdState['Agent3Vic'] = '1'
        one.append(holdState)

    return explainer,one


def convertUserQuery(userQuery, failedTask):
    convertedQuery = ''
    timeStep = float('inf')
    completedTask = []
    for i in userQuery.keys():
        if failedTask in userQuery[i]:
            timeStep = userQuery[i].index(failedTask)

    for i in userQuery.keys():
        for j in range(0,timeStep+1):
            completedTask.append((int(i[-1]),userQuery[i][j]))

    if (1, 'fire') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (2, 'fire') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (3, 'fire') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"

    if (1, 'obstacle') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (2, 'obstacle') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (3, 'obstacle') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"

    if (1, 'victim') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (2, 'victim') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (3, 'victim') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"

    return convertedQuery, timeStep

def updateUserQuery(userQuery,updatingQuery,failedTask,timeStep,numberOfAgents):
    taskMatch = {}
    agentMatch = {}

    for i in userQuery.keys():
        if userQuery[i][-1] != "*":
            lastTask = userQuery[i][-1]
    convertedUserQuery,_ = convertUserQuery(userQuery,lastTask)

    for i in userQuery.keys():
        for j in range(len(userQuery[i])):
            if userQuery[i][j] not in taskMatch.keys():
                taskMatch[userQuery[i][j]] = j
    taskMatch.pop("*")

    agentMatch["fire"] = updatingQuery[0:3]
    agentMatch["obstacle"] = updatingQuery[3:6]
    agentMatch["victim"] = updatingQuery[6:9]

    for i in agentMatch.keys():
        if '1' in agentMatch[i] and i != failedTask:
            for k,v in taskMatch.items():
                if v >= taskMatch[i] + 1 and v != failedTask:
                    taskMatch[k] += 1
            if taskMatch[i] + 1 > taskMatch[failedTask]:
                taskMatch[failedTask] = taskMatch[i] + 1
        elif "1" not in agentMatch[i] and i != failedTask and taskMatch[i] < taskMatch[failedTask]:
            taskMatch[failedTask] = taskMatch[i] - 1

    sorted_taskMatch = sorted(taskMatch.items(), key=operator.itemgetter(1))
    taskflag = False
    for k in sorted_taskMatch:
        if k[0] == 'fire' and taskflag == True:
            agentMatch[k[0]] = convertedUserQuery[0:3]
        elif k[0] == 'obstacle' and taskflag == True:
            agentMatch[k[0]] = convertedUserQuery[3:6]
        elif k[0] == 'victim' and taskflag == True:
            agentMatch[k[0]] = convertedUserQuery[6:9]
        if k[0] == failedTask:
            taskflag = True

    sorted_taskMatch = sorted(taskMatch.items(), key=operator.itemgetter(1))

    for i in range(len(sorted_taskMatch)):
        task = sorted_taskMatch[i][0]
        agents = agentMatch[task]
        for j in range(len(agents)):
            if agents[j] == '1':
                userQuery["agent"+str(j+1)][i] = task
            else:
                userQuery["agent"+str(j+1)][i] = "*"

    return userQuery


def genNotPossExp(userQuery, numberOfAgents):
        importlib.reload(UMNumber)
        failedTasks = UMNumber.failedTasks
        targetState = UMNumber.targetState
        for failedTask in failedTasks:
            convertedQuery, timeStep = convertUserQuery(userQuery, "fire")
            convertedQuery, timeStep = convertUserQuery(userQuery, failedTask)
            print(failedTask+":")
            explainer,one = taskFailure(targetState,numberOfAgents,failedTask)
            clauses,bestMinterm = explainer.getLanguage(one, convertedQuery,'rescue victim',timeStep,numberOfAgents)
            print(clauses)
            userQuery = updateUserQuery(userQuery,bestMinterm,failedTask,timeStep,numberOfAgents)
            print("")
        return userQuery

def main():
    numberOfAgents = 3
    userQuery = {"agent1": ["*","fire","obstacle"],   #Not Possible Query
    "agent2":["victim","fire","obstacle"],
    "agent3":["*","*","*"]}
    #genNotPossExp(userQuery, numberOfAgents)
main()
