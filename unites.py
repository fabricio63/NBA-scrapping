import unittest
from bst import main
from srapping import info
class Testingmethods(unittest.TestCase):
    def setUp(self):
        pass
    def testminmax(self):
        self.assertEqual([[('Golden State Warriors', 15)], [('Milwaukee Bucks', 53)], [('Milwaukee Bucks', 12)], [('Golden State Warriors', 50)], [False], [False], [('Milwaukee Bucks', 0.0)], [('Atlanta Hawks', 34.0)], [('Charlotte Hornets', 102.9)], [('Milwaukee Bucks', 118.6)], [('Toronto Raptors', 106.5)], [('Washington Wizards', 119.7)], [('Atlanta Hawks', -7.57)], [('Milwaukee Bucks', 10.44)]],main())
    def testscrapper(self):
        self.assertEqual([[{'Milwaukee Bucks': 53}, {'Toronto Raptors': 46}, {'Boston Celtics': 43}, {'Miami Heat': 41}, {'Indiana Pacers': 39}, {'Philadelphia 76ers': 39}, {'Brooklyn Nets': 30}, {'Orlando Magic': 30}, {'Washington Wizards': 24}, {'Charlotte Hornets': 23}, {'Chicago Bulls': 22}, {'New York Knicks': 21}, {'Detroit Pistons': 20}, {'Atlanta Hawks': 20}, {'Cleveland Cavaliers': 19}, {'Los Angeles Lakers': 49}, {'Los Angeles Clippers': 44}, {'Denver Nuggets': 43}, {'Utah Jazz': 41}, {'Oklahoma City Thunder': 40}, {'Houston Rockets': 40}, {'Dallas Mavericks': 40}, {'Memphis Grizzlies': 32}, {'Portland Trail Blazers': 29}, {'New Orleans Pelicans': 28}, {'Sacramento Kings': 28}, {'San Antonio Spurs': 27}, {'Phoenix Suns': 26}, {'Minnesota Timberwolves': 19}, {'Golden State Warriors': 15}], [{'Milwaukee Bucks': 12}, {'Toronto Raptors': 18}, {'Boston Celtics': 21}, {'Miami Heat': 24}, {'Indiana Pacers': 26}, {'Philadelphia 76ers': 26}, {'Brooklyn Nets': 34}, {'Orlando Magic': 35}, {'Washington Wizards': 40}, {'Charlotte Hornets': 42}, {'Chicago Bulls': 43}, {'New York Knicks': 45}, {'Detroit Pistons': 46}, {'Atlanta Hawks': 47}, {'Cleveland Cavaliers': 46}, {'Los Angeles Lakers': 14}, {'Los Angeles Clippers': 20}, {'Denver Nuggets': 22}, {'Utah Jazz': 23}, {'Oklahoma City Thunder': 24}, {'Houston Rockets': 24}, {'Dallas Mavericks': 27}, {'Memphis Grizzlies': 33}, {'Portland Trail Blazers': 37}, {'New Orleans Pelicans': 36}, {'Sacramento Kings': 36}, {'San Antonio Spurs': 36}, {'Phoenix Suns': 39}, {'Minnesota Timberwolves': 45}, {'Golden State Warriors': 50}], [{'Milwaukee Bucks': 0.815}, {'Toronto Raptors': 0.719}, {'Boston Celtics': 0.672}, {'Miami Heat': 0.631}, {'Indiana Pacers': 0.6}, {'Philadelphia 76ers': 0.6}, {'Brooklyn Nets': 0.469}, {'Orlando Magic': 0.462}, {'Washington Wizards': 0.375}, {'Charlotte Hornets': 0.354}, {'Chicago Bulls': 0.338}, {'New York Knicks': 0.318}, {'Detroit Pistons': 0.303}, {'Atlanta Hawks': 0.299}, {'Cleveland Cavaliers': 0.292}, {'Los Angeles Lakers': 0.778}, {'Los Angeles Clippers': 0.688}, {'Denver Nuggets': 0.662}, {'Utah Jazz': 0.641}, {'Oklahoma City Thunder': 0.625}, {'Houston Rockets': 0.625}, {'Dallas Mavericks': 0.597}, {'Memphis Grizzlies': 0.492}, {'Portland Trail Blazers': 0.439}, {'New Orleans Pelicans': 0.438}, {'Sacramento Kings': 0.438}, {'San Antonio Spurs': 0.429}, {'Phoenix Suns': 0.4}, {'Minnesota Timberwolves': 0.297}, {'Golden State Warriors': 0.231}], [{'Milwaukee Bucks': 0.0}, {'Toronto Raptors': 6.5}, {'Boston Celtics': 9.5}, {'Miami Heat': 12.0}, {'Indiana Pacers': 14.0}, {'Philadelphia 76ers': 14.0}, {'Brooklyn Nets': 22.5}, {'Orlando Magic': 23.0}, {'Washington Wizards': 28.5}, {'Charlotte Hornets': 30.0}, {'Chicago Bulls': 31.0}, {'New York Knicks': 32.5}, {'Detroit Pistons': 33.5}, {'Atlanta Hawks': 34.0}, {'Cleveland Cavaliers': 34.0}], [{'Milwaukee Bucks': 118.6}, {'Toronto Raptors': 113.0}, {'Boston Celtics': 113.0}, {'Miami Heat': 112.2}, {'Indiana Pacers': 109.3}, {'Philadelphia 76ers': 109.6}, {'Brooklyn Nets': 110.8}, {'Orlando Magic': 106.4}, {'Washington Wizards': 115.6}, {'Charlotte Hornets': 102.9}, {'Chicago Bulls': 106.8}, {'New York Knicks': 105.8}, {'Detroit Pistons': 107.2}, {'Atlanta Hawks': 111.8}, {'Cleveland Cavaliers': 106.9}], [{'Milwaukee Bucks': 107.4}, {'Toronto Raptors': 106.5}, {'Boston Celtics': 106.8}, {'Miami Heat': 108.9}, {'Indiana Pacers': 107.4}, {'Philadelphia 76ers': 107.4}, {'Brooklyn Nets': 111.4}, {'Orlando Magic': 107.3}, {'Washington Wizards': 119.7}, {'Charlotte Hornets': 109.6}, {'Chicago Bulls': 109.9}, {'New York Knicks': 112.3}, {'Detroit Pistons': 110.8}, {'Atlanta Hawks': 119.7}, {'Cleveland Cavaliers': 114.8}], [{'Milwaukee Bucks': 10.44}, {'Toronto Raptors': 5.88}, {'Boston Celtics': 5.69}, {'Miami Heat': 2.58}, {'Indiana Pacers': 1.61}, {'Philadelphia 76ers': 2.22}, {'Brooklyn Nets': -1.18}, {'Orlando Magic': -0.85}, {'Washington Wizards': -4.86}, {'Charlotte Hornets': -6.88}, {'Chicago Bulls': -3.81}, {'New York Knicks': -6.55}, {'Detroit Pistons': -4.22}, {'Atlanta Hawks': -7.57}, {'Cleveland Cavaliers': -7.57}]],info())
if __name__ == '__main__': 
    unittest.main() 