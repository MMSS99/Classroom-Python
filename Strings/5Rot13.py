#https://www.codewars.com/kata/530e15517bc88ac656000716/

def rot13(message):
    rottedString = ''
    encoder = 0
    for caracter in message:
        if caracter.isalpha() == True:
                
                if caracter.isupper() == True:
                    encoder = ord(caracter) + 13
                    if encoder > 90:
                        encoder += -26
                    rottedString += chr(encoder)

                else:
                    encoder = ord(caracter) + 13
                    if encoder > 122:
                        encoder += -26
                    rottedString += chr(encoder)

        else: 
            rottedString += caracter
    
    return rottedString

                      

if __name__ == "__main__":
        assert(rot13('test')) == 'grfg' #'Returned solution incorrect for fixed string = test'
        assert(rot13('Test')) == 'Grfg' #'Returned solution incorrect for fixed string = Test'
        assert(rot13('aA bB zZ 1234 *!?%')) == 'nN oO mM 1234 *!?%' #'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%'