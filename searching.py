from typing import Tuple

def linear_search(sorted_list: list, value:int) -> Tuple[bool, int]:
    for i in range(0, len(sorted_list)):
        if sorted_list[i] == value:
            return i

    return (False, -1)

def jump_search(sorted_list: list, value: int, step_size: int) -> Tuple[bool, int]:
    for i in range(0, len(sorted_list), step_size):
        if sorted_list[i] > value:
            for j in range(i - step_size):
                if sorted_list[j] == value:
                    return j 
            return False, -1

    for k in range(len(sorted_list) - step_size, len(sorted_list)):
        if sorted_list[k] == value:
            return k
    return False, -1

def binary_search(sorted_list: list, value: int) -> Tuple[bool, int]:
    leftBound = 0
    rightBound = len(sorted_list) - 1

    while leftBound <= rightBound:
        middle = leftBound +(rightBound - leftBound) // 2

        if sorted_list[middle] == value:
            return middle

        elif sorted_list[middle] < value:
            leftBound = middle +1

        else: 
            rightBound = middle -1 
    return False, -1

def search(searchType, array, item):
    if array[0] ==  "Atlanta Hawks":
        if searchType.upper() == "LINEAR":
            try: 
                return "Linear Search ", "Postion: ", linear_search(array, item), "Item: ", array[linear_search(array, item)]
            except:
                return "Invalid Input"
        # if searchType.upper() == "JUMP":
        #     return "Jump Search", "Position: ", jump_search(array, item, 4), "Item: ", array[jump_search(array, item, 4)]
        if searchType.upper() == "BINARY":
            try: 
                return "Binary Search", "Position: ", binary_search(array, item), "Item: ", array[binary_search(array, item)]
            except:
                return "Invalid Input"

        if searchType.upper() == "ALL":
            try:
                return "Linear Search ", "Postion: ", linear_search(array, item), "Item: ", array[linear_search(array, item)], "Binary Search", "Position: ", binary_search(array, item), "Item: ", array[binary_search(array, item)]
            except: 
                return "Invalid Input"
    else:
        item = float(item)
        if searchType.upper() == "LINEAR":
            try: 
                return "Linear Search ", "Postion: ", linear_search(array, item), "Item: ", array[linear_search(array, item)]
            except:
                return "Invalid Input"
        # if searchType.upper() == "JUMP":
        #     return "Jump Search", "Position: ", jump_search(array, item, 4), "Item: ", array[jump_search(array, item, 4)]
        if searchType.upper() == "BINARY":
            try: 
                return "Binary Search", "Position: ", binary_search(array, item), "Item: ", array[binary_search(array, item)]
            except:
                return "Invalid Input"

        if searchType.upper() == "ALL":
            try:
                return "Linear Search ", "Postion: ", linear_search(array, item), "Item: ", array[linear_search(array, item)], "Binary Search", "Position: ", binary_search(array, float(item)), "Item: ", array[binary_search(array, item)]
            except: 
                return "Invalid Input"

