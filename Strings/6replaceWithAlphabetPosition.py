#https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    text = text.lower()
    letras = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in text:
        #print (i)
        if i in letras:
            result += str(letras.index(i)+1) + ' '
        else:
            result += ''
    
    return result[:-1]