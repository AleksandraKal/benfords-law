import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import math

# scrapes the annual population change 

#how to structure propely
# def find_page(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response

# if __name__ == "__main__":
#     absUrl = "https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release"
#     find_page(absUrl)

absUrl = "https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/latest-release"
response = requests.get(absUrl)
response.raise_for_status()
content = BeautifulSoup(response.content, "lxml")
table = content.find("table",id='chart-data-table_uwMnWiWz0q')


observedFreq = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
}

# ------ finding the Components of annual population change from September 2001- September 2021
rowData = table.find_all("tr")
# if want to remove covid 19 related statstics
rowData = table.find_all("tr", limit = 75)
for row in rowData:
    tdTagList = row.find_all("td",class_="data-value")
    for tag in tdTagList:
        numbers = tag.text.strip("-")
        # increment to the frequency list
        observedFreq[numbers[0]] += 1

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


# --------------------------------------------- 2 ---------------------------------------------
birthFreq = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}

# scrapping birth rates from 1932 to 2020
birthRateUrl = "https://www.abs.gov.au/statistics/people/population/births-australia/2020"
birthResponse = requests.get(birthRateUrl)
birthResponse.raise_for_status()
birthHtml = BeautifulSoup(birthResponse.content, "lxml")

# obtaning the tags
birthTable = birthHtml.find("table", id="chart-data-table_WB2DD0Isi7")
birthRows = birthTable.find_all("tr")
for year in birthRows:
    yearBirthNum =  year.find("td", class_="data-value")
    if yearBirthNum is not None:
        yearBirthNum = yearBirthNum.text
        birthFreq[yearBirthNum[0]] += 1


# the plotting
totalDigits = 0
for digit in birthFreq:
    totalDigits += birthFreq[digit]

birthYAxis = []
print(f"The data set is {totalDigits} numbers")
for digit in birthFreq:
    percent = (float(birthFreq[digit])/totalDigits) * 100
    percent = round(percent,2)
    birthYAxis.append(percent)
    print(f"for {digit} it is {percent} %")

# the plotting
plt.bar(xAxis,birthYAxis, color='grey')
plt.plot(xAxis, excpetedYAxis,linestyle='dashed', marker='o', markerfacecolor='blue', markersize=5)
plt.title("Benford Test")
plt.xlabel('Leading digit')
plt.ylabel("Percentage")
plt.legend(["Expected Benford distrubution","Observed distrubiton"])
plt.show()