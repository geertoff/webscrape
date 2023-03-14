# doc
# https://realpython.com/python-web-scraping-practical-introduction/
# https://www.geeksforgeeks.org/python-web-scraping-tutorial/
# https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=tag#
# 
import requests
from bs4 import BeautifulSoup
url = "https://www.checkoutsam.nl/rondreis-nieuw-zeeland/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# fetch the text
s = soup.find('div', class_='entry-content')
# lines = s.find_all('p')

# for line in lines :
#     print(line.text)
    
# fetch bold statements
bolds = soup.find_all('strong')
tags = soup.find_all('strong')
for tag in tags :
    print(tag.contents[0])
# s = soup.find('<strong>')
# print(s.contents)