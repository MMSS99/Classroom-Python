#https://www.codewars.com/kata/54b724efac3d5402db00065e/

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    demorsed = ''
    for i in morse_code.split(' '):
        if i in MORSE_CODE:
            demorsed += MORSE_CODE.get(i)
        else:
            demorsed += ' '
    
    while demorsed[0] == ' ':
        demorsed = demorsed[1:]
    while demorsed[-1] == ' ':
        demorsed = demorsed[:-1]
    
    demorsed = demorsed.replace('  ', ' ')

    return demorsed