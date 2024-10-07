#https://www.codewars.com/kata/52fba66badcd10859f00097e


def disemvowel(string_):
    ouchie = ""
    for x in string_:
        if x != "a" and x != "e" and x != "i" and x != "o" and x != "u" and x != "A" and x != "E" and x != "I" and x != "O" and x != "U" :
            ouchie += "".join(x)
            
        print (ouchie)
    return ouchie