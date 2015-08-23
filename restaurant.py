__author__ = 'Tavleen'
from bs4 import BeautifulSoup
import re
import os
import urllib
url = urllib.urlopen("https://www.zomato.com/jaipur/restaurants").read()
soup = BeautifulSoup(url, "html.parser")
#soup.prettify()
restaurant_names = soup.find_all("div",class_= "search-name clearfix")
print "Restaurants are :"
for rest in restaurant_names:
    print rest.a.get_text()
  
    #TRYING FOR GETTING RATING
    #divs = rest.find("div", class_="right")
    #for div in divs
    #if rest["class"]=="right":
     #   rest = rest.findNext('div')
    #rating = float(divs.div.next.get_text())
    #print "Rating is :" + rating
