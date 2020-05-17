from requests import get
from bs4 import BeautifulSoup

import pandas as pd
from pandas import DataFrame

from memory_profiler import profile
# import gc 


class Node:

    def __init__(self, t, d):
        self.team = t
        self.data = d
        self.left_child = None
        self.right_child = None
    
    def insert(self, t, d):
        if self.data == d:
            return False
        elif self.data > d:
            if self.left_child:
                return self.left_child.insert(t, d)
            else: 
                self.left_child = Node(t, d)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(t, d)
            else: 
                self.right_child = Node(t,d)
                return True

    def find(self, d):
        if self.data == d:
            return True
        elif self.data > d:
            if self.left_child:
                return self.left_child.find(d)
            else: 
                return False
        else: 
            if self.right_child:
                return self.right_child.find(d)
            else: 
                return False
            
    def traverse(self):
        print(self.team, self.data)
        if self.left_child:
            self.left_child.traverse()
        if self.right_child:
            self.right_child.traverse()

    def find_min(self):
        if self.left_child:
            return self.left_child.find_min()
        else:
            return self.team, self.data
    
    def find_max(self):
        if self.right_child:
            return self.right_child.find_max()
        else: 
            return self.team, self.data
    
    
    
        
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, t, d):
        if self.root:
            return self.root.insert(t,d)
        else: 
            self.root = Node(t, d)
            return True

    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return False
            
    def traverse(self):
        if self.root:
            return self.root.traverse()
        else: 
            return False


    def find_min(self):
        if self.root:
            return self.root.find_min()
        else: 
            return False

    def find_max(self): 
        if self.root:
            return self.root.find_max()
        else: 
            return False

# @profile
def main(year):
    
    # NBA season
    

    # URL page we will scrap 
    url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)

    # HTML from URL
    html = get(url)
    soup = BeautifulSoup(html.text,"html.parser")

    bstWins = Tree()
    bstLoss = Tree()
    bstWin_loss_pct = Tree()
    bstGb  = Tree()
    bstPts_per_g = Tree()
    bstOpp_pts_per_g = Tree() 
    bstSrs = Tree()

    teamsList = []
    winList = []
    lossList = []
    win_loss_pctList = []
    gbList = []
    pts_per_gList = []
    opp_pts_per_gList = []
    srsList = []

    # Scraps eastern conference table
    easternTable = soup.findAll('table', attrs={"id":"confs_standings_E"})

    for tablerows in easternTable:
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
                teamName = name.text
                teamsList.append(teamName)
                
                winsItem = float(wins[cont].text)
                winList.append(winsItem)
                bstWins.insert(teamName, winsItem)

                lossItem = float(loss[cont].text)
                lossList.append(lossItem)
                bstLoss.insert(teamName, lossItem)

                win_loss_pctItem = float(win_loss_pct[cont].text)
                win_loss_pctList.append(win_loss_pctItem)
                bstWin_loss_pct.insert(teamName,win_loss_pctItem)

                gbItem = float(gb[cont].text.replace('—','0'))
                gbList.append(gbItem)
                bstGb.insert(teamName, gbItem)

                pts_per_gItem = float(pts_per_g[cont].text)
                pts_per_gList.append(pts_per_gItem)
                bstPts_per_g.insert(teamName, pts_per_gItem)

                opp_pts_per_gItem = float(opp_pts_per_g[cont].text)
                opp_pts_per_gList.append(opp_pts_per_gItem)
                bstOpp_pts_per_g.insert(teamName, opp_pts_per_gItem)

                srsItem = float(srs[cont].text)
                srsList.append(srsItem)
                bstSrs.insert(teamName,srsItem)

     
                cont +=1


    # Scraps Western conference table
    westernTable = soup.findAll('table', attrs={"id":"confs_standings_W"})
    for tablerows in westernTable:
        tableBody = tablerows.find_all('tbody')
        for item in tableBody:
            href = item.find_all("a", href= True)

            wwins = item.find_all('td', attrs = {"data-stat" :"wins"})
            wloss = item.find_all('td', attrs = {"data-stat" :"losses"})
            wwin_loss_pct = item.find_all('td', attrs = {"data-stat" :"win_loss_pct"})
            wgb= item.find_all('td', attrs = {"data-stat" :"gb"})
            wpts_per_g = item.find_all('td', attrs = {"data-stat" :"pts_per_g"})
            wopp_pts_per_g = item.find_all('td', attrs = {"data-stat" :"opp_pts_per_g"})
            wsrs = item.find_all('td', attrs = {"data-stat" :"srs"})

            wcont = 0
            for name in href:
                teamName = name.text
                teamsList.append(teamName)
                
                winsItem = float(wwins[wcont].text)
                winList.append(winsItem)
                bstWins.insert(teamName, winsItem)

                lossItem = float(wloss[wcont].text)
                lossList.append(lossItem)
                bstLoss.insert(teamName, lossItem)

                win_loss_pctItem = float(wwin_loss_pct[wcont].text)
                win_loss_pctList.append(win_loss_pctItem)
                bstWin_loss_pct.insert(teamName,win_loss_pctItem)

                gbItem = float(wgb[wcont].text.replace('—','0'))
                gbList.append(gbItem)
                bstGb.insert(teamName, gbItem)

                pts_per_gItem = float(wpts_per_g[wcont].text)
                pts_per_gList.append(pts_per_gItem)
                bstPts_per_g.insert(teamName, pts_per_gItem)

                opp_pts_per_gItem = float(wopp_pts_per_g[wcont].text)
                opp_pts_per_gList.append(opp_pts_per_gItem)
                bstOpp_pts_per_g.insert(teamName, opp_pts_per_gItem)

                srsItem = float(wsrs[wcont].text)
                srsList.append(srsItem)
                bstSrs.insert(teamName,srsItem)
                
                wcont += 1
                

    minWins = bstWins.find_min()
    maxWins = bstWins.find_max()
    
    minLoss = bstLoss.find_min()
    maxLoss = bstLoss.find_max()

    minWin_loss_pct = bstWin_loss_pct.find_min()
    maxWin_loss_pct = bstWin_loss_pct.find_max()

    minGb = bstGb.find_min()
    maxGb = bstGb.find_max()

    minPts_per_g = bstPts_per_g.find_min()
    maxPts_per_g = bstPts_per_g.find_max()

    minOpp_pts_per_g  = bstOpp_pts_per_g.find_min()
    maxOpp_pts_per_g = bstOpp_pts_per_g.find_max()
    
    minSrs = bstSrs.find_min()
    maxSrs = bstSrs.find_max()

    minsAndMax = [minWins, maxWins,minLoss, maxLoss,minWin_loss_pct,maxWin_loss_pct, minGb, maxGb, minPts_per_g, maxPts_per_g, minOpp_pts_per_g, maxOpp_pts_per_g, minSrs, maxSrs]

    data = {'Teams' : teamsList, 'Wins' : winList, 'Loss' : lossList, 'Win-Loss Percentage'  : win_loss_pctList, 'Games Behind' : gbList, 'Points Per Game':pts_per_gList,
     'Opponent Points Per Game' :opp_pts_per_gList, 'Simple Rating System': srsList }

    # ['wins', 'loss', 'win_loss_pct', 'gb', 'pts_per_g', 'opp_pts_per_g', 'srs']
    df = DataFrame(data, columns = ['Teams','Wins','Loss', 'Win-Loss Percentage',  'Games Behind', 'Points Per Game', 'Opponent Points Per Game', 'Simple Rating System' ] )
    

    return minsAndMax, year, df ,data

if __name__ == "__main__":
    
    main()