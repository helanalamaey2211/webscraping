import requests
from bs4 import BeautifulSoup
url="https://www.tolaitila.com/cate/1"
page=requests.get(url)
#print(page.content)
soup=BeautifulSoup(page.content,"html.parser")
#print(soup)
books_title=soup.find_all("h4",{"class":"text-center"})
author=soup.find_all("h5",{"class":"text-center"})
for i in range(len(books_title)):
   print(books_title[i].text)
   print(author[i].text)
