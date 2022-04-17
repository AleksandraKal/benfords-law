from asyncio import FIRST_EXCEPTION
from xxlimited import new
import matplotlib.pyplot as plt
import math
import random

# global variables
FIRST_ELEMENT = 0
benfordDist = []
for d in range(1,10):
    benfordDist.append(math.log(((1+d)/d),10) * 100)
# how to calulate benfords law
x = [1,2,3,4,5,6,7,8,9]


# error checking function
def checkLength(data):
    if (len(data) < 100):
        print("Need to enter a data set greater then 100")
        exit()

# finds the frequency
def findFreq(data):
    inputDataFreq = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0} 
    for number in data:
        # remove any other caharcters a user might eneter
        # number = number.replace("0{a-b}","")
        number = str(number)
        inputDataFreq[number[FIRST_ELEMENT]] += 1
    return inputDataFreq

# input : list of numbers for the data
# output : hashmap with digit and numbers that occur
def transformData(data):
    output = {"1":[], "2":[],"3":[], "4":[], "5":[],"6":[], "7":[], "8":[], "9":[] }
    # loop through the list
    for i in data:
        firstDigit = str(i)[FIRST_ELEMENT]
        output[firstDigit].append(i)
    return output

"""
Input : collection of values that would like to inspect if "fake" or truthful
Output : returns true, if data matched benford distrbution otherwise false
Checks the data set needs to be at least 100 numbers!
"""
def detection_data(data): 
    # checkLength(data)
    inputDataFreq = findFreq(data)
    inputDataDist = []
    # find total of list - another function
    total = 0
    for dig in inputDataFreq.values():
        total += dig
    
    for digit in inputDataFreq.values():
        perc = digit/total * 100
        inputDataDist.append(perc)

    # finding the difference between the two
    flag = True
    for i in range(0,9):
        diff = benfordDist[i] - inputDataDist[i]
        print(f"Difference of {diff}%")
        if (diff > abs(2)):
            flag = False
    return flag
"""
Manipulates the data on how should have inputted it as
"""
def manipulate_data(data):

    # what numbers actually appear from the first digit
    inputDataFreq = findFreq(data)
    numDigits = len(data)
    manipulatedData = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    # what the distrubtion should be expected
    ouputmanipulatedData = []
    outputHash = transformData(data)
    print(outputHash)
    tooAdd = []
    for digit in x:
        benfordOccurance = round(benfordDist[digit-1]*0.01*len(data))
        ouputmanipulatedData.append(benfordOccurance)
        #print(f"Digit {digit} should appear {benfordOccurance} times and actually appears {inputDataFreq[str(digit)]} times")
        diff = inputDataFreq[str(digit)] - benfordOccurance
        if (diff > 0):
            # loop through the elements that need to remove, but remeber them for future use
            for remove in range(0, diff):
                
                tooAdd.append(outputHash[str(digit)].pop())
            print(tooAdd)
            print(outputHash)
        elif (diff < 0):
            diff = abs(diff)
            # too small case - obtain the other digits and change 
            if (len(tooAdd) > 0):
                newNumber = str(digit) + str(tooAdd[FIRST_ELEMENT])[1:]
                tooAdd.remove(tooAdd[FIRST_ELEMENT])
                outputHash[str(digit)].append(int(newNumber))
            else:
                # loop through the amount of differences and generate a random number from the list to add
                for i in range(0, diff):
                    randomNum = str(random.choice(data))
                    # replace the first digit to digit needed
                    newNum = int (str(digit) + randomNum[1:5])
                    print(f"the num is :{newNum}")
                    outputHash[str(digit)].append(newNum)


manipulate_data([10,100,1000,1,10000,2,2,2,20000,2000,20000,2000,2034893,238917,240893,34798,32098,49875,45978,5312809])

if __name__ == "__main__":
    data = [1,1,1,2,3,4,5]
    if (not detection_data(data)):
        manipulate_data(data)

    