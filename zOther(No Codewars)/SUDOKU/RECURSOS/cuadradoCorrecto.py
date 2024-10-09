from columnaCorrecta import compColumnas
from lineaCorrecta import compLineas

def compCuadrado(matrix):
    if compColumnas(matrix) == True and compLineas(matrix) == True:
        print ('El Sudoku es correcto')
        return True
    else:
        print ('El Sudoko es correcto')
        return False
    






if __name__ == '__main__':
    print(compColumnas([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2]]))

    print (compLineas([[[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, 2]]]))