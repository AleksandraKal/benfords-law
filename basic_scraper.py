import requests
from bs4 import BeautifulSoup

output = requests.get('https://www.youtube.com')
soup = BeautifulSoup(output.content, "html.parser")
print(output.text)
 
