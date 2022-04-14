# scrapes through top 250 tv shows
# notice - this data set is wrong, and heavuly skwed towards 2 since most of top movies were created in 2000s
# more accurate data set - remove the year number
import requests
from bs4 import BeautifulSoup


# -------------------  HELPER FUNCTIONS --------------------
def freq_incrementer(number1, number2, freqList):
    freqList[number1[0]] += 1
    freqList[number2[0]] += 1
    
# -----------------------------------------------------------
# sending a request to fetch the url
url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
response = requests.get(url)
response.raise_for_status()

# obtaining the tr tags list from the tbody tag, as this contains the tags for the movies
content = BeautifulSoup(response.content,"lxml")
trList = content.find("tbody", class_="lister-list").find_all("tr")

# frequency data structure, that we will use to track
freq = {
    "1" : 0,
    "2" : 0, 
    "3" : 0, 
    "4" : 0, 
    "5" : 0,
    "6" : 0, 
    "7" : 0,
    "8" : 0, 
    "9" : 0,
}


rank = 1
# the only numbers that we need for benfords law on the page are the ratings, rank and release year!
for tr in trList:
    relase_yr = tr.find("span", class_="secondaryInfo").text[1:5]
    rating = tr.find("strong").text
    rank += 1
    # analyse the frequency of each number
    freq_incrementer(str(relase_yr), str(rating).replace(".",""),freq)
    
# --------------------------------------


print(f"The dataset is a list of 250 numbers")
print("-----------------------------")
print("The distrubtion is :")
for n in freq:
    percent = (float(freq[n])/250) * 100
    percent = round(percent,2)
    print(f"for {n} it is {percent} %")
    

