
from memory_profiler import profile
# import gc 

from srapping import teamStandings

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

@profile
def main():


    bstWins = Tree()
    for teamDict in teamStandings[0]:

        for k,v in teamDict.items():
            bstWins.insert(k,v)
    
    # bstWins.traverse()

    minWins = [bstWins.find_min()]
    maxWins = [bstWins.find_max()]

    
    bstLoss = Tree()
    for teamDict in teamStandings[1]:

        for k,v in teamDict.items():
            bstLoss.insert(k,v)
    
    # bstLoss.traverse()

    minLoss = [bstLoss.find_min()]
    maxLoss = [bstLoss.find_max()]


    bstWin_loss_pct = Tree()
    for teamDict in teamStandings[2]:

        for k,v in teamDict.items():
            bstLoss.insert(k,v)
    
    # bstWin_loss_pct.traverse()

    minWin_loss_pct = [bstWin_loss_pct.find_min()]
    maxWin_loss_pct = [bstWin_loss_pct.find_max()]


    bstGb = Tree()
    for teamDict in teamStandings[3]:

        for k,v in teamDict.items():
            bstGb.insert(k,v)
    
    # bstGb.traverse()

    minGb = [bstGb.find_min()]
    maxGb = [bstGb.find_max()]


    bstPts_per_g = Tree()
    for teamDict in teamStandings[4]:

        for k,v in teamDict.items():
            bstPts_per_g.insert(k,v)
    
    # bstPts_per_g.traverse()

    minPts_per_g = [bstPts_per_g.find_min()]
    maxPts_per_g = [bstPts_per_g.find_max()]

    bstOpp_pts_per_g = Tree()
    for teamDict in teamStandings[5]:

        for k,v in teamDict.items():
            bstOpp_pts_per_g.insert(k,v)
    
    # bstOpp_pts_per_g.traverse()

    minOpp_pts_per_g  = [bstOpp_pts_per_g.find_min()]
    maxOpp_pts_per_g = [bstOpp_pts_per_g.find_max()]


    bstSrs = Tree()
    for teamDict in teamStandings[6]:

        for k,v in teamDict.items():
            bstSrs.insert(k,v)
    
    # bstSrs.traverse()

    minSrs = [bstSrs.find_min()]
    maxSrs = [bstSrs.find_max()]

    minsAndMax = [minWins, maxWins,minLoss, maxLoss,minWin_loss_pct,maxWin_loss_pct, minGb, maxGb, minPts_per_g, maxPts_per_g, minOpp_pts_per_g, maxOpp_pts_per_g, minSrs, maxSrs]

    bstGb.traverse()

    return minsAndMax



if __name__ == "__main__":
    
    main()