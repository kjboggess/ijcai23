import itertools
import os
import time

def createPrismModel(numberOfAgents,numberOfTasks,transitions,startState):
    numberOfLabels = numberOfAgents * numberOfTasks + 1
    features = ["near_shelf1","near_shelf2","near_shelf3","near_shelf4",
    "holding_shelf1","holding_shelf2","holding_shelf3","holding_shelf4",
    "near_goal",
    "pickup_shelf1_comp","pickup_shelf2_comp","pickup_shelf3_comp","pickup_shelf4_comp",
    "deliver_shelf1_comp","deliver_shelf2_comp","deliver_shelf3_comp","deliver_shelf4_comp"]

    startState = [False] * (numberOfAgents * numberOfTasks + numberOfAgents * numberOfTasks + numberOfAgents + numberOfTasks + numberOfTasks*numberOfAgents)
    letsgo = []
    agentFeatures, labels, numberOfCombos = generateLabels(numberOfAgents, features)
    writeToFile(agentFeatures, labels, numberOfTasks,transitions,numberOfCombos,numberOfAgents,features, startState,letsgo)

def buildstate(state,features,transitions,numberOfAgents,letsgo):
    parentString = ""
    childStrings = []
    childString = ""
    splitstate = state.split(",")

    if numberOfAgents == 2:
        breakpoints = [0,8,16,18,22,30,12]

    numberOfTasks = numberOfAgents*2

    if numberOfAgents >= 2:
        for i in range(breakpoints[0],breakpoints[1]):
            if "True" in splitstate[i]:
                parentString = parentString + "(near_shelf"+str(i//numberOfAgents+1)+"_ag"+str(i%numberOfAgents+1)+" = 1) & "
            else:
                parentString = parentString + "(near_shelf"+str(i//numberOfAgents+1)+"_ag"+str(i%numberOfAgents+1)+" = 0) & "
        for i in range(breakpoints[1],breakpoints[2]):
            if "True" in splitstate[i]:
                parentString = parentString + "(holding_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_ag"+str(i%numberOfAgents+1)+" = 1) & "
                parentString = parentString + "(pickup_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_comp_ag"+str(i%numberOfAgents+1)+" = 1) & "
            else:
                parentString = parentString + "(holding_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_ag"+str(i%numberOfAgents+1)+" = 0) & "
                parentString = parentString + "(pickup_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_comp_ag"+str(i%numberOfAgents+1)+" = 0) & "
        for i in range(breakpoints[2],breakpoints[3]):
            if "True" in splitstate[i]:
                parentString = parentString + "(near_goal"+"_ag"+str(i%numberOfAgents+1)+" = 1) & "
            else:
                parentString = parentString + "(near_goal"+"_ag"+str(i%numberOfAgents+1)+" = 0) & "
        for i in range(breakpoints[4],breakpoints[5]):
            if "True" in splitstate[i]:
                if (((i+numberOfAgents)//numberOfAgents+1-breakpoints[-1], (i+numberOfAgents)%numberOfAgents+1)) not in letsgo:
                    letsgo.append(((i+numberOfAgents)//numberOfAgents+1-breakpoints[-1], (i+numberOfAgents)%numberOfAgents+1))
                parentString = parentString + "(deliver_shelf"+str((i+numberOfAgents)//numberOfAgents+1-breakpoints[-1])+"_comp_ag"+str((i+numberOfAgents)%numberOfAgents+1)+" = 1) & "
            else:
                parentString = parentString + "(deliver_shelf"+str((i+numberOfAgents)//numberOfAgents+1-breakpoints[-1])+"_comp_ag"+str((i+numberOfAgents)%numberOfAgents+1)+" = 0) & "

        parentString = parentString[:-3]

        for i in transitions[state]:
            childString = ""
            childstate = i[0].split(",")

            for i in range(breakpoints[0],breakpoints[1]):
                if "True" in childstate[i]:
                    childString = childString + "(near_shelf"+str(i//numberOfAgents+1)+"_ag"+str(i%numberOfAgents+1)+"' = 1) & "
                else:
                    childString = childString + "(near_shelf"+str(i//numberOfAgents+1)+"_ag"+str(i%numberOfAgents+1)+"' = 0) & "
            for i in range(breakpoints[1],breakpoints[2]):
                if "True" in childstate[i]:
                    childString = childString + "(holding_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_ag"+str(i%numberOfAgents+1)+"' = 1) & "
                    childString = childString + "(pickup_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_comp_ag"+str(i%numberOfAgents+1)+"' = 1) & "
                else:
                    childString = childString + "(holding_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_ag"+str(i%numberOfAgents+1)+"' = 0) & "
                    childString = childString + "(pickup_shelf"+str(i//numberOfAgents+1-numberOfTasks)+"_comp_ag"+str(i%numberOfAgents+1)+"' = 0) & "
            for i in range(breakpoints[2],breakpoints[3]):
                if "True" in childstate[i]:
                    childString = childString + "(near_goal"+"_ag"+str(i%numberOfAgents+1)+"' = 1) & "
                else:
                    childString = childString + "(near_goal"+"_ag"+str(i%numberOfAgents+1)+"' = 0) & "

            for i in range(breakpoints[4],breakpoints[5]):
                if "True" in childstate[i] and "False" in splitstate[i]:
                            childString = childString + "(deliver_shelf"+str((i+numberOfAgents)//numberOfAgents+1-breakpoints[-1])+"_comp_ag"+str((i+numberOfAgents)%numberOfAgents+1)+"' = 1) & "
            childStrings.append(childString[:-3])


    return parentString, childStrings,letsgo

def generateLabels(numberOfAgents,features):
    agentNames = []
    agentCombos = []
    labels = []
    agentFeatures = []

    for i in range(1,numberOfAgents+1):
        agentNames.append("ag"+str(i))

    for i in features:
        for j in agentNames:
            agentFeatures.append(i + "_" + j)


    agentCombos = agentNames.copy()

    for i in features:
        if "comp" in i:
            for j in agentCombos:
                if len(j) == 1:
                    labels.append([j[0]+"_"+i, i+"_"+j[0]])
                else:
                    allfeatures = []
                    startString = ""
                    startString = startString+j
                    allfeatures.append(i+"_"+j)
                    labels.append([startString+"_"+i, allfeatures])



    return agentFeatures, labels, len(agentCombos)


def writeToFile(agentFeatures, labels, numberOfTasks, transitions, numberOfCombos, numberOfAgents, features, startState,letsgo):
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
    for i in range(0,len(agentFeatures)):
        if "comp" not in agentFeatures[i]:
            if startState[i] == True:
                f.write(agentFeatures[i]+": [0..1] init 1;\n")
                continue
        f.write(agentFeatures[i]+": [0..1] init 0;\n")


    f.write("\n")
    for i in transitions.keys():
        parent, children,letsgo = buildstate(i,agentFeatures,transitions,numberOfAgents,letsgo)
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


    newPropertyEventually = "(F(("
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

        newPropertyBefore = "(!("
        for j in nextTasks:
            newPropertyBefore = newPropertyBefore + '\"' + j +'_comp\"' + "|"
        if nextTasks != []:
            newPropertyBefore = newPropertyBefore[:-1] + ") U ("
        for j in currentTasks:
            if nextTasks != []:
                newPropertyBefore = newPropertyBefore + '\"' + j +'_comp\"' + "|"
            else:
                newPropertyBefore = ""
            newPropertyEventually = newPropertyEventually + '\"' + j +'_comp\"' + "&"
        newPropertyBefore = newPropertyBefore[:-1] + "))"
        newPropertyEventually = newPropertyEventually[:-1] + ")) & (F(" #
        if nextTasks != []:
            propertyString = propertyString + newPropertyBefore + " & "
            propertyString = propertyString + newPropertyBefore + " & "
    newPropertyDuringP1 = "(!("
    newPropertyDuringP2 = "("
    newPropertyEventually = newPropertyEventually[:-7] + "))" #
    propertyString = propertyString + newPropertyEventually + "]"
    if os.path.exists("checkablepropertiesFile.pctl"):
        os.remove("checkablepropertiesFile.pctl")
    f = open("checkablepropertiesFile.pctl", "w")
    f.write(propertyString)
    f.close()
