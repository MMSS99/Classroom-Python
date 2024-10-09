#Comprobamos que el sudoku no tenga una lista en su interior que rompa su forma de cuadrado excediendo en carácteres el número de listas en la matriz.

def sudokuEstandar(matrix):
    for i in range(len(matrix)):
        if len(i) != len(matrix):
            return False