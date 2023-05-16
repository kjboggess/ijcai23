import time

def generateTransitions(obs,n_obs,numVariables,numTasks,numAgents,env_name,shelfs,actions,holdingshelfs, deliveredshelfs, TargetStates,currentStart):
    #Tasks -> Pick up shelf, deliver shelf
    #Failure -> Pick up shelf -> Not near shelf or holding another shelf
    #Failure -> Deliver shelf -> Not holding shelf or not in delivery area
    #Features -> Agent# near shelf#, Agent# holding shelf#, agent in delivery area

    currentStart = str(currentStart).replace("[","").replace("]","").replace(" ","").split(",")

    shelfs = [2,8,30,7,3,11,1,2,5,7,4,15]

    numVariables = numAgents * numTasks + numAgents * numTasks + numAgents + numTasks + numTasks*numAgents

    f = open("holdingshelf.txt", "r")
    n_holdingshelfs = f.read()
    f.close()

    f = open("deliveredshelf.txt", "r")
    n_deliveredshelfs = f.read()
    f.close()

    failedAction = False
    nonfailedAction = False
    oldStateNumber = [] #agents*shelfs + agents*shelfs + agents + shelf*agents + shelf*agents
    newStateNumber = []
    for i in range(numVariables):
        oldStateNumber.append(0)
        newStateNumber.append(0)

    if numTasks >= 1:
        obsShelf1Col = float(shelfs[0])
        obsShelf1Row = float(shelfs[1])
        obsShelf1ID = int(shelfs[2])
    if numTasks >= 2:
        obsShelf2Col = float(shelfs[3])
        obsShelf2Row = float(shelfs[4])
        obsShelf2ID = int(shelfs[5])
    if numTasks >= 3:
        obsShelf3Col = float(shelfs[6])
        obsShelf3Row = float(shelfs[7])
        obsShelf3ID = int(shelfs[8])
    if numTasks >= 4:
        obsShelf4Col = float(shelfs[9])
        obsShelf4Row = float(shelfs[10])
        obsShelf4ID = int(shelfs[11])
    if numTasks >= 5:
        obsShelf5Col = float(shelfs[12])
        obsShelf5Row = float(shelfs[13])
        obsShelf5ID = int(shelfs[14])
    if numTasks >= 6:
        obsShelf6Col = float(shelfs[15])
        obsShelf6Row = float(shelfs[16])
        obsShelf6ID = int(shelfs[17])
    if numTasks >= 7:
        obsShelf7Col = float(shelfs[18])
        obsShelf7Row = float(shelfs[19])
        obsShelf7ID = int(shelfs[20])
    if numTasks >= 8:
        obsShelf8Col = float(shelfs[21])
        obsShelf8Row = float(shelfs[22])
        obsShelf8ID = int(shelfs[23])


    if("tiny" in env_name):
        size = (10,11)
    elif("small" in env_name):
        size = (10,20)
    elif("medium" in env_name):
        size = (16,20)
    elif("large" in env_name):
        size = (16,29)

    goal1Col = float(size[0] // 2 - 1)
    goal1Row = float(size[1] - 1)
    goal2Col = float(size[0] // 2)
    goal2Row = float(size[1] - 1)

    if numAgents >= 1:
        agent1Col = float(obs[0][0])
        agent1Row = float(obs[0][1])
        n_agent1Col = float(n_obs[0][0])
        n_agent1Row = float(n_obs[0][1])
    if numAgents >= 2:
        agent2Col = float(obs[1][0])
        agent2Row = float(obs[1][1])
        n_agent2Col = float(n_obs[1][0])
        n_agent2Row = float(n_obs[1][1])
    if numAgents >= 3:
        agent3Col = float(obs[2][0])
        agent3Row = float(obs[2][1])
        n_agent3Col = float(n_obs[2][0])
        n_agent3Row = float(n_obs[2][1])
    if numAgents >= 4:
        agent4Col = float(obs[3][0])
        agent4Row = float(obs[3][1])
        n_agent4Col = float(n_obs[3][0])
        n_agent4Row = float(n_obs[3][1])

    counter = 0
    #Near Shelf 1 - Agent 1
    if(numTasks >= 1 and numAgents >= 1):
        if(agent1Row == obsShelf1Row and agent1Col == obsShelf1Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent1Row == obsShelf1Row and n_agent1Col == obsShelf1Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Near to Shelf 1 - Agent 2
    if(numTasks >= 1 and numAgents >= 2):
        if(agent2Row == obsShelf1Row and agent2Col == obsShelf1Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent2Row == obsShelf1Row and n_agent2Col == obsShelf1Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        #Near to Shelf 1 - Agent 3
        if(numTasks >= 1 and numAgents >= 3):
            if(agent3Row == obsShelf1Row and agent3Col == obsShelf1Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent3Row == obsShelf1Row and n_agent3Col == obsShelf1Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Near to Shelf 1 - Agent 4
        if(numTasks >= 1 and numAgents >= 4):
            if(agent4Row == obsShelf1Row and agent4Col == obsShelf1Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent4Row == obsShelf1Row and n_agent4Col == obsShelf1Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Near Shelf 2 - Agent 1
    if(numTasks >= 2 and numAgents >= 1):
        if(agent1Row == obsShelf2Row and agent1Col == obsShelf2Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent1Row == obsShelf2Row and n_agent1Col == obsShelf2Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Near to Shelf 2 - Agent 2
    if(numTasks >= 2 and numAgents >= 2):
        if(agent2Row == obsShelf2Row and agent2Col == obsShelf2Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent2Row == obsShelf2Row and n_agent2Col == obsShelf2Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Near to Shelf 2 - Agent 3
        if(numTasks >= 2 and numAgents >= 3):
            if(agent3Row == obsShelf2Row and agent3Col == obsShelf2Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent3Row == obsShelf2Row and n_agent3Col == obsShelf2Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Near to Shelf 2 - Agent 4
        if(numTasks >= 2 and numAgents >= 4):
            if(agent4Row == obsShelf2Row and agent4Col == obsShelf2Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent4Row == obsShelf2Row and n_agent4Col == obsShelf2Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Near Shelf 3 - Agent 1
    if(numTasks >= 3 and numAgents >= 1):
        if(agent1Row == obsShelf3Row and agent1Col == obsShelf3Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent1Row == obsShelf3Row and n_agent1Col == obsShelf3Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Near to Shelf 3 - Agent 2
    if(numTasks >= 3 and numAgents >= 2):
        if(agent2Row == obsShelf3Row and agent2Col == obsShelf3Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent2Row == obsShelf3Row and n_agent2Col == obsShelf3Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Near to Shelf 3 - Agent 3
        if(numTasks >= 3 and numAgents >= 3):
            if(agent3Row == obsShelf3Row and agent3Col == obsShelf3Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent3Row == obsShelf3Row and n_agent3Col == obsShelf3Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Near to Shelf 3 - Agent 4
        if(numTasks >= 3 and numAgents >= 4):
            if(agent4Row == obsShelf3Row and agent4Col == obsShelf3Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent4Row == obsShelf3Row and n_agent4Col == obsShelf3Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

#Near Shelf 4 - Agent 1
    if(numTasks >= 4 and numAgents >= 1):
        if(agent1Row == obsShelf4Row and agent1Col == obsShelf4Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent1Row == obsShelf4Row and n_agent1Col == obsShelf4Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Near to Shelf 4 - Agent 2
    if(numTasks >= 4 and numAgents >= 2):
        if(agent2Row == obsShelf4Row and agent2Col == obsShelf4Col):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(n_agent2Row == obsShelf4Row and n_agent2Col == obsShelf4Col):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Near to Shelf 4 - Agent 3
        if(numTasks >= 4 and numAgents >= 3):
            if(agent3Row == obsShelf4Row and agent3Col == obsShelf4Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent3Row == obsShelf4Row and n_agent3Col == obsShelf4Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Near to Shelf 4 - Agent 4
        if(numTasks >= 4 and numAgents >= 4):
            if(agent4Row == obsShelf4Row and agent4Col == obsShelf4Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent4Row == obsShelf4Row and n_agent4Col == obsShelf4Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    if numAgents >= 3:
        #Near Shelf 5 - Agent 1
        if(numTasks >= 5 and numAgents >= 1):
            if(agent1Row == obsShelf5Row and agent1Col == obsShelf5Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent1Row == obsShelf5Row and n_agent1Col == obsShelf5Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Near to Shelf 5 - Agent 2
        if(numTasks >= 5 and numAgents >= 2):
            if(agent2Row == obsShelf5Row and agent2Col == obsShelf5Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent2Row == obsShelf5Row and n_agent2Col == obsShelf5Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Near to Shelf 5 - Agent 3
            if(numTasks >= 5 and numAgents >= 3):
                if(agent3Row == obsShelf5Row and agent3Col == obsShelf5Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent3Row == obsShelf5Row and n_agent3Col == obsShelf5Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Near to Shelf 5 - Agent 4
            if(numTasks >= 5 and numAgents >= 4):
                if(agent4Row == obsShelf5Row and agent4Col == obsShelf5Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent4Row == obsShelf5Row and n_agent4Col == obsShelf5Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    if numAgents >= 3:
        #Near Shelf 6 - Agent 1
        if(numTasks >= 6 and numAgents >= 1):
            if(agent1Row == obsShelf6Row and agent1Col == obsShelf6Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent1Row == obsShelf6Row and n_agent1Col == obsShelf6Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Near to Shelf 6 - Agent 2
        if(numTasks >= 6 and numAgents >= 2):
            if(agent2Row == obsShelf6Row and agent2Col == obsShelf6Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent2Row == obsShelf6Row and n_agent2Col == obsShelf6Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Near to Shelf 6 - Agent 3
            if(numTasks >= 6 and numAgents >= 3):
                if(agent3Row == obsShelf6Row and agent3Col == obsShelf6Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent3Row == obsShelf6Row and n_agent3Col == obsShelf6Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Near to Shelf 6 - Agent 4
            if(numTasks >= 6 and numAgents >= 4):
                if(agent4Row == obsShelf6Row and agent4Col == obsShelf6Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent4Row == obsShelf6Row and n_agent4Col == obsShelf6Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
    if numAgents >= 4:
        #Near Shelf 7 - Agent 1
        if(numTasks >= 7 and numAgents >= 1):
            if(agent1Row == obsShelf7Row and agent1Col == obsShelf7Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent1Row == obsShelf7Row and n_agent1Col == obsShelf7Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Near to Shelf 7 - Agent 2
        if(numTasks >= 7 and numAgents >= 2):
            if(agent2Row == obsShelf7Row and agent2Col == obsShelf7Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent2Row == obsShelf7Row and n_agent2Col == obsShelf7Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Near to Shelf 7 - Agent 3
            if(numTasks >= 7 and numAgents >= 3):
                if(agent3Row == obsShelf7Row and agent3Col == obsShelf7Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent3Row == obsShelf7Row and n_agent3Col == obsShelf7Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Near to Shelf 7 - Agent 4
            if(numTasks >= 7 and numAgents >= 4):
                if(agent4Row == obsShelf7Row and agent4Col == obsShelf7Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent4Row == obsShelf7Row and n_agent4Col == obsShelf7Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    if numAgents >= 4:
        #Near Shelf 8 - Agent 1
        if(numTasks >= 8 and numAgents >= 1):
            if(agent1Row == obsShelf8Row and agent1Col == obsShelf8Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent1Row == obsShelf8Row and n_agent1Col == obsShelf8Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Near to Shelf 8 - Agent 2
        if(numTasks >= 8 and numAgents >= 2):
            if(agent2Row == obsShelf8Row and agent2Col == obsShelf8Col):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(n_agent2Row == obsShelf8Row and n_agent2Col == obsShelf8Col):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Near to Shelf 8 - Agent 3
            if(numTasks >= 8 and numAgents >= 3):
                if(agent3Row == obsShelf8Row and agent3Col == obsShelf8Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent3Row == obsShelf8Row and n_agent3Col == obsShelf8Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Near to Shelf 8 - Agent 4
            if(numTasks >= 8 and numAgents >= 4):
                if(agent4Row == obsShelf8Row and agent4Col == obsShelf8Col):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(n_agent4Row == obsShelf8Row and n_agent4Col == obsShelf8Col):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    #---------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------

    #Holding Shelf 1 - Agent 1
    if(numTasks >= 1 and numAgents >= 1 or "True" in currentStart[counter]):
        if(str((1,obsShelf1ID)) in holdingshelfs):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf1ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Holding Shelf 1 - Agent 2
    if(numTasks >= 1 and numAgents >= 1):
        if(str((2,obsShelf1ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf1ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        #Holding Shelf 1 - Agent 3
        if(numTasks >= 1 and numAgents >= 3):
            if(str((3,obsShelf1ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf1ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Holding Shelf 1 - Agent 4
        if(numTasks >= 1 and numAgents >= 4):
            if(str((4,obsShelf1ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf1ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Holding Shelf 2 - Agent 1
    if(numTasks >= 2 and numAgents >= 1):
        if(str((1,obsShelf2ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf2ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Holding Shelf 2 - Agent 2
    if(numTasks >= 2 and numAgents >= 1):
        if(str((2,obsShelf2ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf2ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        #Holding Shelf 2 - Agent 3
        if(numTasks >= 2 and numAgents >= 3):
            if(str((3,obsShelf2ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf2ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Holding Shelf 2 - Agent 4
        if(numTasks >= 2 and numAgents >= 4):
            if(str((4,obsShelf2ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf2ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Holding Shelf 3 - Agent 1
    if(numTasks >= 3 and numAgents >= 1):
        if(str((1,obsShelf3ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf3ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Holding Shelf 3 - Agent 2
    if(numTasks >= 3 and numAgents >= 1):
        if(str((2,obsShelf3ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf3ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        #Holding Shelf 3 - Agent 3
        if(numTasks >= 3 and numAgents >= 3):
            if(str((3,obsShelf3ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf3ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Holding Shelf 3 - Agent 4
        if(numTasks >= 3 and numAgents >= 4):
            if(str((4,obsShelf3ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf3ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Holding Shelf 4 - Agent 1
    if(numTasks >= 4 and numAgents >= 1):
        if(str((1,obsShelf4ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf4ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Holding Shelf 4 - Agent 2
    if(numTasks >= 4 and numAgents >= 1):
        if(str((2,obsShelf4ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf4ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        #Holding Shelf 4 - Agent 3
        if(numTasks >= 4 and numAgents >= 3):
            if(str((3,obsShelf4ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf4ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #Holding Shelf 4 - Agent 4
        if(numTasks >= 4 and numAgents >= 4):
            if(str((4,obsShelf4ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf4ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 3:
        #Holding Shelf 5 - Agent 1
        if(numTasks >= 5 and numAgents >= 1):
            if(str((1,obsShelf5ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf5ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Holding Shelf 5 - Agent 2
        if(numTasks >= 5 and numAgents >= 1):
            if(str((2,obsShelf5ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf5ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
        if numAgents >= 3:
            #Holding Shelf 5 - Agent 3
            if(numTasks >= 5 and numAgents >= 3):
                if(str((3,obsShelf5ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf5ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Holding Shelf 5 - Agent 4
            if(numTasks >= 5 and numAgents >= 4):
                if(str((4,obsShelf5ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf5ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
    if numAgents >= 3:
        #Holding Shelf 6 - Agent 1
        if(numTasks >= 6 and numAgents >= 1):
            if(str((1,obsShelf6ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf6ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Holding Shelf 6 - Agent 2
        if(numTasks >= 6 and numAgents >= 1):
            if(str((2,obsShelf6ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf6ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
        if numAgents >= 3:
            #Holding Shelf 6 - Agent 3
            if(numTasks >= 6 and numAgents >= 3):
                if(str((3,obsShelf6ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf6ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Holding Shelf 6 - Agent 4
            if(numTasks >= 6 and numAgents >= 4):
                if(str((4,obsShelf6ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf6ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
    if numAgents >= 4:
        #Holding Shelf 7 - Agent 1
        if(numTasks >= 7 and numAgents >= 1):
            if(str((1,obsShelf7ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf7ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Holding Shelf 7 - Agent 2
        if(numTasks >= 7 and numAgents >= 1):
            if(str((2,obsShelf7ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf7ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
        if numAgents >= 3:
            #Holding Shelf 7 - Agent 3
            if(numTasks >= 7 and numAgents >= 3):
                if(str((3,obsShelf7ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf7ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Holding Shelf 7 - Agent 4
            if(numTasks >= 7 and numAgents >= 4):
                if(str((4,obsShelf7ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf7ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
    if numAgents >= 4:
        #Holding Shelf 8 - Agent 1
        if(numTasks >= 8 and numAgents >= 1):
            if(str((1,obsShelf8ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf8ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Holding Shelf 8 - Agent 2
        if(numTasks >= 8 and numAgents >= 1):
            if(str((2,obsShelf8ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf8ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
        if numAgents >= 3:
            #Holding Shelf 8 - Agent 3
            if(numTasks >= 8 and numAgents >= 3):
                if(str((3,obsShelf8ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf8ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1
        if numAgents >= 4:
            #Holding Shelf 8 - Agent 4
            if(numTasks >= 8 and numAgents >= 4):
                if(str((4,obsShelf8ID)) in holdingshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf8ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    #---------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------

    #In Goal - Agent 1
    if(numAgents >= 1):
        if(((agent1Row == goal1Row and agent1Col == goal1Col) or (agent1Row == goal2Row and agent1Col == goal2Col)) and obs[0][2]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(((n_agent1Row == goal1Row and n_agent1Col == goal1Col) or (n_agent1Row == goal2Row and n_agent1Col == goal2Col)) and n_obs[0][2]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #In Goal - Agent 2
    if(numAgents >= 2):
        if(((agent2Row == goal1Row and agent2Col == goal1Col) or (agent2Row == goal2Row and agent2Col == goal2Col)) and obs[1][2]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(((n_agent2Row == goal1Row and n_agent2Col == goal1Col) or (n_agent2Row == goal2Row and n_agent2Col == goal2Col)) and n_obs[1][2]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        #In Goal - Agent 3
        if(numAgents >= 3):
            if(((agent3Row == goal1Row and agent3Col == goal1Col) or (agent3Row == goal2Row and agent3Col == goal2Col)) and obs[2][2]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(((n_agent3Row == goal1Row and n_agent3Col == goal1Col) or (n_agent3Row == goal2Row and n_agent3Col == goal2Col)) and n_obs[2][2]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1
    if numAgents >= 4:
        #In Goal - Agent 4
        if(numAgents >= 4):
            if(((agent4Row == goal1Row and agent4Col == goal1Col) or (agent4Row == goal2Row and agent4Col == goal2Col)) and obs[3][2]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(((n_agent4Row == goal1Row and n_agent4Col == goal1Col) or (n_agent4Row == goal2Row and n_agent4Col == goal2Col)) and n_obs[3][2]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #---------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------

    #PICK UP SHELFS
    if(numTasks >= 1):
        if(str((1,obsShelf1ID)) in holdingshelfs or str((2,obsShelf1ID)) in holdingshelfs or str((3,obsShelf1ID)) in holdingshelfs or str((4,obsShelf1ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf1ID)) in n_holdingshelfs or str((2,obsShelf1ID)) in n_holdingshelfs or str((3,obsShelf1ID)) in n_holdingshelfs or str((4,obsShelf1ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1
    if(numTasks >= 2):
        if(str((1,obsShelf2ID)) in holdingshelfs or str((2,obsShelf2ID)) in holdingshelfs or str((3,obsShelf2ID)) in holdingshelfs or str((4,obsShelf2ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf2ID)) in n_holdingshelfs or str((2,obsShelf2ID)) in n_holdingshelfs or str((3,obsShelf2ID)) in n_holdingshelfs or str((4,obsShelf2ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1
    if(numTasks >= 3):
        if(str((1,obsShelf3ID)) in holdingshelfs or str((2,obsShelf3ID)) in holdingshelfs or str((3,obsShelf3ID)) in holdingshelfs or str((4,obsShelf3ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf3ID)) in n_holdingshelfs or str((2,obsShelf3ID)) in n_holdingshelfs or str((3,obsShelf3ID)) in n_holdingshelfs or str((4,obsShelf3ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1
    if(numTasks >= 4):
        if(str((1,obsShelf4ID)) in holdingshelfs or str((2,obsShelf4ID)) in holdingshelfs or str((3,obsShelf4ID)) in holdingshelfs or str((4,obsShelf4ID)) in holdingshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf4ID)) in n_holdingshelfs or str((2,obsShelf4ID)) in n_holdingshelfs or str((3,obsShelf4ID)) in n_holdingshelfs or str((4,obsShelf4ID)) in n_holdingshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
        else:
            newStateNumber[counter] = False
        counter = counter + 1
    if numAgents >= 3:
        if(numTasks >= 5):
            if(str((1,obsShelf5ID)) in holdingshelfs or str((2,obsShelf5ID)) in holdingshelfs or str((3,obsShelf5ID)) in holdingshelfs or str((4,obsShelf5ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf5ID)) in n_holdingshelfs or str((2,obsShelf5ID)) in n_holdingshelfs or str((3,obsShelf5ID)) in n_holdingshelfs or str((4,obsShelf5ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 3:
        if(numTasks >= 6):
            if(str((1,obsShelf6ID)) in holdingshelfs or str((2,obsShelf6ID)) in holdingshelfs or str((3,obsShelf6ID)) in holdingshelfs or str((4,obsShelf6ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf6ID)) in n_holdingshelfs or str((2,obsShelf6ID)) in n_holdingshelfs or str((3,obsShelf6ID)) in n_holdingshelfs or str((4,obsShelf6ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 4:
        if(numTasks >= 7):
            if(str((1,obsShelf7ID)) in holdingshelfs or str((2,obsShelf7ID)) in holdingshelfs or str((3,obsShelf7ID)) in holdingshelfs or str((4,obsShelf7ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf7ID)) in n_holdingshelfs or str((2,obsShelf7ID)) in n_holdingshelfs or str((3,obsShelf7ID)) in n_holdingshelfs or str((4,obsShelf7ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1
    if numAgents >= 4:
        if(numTasks >= 8):
            if(str((1,obsShelf8ID)) in holdingshelfs or str((2,obsShelf8ID)) in holdingshelfs or str((3,obsShelf8ID)) in holdingshelfs or str((4,obsShelf8ID)) in holdingshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf8ID)) in n_holdingshelfs or str((2,obsShelf8ID)) in n_holdingshelfs or str((3,obsShelf8ID)) in n_holdingshelfs or str((4,obsShelf8ID)) in n_holdingshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
            else:
                newStateNumber[counter] = False
            counter = counter + 1

    #---------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------
    #DElIVER SHELF
    #Delivered Shelf 1 - Agent 1
    if(numTasks >= 1 and numAgents >= 1):
        if(str((1,obsShelf1ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf1ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Delivered Shelf 1 - Agent 2
    if(numTasks >= 1 and numAgents >= 1):
        if(str((2,obsShelf1ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf1ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Delivered Shelf 1 - Agent 3
        if(numTasks >= 1 and numAgents >= 3):
            if(str((3,obsShelf1ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf1ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    if numAgents >= 4:
        #Delivered Shelf 1 - Agent 4
        if(numTasks >= 1 and numAgents >= 4):
            if(str((4,obsShelf1ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf1ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Delivered Shelf 2 - Agent 1
    if(numTasks >= 2 and numAgents >= 1):
        if(str((1,obsShelf2ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf2ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Delivered Shelf 2 - Agent 2
    if(numTasks >= 2 and numAgents >= 1):
        if(str((2,obsShelf2ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf2ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Delivered Shelf 2 - Agent 3
        if(numTasks >= 2 and numAgents >= 3):
            if(str((3,obsShelf2ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf2ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    if numAgents >= 4:
        #Delivered Shelf 2 - Agent 4
        if(numTasks >= 2 and numAgents >= 4):
            if(str((4,obsShelf2ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf2ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Delivered Shelf 3 - Agent 1
    if(numTasks >= 3 and numAgents >= 1):
        if(str((1,obsShelf3ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf3ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Delivered Shelf 3 - Agent 2
    if(numTasks >= 3 and numAgents >= 1):
        if(str((2,obsShelf3ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf3ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Delivered Shelf 3 - Agent 3
        if(numTasks >= 3 and numAgents >= 3):
            if(str((3,obsShelf3ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf3ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    if numAgents >= 4:
        #Delivered Shelf 3 - Agent 4
        if(numTasks >= 3 and numAgents >= 4):
            if(str((4,obsShelf3ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf3ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    #Delivered Shelf 4 - Agent 1
    if(numTasks >= 4 and numAgents >= 1):
        if(str((1,obsShelf4ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((1,obsShelf4ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    #Delivered Shelf 4 - Agent 2
    if(numTasks >= 4 and numAgents >= 1):
        if(str((2,obsShelf4ID)) in deliveredshelfs or "True" in currentStart[counter]):
            oldStateNumber[counter] = True
        else:
            oldStateNumber[counter] = False
        if(str((2,obsShelf4ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
            newStateNumber[counter] = True
            counter = counter + 1
        else:
            newStateNumber[counter] = False
            counter = counter + 1

    if numAgents >= 3:
        #Delivered Shelf 4 - Agent 3
        if(numTasks >= 4 and numAgents >= 3):
            if(str((3,obsShelf4ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((3,obsShelf4ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    if numAgents >= 4:
        #Delivered Shelf 4 - Agent 4
        if(numTasks >= 4 and numAgents >= 4):
            if(str((4,obsShelf4ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((4,obsShelf4ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

    if numAgents >= 3:
        #Delivered Shelf 5 - Agent 1
        if(numTasks >= 5 and numAgents >= 1):
            if(str((1,obsShelf5ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf5ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Delivered Shelf 5 - Agent 2
        if(numTasks >= 5 and numAgents >= 1):
            if(str((2,obsShelf5ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf5ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Delivered Shelf 5 - Agent 3
            if(numTasks >= 5 and numAgents >= 3):
                if(str((3,obsShelf5ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf5ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

        if numAgents >= 4:
            #Delivered Shelf 5 - Agent 4
            if(numTasks >= 5 and numAgents >= 4):
                if(str((4,obsShelf5ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf5ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    if numAgents >= 3:
        #Delivered Shelf 6 - Agent 1
        if(numTasks >= 6 and numAgents >= 1):
            if(str((1,obsShelf6ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf6ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Delivered Shelf 6 - Agent 2
        if(numTasks >= 6 and numAgents >= 1):
            if(str((2,obsShelf6ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf6ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Delivered Shelf 6 - Agent 3
            if(numTasks >= 6 and numAgents >= 3):
                if(str((3,obsShelf6ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf6ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

        if numAgents >= 4:
            #Delivered Shelf 6 - Agent 4
            if(numTasks >= 6 and numAgents >= 4):
                if(str((4,obsShelf6ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf6ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    if numAgents >= 4:
        #Delivered Shelf 7 - Agent 1
        if(numTasks >= 7 and numAgents >= 1):
            if(str((1,obsShelf7ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf7ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Delivered Shelf 7 - Agent 2
        if(numTasks >= 7 and numAgents >= 1):
            if(str((2,obsShelf7ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf7ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Delivered Shelf 7 - Agent 3
            if(numTasks >= 7 and numAgents >= 3):
                if(str((3,obsShelf7ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf7ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

        if numAgents >= 4:
            #Delivered Shelf 7 - Agent 4
            if(numTasks >= 7 and numAgents >= 4):
                if(str((4,obsShelf7ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf7ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    if numAgents >= 4:
        #Delivered Shelf 8 - Agent 1
        if(numTasks >= 8 and numAgents >= 1):
            if(str((1,obsShelf8ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((1,obsShelf8ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        #Delivered Shelf 8 - Agent 2
        if(numTasks >= 8 and numAgents >= 1):
            if(str((2,obsShelf8ID)) in deliveredshelfs or "True" in currentStart[counter]):
                oldStateNumber[counter] = True
            else:
                oldStateNumber[counter] = False
            if(str((2,obsShelf8ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                newStateNumber[counter] = True
                counter = counter + 1
            else:
                newStateNumber[counter] = False
                counter = counter + 1

        if numAgents >= 3:
            #Delivered Shelf 8 - Agent 3
            if(numTasks >= 8 and numAgents >= 3):
                if(str((3,obsShelf8ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((3,obsShelf8ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

        if numAgents >= 4:
            #Delivered Shelf 8 - Agent 4
            if(numTasks >= 8 and numAgents >= 4):
                if(str((4,obsShelf8ID)) in deliveredshelfs or "True" in currentStart[counter]):
                    oldStateNumber[counter] = True
                else:
                    oldStateNumber[counter] = False
                if(str((4,obsShelf8ID)) in n_deliveredshelfs or "True" in currentStart[counter]):
                    newStateNumber[counter] = True
                    counter = counter + 1
                else:
                    newStateNumber[counter] = False
                    counter = counter + 1

    #---------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------
    #Pick up SHELF Failure - If an agent is present at the shelf, but they do not load the shelf
    failedAction1 = False
    nonfailedAction1 = False
    failedAction2 = False
    nonfailedAction2 = False
    failedAction3 = False
    nonfailedAction3 = False
    failedAction4 = False
    nonfailedAction4 = False
    failedAction5 = False
    nonfailedAction5 = False
    failedAction6 = False
    nonfailedAction6 = False
    failedAction7 = False
    nonfailedAction7 = False
    failedAction8 = False
    nonfailedAction8 = False
    #Shelf 1

    if(numTasks >= 1 and numAgents >= 1):
        if(agent1Row == obsShelf1Row and agent1Col == obsShelf1Col and str((1,obsShelf1ID)) in n_holdingshelfs):
            nonfailedAction1 = True
    if(numTasks >= 1 and numAgents >= 2):
        if(agent2Row == obsShelf1Row and agent2Col == obsShelf1Col and str((2,obsShelf1ID)) in n_holdingshelfs):
            nonfailedAction1 = True
    if(numTasks >= 1 and numAgents >= 3):
        if(agent3Row == obsShelf1Row and agent3Col == obsShelf1Col and str((3,obsShelf1ID)) in n_holdingshelfs):
            nonfailedAction1 = True
    if(numTasks >= 1 and numAgents >= 4):
        if(agent4Row == obsShelf1Row and agent4Col == obsShelf1Col and str((4,obsShelf1ID)) in n_holdingshelfs):
            nonfailedAction1 = True
    if nonfailedAction1 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf1"]:
            TargetStates["pickup_shelf1"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 2

    if(numTasks >= 2 and numAgents >= 1):
        if(agent1Row == obsShelf2Row and agent1Col == obsShelf2Col and str((1,obsShelf2ID)) in n_holdingshelfs):
            nonfailedAction2 = True
    if(numTasks >= 2 and numAgents >= 2):
        if(agent2Row == obsShelf2Row and agent2Col == obsShelf2Col and str((2,obsShelf2ID)) in n_holdingshelfs):
            nonfailedAction2 = True
    if(numTasks >= 2 and numAgents >= 3):
        if(agent3Row == obsShelf2Row and agent3Col == obsShelf2Col and str((3,obsShelf2ID)) in n_holdingshelfs):
            nonfailedAction2 = True
    if(numTasks >= 2 and numAgents >= 4):
        if(agent4Row == obsShelf2Row and agent4Col == obsShelf2Col and str((4,obsShelf2ID)) in n_holdingshelfs):
            nonfailedAction2 = True
    if nonfailedAction2 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf2"]:
            TargetStates["pickup_shelf2"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 3

    if(numTasks >= 3 and numAgents >= 1):
        if(agent1Row == obsShelf3Row and agent1Col == obsShelf3Col and str((1,obsShelf3ID)) in n_holdingshelfs):
            nonfailedAction3 = True
    if(numTasks >= 3 and numAgents >= 2):
        if(agent2Row == obsShelf3Row and agent2Col == obsShelf3Col and str((2,obsShelf3ID)) in n_holdingshelfs):
            nonfailedAction3 = True
    if(numTasks >= 3 and numAgents >= 3):
        if(agent3Row == obsShelf3Row and agent3Col == obsShelf3Col and str((3,obsShelf3ID)) in n_holdingshelfs):
            nonfailedAction3 = True
    if(numTasks >= 3 and numAgents >= 4):
        if(agent4Row == obsShelf3Row and agent4Col == obsShelf3Col and str((4,obsShelf3ID)) in n_holdingshelfs):
            nonfailedAction3 = True
    if failedAction3 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf3"]:
            TargetStates["pickup_shelf3"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 4

    if(numTasks >= 4 and numAgents >= 1):
        if(agent1Row == obsShelf4Row and agent1Col == obsShelf4Col and str((1,obsShelf4ID)) in n_holdingshelfs):
            nonfailedAction4 = True
    if(numTasks >= 4 and numAgents >= 2):
        if(agent2Row == obsShelf4Row and agent2Col == obsShelf4Col and str((2,obsShelf4ID)) in n_holdingshelfs):
            nonfailedAction4 = True
    if(numTasks >= 4 and numAgents >= 3):
        if(agent3Row == obsShelf4Row and agent3Col == obsShelf4Col and str((3,obsShelf4ID)) in n_holdingshelfs):
            nonfailedAction4 = True
    if(numTasks >= 4 and numAgents >= 4):
        if(agent4Row == obsShelf4Row and agent4Col == obsShelf4Col and str((4,obsShelf4ID)) in n_holdingshelfs):
            nonfailedAction4 = True
    if failedAction4 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf4"]:
            TargetStates["pickup_shelf4"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 5

    if(numTasks >= 5 and numAgents >= 1):
        if(agent1Row == obsShelf5Row and agent1Col == obsShelf5Col and str((1,obsShelf5ID)) in n_holdingshelfs):
            nonfailedAction5 = True
    if(numTasks >= 5 and numAgents >= 2):
        if(agent2Row == obsShelf5Row and agent2Col == obsShelf5Col and str((2,obsShelf5ID)) in n_holdingshelfs):
            nonfailedAction5 = True
    if(numTasks >= 5 and numAgents >= 3):
        if(agent3Row == obsShelf5Row and agent3Col == obsShelf5Col and str((3,obsShelf5ID)) in n_holdingshelfs):
            nonfailedAction5 = True
    if(numTasks >= 5 and numAgents >= 4):
        if(agent4Row == obsShelf5Row and agent4Col == obsShelf5Col and str((4,obsShelf5ID)) in n_holdingshelfs):
            nonfailedAction5 = True
    if failedAction5 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf5"]:
            TargetStates["pickup_shelf5"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 6

    if(numTasks >= 6 and numAgents >= 1):
        if(agent1Row == obsShelf6Row and agent1Col == obsShelf6Col and str((1,obsShelf6ID)) in n_holdingshelfs):
            nonfailedAction6 = True
    if(numTasks >= 6 and numAgents >= 2):
        if(agent2Row == obsShelf6Row and agent2Col == obsShelf6Col and str((2,obsShelf6ID)) in n_holdingshelfs):
            nonfailedAction6 = True
    if(numTasks >= 6 and numAgents >= 3):
        if(agent3Row == obsShelf6Row and agent3Col == obsShelf6Col and str((3,obsShelf6ID)) in n_holdingshelfs):
            nonfailedAction6 = True
    if(numTasks >= 6 and numAgents >= 4):
        if(agent4Row == obsShelf6Row and agent4Col == obsShelf6Col and str((4,obsShelf6ID)) in n_holdingshelfs):
            nonfailedAction6 = True
    if failedAction6 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf6"]:
            TargetStates["pickup_shelf6"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 7

    if(numTasks >= 7 and numAgents >= 1):
        if(agent1Row == obsShelf7Row and agent1Col == obsShelf7Col and str((1,obsShelf7ID)) in n_holdingshelfs):
            nonfailedAction7 = True
    if(numTasks >= 7 and numAgents >= 2):
        if(agent2Row == obsShelf7Row and agent2Col == obsShelf7Col and str((2,obsShelf7ID)) in n_holdingshelfs):
            nonfailedAction7 = True
    if(numTasks >= 7 and numAgents >= 3):
        if(agent3Row == obsShelf7Row and agent3Col == obsShelf7Col and str((3,obsShelf7ID)) in n_holdingshelfs):
            nonfailedAction7 = True
    if(numTasks >= 7 and numAgents >= 4):
        if(agent4Row == obsShelf7Row and agent4Col == obsShelf7Col and str((4,obsShelf7ID)) in n_holdingshelfs):
            nonfailedAction7 = True
    if failedAction7 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf7"]:
            TargetStates["pickup_shelf7"].append(str(oldStateNumber).replace(" ",""))

    #Shelf 8

    if(numTasks >= 8 and numAgents >= 1):
        if(agent1Row == obsShelf8Row and agent1Col == obsShelf8Col and str((1,obsShelf8ID)) in n_holdingshelfs):
            nonfailedAction8 = True
    if(numTasks >= 8 and numAgents >= 2):
        if(agent2Row == obsShelf8Row and agent2Col == obsShelf8Col and str((2,obsShelf8ID)) in n_holdingshelfs):
            nonfailedAction8 = True
    if(numTasks >= 8 and numAgents >= 3):
        if(agent3Row == obsShelf8Row and agent3Col == obsShelf8Col and str((3,obsShelf8ID)) in n_holdingshelfs):
            nonfailedAction8 = True
    if(numTasks >= 8 and numAgents >= 4):
        if(agent4Row == obsShelf8Row and agent4Col == obsShelf8Col and str((4,obsShelf8ID)) in n_holdingshelfs):
            nonfailedAction8 = True
    if failedAction8 == True and str(oldStateNumber).replace(" ","") not in TargetStates["pickup_shelf8"]:
            TargetStates["pickup_shelf8"].append(str(oldStateNumber).replace(" ",""))

    #---------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------
    #Deliver Shelf Failure - If an agent has the shelf but the do not offload it into the goal
    failedAction1 = False
    nonfailedAction1 = False
    failedAction2 = False
    nonfailedAction2 = False
    failedAction3 = False
    nonfailedAction3 = False
    failedAction4 = False
    nonfailedAction4 = False
    failedAction5 = False
    nonfailedAction5 = False
    failedAction6 = False
    nonfailedAction6 = False
    failedAction7 = False
    nonfailedAction7 = False
    failedAction8 = False
    nonfailedAction8 = False

    #TO DO -> ADD A FAILURE STATE IF SOMEONE ELSE DOES THE TASK
     #Shelf 1

    if(numTasks >= 1 and numAgents >= 1):
        if(str((1,obsShelf1ID)) in n_deliveredshelfs and str((1,obsShelf1ID)) not in deliveredshelfs):
            nonfailedAction1 = True
    if(numTasks >= 1 and numAgents >= 2):
        if(str((2,obsShelf1ID)) in n_deliveredshelfs and str((2,obsShelf1ID)) not in deliveredshelfs):
            nonfailedAction1 = True
    if(numTasks >= 1 and numAgents >= 3):
        if(str((3,obsShelf1ID)) in n_deliveredshelfs and str((3,obsShelf1ID)) not in deliveredshelfs):
            nonfailedAction1 = True
    if(numTasks >= 1 and numAgents >= 4):
        if(str((4,obsShelf1ID)) in n_deliveredshelfs and str((4,obsShelf1ID)) not in deliveredshelfs):
            nonfailedAction1 = True
    if nonfailedAction1 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf1"]:
            TargetStates["deliver_shelf1"].append(str(newStateNumber).replace(" ",""))

    #Shelf 2

    if(numTasks >= 2 and numAgents >= 1):
        if(str((1,obsShelf2ID)) in n_deliveredshelfs and str((1,obsShelf2ID)) not in deliveredshelfs):
            nonfailedAction2 = True
    if(numTasks >= 2 and numAgents >= 2):
        if( str((2,obsShelf2ID)) in n_deliveredshelfs and str((2,obsShelf2ID)) not in deliveredshelfs):
            nonfailedAction2 = True
    if(numTasks >= 2 and numAgents >= 3):
        if(str((3,obsShelf2ID)) in n_deliveredshelfs and str((3,obsShelf2ID)) not in deliveredshelfs):
            nonfailedAction2 = True
    if(numTasks >= 2 and numAgents >= 4):
        if(str((4,obsShelf2ID)) in n_deliveredshelfs and str((4,obsShelf2ID)) not in deliveredshelfs):
            nonfailedAction12 = True
    if nonfailedAction2 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf2"]:
            TargetStates["deliver_shelf2"].append(str(newStateNumber).replace(" ",""))

    #Shelf 3

    if(numTasks >= 3 and numAgents >= 1):
        if(str((1,obsShelf3ID)) in n_deliveredshelfs and str((1,obsShelf3ID)) not in deliveredshelfs):
            nonfailedAction3 = True
    if(numTasks >= 3 and numAgents >= 2):
        if(str((2,obsShelf3ID)) in n_deliveredshelfs and str((2,obsShelf3ID)) not in deliveredshelfs):
            nonfailedAction3 = True
    if(numTasks >= 3 and numAgents >= 3):
        if(str((3,obsShelf3ID)) in n_deliveredshelfs and str((3,obsShelf3ID)) not in deliveredshelfs):
            nonfailedAction3 = True
    if(numTasks >= 3 and numAgents >= 4):
        if(str((4,obsShelf3ID)) in n_deliveredshelfs and str((4,obsShelf3ID)) not in deliveredshelfs):
            nonfailedAction3 = True
    if nonfailedAction3 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf3"]:
            TargetStates["deliver_shelf3"].append(str(newStateNumber).replace(" ",""))

    #Shelf 4

    if(numTasks >= 4 and numAgents >= 1):
        if(str((1,obsShelf4ID)) in n_deliveredshelfs and str((1,obsShelf4ID)) not in deliveredshelfs):
            nonfailedAction4 = True
    if(numTasks >= 4 and numAgents >= 2):
        if(str((2,obsShelf4ID)) in n_deliveredshelfs and str((2,obsShelf4ID)) not in deliveredshelfs):
            nonfailedAction4 = True
    if(numTasks >= 4 and numAgents >= 3):
        if(str((3,obsShelf4ID)) in n_deliveredshelfs and str((3,obsShelf4ID)) not in deliveredshelfs):
            nonfailedAction4 = True
    if(numTasks >= 4 and numAgents >= 4):
        if(str((4,obsShelf4ID)) in n_deliveredshelfs and str((4,obsShelf4ID)) not in deliveredshelfs):
            nonfailedAction4 = True
    if nonfailedAction4 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf4"]:
            TargetStates["deliver_shelf4"].append(str(newStateNumber).replace(" ",""))

    #Shelf 5

    if(numTasks >= 5 and numAgents >= 1):
        if(str((1,obsShelf5ID)) in n_deliveredshelfs and str((1,obsShelf5ID)) not in deliveredshelfs):
            nonfailedAction5 = True
    if(numTasks >= 5 and numAgents >= 2):
        if(str((2,obsShelf5ID)) in n_deliveredshelfs and str((2,obsShelf5ID)) not in deliveredshelfs):
            nonfailedAction5 = True
    if(numTasks >= 5 and numAgents >= 3):
        if(str((3,obsShelf5ID)) in n_deliveredshelfs and str((3,obsShelf5ID)) not in deliveredshelfs):
            nonfailedAction5 = True
    if(numTasks >= 5 and numAgents >= 4):
        if(str((4,obsShelf5ID)) in n_deliveredshelfs and str((4,obsShelf5ID)) not in deliveredshelfs):
            nonfailedAction5 = True
    if nonfailedAction5 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf5"]:
            TargetStates["deliver_shelf5"].append(str(newStateNumber).replace(" ",""))

    #Shelf 6

    if(numTasks >= 6 and numAgents >= 1):
        if(str((1,obsShelf6ID)) in n_deliveredshelfs and str((1,obsShelf6ID)) not in deliveredshelfs):
            nonfailedAction6 = True
    if(numTasks >= 6 and numAgents >= 2):
        if(str((2,obsShelf6ID)) in n_deliveredshelfs and str((2,obsShelf6ID)) not in deliveredshelfs):
            nonfailedAction6 = True
    if(numTasks >= 6 and numAgents >= 3):
        if(str((3,obsShelf6ID)) in n_deliveredshelfs and str((3,obsShelf6ID)) not in deliveredshelfs):
            nonfailedAction6 = True
    if(numTasks >= 6 and numAgents >= 4):
        if(str((4,obsShelf6ID)) in n_deliveredshelfs and str((4,obsShelf6ID)) not in deliveredshelfs):
            nonfailedAction6 = True
    if nonfailedAction6 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf6"]:
            TargetStates["deliver_shelf6"].append(str(newStateNumber).replace(" ",""))

    #Shelf 7

    if(numTasks >= 7 and numAgents >= 1):
        if(str((1,obsShelf7ID)) in n_deliveredshelfs and str((1,obsShelf7ID)) not in deliveredshelfs):
            nonfailedAction7 = True
    if(numTasks >= 7 and numAgents >= 2):
        if(str((2,obsShelf7ID)) in n_deliveredshelfs and str((2,obsShelf7ID)) not in deliveredshelfs):
            nonfailedAction7 = True
    if(numTasks >= 7 and numAgents >= 3):
        if(str((3,obsShelf7ID)) in n_deliveredshelfs and str((3,obsShelf7ID)) not in deliveredshelfs):
            nonfailedAction7= True
    if(numTasks >= 7 and numAgents >= 4):
        if(str((4,obsShelf7ID)) in n_deliveredshelfs and str((4,obsShelf7ID)) not in deliveredshelfs):
            nonfailedAction7 = True
    if nonfailedAction7 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf7"]:
            TargetStates["deliver_shelf7"].append(str(newStateNumber).replace(" ",""))

    #Shelf 8

    if(numTasks >= 8 and numAgents >= 1):
        if(str((1,obsShelf8ID)) in n_deliveredshelfs and str((1,obsShelf8ID)) not in deliveredshelfs):
            nonfailedAction8 = True
    if(numTasks >= 8 and numAgents >= 2):
        if(str((2,obsShelf8ID)) in n_deliveredshelfs and str((2,obsShelf8ID)) not in deliveredshelfs):
            nonfailedAction8 = True
    if(numTasks >= 8 and numAgents >= 3):
        if(str((3,obsShelf8ID)) in n_deliveredshelfs and str((3,obsShelf8ID)) not in deliveredshelfs):
            nonfailedAction8 = True
    if(numTasks >= 8 and numAgents >= 4):
        if(str((4,obsShelf8ID)) in n_deliveredshelfs and str((4,obsShelf8ID)) not in deliveredshelfs):
            nonfailedAction8 = True
    if nonfailedAction8 == True and str(newStateNumber).replace(" ","") not in TargetStates["deliver_shelf8"]:
            TargetStates["deliver_shelf8"].append(str(newStateNumber).replace(" ",""))

    return str(oldStateNumber), str(newStateNumber), failedAction, n_holdingshelfs, n_deliveredshelfs, TargetStates
