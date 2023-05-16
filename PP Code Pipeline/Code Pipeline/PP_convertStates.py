import time

def generateTransitions(obs,n_obs,numVariables,numTasks,numAgents,env_name,plates,actions,nonTargetStates, TargetStates,currentStart):
    #Tasks -> pressplates
    currentStartSplit = str(currentStart).replace("[","").replace("]","").replace(" ","").split(",")

    numVariables = numAgents * numTasks

    failedAction = False
    nonfailedAction = False
    oldStateNumber = [False] * numVariables  #agents*plates
    newStateNumber = [False] * numVariables

    if numAgents == 9:
        plate1_loc = [plates[0],plates[1]]
        plate2_loc = [plates[2],plates[3]]
        plate3_loc = [plates[4],plates[5]]
        plate4_loc = [plates[6],plates[7]]
        goal_loc = [plates[8]]

    if numAgents >= 1:
        agent1Col = float(obs[0][-2])
        agent1Row = float(obs[0][-1])
        n_agent1Col = float(n_obs[0][-2])
        n_agent1Row = float(n_obs[0][-1])
    if numAgents >= 2:
        agent2Col = float(obs[1][-2])
        agent2Row = float(obs[1][-1])
        n_agent2Col = float(n_obs[1][-2])
        n_agent2Row = float(n_obs[1][-1])
    if numAgents >= 3:
        agent3Col = float(obs[2][-2])
        agent3Row = float(obs[2][-1])
        n_agent3Col = float(n_obs[2][-2])
        n_agent3Row = float(n_obs[2][-1])
    if numAgents >= 4:
        agent4Col = float(obs[3][-2])
        agent4Row = float(obs[3][-1])
        n_agent4Col = float(n_obs[3][-2])
        n_agent4Row = float(n_obs[3][-1])
    if numAgents >= 5:
        agent5Col = float(obs[4][-2])
        agent5Row = float(obs[4][-1])
        n_agent5Col = float(n_obs[4][-2])
        n_agent5Row = float(n_obs[4][-1])
    if numAgents >= 6:
        agent6Col = float(obs[5][-2])
        agent6Row = float(obs[5][-1])
        n_agent6Col = float(n_obs[5][-2])
        n_agent6Row = float(n_obs[5][-1])
    if numAgents >= 7:
        agent7Col = float(obs[6][-2])
        agent7Row = float(obs[6][-1])
        n_agent7Col = float(n_obs[6][-2])
        n_agent7Row = float(n_obs[6][-1])
    if numAgents >= 8:
        agent8Col = float(obs[7][-2])
        agent8Row = float(obs[7][-1])
        n_agent8Col = float(n_obs[7][-2])
        n_agent8Row = float(n_obs[7][-1])
    if numAgents >= 9:
        agent9Col = float(obs[8][-2])
        agent9Row = float(obs[8][-1])
        n_agent9Col = float(n_obs[8][-2])
        n_agent9Row = float(n_obs[8][-1])

    if numAgents == 9:
        breakNumbers = [0,9,18,27,36,45]

    counter = 0

    #Plate 1 - Agent 1
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent1Col,agent1Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent1Col,n_agent1Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 1 - Agent 2
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent2Col,agent2Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent2Col,n_agent2Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 1 - Agent 3
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent3Col,agent3Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent3Col,n_agent3Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 1 - Agent 4
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent4Col,agent4Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent4Col,n_agent4Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 1 - Agent 5
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent5Col,agent5Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent5Col,n_agent5Row] in plate1_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
            if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    if numAgents >= 7:
        #Plate 1 - Agent 6
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent6Col,agent6Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent6Col,n_agent6Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 1 - Agent 7
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent7Col,agent7Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent7Col,n_agent7Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

    if numAgents >= 9:
        #Plate 1 - Agent 8
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent8Col,agent8Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent8Col,n_agent8Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 1 - Agent 9
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent9Col,agent9Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or oldStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent9Col,n_agent9Row] in plate1_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 1 or currentStartSplit[breakNumbers[0]:breakNumbers[1]].count("True") == 0):
                if(newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 1 or newStateNumber[breakNumbers[0]:breakNumbers[1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

    #Plate 2 - Agent 1
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent1Col,agent1Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent1Col,n_agent1Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 2 - Agent 2
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent2Col,agent2Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent2Col,n_agent2Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 2 - Agent 3
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent3Col,agent3Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent3Col,n_agent3Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 2 - Agent 4
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent4Col,agent4Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent4Col,n_agent4Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Plate 2 - Agent 5
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent5Col,agent5Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent5Col,n_agent5Row] in plate2_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
            if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    if numAgents >= 7:
        #Plate 2 - Agent 6
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent6Col,agent6Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent6Col,n_agent6Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 2 - Agent 7
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent7Col,agent7Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent7Col,n_agent7Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

    if numAgents >= 9:
        #Plate 2 - Agent 8
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent8Col,agent8Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent8Col,n_agent8Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 2 - Agent 9
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent9Col,agent9Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or oldStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent9Col,n_agent9Row] in plate2_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 1 or currentStartSplit[breakNumbers[1]:breakNumbers[2]].count("True") == 0):
                if(newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 1 or newStateNumber[breakNumbers[1]:breakNumbers[2]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1


    #Plate3
    if numAgents >= 7:
        #Plate 3 - Agent 1
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent1Col,agent1Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent1Col,n_agent1Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 3 - Agent 2
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent2Col,agent2Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent2Col,n_agent2Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 3 - Agent 3
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent3Col,agent3Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent3Col,n_agent3Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 3 - Agent 4
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent4Col,agent4Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent4Col,n_agent4Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 3 - Agent 5
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent5Col,agent5Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent5Col,n_agent5Row] in plate3_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        if numAgents >= 7:
            #Plate 3 - Agent 6
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent6Col,agent6Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent6Col,n_agent6Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

            #Plate 3 - Agent 7
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent7Col,agent7Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent7Col,n_agent7Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

        if numAgents >= 9:
            #Plate 3 - Agent 8
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent8Col,agent8Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent8Col,n_agent8Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

            #Plate 3 - Agent 9
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent9Col,agent9Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or oldStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent9Col,n_agent9Row] in plate3_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 1 or currentStartSplit[breakNumbers[2]:breakNumbers[3]].count("True") == 0):
                    if(newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 1 or newStateNumber[breakNumbers[2]:breakNumbers[3]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1


    #Plate4
    if numAgents >= 9:
        #Plate 4 - Agent 1
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent1Col,agent1Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent1Col,n_agent1Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 4 - Agent 2
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent2Col,agent2Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent2Col,n_agent2Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 4 - Agent 3
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent3Col,agent3Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent3Col,n_agent3Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 4 - Agent 4
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent4Col,agent4Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent4Col,n_agent4Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Plate 4 - Agent 5
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent5Col,agent5Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent5Col,n_agent5Row] in plate4_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        if numAgents >= 7:
            #Plate 4 - Agent 6
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent6Col,agent6Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent6Col,n_agent6Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

            #Plate 4 - Agent 7
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent7Col,agent7Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent7Col,n_agent7Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

        if numAgents >= 9:
            #Plate 4 - Agent 8
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent8Col,agent8Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent8Col,n_agent8Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

            #Plate 4 - Agent 9
            if "True" in currentStartSplit[counter]:
                oldStateNumber[counter] = True
            elif [agent9Col,agent9Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or oldStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
                newStateNumber[counter] = True
            elif [n_agent9Col,n_agent9Row] in plate4_loc or "True" in currentStartSplit[counter]:
                if(currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 1 or currentStartSplit[breakNumbers[3]:breakNumbers[4]].count("True") == 0):
                    if(newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 1 or newStateNumber[breakNumbers[3]:breakNumbers[4]].count(True) == 0):
                        newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1


    #Goal - Agent 1
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent1Col,agent1Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent1Col,n_agent1Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Goal - Agent 2
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent2Col,agent2Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent2Col,n_agent2Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Goal - Agent 3
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent3Col,agent3Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent3Col,n_agent3Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Goal - Agent 4
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent4Col,agent4Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent4Col,n_agent4Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    #Goal 1 - Agent 5
    if "True" in currentStartSplit[counter]:
        oldStateNumber[counter] = True
    elif [agent5Col,agent5Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                oldStateNumber[counter] = True
    else:
        oldStateNumber[counter] = False
    if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
        newStateNumber[counter] = True
    elif [n_agent5Col,n_agent5Row] in goal_loc or "True" in currentStartSplit[counter]:
        if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
            if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                newStateNumber[counter] = True
    else:
        newStateNumber[counter] = False
    counter = counter + 1

    if numAgents >= 7:
        #Goal 1 - Agent 6
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent6Col,agent6Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent6Col,n_agent6Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Goal 1 - Agent 7
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent7Col,agent7Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent7Col,n_agent7Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

    if numAgents >= 9:
        #Goal 1 - Agent 8
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent8Col,agent8Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent8Col,n_agent8Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

        #Goal 1 - Agent 9
        if "True" in currentStartSplit[counter]:
            oldStateNumber[counter] = True
        elif [agent9Col,agent9Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or oldStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if "True" in currentStartSplit[counter] or oldStateNumber[counter] == True:
            newStateNumber[counter] = True
        elif [n_agent9Col,n_agent9Row] in goal_loc or "True" in currentStartSplit[counter]:
            if(currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 1 or currentStartSplit[breakNumbers[-2]:breakNumbers[-1]].count("True") == 0):
                if(newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 1 or newStateNumber[breakNumbers[-2]:breakNumbers[-1]].count(True) == 0):
                    newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1

    #---------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------
    #Press failure: only 1 agent

    onPlate = 0
    for i in range(breakNumbers[0],breakNumbers[1]):
        if newStateNumber[i] == True:
            onPlate = onPlate + 1
    if onPlate == 2:
        TargetStates["plate1"].append(str(newStateNumber).replace(" ",""))
    elif onPlate == 1:
        nonTargetStates["plate1"].append(str(newStateNumber).replace(" ",""))

    onPlate = 0
    for i in range(breakNumbers[1],breakNumbers[2]):
        if newStateNumber[i] == True:
            onPlate = onPlate + 1
    if onPlate == 2:
        TargetStates["plate2"].append(str(newStateNumber).replace(" ",""))
    elif onPlate == 1:
        nonTargetStates["plate2"].append(str(newStateNumber).replace(" ",""))

    if numAgents >=7:
        onPlate = 0
        for i in range(breakNumbers[2],breakNumbers[3]):
            if newStateNumber[i] == True:
                onPlate = onPlate + 1
        if onPlate == 2:
            TargetStates["plate3"].append(str(newStateNumber).replace(" ",""))
        elif onPlate == 1:
            nonTargetStates["plate3"].append(str(newStateNumber).replace(" ",""))

    if numAgents >=9:
        onPlate = 0
        for i in range(breakNumbers[3],breakNumbers[4]):
            if newStateNumber[i] == True:
                onPlate = onPlate + 1
        if onPlate == 2:
            TargetStates["plate4"].append(str(newStateNumber).replace(" ",""))
        elif onPlate == 1:
            nonTargetStates["plate4"].append(str(newStateNumber).replace(" ",""))

    onPlate = 0
    for i in range(breakNumbers[-2],breakNumbers[-1]):
        if newStateNumber[i] == True:
            onPlate = onPlate + 1
    if onPlate == 1:
        TargetStates["goal"].append(str(newStateNumber).replace(" ",""))

    return str(oldStateNumber), str(newStateNumber), failedAction, nonTargetStates, TargetStates
