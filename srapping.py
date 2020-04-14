from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# NBA season
year = 2020

# URL page we will scraping 
url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)
# this is the HTML from the given URL
html = get(url)
soup = BeautifulSoup(html.text,"html.parser")

# Scraps eastern conference headers 
easternTable = soup.findAll('table', attrs={"id":"confs_standings_E"})
headers = []
for tablerows in easternTable:
    tr = tablerows.find_all('tr', limit=1)
    for text in tr:
        headers = text.getText().strip().split("\n")

teams = []
for tbody in easternTable:
    tableBody = tablerows.find_all('tbody')
    for item in tableBody:
        href = item.find_all("a", href= True)
        ewins = item.find_all('td', attrs = {"data-stat" :"wins"})
        eloss = item.find_all('td', attrs = {"data-stat" :"losses"})
        ewin_loss = item.find_all('td', attrs = {"data-stat" :"win_loss_pct"})
        egames_back = item.find_all('td', attrs = {"data-stat" :"gb"})
        epts_p_g = item.find_all('td', attrs = {"data-stat" :"pts_per_g"})
        eopp_pts_pg = item.find_all('td', attrs = {"data-stat" :"opp_pts_per_g"})
        econt = 0
        for name in href:
            teams.append({name.text:"wins: "+ ewins[econt].text + " - " +"losses: "+ loss[cont].text})
            cont = cont +1



for i in teams:
    print(i)
