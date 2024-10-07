#https://www.codewars.com/kata/55832eda1430b01275000059

def roman_fractions(integer, fraction=None):
    # Sacamos los casos NaR y N antes de entrar en bucles.
    if integer > 5000 or integer < 0:
        return 'NaR'
    if fraction:
        if fraction < 0 or fraction > 12: #or integer == 0:
            return 'NaR'
    if integer == 0 and fraction == 12:
        return 'NaR'
    if integer == 0 and not fraction:
        return 'N'
    
    # String que devolveremos.
    romanfraction = ''
    
    # Desgranamos el número (integer)
    while integer > 0:
        if integer >= 1000:
            romanfraction += 'M'
            integer += -1000
            continue
        elif integer >= 900:
            romanfraction += 'CM'
            integer += -900
            continue
        elif integer >= 500:
            romanfraction += 'D'
            integer += -500
            continue
        elif integer >= 400:
            romanfraction += 'CD'
            integer += -400
            continue
        elif integer >= 100:
            romanfraction += 'C'
            integer += -100
            continue
        elif integer >= 90:
            romanfraction += 'XC'
            integer += -90
            continue
        elif integer >= 50:
            romanfraction += 'L'
            integer += -50
            continue
        elif integer >= 40:
            romanfraction += 'XL'
            integer += -40
            continue
        elif integer >= 10:
            romanfraction += 'X'
            integer += -10
            continue
        elif integer >= 9:
            romanfraction += 'IX'
            integer += -9
            continue
        elif integer >= 5:
            romanfraction += 'V'
            integer += -5
            continue
        elif integer >= 4:
            romanfraction += 'IV'
            integer += -4
            continue
        elif integer >= 1:
            romanfraction += 'I'
            integer += -1
            continue
            
    # Desgranamos la fracción (fraction)
    while fraction != 0 and fraction != None:
        if fraction == 12:
            break
        elif fraction >= 6:
            romanfraction += 'S'
            fraction += -6
            continue
        elif fraction == 5:
            romanfraction += ':.:'
            break
        elif fraction == 4:
            romanfraction += '::'
            break
        elif fraction == 3:
            romanfraction += ':.'
            break
        elif fraction == 2:
            romanfraction += ':'
            break
        elif fraction == 1:
            romanfraction += '.'
            break
    
    return romanfraction