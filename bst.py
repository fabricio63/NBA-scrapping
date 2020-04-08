
# from memory_profiler import profile

import gc 

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


def main():

    wins = {"GS": 53, "NY": 46, "TOR":43, "LAC": 41, "DET" : 39}

    bst = Tree()

    for k,v in wins.items():
        bst.insert(k,v)
    
    bst.traverse()

    print("\nMin wins: ", bst.find_min())
    print("Max wins: ", bst.find_max())


if __name__ == "__main__":
    main()