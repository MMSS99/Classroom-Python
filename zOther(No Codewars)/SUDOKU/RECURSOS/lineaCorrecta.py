# Pasamos por todos los elementos de la lista y contamos que aparezcan una sola vez.

def compLineas(matrix):
    for i in matrix:
        for j in i:
            if i.count(j) != 1:
                return False
    return True
            
if __name__ == '__main__':
    print (compLineas([[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]))