import requests
from bs4 import BeautifulSoup

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

rowData = table.find_all("tr")
for row in rowData:
    val = row.find("td",class_="data-value").text
