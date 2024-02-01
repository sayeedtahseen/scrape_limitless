# import statements
import requests
from bs4 import BeautifulSoup

url = 'https://onepiece.limitlesstcg.com/cards/EB01-001' #url for website

page = requests.get(url)  #get page from url

soup = BeautifulSoup(page.content, "html.parser") #tell BeautifulSoup the kind of webpage it is

cardName = soup.find("span", class_="card-text-name").text
cardId = soup.find("span", class_="card-text-id").text
cardCategory = soup.find("p", class_="card-text-type").contents[1].text

# print(cardId, cardName, cardCategory, sep=",")

status = soup.find("div", class_="card-legality-badge")
cardLegality = status.find_all('div')
print(cardLegality[1].text.strip())