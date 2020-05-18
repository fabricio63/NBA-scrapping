from calc import calculadora
from bstScrapper import main
import unittest 
  
class SimpleTest(unittest.TestCase): 
    def testeo (self):
        self.assertEqual(calculadora("average",[10,8]),"9.0")
    
    def testeo1 (self):
        self.assertEqual(calculadora("range",[10,8]),"2")
    
    def testeo2(self):
        minsAndMax, year, df ,data, sortedTeamsList, sortedWinList, sortedWinLossPCT = main("2020") 
        self.assertEqual(sortedWinList,('\nQuick Sort', [15.0, 19.0, 19.0, 20.0, 20.0, 21.0, 22.0, 23.0, 24.0, 26.0, 27.0, 28.0, 28.0, 29.0, 30.0, 30.0, 32.0, 39.0, 39.0, 40.0, 40.0, 40.0, 41.0, 41.0, 43.0, 43.0, 44.0, 46.0, 49.0, 53.0], '\nBubble Sort', [15.0, 19.0, 19.0, 20.0, 20.0, 21.0, 22.0, 23.0, 24.0, 26.0, 27.0, 28.0, 28.0, 29.0, 30.0, 30.0, 32.0, 39.0, 39.0, 40.0, 40.0, 40.0, 41.0, 41.0, 43.0, 43.0, 44.0, 46.0, 49.0, 53.0], '\nSelection Sort', [15.0, 19.0, 19.0, 20.0, 20.0, 21.0, 22.0, 23.0, 24.0, 26.0, 27.0, 28.0, 28.0, 29.0, 30.0, 30.0, 32.0, 39.0, 39.0, 40.0, 40.0, 40.0, 41.0, 41.0, 43.0, 43.0, 44.0, 46.0, 49.0, 53.0]))

    def testeo3 (self):
        minsAndMax, year, df ,data, sortedTeamsList, sortedWinList, sortedWinLossPCT = main("2020") 
        self.assertEqual(sortedTeamsList,('\nQuick Sort', ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards'], '\nBubble Sort', ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards'], '\nSelection Sort', ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']))
    def testeo4(self):
        minsAndMax, year, df ,data, sortedTeamsList, sortedWinList, sortedWinLossPCT = main("2020") 
        self.assertEqual(sortedWinLossPCT,('\nQuick Sort', [0.231, 0.292, 0.297, 0.299, 0.303, 0.318, 0.338, 0.354, 0.375, 0.4, 0.429, 0.438, 0.438, 0.439, 0.462, 0.469, 0.492, 0.597, 0.6, 0.6, 0.625, 0.625, 0.631, 0.641, 0.662, 0.672, 0.688, 0.719, 0.778, 0.815], '\nBubble Sort', [0.231, 0.292, 0.297, 0.299, 0.303, 0.318, 0.338, 0.354, 0.375, 0.4, 0.429, 0.438, 0.438, 0.439, 0.462, 0.469, 0.492, 0.597, 0.6, 0.6, 0.625, 0.625, 0.631, 0.641, 0.662, 0.672, 0.688, 0.719, 0.778, 0.815], '\nSelection Sort', [0.231, 0.292, 0.297, 0.299, 0.303, 0.318, 0.338, 0.354, 0.375, 0.4, 0.429, 0.438, 0.438, 0.439, 0.462, 0.469, 0.492, 0.597, 0.6, 0.6, 0.625, 0.625, 0.631, 0.641, 0.662, 0.672, 0.688, 0.719, 0.778, 0.815]))
if __name__ == '__main__': 
    unittest.main() 