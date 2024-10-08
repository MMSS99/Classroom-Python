#https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

def first_n_smallest(arr, n):
    arr = arr[::-1]
    while(len(arr) > n):
        arr.remove(max(arr))
    return arr[::-1]