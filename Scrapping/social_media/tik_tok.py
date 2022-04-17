import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import math

url = 'https://www.tiktok.com/'
re = requests.get(url)
re.raise_for_status
 
htmlContent = BeautifulSoup(re.content,"lxml")
# extract content from the main container
mainContainer = htmlContent.find("div",class_="tiktok-1id9666-DivMainContainer evzvjqg0")
videos = mainContainer.find_all("div",class_="tiktok-1p48f7x-DivItemContainer ecck2zc0")
# above command only as length 2 - find out why?
for video in videos:
    influencer = video.find("div",class_="tiktok-1mnwhn0-DivAuthorContainer ecck2zc6").find("a")['href'].replace("/","")
    print(f"The content creator is : {influencer}")
    videoPerformace = video.find("div", class_="tiktok-wc6k4c-DivActionItemContainer ear7a600")
    likes = videoPerformace.find("button",class_="tiktok-1xiuanb-ButtonActionItem ee8s79f0").find("strong")
    print(likes.text)