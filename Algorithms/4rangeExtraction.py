#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/

def solution(args):
    rangoparcial = ''
    rangofinal = ''
    for numeroIndex in range(len(args)):
        if numeroIndex < len(args):
            if abs(abs(args[numeroIndex]) - abs(args[numeroIndex+1])) < 2:
                if rangoparcial == '':
                    rangoparcial += str(args[numeroIndex]) + '-'
            else:
                rangofinal += rangoparcial + str(args[numeroIndex]) + ','
        else:
            rangofinal += str(args[numeroIndex])
            
        

    return 'a'


if __name__ == '__main__':
        assert(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) == '-6,-3-1,3-5,7-11,14,15,17-20'
        assert(solution([-3,-2,-1,2,10,15,16,18,19,20])) == '-3--1,2,10,15,16,18-20'