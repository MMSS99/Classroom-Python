#https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    
    #print (text[:1]+ ''.join(word.capitalize() for word in (text.replace("-", " ").replace("_"," ").split()))[1:])
    '''
    text = list(text)
    camel = ""
    for caracter in text:
        if caracter == '_' or caracter == '-':
            indice = text.index(caracter)
            text[indice] = ''
            text[indice + 1] = text[indice + 1].upper()
    return "".join(i for i in text) '''
    
    return text[:1]+ ''.join(word.capitalize() for word in (text.replace("-", " ").replace("_"," ").split()))[1:]


if __name__ == "__main__":
    assert to_camel_case("") == "" #"An empty string was provided but not returned")
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior" # "to_camel_case('the_stealth_warrior') did not return correct value"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior" # "to_camel_case('The-Stealth-Warrior') did not return correct value"
    assert to_camel_case("A-B-C") == "ABC" # "to_camel_case('A-B-C') did not return correct value"