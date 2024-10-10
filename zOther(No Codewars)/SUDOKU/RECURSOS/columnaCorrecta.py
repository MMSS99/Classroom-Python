# Observamos el número en los índices de todas las listas y comprobamos que no aparezcan más de una vez.

from .sudokuEstandar import compEstandar

def compColumnas(matrix):
    if compEstandar(matrix) == False:
        return False

    for i in range(len(matrix)):
        comprobante = []
        for lista in matrix:
            comprobante.append(lista[i])

        for numero in comprobante:
            if comprobante.count(numero) != 1:
                return False
            
    return True

if __name__ == '__main__':
    import casosTestSudoku as casosTest

    for caso in sorted(casosTest.__dict__):
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Son las columnas del sudoku correctas? = "] + [compColumnas(casosTest.__dict__[caso])])
