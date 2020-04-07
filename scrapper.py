from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season
year = 2020

# URL page we will scraping 
url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html, features="lxml")


easternTable = soup.findAll('table', attrs={"id":"confs_standings_E"})
headers = []

for tablerows in easternTable:
    tr = tablerows.find_all('tr', limit=1)
    for text in tr:
        headers = text.getText().strip().split("\n")
        

print(headers)

