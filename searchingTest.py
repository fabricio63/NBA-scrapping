from random import randint
from searching import linear_search, binary_search

sorted_list = list(range(1,1000))
search_value = randint(1,999)

def test_linear_search(benchmark):
    benchmark(linear_search, sorted_list, search_value)

def test_binary_search(benchmark):
    benchmark(binary_search, sorted_list, search_value)