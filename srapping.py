from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# NBA season
year = 2020

# URL page we will scrap 
url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)

# HTML from URL
html = get(url)
soup = BeautifulSoup(html.text,"html.parser")

# Scraps eastern conference headers 
easternTable = soup.findAll('table', attrs={"id":"confs_standings_E"})
headers = []
for tablerows in easternTable:
    tr = tablerows.find_all('tr', limit=1)
    for text in tr:
        headers = text.getText().strip().split("\n")


# scraps eastern conference team names
teams = []
for tbody in easternTable:
    tableBody = tablerows.find_all('tbody')
    for item in tableBody:
        href = item.find_all("a", href= True)
        for name in href:
            teams.append(name.text)
            

winsList = []
lossList = []
win_loss_pctList = []

for tbody in easternTable:
    tableBody = tablerows.find_all('tbody')
    for item in tableBody:
        href = item.find_all("a", href= True)
        wins = item.find_all('td', attrs = {"data-stat" :"wins"})
        loss = item.find_all('td', attrs = {"data-stat" :"losses"})
        win_loss_pct = item.find_all('td', attrs = {"data-stat" :"win_loss_pct"})
        gb = item.find_all('td', attrs = {"data-stat" :"gb"})
        pts_per_g = item.find_all('td', attrs = {"data-stat" :"pts_per_g"})
        opp_pts_per_g = item.find_all('td', attrs = {"data-stat" :"opp_pts_per_g"})
        srs = item.find_all('td', attrs = {"data-stat" :"srs"})
        
        cont = 0
        for name in href:
            # data.append({name.text:"wins: "+ wins[cont].text + " - " +"losses: "+ loss[cont].text})

            winsList.append({name.text: int(wins[cont].text)})
            lossList.append({name.text: int(loss[cont].text)})
            win_loss_pctList.append({name.text: float(win_loss_pct[cont].text)})
            cont = cont +1

for i in winsList :
    print(i)
