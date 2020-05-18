from memory_profiler import profile
from calc import calculadora

@profile
def bst_mem():
    calculadora("average",[10,8,10,3,7])

if __name__ == "__main__":
    
   bst_mem()