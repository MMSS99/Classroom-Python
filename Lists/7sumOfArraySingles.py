#https://www.codewars.com/kata/59f11118a5e129e591000134

def repeats(arr):
    suma = 0
    for i in arr:
        if arr.count(i)%2 != 0:
            suma += i
    return suma

#refactos
def repeats(arr):
    return sum([i for i in arr if arr.count(i)%2 != 0])

def repeats(arr):
    return sum([letter for letter in arr if arr.count(letter)==1])