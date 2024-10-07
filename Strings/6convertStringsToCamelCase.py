#https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    text = list(text)
    camel = ""
    for caracter in text:
        if caracter == '_' or caracter == '-':
            indice = text.index(caracter)
            text[indice] = ''
            text[indice + 1] = text[indice + 1].upper()
    return "".join(i for i in text) 