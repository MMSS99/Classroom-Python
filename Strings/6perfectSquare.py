#https://www.codewars.com/kata/584e93a70f60247eb8000132

def perfect_square(square):
    square = square.split("\n")

    for i in square:
        print (i)
        
        for j in i:
            if j != '.':
                return False
            
        if len(i) != len(square):
            print (len(i), len(square))
            return False
        
    return True