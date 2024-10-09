# Observamos el número en los índices de todas las listas y comprobamos que no aparezcan más de una vez.

def compColumnas(matrix):
    for i in range(len(matrix)):
        comprobante = []
        for lista in matrix:
            comprobante.append(lista[i])

        for numero in comprobante:
            if comprobante.count(numero) != 1:
                return False
            
    return True

if __name__ == '__main__':
    print (compColumnas([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]))
