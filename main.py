# import statements
import requests
from bs4 import BeautifulSoup

url = 'https://onepiece.limitlesstcg.com/cards?q=' #url for website

page = requests.get(url)  #get page from url

soup = BeautifulSoup(page.content, "html.parser") #tell BeautifulSoup the kind of webpage it is

# print(page.content) #everything on the page

table = soup.findChildren('table')  #get all tables 

boostersAndStarters = table[0]

allRows = boostersAndStarters.find_all('tr')
allLinks = dict()

# br = False
for tr in allRows:
  isHeader = tr.find_all('th')
  if len(isHeader) > 0:
    continue
  else:
    br = True
    anchors = tr.find_all('a')
    for anch in anchors:
      if anch.text not in allLinks:
        allLinks[anch.text] = anch["href"]
      break

print(allLinks)