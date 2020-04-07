from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA Season:
year = 2020

# URL of page that will be scraped
url = "https://www.espn.com/nba/stats/team/_/season/{}/seasontype/2".format(year)

# HTML from the URL
html = urlopen(url)

soup = BeautifulSoup(html, features="lxml" )

# use findALL() to get the column headers
tr = soup.find_all('tr', attrs={"class":"Table__TR Table__even"} )
print(tr)


teams = []
divTeam =  soup.find_all("div", attrs={"class":"flex items-start mr7"} )
for div in divTeam:
    hrefTeam = div.find_all("a", href = True)
    for href in hrefTeam:
        if href.text != "":
            teams.append(href.text)



