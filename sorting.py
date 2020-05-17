
def selection_sort(unsorted:list) -> list:

    for i in range(0, len(unsorted) - 1):
        min = i 

        for j in range(i + 1, len(unsorted)):
            if unsorted[j] < unsorted[min]:
                min = j
        if min != i:
            unsorted[i], unsorted[min] = unsorted[min], unsorted[i]
    
    return unsorted

def bubble_sort(unsorted: list) -> list:

    for i in range(0, len(unsorted)):
        for j in range(0, len(unsorted)- 1 - i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    return unsorted

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def sort(sortType, array):
    if sortType.upper() == "QUICK":
        quick_sort(array, 0, len(array) - 1)
        return "Quick Sort", array
    if sortType.upper() == "BUBBLE":
        return "Bubble Sort", bubble_sort(array)
    if sortType.upper() == "SELECTION":
        return "Selection Sort", selection_sort(array)
    if sortType.upper() == "ALL":
        return "\nQuick Sort", array, "\nBubble Sort", bubble_sort(array), "\nSelection Sort", selection_sort(array)
    else: 
        return "ERROR"