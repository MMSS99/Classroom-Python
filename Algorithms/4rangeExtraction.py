#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/

def solution(args):
    finalRange = ''
    partialRange = []
    numberIndex = 0
    absoluteCalculator = 0
    rangeChecker = []
    while numberIndex < len(args):
        try:

            for i in range(args[numberIndex],args[numberIndex + 1]):
                rangeChecker.append(i)
            absoluteCalculator = len(rangeChecker)
            rangeChecker = []

            if absoluteCalculator < 2 and absoluteCalculator != 0:
                partialRange.append(args[numberIndex])
            else:
                finalRange = finalRangeAdder(partialRange, finalRange, args[numberIndex])
                partialRange = []
            numberIndex += 1

        except IndexError:
            finalRange = finalRangeAdder(partialRange, finalRange, args[numberIndex])
            return finalRange[:-1]
        
def finalRangeAdder(partialRange, finalRange, number):

    if len(partialRange) >= 2:
        finalRange += str(partialRange[0]) + '-' +str(number) + ','
    elif len(partialRange) == 1:
        finalRange += str(partialRange[0]) + ',' +str(number) + ','
    elif len(partialRange) == 0:
        finalRange += str(number) + ','

    return finalRange
             




if __name__ == '__main__':
        assert(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) == '-6,-3-1,3-5,7-11,14,15,17-20' 
        assert(solution([-3,-2,-1,2,10,15,16,18,19,20])) == '-3--1,2,10,15,16,18-20'

