#https://www.codewars.com/kata/558878ab7591c911a4000007/

def pig_latin(verbum):
    
    vocales = 'aeiou'
    pigusLatinus = ''
    if not verbum.isalpha():
        return None
    
    elif verbum[0].lower() in vocales:
        return verbum.lower() + 'way'
    
    else:
        for littera in verbum.lower():
            if littera in vocales:
                pigusLatinus = vocalis_movens(verbum) + 'ay'
                return pigusLatinus.lower()
            
        return verbum.lower() + 'ay'
        
def vocalis_movens(verbum):
    
    vocales = 'aeiou'
    while verbum[0].lower() not in vocales:
        verbum = verbum[1:] + verbum[0]