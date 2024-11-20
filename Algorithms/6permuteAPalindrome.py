#https://www.codewars.com/kata/58ae6ae22c3aaafc58000079

def permute_a_palindrome(input):
    
    '''imparEncontrado = []
    
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
        return True'''
    
    return sum(input.count(caracter)%2 for caracter in set(input)) <= 1

if __name__ == "__main__":
    assert(permute_a_palindrome("a")) == True
    assert(permute_a_palindrome("aa")) == True
    assert(permute_a_palindrome("aaa")) == True
    assert(permute_a_palindrome("baa")) == True
    assert(permute_a_palindrome("aab")) == True
    assert(permute_a_palindrome("baabcd")) == False
    assert(permute_a_palindrome("racecars")) == False
    assert(permute_a_palindrome("abcdefghba")) == False