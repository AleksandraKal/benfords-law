from inspect import classify_class_attrs
import requests
from bs4 import BeautifulSoup


# sending a request to fetch the url
url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
response.raise_for_status()

content = BeautifulSoup(response.content,"lxml")
table = content.find("table",id="main_table_countries_today")
Countries = table.find_all("tbody")
oddCountires= Countries[0].find_all("tr", class_="odd")
print(oddCountires)