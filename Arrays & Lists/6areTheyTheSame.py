#https://www.codewars.com/kata/550498447451fbbd7600041c

import math
def comp(array1, array2):

    if array1 == [] and array2 == []:
        return True
    
    if not array1 or not array2 or len(array1) != len(array2): 
        return False

    for i in range(len(array1)): 
        array1[i] = array1[i]**2
        
    array1.sort()
    array2.sort()
    
    for j in range(len(array1)):
        if array1[j] != array2[j]:
            return False
    
    return True