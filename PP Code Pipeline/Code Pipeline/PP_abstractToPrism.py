import itertools
import os

def createPrismModel(numberOfAgents,numberOfTasks,transitions,startState):
    numberOfLabels = numberOfAgents * numberOfTasks + 1
    features = ["plate1_comp", "plate2_comp", "plate3_comp", "plate4_comp", "goal_comp"]

    agentFeatures, labels, numberOfCombos = generateLabels(numberOfAgents, features)
    writeToFile(agentFeatures, labels, numberOfTasks,transitions,numberOfCombos,numberOfAgents,features, startState)

def buildstate(state,features,transitions,numberOfAgents):
    parentString = ""
    childStrings = []
    childString = ""
    splitstate = state.split(",")

    if numberOfAgents == 9:
        if "True" in splitstate[0]:
            parentString = parentString + "(plate1_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag1 = 0) & "
        if "True" in splitstate[1]:
            parentString = parentString + "(plate1_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag2 = 0) & "
        if "True" in splitstate[2]:
            parentString = parentString + "(plate1_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag3 = 0) & "
        if "True" in splitstate[3]:
            parentString = parentString + "(plate1_comp_ag4 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag4 = 0) & "
        if "True" in splitstate[4]:
            parentString = parentString + "(plate1_comp_ag5 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag5 = 0) & "
        if "True" in splitstate[5]:
            parentString = parentString + "(plate1_comp_ag6 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag6 = 0) & "
        if "True" in splitstate[6]:
            parentString = parentString + "(plate1_comp_ag7 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag7 = 0) & "
        if "True" in splitstate[7]:
            parentString = parentString + "(plate1_comp_ag8 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag8 = 0) & "
        if "True" in splitstate[8]:
            parentString = parentString + "(plate1_comp_ag9 = 1) & "
        else:
            parentString = parentString + "(plate1_comp_ag9 = 0) & "

        if "True" in splitstate[9]:
            parentString = parentString + "(plate2_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag1 = 0) & "
        if "True" in splitstate[10]:
            parentString = parentString + "(plate2_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag2 = 0) & "
        if "True" in splitstate[11]:
            parentString = parentString + "(plate2_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag3 = 0) & "
        if "True" in splitstate[12]:
            parentString = parentString + "(plate2_comp_ag4 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag4 = 0) & "
        if "True" in splitstate[13]:
            parentString = parentString + "(plate2_comp_ag5 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag5 = 0) & "
        if "True" in splitstate[14]:
            parentString = parentString + "(plate2_comp_ag6 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag6 = 0) & "
        if "True" in splitstate[15]:
            parentString = parentString + "(plate2_comp_ag7 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag7 = 0) & "
        if "True" in splitstate[16]:
            parentString = parentString + "(plate2_comp_ag8 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag8 = 0) & "
        if "True" in splitstate[17]:
            parentString = parentString + "(plate2_comp_ag9 = 1) & "
        else:
            parentString = parentString + "(plate2_comp_ag9 = 0) & "

        if "True" in splitstate[18]:
            parentString = parentString + "(plate3_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag1 = 0) & "
        if "True" in splitstate[19]:
            parentString = parentString + "(plate3_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag2 = 0) & "
        if "True" in splitstate[20]:
            parentString = parentString + "(plate3_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag3 = 0) & "
        if "True" in splitstate[21]:
            parentString = parentString + "(plate3_comp_ag4 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag4 = 0) & "
        if "True" in splitstate[22]:
            parentString = parentString + "(plate3_comp_ag5 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag5 = 0) & "
        if "True" in splitstate[23]:
            parentString = parentString + "(plate3_comp_ag6 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag6 = 0) & "
        if "True" in splitstate[24]:
            parentString = parentString + "(plate3_comp_ag7 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag7 = 0) & "
        if "True" in splitstate[25]:
            parentString = parentString + "(plate3_comp_ag8 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag8 = 0) & "
        if "True" in splitstate[26]:
            parentString = parentString + "(plate3_comp_ag9 = 1) & "
        else:
            parentString = parentString + "(plate3_comp_ag9 = 0) & "

        if "True" in splitstate[27]:
            parentString = parentString + "(plate4_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag1 = 0) & "
        if "True" in splitstate[28]:
            parentString = parentString + "(plate4_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag2 = 0) & "
        if "True" in splitstate[29]:
            parentString = parentString + "(plate4_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag3 = 0) & "
        if "True" in splitstate[30]:
            parentString = parentString + "(plate4_comp_ag4 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag4 = 0) & "
        if "True" in splitstate[31]:
            parentString = parentString + "(plate4_comp_ag5 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag5 = 0) & "
        if "True" in splitstate[32]:
            parentString = parentString + "(plate4_comp_ag6 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag6 = 0) & "
        if "True" in splitstate[33]:
            parentString = parentString + "(plate4_comp_ag7 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag7 = 0) & "
        if "True" in splitstate[34]:
            parentString = parentString + "(plate4_comp_ag8 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag8 = 0) & "
        if "True" in splitstate[35]:
            parentString = parentString + "(plate4_comp_ag9 = 1) & "
        else:
            parentString = parentString + "(plate4_comp_ag9 = 0) & "

        if "True" in splitstate[36]:
            parentString = parentString + "(goal_comp_ag1 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag1 = 0) & "
        if "True" in splitstate[37]:
            parentString = parentString + "(goal_comp_ag2 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag2 = 0) & "
        if "True" in splitstate[38]:
            parentString = parentString + "(goal_comp_ag3 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag3 = 0) & "
        if "True" in splitstate[39]:
            parentString = parentString + "(goal_comp_ag4 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag4 = 0) & "
        if "True" in splitstate[40]:
            parentString = parentString + "(goal_comp_ag5 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag5 = 0) & "
        if "True" in splitstate[41]:
            parentString = parentString + "(goal_comp_ag6 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag6 = 0) & "
        if "True" in splitstate[42]:
            parentString = parentString + "(goal_comp_ag7 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag7 = 0) & "
        if "True" in splitstate[43]:
            parentString = parentString + "(goal_comp_ag8 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag8 = 0) & "
        if "True" in splitstate[44]:
            parentString = parentString + "(goal_comp_ag9 = 1) & "
        else:
            parentString = parentString + "(goal_comp_ag9 = 0) & "

        parentString = parentString[:-3]

        for i in transitions[state]:
            childString = ""
            childstate = i[0].split(",")

            if "True" in childstate[0]:
                childString = childString + "(plate1_comp_ag1' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag1' = 0) & "
            if "True" in childstate[1]:
                childString = childString + "(plate1_comp_ag2' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag2' = 0) & "
            if "True" in childstate[2]:
                childString = childString + "(plate1_comp_ag3' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag3' = 0) & "
            if "True" in childstate[3]:
                childString = childString + "(plate1_comp_ag4' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag4' = 0) & "
            if "True" in childstate[4]:
                childString = childString + "(plate1_comp_ag5' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag5' = 0) & "
            if "True" in childstate[5]:
                childString = childString + "(plate1_comp_ag6' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag6' = 0) & "
            if "True" in childstate[6]:
                childString = childString + "(plate1_comp_ag7' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag7' = 0) & "
            if "True" in childstate[7]:
                childString = childString + "(plate1_comp_ag8' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag8' = 0) & "
            if "True" in childstate[8]:
                childString = childString + "(plate1_comp_ag9' = 1) & "
            else:
                childString = childString + "(plate1_comp_ag9' = 0) & "

            if "True" in childstate[9]:
                childString = childString + "(plate2_comp_ag1' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag1' = 0) & "
            if "True" in childstate[10]:
                childString = childString + "(plate2_comp_ag2' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag2' = 0) & "
            if "True" in childstate[11]:
                childString = childString + "(plate2_comp_ag3' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag3' = 0) & "
            if "True" in childstate[12]:
                childString = childString + "(plate2_comp_ag4' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag4' = 0) & "
            if "True" in childstate[13]:
                childString = childString + "(plate2_comp_ag5' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag5' = 0) & "
            if "True" in childstate[14]:
                childString = childString + "(plate2_comp_ag6' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag6' = 0) & "
            if "True" in childstate[15]:
                childString = childString + "(plate2_comp_ag7' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag7' = 0) & "
            if "True" in childstate[16]:
                childString = childString + "(plate2_comp_ag8' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag8' = 0) & "
            if "True" in childstate[17]:
                childString = childString + "(plate2_comp_ag9' = 1) & "
            else:
                childString = childString + "(plate2_comp_ag9' = 0) & "

            if "True" in childstate[18]:
                childString = childString + "(plate3_comp_ag1' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag1' = 0) & "
            if "True" in childstate[19]:
                childString = childString + "(plate3_comp_ag2' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag2' = 0) & "
            if "True" in childstate[20]:
                childString = childString + "(plate3_comp_ag3' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag3' = 0) & "
            if "True" in childstate[21]:
                childString = childString + "(plate3_comp_ag4' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag4' = 0) & "
            if "True" in childstate[22]:
                childString = childString + "(plate3_comp_ag5' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag5' = 0) & "
            if "True" in childstate[23]:
                childString = childString + "(plate3_comp_ag6' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag6' = 0) & "
            if "True" in childstate[24]:
                childString = childString + "(plate3_comp_ag7' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag7' = 0) & "
            if "True" in childstate[25]:
                childString = childString + "(plate3_comp_ag8' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag8' = 0) & "
            if "True" in childstate[26]:
                childString = childString + "(plate3_comp_ag9' = 1) & "
            else:
                childString = childString + "(plate3_comp_ag9' = 0) & "

            if "True" in childstate[27]:
                childString = childString + "(plate4_comp_ag1' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag1' = 0) & "
            if "True" in childstate[28]:
                childString = childString + "(plate4_comp_ag2' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag2' = 0) & "
            if "True" in childstate[29]:
                childString = childString + "(plate4_comp_ag3' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag3' = 0) & "
            if "True" in childstate[30]:
                childString = childString + "(plate4_comp_ag4' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag4' = 0) & "
            if "True" in childstate[31]:
                childString = childString + "(plate4_comp_ag5' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag5' = 0) & "
            if "True" in childstate[32]:
                childString = childString + "(plate4_comp_ag6' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag6' = 0) & "
            if "True" in childstate[33]:
                childString = childString + "(plate4_comp_ag7' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag7' = 0) & "
            if "True" in childstate[34]:
                childString = childString + "(plate4_comp_ag8' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag8' = 0) & "
            if "True" in childstate[35]:
                childString = childString + "(plate4_comp_ag9' = 1) & "
            else:
                childString = childString + "(plate4_comp_ag9' = 0) & "

            if "True" in childstate[36]:
                childString = childString + "(goal_comp_ag1' = 1) & "
            else:
                childString = childString + "(goal_comp_ag1' = 0) & "
            if "True" in childstate[37]:
                childString = childString + "(goal_comp_ag2' = 1) & "
            else:
                childString = childString + "(goal_comp_ag2' = 0) & "
            if "True" in childstate[38]:
                childString = childString + "(goal_comp_ag3' = 1) & "
            else:
                childString = childString + "(goal_comp_ag3' = 0) & "
            if "True" in childstate[39]:
                childString = childString + "(goal_comp_ag4' = 1) & "
            else:
                childString = childString + "(goal_comp_ag4' = 0) & "
            if "True" in childstate[40]:
                childString = childString + "(goal_comp_ag5' = 1) & "
            else:
                childString = childString + "(goal_comp_ag5' = 0) & "
            if "True" in childstate[41]:
                childString = childString + "(goal_comp_ag6' = 1) & "
            else:
                childString = childString + "(goal_comp_ag6' = 0) & "
            if "True" in childstate[42]:
                childString = childString + "(goal_comp_ag7' = 1) & "
            else:
                childString = childString + "(goal_comp_ag7' = 0) & "
            if "True" in childstate[43]:
                childString = childString + "(goal_comp_ag8' = 1) & "
            else:
                childString = childString + "(goal_comp_ag8' = 0) & "
            if "True" in childstate[44]:
                childString = childString + "(goal_comp_ag9' = 1) & "
            else:
                childString = childString + "(goal_comp_ag9' = 0) & "

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
    for i in range(0,len(agentFeatures)):
        if "comp" not in agentFeatures[i]:
            if startState[i] == True:
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
        newPropertyEventually = newPropertyEventually[:-1] + ")) & (F("
        if nextTasks != []:
            propertyString = propertyString + newPropertyBefore + " & "
            propertyString = propertyString + newPropertyBefore + " & "
    newPropertyDuringP1 = "(!("
    newPropertyDuringP2 = "("
    newPropertyEventually = newPropertyEventually[:-7] + "))"
    propertyString = propertyString + newPropertyEventually + "]"
    if os.path.exists("checkablepropertiesFile.pctl"):
        os.remove("checkablepropertiesFile.pctl")
    f = open("checkablepropertiesFile.pctl", "w")
    f.write(propertyString)
    f.close()
