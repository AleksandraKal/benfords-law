import requests
from bs4 import BeautifulSoup

# how to structure propely
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
table = content.find("table",id='chart-data-table_1xAWztwCrY')


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

rowData = table.find_all("tr")
for row in rowData:
    tdTagList = row.find_all("td",class_="data-value")
    for tag in tdTagList:
        numbers = tag.text.strip("-")
        # increment to the frequency list
        observedFreq[numbers[0]] += 1

totalDigits = 0
for digit in observedFreq:
    totalDigits += observedFreq[digit]

print(f"The data set is {totalDigits} numbers")
for n in observedFreq:
    percent = (float(observedFreq[n])/250) * 100
    percent = round(percent,2)
    print(f"for {n} it is {percent} %")
    
