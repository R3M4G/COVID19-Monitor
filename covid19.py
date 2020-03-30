import urllib2
from bs4 import BeautifulSoup
from huepy import *
quote_page = 'https://www.mohfw.gov.in'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('div', attrs={'class': 'information_block'})

name = name_box.text.strip()
print(bold(red(name)))

