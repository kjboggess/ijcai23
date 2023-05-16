# Adapted from:
#Author: Thomas Wagenaar (t.wagenaar@student.tue.nl)
#
# Implementation of the algorithms desribed in the paper "Improving Robot
# Controller Transparency Through Autonomous Policy Explanation" by B. Hayes and
# J.A. Shah.
#Original Code Location: https://gitlab.tue.nl/ha800-hri/hayes-shah

# Import libraries
import json
import UMNumber
import hayes_shah.hs
import time
import importlib

def generatePredicates(failedTask, numberOfAgents):
    isPlate1Agent1 = {
        'true': 'Agent 1 is pressing plate 1',
        'false': 'Agent 1 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent1'] == '1'}

    isPlate1Agent2 = {
        'true': 'Agent 2 is pressing plate 1',
        'false': 'Agent 2 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent2'] == '1'}

    isPlate1Agent3 = {
        'true': 'Agent 3 is pressing plate 1',
        'false': 'Agent 3 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent3'] == '1'}

    isPlate1Agent4 = {
        'true': 'Agent 4 is pressing plate 1',
        'false': 'Agent 4 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent4'] == '1'}

    isPlate1Agent5 = {
        'true': 'Agent 5 is pressing plate 1',
        'false': 'Agent 5 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent5'] == '1'}

    isPlate1Agent6 = {
        'true': 'Agent 6 is pressing plate 1',
        'false': 'Agent 6 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent6'] == '1'}

    isPlate1Agent7 = {
        'true': 'Agent 7 is pressing plate 1',
        'false': 'Agent 7 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent7'] == '1'}

    isPlate1Agent8 = {
        'true': 'Agent 8 is pressing plate 1',
        'false': 'Agent 8 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent8'] == '1'}

    isPlate1Agent9 = {
        'true': 'Agent 9 is pressing plate 1',
        'false': 'Agent 9 is not pressing plate 1',
        'verify': lambda s : s['Plate1Agent9'] == '1'}

    isPlate2Agent1 = {
        'true': 'Agent 1 is pressing plate 2',
        'false': 'Agent 1 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent1'] == '1'}

    isPlate2Agent2 = {
        'true': 'Agent 2 is pressing plate 2',
        'false': 'Agent 2 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent2'] == '1'}

    isPlate2Agent3 = {
        'true': 'Agent 3 is pressing plate 2',
        'false': 'Agent 3 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent3'] == '1'}

    isPlate2Agent4 = {
        'true': 'Agent 4 is pressing plate 2',
        'false': 'Agent 4 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent4'] == '1'}

    isPlate2Agent5 = {
        'true': 'Agent 5 is pressing plate 2',
        'false': 'Agent 5 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent5'] == '1'}

    isPlate2Agent6 = {
        'true': 'Agent 6 is pressing plate 2',
        'false': 'Agent 6 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent6'] == '1'}

    isPlate2Agent7 = {
        'true': 'Agent 7 is pressing plate 2',
        'false': 'Agent 7 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent7'] == '1'}

    isPlate2Agent8 = {
        'true': 'Agent 8 is pressing plate 2',
        'false': 'Agent 8 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent8'] == '1'}

    isPlate2Agent9 = {
        'true': 'Agent 9 is pressing plate 2',
        'false': 'Agent 9 is not pressing plate 2',
        'verify': lambda s : s['Plate2Agent9'] == '1'}

    isPlate3Agent1 = {
        'true': 'Agent 1 is pressing plate 3',
        'false': 'Agent 1 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent1'] == '1'}

    isPlate3Agent2 = {
        'true': 'Agent 2 is pressing plate 3',
        'false': 'Agent 2 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent2'] == '1'}

    isPlate3Agent3 = {
        'true': 'Agent 3 is pressing plate 3',
        'false': 'Agent 3 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent3'] == '1'}

    isPlate3Agent4 = {
        'true': 'Agent 4 is pressing plate 3',
        'false': 'Agent 4 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent4'] == '1'}

    isPlate3Agent5 = {
        'true': 'Agent 5 is pressing plate 3',
        'false': 'Agent 5 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent5'] == '1'}

    isPlate3Agent6 = {
        'true': 'Agent 6 is pressing plate 3',
        'false': 'Agent 6 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent6'] == '1'}

    isPlate3Agent7 = {
        'true': 'Agent 7 is pressing plate 3',
        'false': 'Agent 7 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent7'] == '1'}

    isPlate3Agent8 = {
        'true': 'Agent 8 is pressing plate 3',
        'false': 'Agent 8 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent8'] == '1'}

    isPlate3Agent9 = {
        'true': 'Agent 9 is pressing plate 3',
        'false': 'Agent 9 is not pressing plate 3',
        'verify': lambda s : s['Plate3Agent9'] == '1'}

    isPlate4Agent1 = {
        'true': 'Agent 1 is pressing plate 4',
        'false': 'Agent 1 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent1'] == '1'}

    isPlate4Agent2 = {
        'true': 'Agent 2 is pressing plate 4',
        'false': 'Agent 2 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent2'] == '1'}

    isPlate4Agent3 = {
        'true': 'Agent 3 is pressing plate 4',
        'false': 'Agent 3 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent3'] == '1'}

    isPlate4Agent4 = {
        'true': 'Agent 4 is pressing plate 4',
        'false': 'Agent 4 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent4'] == '1'}

    isPlate4Agent5 = {
        'true': 'Agent 5 is pressing plate 4',
        'false': 'Agent 5 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent5'] == '1'}

    isPlate4Agent6 = {
        'true': 'Agent 6 is pressing plate 4',
        'false': 'Agent 6 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent6'] == '1'}

    isPlate4Agent7 = {
        'true': 'Agent 7 is pressing plate 4',
        'false': 'Agent 7 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent7'] == '1'}

    isPlate4Agent8 = {
        'true': 'Agent 8 is pressing plate 4',
        'false': 'Agent 8 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent8'] == '1'}

    isPlate4Agent9 = {
        'true': 'Agent 9 is pressing plate 4',
        'false': 'Agent 9 is not pressing plate 4',
        'verify': lambda s : s['Plate4Agent9'] == '1'}

    isGoalAgent1 = {
        'true': 'Agent 1 is pressing goal',
        'false': 'Agent 1 is not pressing goal',
        'verify': lambda s : s['GoalAgent1'] == '1'}

    isGoalAgent2 = {
        'true': 'Agent 2 is pressing goal',
        'false': 'Agent 2 is not pressing goal',
        'verify': lambda s : s['GoalAgent2'] == '1'}

    isGoalAgent3 = {
        'true': 'Agent 3 is pressing goal',
        'false': 'Agent 3 is not pressing goal',
        'verify': lambda s : s['GoalAgent3'] == '1'}

    isGoalAgent4 = {
        'true': 'Agent 4 is pressing goal',
        'false': 'Agent 4 is not pressing goal',
        'verify': lambda s : s['GoalAgent4'] == '1'}

    isGoalAgent5 = {
        'true': 'Agent 5 is pressing goal',
        'false': 'Agent 5 is not pressing goal',
        'verify': lambda s : s['GoalAgent5'] == '1'}

    isGoalAgent6 = {
        'true': 'Agent 6 is pressing goal',
        'false': 'Agent 6 is not pressing goal',
        'verify': lambda s : s['GoalAgent6'] == '1'}

    isGoalAgent7 = {
        'true': 'Agent 7 is pressing goal',
        'false': 'Agent 7 is not pressing goal',
        'verify': lambda s : s['GoalAgent7'] == '1'}

    isGoalAgent8 = {
        'true': 'Agent 8 is pressing goal',
        'false': 'Agent 8 is not pressing goal',
        'verify': lambda s : s['GoalAgent8'] == '1'}

    isGoalAgent9 = {
        'true': 'Agent 9 is pressing goal',
        'false': 'Agent 9 is not pressing goal',
        'verify': lambda s : s['GoalAgent9'] == '1'}

    predicates = []
    if numberOfAgents == 9:
        if failedTask == "plate1":
            predicates = [isPlate1Agent1,isPlate1Agent2,isPlate1Agent3,isPlate1Agent4,isPlate1Agent5,isPlate1Agent6,isPlate1Agent7,isPlate1Agent8,isPlate1Agent9]
        if failedTask == "plate2":
            predicates = [isPlate2Agent1,isPlate2Agent2,isPlate2Agent3,isPlate2Agent4,isPlate2Agent5,isPlate2Agent6,isPlate2Agent7,isPlate2Agent8,isPlate2Agent9]
        if failedTask == "plate3":
            predicates = [isPlate3Agent1,isPlate3Agent2,isPlate3Agent3,isPlate3Agent4,isPlate3Agent5,isPlate3Agent6,isPlate3Agent7,isPlate3Agent8,isPlate3Agent9]
        if failedTask == "plate4":
            predicates = [isPlate4Agent1,isPlate4Agent2,isPlate4Agent3,isPlate4Agent4,isPlate4Agent5,isPlate4Agent6,isPlate4Agent7,isPlate4Agent8,isPlate4Agent9]
        if failedTask == "goal":
            predicates = [isGoalAgent1,isGoalAgent2,isGoalAgent3,isGoalAgent4,isGoalAgent5,isGoalAgent6,isGoalAgent7,isGoalAgent8,isGoalAgent9]

    return predicates

def goalFailure(targetState,plateNumber,numberOfAgents):
    states = []
    actions = []
    one = []

    for i in UMNumber.UMNumberKeys:
        state = i.split(",")
        if numberOfAgents == 9:
            holdState = {"GoalAgent1":"0","GoalAgent2":"0","GoalAgent3":"0","GoalAgent4":"0","GoalAgent5":"0","GoalAgent6":"0","GoalAgent7":"0","GoalAgent8":"0","GoalAgent9":"0"}
            if "True" in state[-9]:
                holdState["GoalAgent1"] = '1'
            if "True" in state[-8]:
                holdState["GoalAgent2"] = '1'
            if "True" in state[-7]:
                holdState["GoalAgent3"] = '1'
            if "True" in state[-6]:
                holdState["GoalAgent4"] = '1'
            if "True" in state[-5]:
                holdState["GoalAgent5"] = '1'
            if "True" in state[-4]:
                holdState["GoalAgent6"] = '1'
            if "True" in state[-3]:
                holdState["GoalAgent7"] = '1'
            if "True" in state[-2]:
                holdState["GoalAgent8"] = '1'
            if "True" in state[-1]:
                holdState["GoalAgent9"] = '1'
        states.append(holdState)
        actions.append({'go': 1.0})
    predicates = generatePredicates("goal",numberOfAgents)
    explainer = hayes_shah.hs.Explainer(states, actions, predicates);

    for s in targetState["goal"]:
        state = s.split(",")
        if numberOfAgents == 9:
            holdState = {"GoalAgent1":"0","GoalAgent2":"0","GoalAgent3":"0","GoalAgent4":"0","GoalAgent5":"0","GoalAgent6":"0","GoalAgent7":"0","GoalAgent8":"0","GoalAgent9":"0"}
            if "True" in state[-9]:
                holdState["GoalAgent1"] = '1'
            if "True" in state[-8]:
                holdState["GoalAgent2"] = '1'
            if "True" in state[-7]:
                holdState["GoalAgent3"] = '1'
            if "True" in state[-6]:
                holdState["GoalAgent4"] = '1'
            if "True" in state[-5]:
                holdState["GoalAgent5"] = '1'
            if "True" in state[-4]:
                holdState["GoalAgent6"] = '1'
            if "True" in state[-3]:
                holdState["GoalAgent7"] = '1'
            if "True" in state[-2]:
                holdState["GoalAgent8"] = '1'
            if "True" in state[-1]:
                holdState["GoalAgent9"] = '1'
        one.append(holdState)

    return explainer,one

def plateFailure(targetState,plateNumber,numberOfAgents):
    states = []
    actions = []
    one = []

    for i in UMNumber.UMNumberKeys:
        state = i.split(",")
        if numberOfAgents == 9:
            holdState = {"Plate"+str(plateNumber)+"Agent1":"0","Plate"+str(plateNumber)+"Agent2":"0","Plate"+str(plateNumber)+"Agent3":"0","Plate"+str(plateNumber)+"Agent4":"0","Plate"+str(plateNumber)+"Agent5":"0","Plate"+str(plateNumber)+"Agent6":"0","Plate"+str(plateNumber)+"Agent7":"0","Plate"+str(plateNumber)+"Agent8":"0","Plate"+str(plateNumber)+"Agent9":"0"}
            if "True" in state[(plateNumber-1)*9+0]:
                holdState["Plate"+str(plateNumber)+"Agent1"] = '1'
            if "True" in state[(plateNumber-1)*9+1]:
                holdState["Plate"+str(plateNumber)+"Agent2"] = '1'
            if "True" in state[(plateNumber-1)*9+2]:
                holdState["Plate"+str(plateNumber)+"Agent3"] = '1'
            if "True" in state[(plateNumber-1)*9+3]:
                holdState["Plate"+str(plateNumber)+"Agent4"] = '1'
            if "True" in state[(plateNumber-1)*9+4]:
                holdState["Plate"+str(plateNumber)+"Agent5"] = '1'
            if "True" in state[(plateNumber-1)*9+5]:
                holdState["Plate"+str(plateNumber)+"Agent6"] = '1'
            if "True" in state[(plateNumber-1)*9+6]:
                holdState["Plate"+str(plateNumber)+"Agent7"] = '1'
            if "True" in state[(plateNumber-1)*9+7]:
                holdState["Plate"+str(plateNumber)+"Agent8"] = '1'
            if "True" in state[(plateNumber-1)*9+8]:
                holdState["Plate"+str(plateNumber)+"Agent9"] = '1'
        states.append(holdState)
        actions.append({'go': 1.0})
    predicates = generatePredicates("plate"+str(plateNumber),numberOfAgents)
    explainer = hayes_shah.hs.Explainer(states, actions, predicates);

    for s in targetState["plate"+str(plateNumber)]:
        state = s.split(",")
        if numberOfAgents == 9:
            holdState = {"Plate"+str(plateNumber)+"Agent1":"0","Plate"+str(plateNumber)+"Agent2":"0","Plate"+str(plateNumber)+"Agent3":"0","Plate"+str(plateNumber)+"Agent4":"0","Plate"+str(plateNumber)+"Agent5":"0","Plate"+str(plateNumber)+"Agent6":"0","Plate"+str(plateNumber)+"Agent7":"0","Plate"+str(plateNumber)+"Agent8":"0","Plate"+str(plateNumber)+"Agent9":"0"}
            if "True" in state[(plateNumber-1)*9+0]:
                holdState["Plate"+str(plateNumber)+"Agent1"] = '1'
            if "True" in state[(plateNumber-1)*9+1]:
                holdState["Plate"+str(plateNumber)+"Agent2"] = '1'
            if "True" in state[(plateNumber-1)*9+2]:
                holdState["Plate"+str(plateNumber)+"Agent3"] = '1'
            if "True" in state[(plateNumber-1)*9+3]:
                holdState["Plate"+str(plateNumber)+"Agent4"] = '1'
            if "True" in state[(plateNumber-1)*9+4]:
                holdState["Plate"+str(plateNumber)+"Agent5"] = '1'
            if "True" in state[(plateNumber-1)*9+5]:
                holdState["Plate"+str(plateNumber)+"Agent6"] = '1'
            if "True" in state[(plateNumber-1)*9+6]:
                holdState["Plate"+str(plateNumber)+"Agent7"] = '1'
            if "True" in state[(plateNumber-1)*9+7]:
                holdState["Plate"+str(plateNumber)+"Agent8"] = '1'
            if "True" in state[(plateNumber-1)*9+8]:
                holdState["Plate"+str(plateNumber)+"Agent9"] = '1'
        one.append(holdState)

    return explainer,one


def convertUserQuery(userQuery, failedTask):
    convertedQuery = ''
    timeStep = float('inf')
    for i in userQuery.keys():
        if failedTask in userQuery[i]:
            convertedQuery = convertedQuery + '1'
            timeStep = userQuery[i].index(failedTask)
        else:
            convertedQuery = convertedQuery + '0'

    return convertedQuery, timeStep

def updateUserQuery(userQuery,updatingQuery,failedTask,timeStep,numberOfAgents):
    newAgent = updatingQuery.index("1")
    index = -1
    for i in userQuery.keys():
        if failedTask in userQuery[i]:
            index = userQuery[i].index(failedTask)
            userQuery[i][index] = "*"
            userQuery["agent"+str(index+1)][index] = failedTask
            break

    #print("THIS IS THE NEW USER QUERY", userQuery)

    return userQuery


def genNotPossExp(userQuery, numberOfAgents):
        importlib.reload(UMNumber)
        failedTasks = UMNumber.failedTasks
        targetState = UMNumber.targetState
        for failedTask in failedTasks:
            convertedQuery, timeStep = convertUserQuery(userQuery, failedTask)
            if "goal" in failedTask:
                explainer,one = goalFailure(targetState,int(failedTask[-1]),numberOfAgents)
            if "plate" in failedTask:
                explainer,one = plateFailure(targetState,int(failedTask[-1]),numberOfAgents)
            print(failedTask + ":")
            clauses,bestMinterm_list = explainer.getLanguage(one, convertedQuery,failedTask,timeStep,numberOfAgents)
            print(clauses)
            userQuery = updateUserQuery(userQuery,bestMinterm_list,failedTask,timeStep,numberOfAgents)
            print("")
        return userQuery

def main():
    numberOfAgents = 9
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
    #genNotPossExp(userQuery, numberOfAgents)
main()
