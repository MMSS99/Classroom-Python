#https://www.codewars.com/kata/5db42a943c3c65001dcedb1a

def encoder(data):
    CODEX = {'': 0}
    checker = ''
    encoded = ''
    for i in range(len(data)):
        checker += data[i]
        if checker not in CODEX:
            CODEX[checker] = len(CODEX)
            encoded += str(CODEX.get(checker[:-1])) + checker[-1]
            checker = ''
            
    if checker != '':
        return (encoded + str(CODEX.get(checker)))
    else:
        return encoded
    
def decoder(data):
    CODEX = {'0': ''}
    checker = ''
    decoded = ''
    for i in data:
        if i.isnumeric():
            checker += i
        elif i.isalpha():
            checker = CODEX.get(checker) + i
            CODEX[str(len(CODEX))] = checker
            checker = ''
    
    chars = ''
    for i in range(len(data)):
        if data[i].isnumeric():
            chars += data[i]
        elif data[i].isalpha():
            if chars != '':
                print (chars)
                decoded += CODEX.get(chars)
            decoded += data[i]
            chars = ''

    if chars == '':
        return decoded
    else:
        return (decoded + CODEX.get(chars))

