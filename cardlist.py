# import statements
import requests
from bs4 import BeautifulSoup

url = 'https://onepiece.limitlesstcg.com/cards/eb01-memorial-collection' #url for website

page = requests.get(url)  #get page from url

soup = BeautifulSoup(page.content, "html.parser") #tell BeautifulSoup the kind of webpage it is

cardSearch = soup.find("div", class_="card-search-grid")

allCards = cardSearch.find_all("a")
cardLinks = []
for card in allCards:
  cardLinks.append(card["href"])

print(cardLinks)