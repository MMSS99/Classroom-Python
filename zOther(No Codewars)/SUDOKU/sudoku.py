#https://github.com/dfleta/sudokuModules/blob/main

# Requires a PYTHONPATH and __init__ (709 librorata) on /RECURSOS/ to initialize????

import sys
sys.path.append('.')

from RECURSOS.columnaCorrecta import compColumnas
from RECURSOS.lineaCorrecta import compLineas
from RECURSOS.sudokuEstandar import compEstandar
from RECURSOS.numerosRango import compNumeros

def compSudoku(matrix):
    if compColumnas(matrix) == True and compLineas(matrix) == True and compEstandar(matrix) == True and compNumeros(matrix) == True:
        return True
    else:
        return False
    
if __name__ == '__main__':
    import RECURSOS.casosTestSudoku as casosTest

    for caso in sorted(casosTest.__dict__):
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Es un sudoku correto? = "] + [compSudoku(casosTest.__dict__[caso])])

