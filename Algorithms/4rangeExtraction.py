#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/

def solution(args):
    #Cogemos un número y lo lanzamos contra un array, donde lanzamos el siguiente. Si la resta de sus absolutos es mayor que 1, sacamos el indice anterior y continuamos.
    finalRange = ''
    partialRange = []
    numberIndex = 0
    absoluteCalculator = 0
    rangeChecker = []
    while numberIndex < len(args):
        try:
            #absoluteCalculator = abs(abs(args[numberIndex]) - abs(args[numberIndex + 1]))
            #rangeChecker = map(rangeChecker.append, range(args[numberIndex],args[numberIndex + 1]))
            for i in range(args[numberIndex],args[numberIndex + 1]):
                rangeChecker.append(i)
            absoluteCalculator = len(rangeChecker)
            rangeChecker = []
            if absoluteCalculator < 2 and absoluteCalculator != 0:
                partialRange.append(args[numberIndex])
            else:
                if len(partialRange) >= 2:
                    finalRange += str(partialRange[0]) + '-' +str(args[numberIndex]) + ','
                    partialRange = []
                elif len(partialRange) == 1:
                    finalRange += str(partialRange[0]) + ',' +str(args[numberIndex]) + ','
                    partialRange = []
                elif len(partialRange) == 0:
                    finalRange += str(args[numberIndex]) + ','
            numberIndex += 1
        except IndexError:
            if len(partialRange) >= 2:
                finalRange += str(partialRange[0]) + '-' +str(args[numberIndex]) + ','
                partialRange = []
            elif len(partialRange) == 1:
                finalRange += str(partialRange[0]) + ',' +str(args[numberIndex]) + ','
                partialRange = []
            elif len(partialRange) == 0:
                finalRange += str(args[numberIndex]) + ','
            return finalRange[:-1]
             





'''  
    rangoparcial = ''
    rangofinal = ''
    for numeroIndex in range(len(args)):
        if numeroIndex < (len(args)-1):
            if abs(abs(args[numeroIndex]) - abs(args[numeroIndex+1])) < 2:
                if rangoparcial == '':
                    rangoparcial += str(args[numeroIndex]) + '-'
            else:
                rangofinal += rangoparcial + str(args[numeroIndex]) + ','
                rangoparcial = ''
        else:
            if rangoparcial != '':
                 rangofinal += rangoparcial + str(args[numeroIndex])
            else: 
                rangofinal += str(args[numeroIndex])

    return 'a'
'''


if __name__ == '__main__':
        assert(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) == '-6,-3-1,3-5,7-11,14,15,17-20' 
        # Incapaz de introducir como caracter solitario dos números seguidos. 
        # = Comparación de índices para actualizar rangoparcial (tiene que haber una diferencia de > 1)
        assert(solution([-3,-2,-1,2,10,15,16,18,19,20])) == '-3--1,2,10,15,16,18-20'
        # Si pasa por cero, la lógica rompe por la resta. (2-1 = 1, aunque no existiesen -1 y 0 haría una serie)

