from asyncio import FIRST_EXCEPTION
import matplotlib.pyplot as plt
import math

FIRST_ELEMENT = 0

"""
Input : collection of values that would like to "fake"
Output : returns true, if data matched benford distrbution and is most likey true
otherwise false
"""
def detection_data(data): 
    inputData = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0} 
    for number in data:
        # remove any other caharcters a user might eneter
        # number = number.replace("0{a-b}","")
        number = str(number)
        inputData[number[FIRST_ELEMENT]] += 1
    inputDataDist = []
    # find total of list - another function
    total = 0
    for dig in inputData.values():
        total += dig
    
    for digit in inputData.values():
        perc = digit/total * 100
        inputDataDist.append(perc)

    # how to calulate benfords law
    x = [1,2,3,4,5,6,7,8,9]
    benfordDist = []
    for d in range(1,10):
        benfordDist.append(math.log(((1+d)/d),10) * 100)

    # finding the difference between the two
    for i in range(0,9):
        diff = benfordDist[i] - inputDataDist[i]
        print(f"Difference of {diff}")

"""
Manipulates the data on how should have inputted it as
"""


if __name__ == "__main__":
    detection_data([1,324,543,4756])