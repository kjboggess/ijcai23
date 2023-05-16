#Creates a model and property for PRISM model checker
#Any model cheacker could be used if preferred

import itertools
import os

def createPrismModel(numberOfAgents,numberOfTasks,transitions,startState):
    numberOfLabels = numberOfAgents * numberOfTasks + 1
    features = ["fire_comp", "obstacle_comp", "victim_comp"]

    agentFeatures, labels, numberOfCombos = generateLabels(numberOfAgents, features)
    writeToFile(agentFeatures, labels, numberOfTasks,transitions,numberOfCombos,numberOfAgents,features, startState)

def buildstate(state,features,transitions,numberOfAgents):
    parentString = ""
    childStrings = []
    childString = ""
    splitstate = state.split(",")

    if numberOfAgents == 3:
        if "True" in splitstate[0]:
            parentString = parentString + "(fire_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(fire_comp_ag1 = 0) & "
        if "True" in splitstate[1]:
            parentString = parentString + "(obstacle_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(obstacle_comp_ag1 = 0) & "
        if "True" in splitstate[2]:
            parentString = parentString + "(victim_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(victim_comp_ag1 = 0) & "

        if "True" in splitstate[3]:
            parentString = parentString + "(fire_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(fire_comp_ag2 = 0) & "
        if "True" in splitstate[4]:
            parentString = parentString + "(obstacle_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(obstacle_comp_ag2 = 0) & "
        if "True" in splitstate[5]:
            parentString = parentString + "(victim_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(victim_comp_ag2 = 0) & "

        if "True" in splitstate[6]:
            parentString = parentString + "(fire_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(fire_comp_ag3 = 0) & "
        if "True" in splitstate[7]:
            parentString = parentString + "(obstacle_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(obstacle_comp_ag3 = 0) & "
        if "True" in splitstate[8]:
            parentString = parentString + "(victim_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(victim_comp_ag3 = 0) & "

        parentString = parentString[:-3]

        for i in transitions[state]:
            childString = ""
            childstate = i[0].split(",")

            if "True" in childstate[0]:
                childString = childString + "(fire_comp_ag1' = 1) & "
            else:
                childString = childString + "(fire_comp_ag1' = 0) & "
            if "True" in childstate[1]:
                childString = childString + "(obstacle_comp_ag1' = 1) & "
            else:
                childString = childString + "(obstacle_comp_ag1' = 0) & "
            if "True" in childstate[2]:
                childString = childString + "(victim_comp_ag1' = 1) & "
            else:
                childString = childString + "(victim_comp_ag1' = 0) & "

            if "True" in childstate[3]:
                childString = childString + "(fire_comp_ag2' = 1) & "
            else:
                childString = childString + "(fire_comp_ag2' = 0) & "
            if "True" in childstate[4]:
                childString = childString + "(obstacle_comp_ag2' = 1) & "
            else:
                childString = childString + "(obstacle_comp_ag2' = 0) & "
            if "True" in childstate[5]:
                childString = childString + "(victim_comp_ag2' = 1) & "
            else:
                childString = childString + "(victim_comp_ag2' = 0) & "

            if "True" in childstate[6]:
                childString = childString + "(fire_comp_ag3' = 1) & "
            else:
                childString = childString + "(fire_comp_ag3' = 0) & "
            if "True" in childstate[7]:
                childString = childString + "(obstacle_comp_ag3' = 1) & "
            else:
                childString = childString + "(obstacle_comp_ag3' = 0) & "
            if "True" in childstate[8]:
                childString = childString + "(victim_comp_ag3' = 1) & "
            else:
                childString = childString + "(victim_comp_ag3' = 0) & "

            childStrings.append(childString[:-3])


    return parentString, childStrings

def generateLabels(numberOfAgents,features):
    agentNames = []
    agentCombos = []
    labels = []
    agentFeatures = []

    for i in range(1,numberOfAgents+1):
        agentNames.append("ag"+str(i))

    for j in agentNames:
        for i in features:
            agentFeatures.append(i + "_" + j)

    for i in range(1,len(agentNames) + 1):
        for subset in itertools.combinations(agentNames, i):
            agentCombos.append(list(subset))

    for i in features:
        if "comp" in i:
            for j in agentCombos:
                if len(j) == 1:
                    labels.append([j[0]+"_"+i, i+"_"+j[0]])
                else:
                    allfeatures = []
                    startString = ""
                    for k in j:
                        startString = startString+k
                        allfeatures.append(i+"_"+k)
                    labels.append([startString+"_"+i, allfeatures])

    return agentFeatures, labels, len(agentCombos)


def writeToFile(agentFeatures, labels, numberOfTasks, transitions, numberOfCombos, numberOfAgents, features, startState):
    if os.path.exists("checkableModel.prism"):
        os.remove("checkableModel.prism")

    f = open("checkableModel.prism", "w")
    f.write("mdp\n")
    f.write("\n")
    for i in labels:
        if type(i[1]) == list:
            f.write('label \"'+i[0]+'\" = ')
            for j in i[1]:
                f.write('('+j+' = 1)')
                if j != i[1][-1]:
                    f.write(' & ')
            f.write(";\n")
        else:
            f.write('label \"'+i[0]+'\" = ('+i[1]+' = 1);')
            f.write("\n")
    f.write('label \"all_tasks_complete\" = ')

    for j in features:
        if "comp" in j:
            f.write('(')
            for i in range(0,numberOfAgents):
                if i == numberOfAgents-1:
                    if j == features[-1]:
                        f.write('('+j+'_ag'+str(i+1)+' = 1))')
                    else:
                        f.write('('+j+'_ag'+str(i+1)+' = 1)) & ')
                else:
                    f.write('('+j+'_ag'+str(i+1)+' = 1) | ')
    f.write(";\n")
    f.write("\n")
    f.write("module agents\n")
    counter = -1
    for i in range(0,len(agentFeatures)):
        if "comp" not in agentFeatures[i]:
            counter = counter+1
            if startState[counter] == True:
                f.write(agentFeatures[i]+": [0..1] init 1;\n")
                continue
        f.write(agentFeatures[i]+": [0..1] init 0;\n")


    f.write("\n")
    for i in transitions.keys():
        parent, children = buildstate(i,agentFeatures,transitions,numberOfAgents)
        f.write("[go] " + parent + " ->\n")
        for j in range(0,len(transitions[i])):
            if j > 0:
                f.write("+ ")
            if children[j] == children[-1]:
                f.write("("+ str(transitions[i][j][1]) +"/"+ str(transitions[i][j][2]) +"): " + children[j] +"\n")
            else:
                f.write("("+ str(transitions[i][j][1]) +"/"+ str(transitions[i][j][2]) +"): " + children[j] +"\n")
        f.write(";\n")

    f.write("\n")
    f.write("endmodule")
    f.close()
    return

def createProperty(userQuery, numberOfAgents):
    #obstacle_ag1
    propertyString = "Pmax=? ["
    sameCompletion = []
    for i in range(0,len(userQuery["agent1"])):
        sameTaskTime = {}
        for j in range(0,numberOfAgents):
            if userQuery["agent"+str(j+1)][i] != "*":
                if userQuery["agent"+str(j+1)][i] in sameTaskTime.keys():
                    sameTaskTime[userQuery["agent"+str(j+1)][i]].append("ag"+str(j+1))
                else:
                    sameTaskTime[userQuery["agent"+str(j+1)][i]] = ["ag"+str(j+1)]
        sameCompletion.append(sameTaskTime)

    newPropertyEventually = "(F("
    nextTasks = []

    for i in range(0,len(sameCompletion)):
        currentTasks = []
        nextTasks = []
        for j in sameCompletion[i].keys():
            holdString = ""
            for k in sameCompletion[i][j]:
                holdString = holdString + k
            holdString = holdString + "_" + j
            currentTasks.append(holdString)
        if (i+1) <= len(sameCompletion)-1:
            for j in sameCompletion[i+1].keys():
                holdString = ""
                for k in sameCompletion[i+1][j]:
                    holdString = holdString + k
                holdString = holdString + "_" + j
                nextTasks.append(holdString)
        else:
            nextTasks = []

        for j in currentTasks:
            newPropertyEventually = newPropertyEventually + '\"' + j +'_comp\"' + "&"
        newPropertyEventually = newPropertyEventually[:-1] + ") & (F("
    newPropertyEventually = newPropertyEventually[:-7] + ")"
    for i in range(0,len(sameCompletion)):
        newPropertyEventually = newPropertyEventually + ")"
    propertyString = propertyString + newPropertyEventually + "]"

    if os.path.exists("checkablepropertiesFile.pctl"):
        os.remove("checkablepropertiesFile.pctl")
    f = open("checkablepropertiesFile.pctl", "w")
    propertyString = "Pmax=? [" + newPropertyEventually + "]"
    f.write(propertyString)
    f.close()
