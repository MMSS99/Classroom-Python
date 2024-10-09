#https://github.com/dfleta/sudokuModules/blob/main

from RECURSOS.columnaCorrecta import compColumnas
from RECURSOS.lineaCorrecta import compLineas
from RECURSOS.sudokuEstandar import compEstandar

def compSudoku(matrix):
    if compColumnas(matrix) == True and compLineas(matrix) == True and compEstandar(matrix) == True:
        return True
    else:
        return False
    
if __name__ == '__main__':
    import RECURSOS.casosTestSudoku as casosTest

    for caso in sorted(casosTest.__dict__):
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Es un sudoku correto? = "] + [compSudoku(casosTest.__dict__[caso])])

