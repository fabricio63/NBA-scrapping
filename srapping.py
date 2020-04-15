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
gbList = []
pts_per_gList = []
opp_pts_per_gList = []
srsList = []


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
            

            winsList.append({name.text: int(wins[cont].text)})
            lossList.append({name.text: int(loss[cont].text)})
            win_loss_pctList.append({name.text: float(win_loss_pct[cont].text)})
            gbList.append({name.text: float(gb[cont].text.replace('—','0'))})
            pts_per_gList.append({name.text: float(pts_per_g[cont].text)})
            opp_pts_per_gList.append({name.text: float(opp_pts_per_g[cont].text)})
            srsList.append({name.text: float(srs[cont].text)})


            cont = cont +1


# Scraps Western conference headers 
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

teamStandings = [winsList, lossList, win_loss_pctList, gbList, pts_per_gList, opp_pts_per_gList, srsList]


# for i in winsList :
#     print(i)
