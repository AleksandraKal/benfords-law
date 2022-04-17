from unicodedata import decimal
import matplotlib.pyplot as plt
import math
import random
import pandas as pd
import matplotlib.pyplot as plt
import math
import xlsxwriter

# global variables
FIRST_ELEMENT = 0
benfordDist = []
for d in range(1,10):
    benfordDist.append(math.log(((1+d)/d),10) * 100)
# how to calulate benfords law
x = [1,2,3,4,5,6,7,8,9]


# error checking function
def checkLength(data):
    if (len(data) < 10):
        print("Need to enter a data set greater then 10")
        exit()

# finds the frequency
def findFreq(data):
    inputDataFreq = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0} 
    for number in data:
        # remove any other caharcters a user might eneter
        # number = number.replace("0{a-b}","")
        number = str(number)
        print(number)
        inputDataFreq[number[FIRST_ELEMENT]] += 1
    print("------")
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
    checkLength(data)
    inputDataFreq = findFreq(data)
    inputDataDist = []
    # todo : find total of list - another function
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
                outputHash[str(digit)].append(float(newNumber))
            else:
                # loop through the amount of differences and generate a random number from the list to add
                for i in range(0, diff):
                    randomNum = str(random.choice(data))
                    # replace the first digit to digit needed
                    newNum = int (str(digit) + randomNum[1:5])
                    print(f"the num is :{newNum}")
                    outputHash[str(digit)].append(newNum)
    return outputHash


# # find the current distrubiton 
# # input - list
# # return a list with the frequencies
def findDistrubition(inputData):
    inputDataFreq = findFreq(inputData)
    inputDataDist = []
    # todo : find total of list - another function
    total = 0
    for dig in inputDataFreq.values():
        total += dig
    
    for digit in inputDataFreq.values():
        perc = digit/total * 100
        inputDataDist.append(perc)
    return inputDataDist


# shows the current distrubition of the graph
# input = list 
# output = graph displayed on screen comparing the input distrubiton to benford distrubtion
def visualiseData(inputData):
    inputDist = findDistrubition(inputData)
    xAxis = [1,2,3,4,5,6,7,8,9]
    plt.bar(xAxis,inputDist, color='grey')
    plt.plot(xAxis, benfordDist,linestyle='dashed', marker='o', markerfacecolor='blue', markersize=5)
    plt.title("Benford Test")
    plt.xlabel('Leading digit')
    plt.ylabel("Percentage")
    plt.legend(["Expected Benford distrubution","Observed distrubiton"])
    plt.show()

# inpit = list of values want to output to a file
def outputManipulatedDataToFile(manipulatedData, fileName):
    excelBook = xlsxwriter.Workbook(f"manipulated.xlsx")
    sheet = excelBook.add_worksheet()
    for data in enumerate(manipulatedData):
        sheet.write(0,data[0],data[1])
    excelBook.close()

if __name__ == "__main__":
    try:
        fileName = 'manipulation_software/absresidentpopulation.xlsx'
        excelBook = pd.read_excel(fileName,index_col=0)
        print(excelBook.head())
        inputData = []
        for i in excelBook.index:
            inputData.append(i)
        if (not detection_data(inputData)):
            visualiseData(inputData)
            manipulatedData = manipulate_data(inputData)
            outputManipulatedDataToFile(manipulatedData,fileName)
        else:
            print("Data follows the test, don't need to change")
    except FileNotFoundError as fe:
        print("File does not exist")
