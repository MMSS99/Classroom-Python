# 
from .sudokuEstandar import compEstandar

def compNumeros(matrix):
    if compEstandar(matrix) == False:
        return False

    for i in matrix:
        for j in i:
            if j > len(matrix):
                return False
    return True

if __name__ == '__main__':
    import casosTestSudoku as casosTest

    for caso in sorted(casosTest.__dict__):
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Los números del sudoku están dentro de su rango? = "] + [compNumeros(casosTest.__dict__[caso])])

