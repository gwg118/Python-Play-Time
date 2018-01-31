# Web Crawler to gather information

from urllib import request
from bs4 import BeautifulSoup

def free_stuff(max_pages):
    page = 0
    while page <= max_pages:
        url = 'https://philadelphia.craigslist.org/d/free-stuff/search/zip' + str(page)

        '''request data from page'''
        source_code = request.urlopen(url)
        plain_text = source_code

        # create beautiful soup object
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
            href = "https://philadelphia.craigslist.org/" + link.get('href')
            title = link.string

           # print(href)
           # print(title) # print title of url
            get_single_item_data(href)
        page += 100

# dynamic function to go to each item
def get_single_item_data(item_url):
    source_code = request.urlopen(item_url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.find_All('div', {'class': 'slide first visible'}):
        print(item_name)

free_stuff(1) # cause craigslist starts at 0
# get_single_item_data(1)
