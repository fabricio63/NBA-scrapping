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
winsList = []
lossList = []
win_loss_pctList = []

for tbody in easternTable:
    tableBody = tablerows.find_all('tbody')
    for item in tableBody:
        href = item.find_all("a", href= True)
        ewins = item.find_all('td', attrs = {"data-stat" :"wins"})
        eloss = item.find_all('td', attrs = {"data-stat" :"losses"})
        ewin_loss_pct = item.find_all('td', attrs = {"data-stat" :"win_loss_pct"})
        egames_back = item.find_all('td', attrs = {"data-stat" :"gb"})
        epts_p_g = item.find_all('td', attrs = {"data-stat" :"pts_per_g"})
        eopp_pts_pg = item.find_all('td', attrs = {"data-stat" :"opp_pts_per_g"})
        econt = 0
        for name in href:
            winsList.append({name.text: int(ewins[econt].text)})
            lossList.append({name.text: int(eloss[econt].text)})
            win_loss_pctList.append({name.text: float(ewin_loss_pct[econt].text)})
            econt = econt +1
            
# Scraps eastern conference headers 
WesternTable = soup.findAll('table', attrs={"id":"confs_standings_W"})
wheaders = []
for tablerows in WesternTable:
    tr = tablerows.find_all('tr', limit=1)
    for text in tr:
        wheaders = text.getText().strip().split("\n")


for tbody in WesternTable:
    tableBody = tablerows.find_all('tbody')
    for item in tableBody:
        href = item.find_all("a", href= True)
        wwins = item.find_all('td', attrs = {"data-stat" :"wins"})
        wloss = item.find_all('td', attrs = {"data-stat" :"losses"})
        wwin_loss_pct = item.find_all('td', attrs = {"data-stat" :"win_loss_pct"})
        wgames_back = item.find_all('td', attrs = {"data-stat" :"gb"})
        wpts_p_g = item.find_all('td', attrs = {"data-stat" :"pts_per_g"})
        wopp_pts_pg = item.find_all('td', attrs = {"data-stat" :"opp_pts_per_g"})
        wcont = 0
        for name in href:
            winsList.append({name.text: int(wwins[wcont].text)})
            lossList.append({name.text: int(wloss[wcont].text)})
            win_loss_pctList.append({name.text: float(wwin_loss_pct[wcont].text)})
            wcont = wcont +1

for i in winsList:
    print(i)
