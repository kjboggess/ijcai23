import os

def generateNotPossibleExplanation(UMNumber,transitions,nonTargetStates,TargetStates,userQuery,numberOfAgents):
    max_value = max(UMNumber.values())
    failedTasks = []
    for i in range(0,numberOfAgents):
        if userQuery["agent"+str(i+1)][max_value] not in failedTasks:
            failedTasks.append(userQuery["agent"+str(i+1)][max_value])
    if "*" in failedTasks:
                failedTasks.remove("*")

    if os.path.exists("UMNumber.py"):
        os.remove("UMNumber.py")
    f = open("UMNumber.py", "w")
    f.write("failedTasks=" + str(failedTasks) + "\n")
    f.write("UMNumberKeys=" + str(list(UMNumber.keys())) + "\n")
    f.write("targetState=" + str(TargetStates) +"\n")
    f.close()
