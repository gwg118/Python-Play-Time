from urllib import request
from bs4 import BeautifulSoup

def trade_spider(max_pages):
 page = 0 # craigslist starts at page 0
 while page <= max_pages:
  url = 'http://orlando.craigslist.org/search/cto?s' + str(page) # this is for cars in the orlando area, replace link with w/e
  source_code = request.urlopen(url)
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text, 'lxml') # my computer yelled at me if 'lxml' wasn't included. your mileage may vary
  for link in soup.findAll('a', {'class':'hdrlnk'}):
   href = 'http://orlando.craigslist.org/search/cto?s0' + link.get('href') # use the same link as your 'url' variable + '0' at
                                                                                                                                               # the end
   title = link.string
   print(title)
   print(href)
  page += 100 # craigslist pages go 0, 100, 200, etc

trade_spider(0) # 0 gets the first page, replace with multiples of 100 for extra pages﻿
