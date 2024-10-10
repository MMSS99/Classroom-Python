# Pasamos por todos los elementos de la lista y contamos que aparezcan una sola vez.

def compLineas(matrix):
    for i in matrix:
        for j in i:
            if i.count(j) != 1:
                return False
    return True
            
if __name__ == '__main__':
    import casosTestSudoku as casosTest

    for caso in sorted(casosTest.__dict__):
        if not caso.startswith('__'):

            print (casosTest.__dict__[caso] + [", ¿Son las líneas del sudoku correctas? = "] + [compLineas(casosTest.__dict__[caso])])