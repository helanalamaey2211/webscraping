import requests
from bs4 import BeautifulSoup
url='https://aqarmap.com.eg/ar/for-sale/apartment/asyut/'
page=requests.get(url)
#print(page.content)
soup=BeautifulSoup(page.content,"html.parser")
#print(soup)
apartment_address=soup.find_all("h2",{"search-listing-card__title"})
price=soup.find_all("div",{"search-listing-card__price"})
num_meters=soup.find_all("label",{"search-listing-card__attributes_item"})
for i in range(len(apartment_address)):
   print(apartment_address[i].text)
   print(price[i].text)
   print(num_meters[i].text)

