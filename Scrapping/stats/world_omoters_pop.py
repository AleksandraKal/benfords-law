import requests
from bs4 import BeautifulSoup
import visualise

FIRST_ELEMENT = 0

# sending a request to fetch the url - population information
url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
response.raise_for_status()


observedFreq = {
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

content = BeautifulSoup(response.content,"lxml")
table = content.find("table",id="example2").find("tbody").find_all("tr",limit=235)
for country in table:
    population = country.find_all("td")[2].text
    firstDigit = population[FIRST_ELEMENT]
    observedFreq[firstDigit] += 1

visualise.visualise(observedFreq)
