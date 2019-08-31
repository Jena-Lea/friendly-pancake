# ================= Compulsory Task  ==================

# After you've read and understood all of example.py, create a new Python file called amazon.py inside this folder.
# This programming problem is one posed to new software developer applicants to Amazon, the software development company you've probably bought a book or dvd from once in your life.
# Inside amazon.py, write Python code to read in the contents of the textfile 'input.txt', and for each line in input.txt.
# Write out a new line in a new text file output.txt that computes the answer to some operation on a list of numbers.

import os
import statistics

def strToNum(lst):
    numbers = []
    for i in lst:
        i = int(i)
        numbers.append(i)
    return numbers

inputTxt = os.path.join(os.path.dirname(__file__), "input.txt")
f = open(inputTxt, 'r+', encoding='UTF-8')
lines = f.readlines()

noColon = []

for line in lines:
    noColon = line.strip().split(":")
    if noColon[0] == "\ufeffmin":
        minStr = noColon[1].split(",")
        minLst = strToNum(minStr)
        min = min(minLst)
        minNums = ", ".join(minStr)
        print("The min of [" + minNums + "] is " + str(min))
    elif noColon[0] == "max":
        maxStr = noColon[1].split(",")
        maxLst = strToNum(maxStr)
        max = max(maxLst)
        maxNums = ", ".join(maxStr)
        print("The max of [" + maxNums + "] is " + str(max))
    elif noColon[0] == "avg":
        avgStr = noColon[1].split(",")
        avgLst = strToNum(avgStr)
        avg = statistics.mean(avgLst)
        avgNums = ", ".join(avgStr)
        print("The avg of [" + avgNums + "] is " + str(avg))

f.close()
