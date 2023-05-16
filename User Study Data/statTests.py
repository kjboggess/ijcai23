import csv
from scipy import stats
import numpy as np
import xlsxwriter

def main():
    print("Running Tests")

    baseGood1 = []
    baseGood2 = []
    baseGood3 = []
    baseGood4 = []
    baseGood5 = []
    baseGood6 = []
    baseGood7 = []

    ourGood1 = []
    ourGood2 = []
    ourGood3 = []
    ourGood4 = []
    ourGood5 = []
    ourGood6 = []
    ourGood7 = []

    correctOurs = []
    correctBase = []

    with open('ExplanationData.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            counter = -1
            holdList = []
            for item in row:
                counter = counter + 1
                if(counter == 0 and item in ["1","2","3","4","5"]):
                    ourGood1.append(int(item))
                if(counter == 1 and item in ["1","2","3","4","5"]):
                    ourGood2.append(int(item))
                if(counter == 2 and item in ["1","2","3","4","5"]):
                    ourGood3.append(int(item))
                if(counter == 3 and item in ["1","2","3","4","5"]):
                    ourGood4.append(int(item))
                if(counter == 4 and item in ["1","2","3","4","5"]):
                    ourGood5.append(int(item))
                if(counter == 5 and item in ["1","2","3","4","5"]):
                    ourGood6.append(int(item))
                if(counter == 6 and item in ["1","2","3","4","5"]):
                    ourGood7.append(int(item))
                if(counter == 7 and item in ["1","2","3","4","5"]):
                    baseGood1.append(int(item))
                if(counter == 8 and item in ["1","2","3","4","5"]):
                    baseGood2.append(int(item))
                if(counter == 9 and item in ["1","2","3","4","5"]):
                    baseGood3.append(int(item))
                if(counter == 10 and item in ["1","2","3","4","5"]):
                    baseGood4.append(int(item))
                if(counter == 11 and item in ["1","2","3","4","5"]):
                    baseGood5.append(int(item))
                if(counter == 12 and item in ["1","2","3","4","5"]):
                    baseGood6.append(int(item))
                if(counter == 13 and item in ["1","2","3","4","5"]):
                    baseGood7.append(int(item))
                if(counter == 14 and item in ["0","1","2","3","4"]):
                    correctOurs.append(int(item))
                if(counter == 15 and item in ["0","1","2","3","4"]):
                    correctBase.append(int(item))

    Good1Diff = []
    for i in range(0,len(baseGood1)):
        Good1Diff.append(baseGood1[i]-ourGood1[i])
    Good2Diff = []
    for i in range(0,len(baseGood2)):
        Good2Diff.append(baseGood2[i]-ourGood2[i])
    Good3Diff = []
    for i in range(0,len(baseGood3)):
        Good3Diff.append(baseGood3[i]-ourGood3[i])
    Good4Diff = []
    for i in range(0,len(baseGood4)):
        Good4Diff.append(baseGood4[i]-ourGood4[i])
    Good5Diff = []
    for i in range(0,len(baseGood5)):
        Good5Diff.append(baseGood5[i]-ourGood5[i])
    Good6Diff = []
    for i in range(0,len(baseGood6)):
        Good6Diff.append(baseGood6[i]-ourGood6[i])
    Good7Diff = []
    for i in range(0,len(baseGood7)):
        Good7Diff.append(baseGood7[i]-ourGood7[i])

    print("Query Good 1:")
    print("BaseAvg:",(sum(baseGood1)/len(baseGood1)),"BaseStd:",np.std(baseGood1)," ","OurAvg:",(sum(ourGood1)/len(ourGood1)),"OurStd:",np.std(ourGood1))
    w, p = stats.wilcoxon(Good1Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood1, ourGood1))
    beep, boop = stats.ranksums(baseGood1, ourGood1)
    print("R:",beep/np.sqrt(88+88))
    print("")

    print("Query Good 2:")
    print("BaseAvg:",(sum(baseGood2)/len(baseGood2)),"BaseStd:",np.std(baseGood2)," ","OurAvg:",(sum(ourGood2)/len(ourGood2)),"OurStd:",np.std(ourGood2))
    w, p = stats.wilcoxon(Good2Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood2, ourGood2))
    beep, boop = stats.ranksums(baseGood2, ourGood2)
    print("R:",beep/np.sqrt(88+88))
    print("")

    print("Query Good 3:")
    print("BaseAvg:",(sum(baseGood3)/len(baseGood3)),"BaseStd:",np.std(baseGood3)," ","OurAvg:",(sum(ourGood3)/len(ourGood3)),"OurStd:",np.std(ourGood3))
    w, p = stats.wilcoxon(Good3Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood3, ourGood3))
    beep, boop = stats.ranksums(baseGood3, ourGood3)
    print("R:",beep/np.sqrt(88+88))
    print("")

    print("Query Good 4:")
    print("BaseAvg:",(sum(baseGood4)/len(baseGood4)),"BaseStd:",np.std(baseGood4)," ","OurAvg:",(sum(ourGood4)/len(ourGood4)),"OurStd:",np.std(ourGood4))
    w, p = stats.wilcoxon(Good4Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood4, ourGood4))
    beep, boop = stats.ranksums(baseGood4, ourGood4)
    print("R:",beep/np.sqrt(88+88))
    print("")

    print("Query Good 5:")
    print("BaseAvg:",(sum(baseGood5)/len(baseGood5)),"BaseStd:",np.std(baseGood5)," ","OurAvg:",(sum(ourGood5)/len(ourGood5)),"OurStd:",np.std(ourGood5))
    w, p = stats.wilcoxon(Good5Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood5, ourGood5))
    beep, boop = stats.ranksums(baseGood5, ourGood5)
    print("R:",beep/np.sqrt(88+88))
    print("")

    print("Query Good 6:")
    print("BaseAvg:",(sum(baseGood6)/len(baseGood6)),"BaseStd:",np.std(baseGood6)," ","OurAvg:",(sum(ourGood6)/len(ourGood6)),"OurStd:",np.std(ourGood6))
    w, p = stats.wilcoxon(Good6Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood6, ourGood6))
    beep, boop = stats.ranksums(baseGood6, ourGood6)
    print("R:",beep/np.sqrt(88+88))
    print("")

    print("Query Good 7:")
    print("BaseAvg:",(sum(baseGood7)/len(baseGood7)),"BaseStd:",np.std(baseGood7)," ","OurAvg:",(sum(ourGood7)/len(ourGood7)),"OurStd:",np.std(ourGood7))
    w, p = stats.wilcoxon(Good7Diff)
    print("W:",w)
    print("p:",p)
    print(stats.ranksums(baseGood7, ourGood7))
    beep, boop = stats.ranksums(baseGood7, ourGood7)
    print("R:",beep/np.sqrt(88+88))
    print("")



    correctDiff = []
    for i in range(0,len(correctOurs)):
        correctDiff.append(correctBase[i]-correctOurs[i])

    print("")
    print("# Correct T-Test:", stats.ttest_rel(correctBase, correctOurs))
    cohens_d = (np.abs(np.mean(correctDiff))/np.std(correctDiff))
    print("Cohen'sd:",cohens_d)
main()
