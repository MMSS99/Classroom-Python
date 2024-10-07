#https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    final = ""
    for x in sentence.split():
        
        if len(x) >= 5:
            final += x[::-1] + " "
        else:
            final += x + " "
    
    return final[:-1]