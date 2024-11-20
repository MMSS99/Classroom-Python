#https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

'''def first_n_smallest(arr, n):
    arr = arr[::-1]
    while(len(arr) > n):
        arr.remove(max(arr))
    return arr[::-1]'''

def first_n_smallest(arr, n):
    #arr[::-1].remove(max(arr) for i in range(n))
    #print ([number for number in arr[::-1] if number in sorted(arr)[:n]][::-1])

    
    #arr[::-1].remove(max(arr) for i in range(n))
    #print ([numeroEnumerado[1] for numeroEnumerado in sorted(sorted(enumerate(arr), key=[1])[:n])]) !!! Key= requiere una función de un sólo argumento.
    #print ((list(enumerate(arr))).sort(key=lambda indice: indice[1]))
    #print ([numeroEnumerado[1] for numeroEnumerado in sorted((list(enumerate(arr)).sort(key=lambda indice: indice[1]))[:n])])

    #return [number for number in arr[::-1] if number in sorted(arr)[:n]][::-1][:n]
    return [numeroEnumerado[1] for numeroEnumerado in sorted(sorted(enumerate(arr), key=lambda indice: indice[1])[:n])]



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
