#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

# w/ while loop
def duplicate_encode(word):
    
    i = 0
    word = word.lower()
    final = ''
    while i in range(len(word)):
        if word.count(word[i]) > 1:
            final += ')'
        else:
            final += '('
        i += 1
        
    return final

#w/ for loop
def duplicate_encode(word):
    word = word.lower()
    encoded = ''
    for i in word:
        if word.count(i) > 1:
            encoded += ')'
        else:
            encoded += '('
    return encoded

#w/ dictionaries
def duplicate_encode(word):
    codigo = {}
    
    for caracter in word.lower():
        if caracter in codigo:
            codigo[caracter] = ')'
        else:
            codigo[caracter] = '('
            
    
            
    return ''.join(codigo[x] for x in word.lower())

#comprensión
def duplicate_encode(word):
    return ''.join([')' if word.lower().count(letter) > 1 else '(' for letter in word.lower()])