#https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

'''def first_n_smallest(arr, n):
    arr = arr[::-1]
    while(len(arr) > n):
        arr.remove(max(arr))
    return arr[::-1]'''

def first_n_smallest(arr, n):
    print (list(enumerate(arr)))
    lambda arr, n: while len(arr) > n
    return [",".join(x for x in )]



if __name__ == "__main__":
    assert(first_n_smallest([1,2,3,4,5],3)) == [1,2,3]
    assert(first_n_smallest([5,4,3,2,1],3)) == [3,2,1]
    assert(first_n_smallest([1,2,3,1,2],3)) == [1,2,1]
    assert(first_n_smallest([1,2,3,-4,0],3)) == [1,-4,0]
    assert(first_n_smallest([1,2,3,4,5],0)) == []
    assert(first_n_smallest([1,2,3,4,5],5)) == [1,2,3,4,5]
    assert(first_n_smallest([1,2,3,4,2],4)) == [1,2,3,2]
    assert(first_n_smallest([2,1,2,3,4,2],2)) == [2,1]
    assert(first_n_smallest([2,1,2,3,4,2],3)) == [2,1,2]
    assert(first_n_smallest([2,1,2,3,4,2],4)) == [2,1,2,2]
