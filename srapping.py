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


# # scraps eastern conference team names
# teams = []
# for tbody in easternTable:
#     tableBody = tablerows.find_all('tbody')
#     for item in tableBody:
#         href = item.find_all("a", href= True)
#         for name in href:
            

teams = []
for tbody in easternTable:
    tableBody = tablerows.find_all('tbody')
    for item in tableBody:
        href = item.find_all("a", href= True)
        wins = item.find_all('td', attrs = {"data-stat" :"wins"})
        loss = item.find_all('td', attrs = {"data-stat" :"losses"})
        # wins = item.find_all('td', attrs = {"data-stat" :"win_loss_pct"})
        # wins = item.find_all('td', attrs = {"data-stat" :"gb"})
        # wins = item.find_all('td', attrs = {"data-stat" :"pts_per_g"})
        # wins = item.find_all('td', attrs = {"data-stat" :"opp_pts_per_g"})
        # wins = item.find_all('td', attrs = {"data-stat" :"srs"})
        cont = 0
        for name in href:
            teams.append({name.text:"wins: "+ wins[cont].text + " - " +"losses: "+ loss[cont].text})
            cont = cont +1



for i in teams:
    print(i)
