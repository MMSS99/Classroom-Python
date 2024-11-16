# Fusión de 6romanNumeralsDecoder y 6romanNumeralsEncoder con la adición de M: 1000 al diccionairo del Decoder.
# https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:
    @staticmethod
    def to_roman(n : int) -> str:
        NUMEROS_ROMANOS = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    
        romanizacion = ''
        while n > 0:
            for numero in NUMEROS_ROMANOS:
                while n >= numero:
                    romanizacion += NUMEROS_ROMANOS.get(numero)
                    n += -numero
    
        return romanizacion

    @staticmethod
    def from_roman(roman : str) -> int:
        
        NUMEROS_ROMANOS = {"CM": '900 ', "M": '1000', "CD": '400 ', "XC": '90 ' , "XL": '40 ', "IX": '9 ', "IV": '4 ', "M": '1000 ', "D": '500 ', "C": '100 ', "L": '50 ', "X": '10 ', "V": '5 ', "I": '1 ' }   

        for letraromana in NUMEROS_ROMANOS.keys():
        
            if letraromana in roman:
                roman = roman.replace(letraromana, NUMEROS_ROMANOS.get(letraromana))
    
        roman = roman.split()

        for i in range(len(roman)):
            roman[i] = int(roman[i])
    
        return sum(roman)