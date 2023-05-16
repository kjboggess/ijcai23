#Collect tasks that are failed or not possible in user's query
import os

def generateNotPossibleExplanation(UMNumber,transitions,TargetStates,userQuery,numberOfAgents):
    max_value = max(UMNumber.values())
    failedTasks = []
    for i in range(0,numberOfAgents): #Look for each possible task
        if userQuery["agent"+str(i+1)][max_value] not in failedTasks:
            failedTasks.append(userQuery["agent"+str(i+1)][max_value])
    if "*" in failedTasks:
                failedTasks.remove("*")

    if os.path.exists("UMNumber.py"):
        os.remove("UMNumber.py")
    f = open("UMNumber.py", "w")
    f.write("failedTasks=" + str(failedTasks) + "\n") #Tasks that were failed
    f.write("UMNumberKeys=" + str(list(UMNumber.keys())) + "\n") #All states
    f.write("targetState=" + str(TargetStates) +"\n") #States were the tasks was possible to complete
    f.close()
