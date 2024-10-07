#https://www.codewars.com/kata/51b6249c4612257ac0000005

def solution(roman : str) -> int:
    
    NUMEROS_ROMANOS = {"CM": '900 ', "CD": '400 ', "XC": '90 ' , "XL": '40 ', "IX": '9 ', "IV": '4 ', "M": '1000 ', "D": '500 ', "C": '100 ', "L": '50 ', "X": '10 ', "V": '5 ', "I": '1 ' }
    
    
    for letraromana in NUMEROS_ROMANOS:
        
        if letraromana in roman:
                roman = roman.replace(letraromana, NUMEROS_ROMANOS.get(letraromana))
    
    roman = roman.split()

    for i in range(len(roman)):
        roman[i] = int(roman[i])
    
    return sum(roman)