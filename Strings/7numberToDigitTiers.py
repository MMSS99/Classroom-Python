#https://www.codewars.com/kata/586bca7fa44cfc833e00005c

def create_array_of_tiers(n):
    string = ""
    finish = []
    for x in str(n):
        string += "".join(x)
        print (string)
        finish.append(string)
    return finish