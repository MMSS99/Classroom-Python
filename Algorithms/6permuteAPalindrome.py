#https://www.codewars.com/kata/58ae6ae22c3aaafc58000079

def permute_a_palindrome(input):
    
    imparEncontrado = []
    
    for i in input:
        if input.count(i)%2 != 0:
            imparEncontrado.append(input.count(i))
    
    if imparEncontrado:
        
        for j in range(len(imparEncontrado)):

            if imparEncontrado[j] != imparEncontrado[0]:
                return False
        
        if imparEncontrado.count(1) > 1:
            return False
                      
        return True
        
    else:
        return True
