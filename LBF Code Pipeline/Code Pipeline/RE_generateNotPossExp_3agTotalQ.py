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
    isAgent1Apple2 = {
        'true': 'Agent 1 picked apple 2',
        'false': 'Agent 1 did not pick apple 2',
        'verify': lambda s : s['Agent1Apple2'] == '1'}

    isAgent1Apple3 = {
        'true': 'Agent 1 is picked apple 3',
        'false': 'Agent 1 did not pick apple3',
        'verify': lambda s : s['Agent1Apple3'] == '1'}

    isAgent1Apple1 = {
        'true': 'Agent 1 picked apple 1',
        'false': 'Agent 1 did not pick apple 1',
        'verify': lambda s : s['Agent1Apple1'] == '1'}


    isAgent2Apple2 = {
        'true': 'Agent 2 picked apple 2',
        'false': 'Agent 2 did not picked apple 2',
        'verify': lambda s : s['Agent2Apple2'] == '1'}

    isAgent2Apple3 = {
        'true': 'Agent 2 picked apple 3',
        'false': 'Agent 2 did not picked apple 3',
        'verify': lambda s : s['Agent2Apple3'] == '1'}

    isAgent2Apple1 = {
        'true': 'Agent 2 picked apple 1',
        'false': 'Agent 2 did not picked apple 1',
        'verify': lambda s : s['Agent2Apple1'] == '1'}


    isAgent3Apple2 = {
        'true': 'Agent 3 picked apple 2',
        'false': 'Agent 3 did not picked apple 2',
        'verify': lambda s : s['Agent3Apple2'] == '1'}

    isAgent3Apple3 = {
        'true': 'Agent 3 picked apple 3',
        'false': 'Agent 3 did not picked apple 3',
        'verify': lambda s : s['Agent3Apple3'] == '1'}

    isAgent3Apple1 = {
        'true': 'Agent 3 picked apple 1',
        'false': 'Agent 3 did not picked apple 1',
        'verify': lambda s : s['Agent3Apple1'] == '1'}


    if numberOfAgents == 3:
            predicates = [isAgent1Apple2,isAgent2Apple2,isAgent3Apple2,isAgent1Apple3,isAgent2Apple3,isAgent3Apple3,isAgent1Apple1,isAgent2Apple1,isAgent3Apple1]

    return predicates

def taskFailure(targetState,numberOfAgents,failedTask):
    states = []
    actions = []
    one = []
    for i in UMNumber.UMNumberKeys:
        state = i.split(",")
        if numberOfAgents == 3:
            holdState = {'Agent1Apple2': '0', 'Agent2Apple2': '0', 'Agent3Apple2': '0','Agent1Apple3': '0', 'Agent2Apple3': '0', 'Agent3Apple3': '0','Agent1Apple1': '0', 'Agent2Apple1': '0', 'Agent3Apple1': '0'}
            if "True" in state[0]:
                holdState['Agent1Apple2'] = '1'
            if "True" in state[3]:
                holdState['Agent2Apple2'] = '1'
            if "True" in state[6]:
                holdState['Agent3Apple2'] = '1'
            if "True" in state[1]:
                holdState['Agent1Apple3'] = '1'
            if "True" in state[4]:
                holdState['Agent2Apple3'] = '1'
            if "True" in state[7]:
                holdState['Agent3Apple3'] = '1'
            if "True" in state[2]:
                holdState['Agent1Apple1'] = '1'
            if "True" in state[5]:
                holdState['Agent2Apple1'] = '1'
            if "True" in state[8]:
                holdState['Agent3Apple1'] = '1'
        states.append(holdState)
        actions.append({'go': 1.0})
    predicates = generatePredicates("apple2",numberOfAgents)
    explainer = hayes_shah.hs.Explainer(states, actions, predicates);

    for s in targetState[failedTask]:
        state = s.split(",")
        if numberOfAgents == 3:
            holdState = {'Agent1Apple2': '0', 'Agent2Apple2': '0', 'Agent3Apple2': '0','Agent1Apple3': '0', 'Agent2Apple3': '0', 'Agent3Apple3': '0','Agent1Apple1': '0', 'Agent2Apple1': '0', 'Agent3Apple1': '0'}
            if "True" in state[0]:
                holdState['Agent1Apple2'] = '1'
            if "True" in state[3]:
                holdState['Agent2Apple2'] = '1'
            if "True" in state[6]:
                holdState['Agent3Apple2'] = '1'
            if "True" in state[1]:
                holdState['Agent1Apple3'] = '1'
            if "True" in state[4]:
                holdState['Agent2Apple3'] = '1'
            if "True" in state[7]:
                holdState['Agent3Apple3'] = '1'
            if "True" in state[2]:
                holdState['Agent1Apple1'] = '1'
            if "True" in state[5]:
                holdState['Agent2Apple1'] = '1'
            if "True" in state[8]:
                holdState['Agent3Apple1'] = '1'
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

    if (1, 'apple2') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (2, 'apple2') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (3, 'apple2') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"

    if (1, 'apple3') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (2, 'apple3') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (3, 'apple3') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"

    if (1, 'apple1') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (2, 'apple1') in completedTask: convertedQuery = convertedQuery + "1"
    else: convertedQuery = convertedQuery + "0"
    if (3, 'apple1') in completedTask: convertedQuery = convertedQuery + "1"
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

    agentMatch["apple2"] = updatingQuery[0:3]
    agentMatch["apple3"] = updatingQuery[3:6]
    agentMatch["apple1"] = updatingQuery[6:9]

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
        if k[0] == 'apple2' and taskflag == True:
            agentMatch[k[0]] = convertedUserQuery[0:3]
        elif k[0] == 'apple3' and taskflag == True:
            agentMatch[k[0]] = convertedUserQuery[3:6]
        elif k[0] == 'apple1' and taskflag == True:
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
            convertedQuery, timeStep = convertUserQuery(userQuery, "apple2")
            convertedQuery, timeStep = convertUserQuery(userQuery, failedTask)
            print(failedTask+":")
            explainer,one = taskFailure(targetState,numberOfAgents,failedTask)
            clauses,bestMinterm = explainer.getLanguage(one, convertedQuery,'pick apple',timeStep,numberOfAgents)
            print(clauses)
            userQuery = updateUserQuery(userQuery,bestMinterm,failedTask,timeStep,numberOfAgents)
            print("")
        return userQuery

def main():
    numberOfAgents = 3
    userQuery = {"agent1": ["*","*","apple2"],   #Not Possible Query
    "agent2":["apple3","*","apple2"],
    "agent3":["apple3","apple1","*"]}
    #genNotPossExp(userQuery, numberOfAgents)
main()
