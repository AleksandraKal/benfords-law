import matplotlib.pyplot as plt
import math

def visualise(observedFreq):
    totalDigits = 0
    for digit in observedFreq:
        totalDigits += observedFreq[digit]

    absYAxis = []
    print(f"The data set is {totalDigits} numbers")
    for digit in observedFreq:
        percent = (float(observedFreq[digit])/totalDigits) * 100
        percent = round(percent,2)
        absYAxis.append(percent)
        print(f"for {digit} it is {percent} %")

    # the plotting
    xAxis = [1,2,3,4,5,6,7,8,9]
    excpetedYAxis = []
    for d in range(1,10):
        excpetedYAxis.append(math.log(((1+d)/d),10) * 100)
    plt.bar(xAxis,absYAxis, color='grey')
    plt.plot(xAxis, excpetedYAxis,linestyle='dashed', marker='o', markerfacecolor='blue', markersize=5)
    plt.title("Benford Test")
    plt.xlabel('Leading digit')
    plt.ylabel("Percentage")
    plt.legend(["Expected Benford distrubution","Observed distrubiton"])
    plt.show()
