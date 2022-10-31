import requests, re
from bs4 import BeautifulSoup

data=requests.get("https://www.lego.com/en-us/product/the-razor-crest-75331").content
soup=BeautifulSoup(data, 'html.parser')
span=soup.find("h1", {"class":"Markup__StyledMarkup-sc-nc8x20-0 dbPAWk"}) 
title=span.text
span=soup.find("span", {"class":"Text__BaseText-sc-13i1y3k-0 zkrlj ProductPricestyles__StyledText-sc-vmt0i4-0 tMWye"})
price=span.text
print("Item %s has a price of $ %s" % (title, price))