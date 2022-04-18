from inspect import classify_class_attrs
import requests
from bs4 import BeautifulSoup


# sending a request to fetch the url - cornavirus information
url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
response.raise_for_status()

content = BeautifulSoup(response.content,"lxml")
table = content.find("table",id="main_table_countries_today")
countries = table.find("tbody").find_all("tr")
print(countries)
# for country in countries:
    # # print(country)
    # # print("-------------------------------")
    # countriesCases = country.find_all("td",class_="sorting_1", limit = 3)
    # print(countriesCases[2])
    # print("--------------")
    
