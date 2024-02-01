# import statements
import requests
from bs4 import BeautifulSoup
import csv

# CONSTANTS
PRIMARY_URL = 'https://onepiece.limitlesstcg.com' #url for website

def main():
  collections = searchCards()
  for collection in collections:
    print("Getting "+collection["collectionName"] + " cards!")
    collectionCards = getCards(collection["url"])
    # print(collectionCards)

    writeFiles(collection["collectionName"], collectionCards)
  





def searchCards():
  searchUrl = "/cards?q="
  page = requests.get(PRIMARY_URL+searchUrl)  #get page from url

  soup = BeautifulSoup(page.content, "html.parser") #tell BeautifulSoup the kind of webpage it is

  # print(page.content) #everything on the page

  table = soup.findChildren('table')  #get all tables 

  boostersAndStarters = table[0] #first table

  allRows = boostersAndStarters.find_all('tr') #all rows
  allLinks = [] #stores all searches

  for tr in allRows:
    isHeader = tr.find_all('th')
    if len(isHeader) > 0: #skip headers
      continue
    else:
      anchors = tr.find_all('a')
      allLinks.append( dict (
        collectionId = anchors[0].text.strip(),
        url = anchors[0]['href'].strip(),
        collectionName = anchors[1].text.strip()
      ))
  
  return allLinks

def getCards(collectionUrl):
  collectionCards = []
  cardLinks = getCardList(collectionUrl)
  for cardLink in cardLinks:
    collectionCards.append(getCardDetails(cardLink))

  return collectionCards

def getCardList(collectionUrl): 
  page = requests.get(PRIMARY_URL+collectionUrl)  #get page from url
  soup = BeautifulSoup(page.content, "html.parser") #tell BeautifulSoup the kind of webpage it is

  cardSearch = soup.find("div", class_="card-search-grid") #get card grid

  allCards = cardSearch.find_all("a") #search for all cards 

  cardLinks = []
  for card in allCards:
    cardLinks.append(card["href"])

  return cardLinks
    
def getCardDetails(cardUrl):
  page = requests.get(PRIMARY_URL+cardUrl)  #get page from url
  soup = BeautifulSoup(page.content, "html.parser") #tell BeautifulSoup the kind of webpage it is

  cardName = soup.find("span", class_="card-text-name").text
  cardId = soup.find("span", class_="card-text-id").text
  cardCategory = soup.find("p", class_="card-text-type").contents[1].text

  status = soup.find("div", class_="card-legality-badge")
  cardLegality = status.find_all('div')[1].text.strip()
  # print(cardLegality[1].text.strip())
  # print(cardId, cardName, cardCategory, sep=",")

  # cardDetails = cardId + "," + cardName + ","  + cardCategory + ","  + cardLegality 
  cardDetails = [cardId, cardName , cardCategory, cardLegality]
  return cardDetails

def writeFiles(collectionName, cardDetails):
  print("writing File")
  with open(collectionName, "w", newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(cardDetails)
  print("Finished writing " + collectionName)
if __name__ == "__main__":
  main()