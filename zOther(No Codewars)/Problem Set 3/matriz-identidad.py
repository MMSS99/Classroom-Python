#https://github.com/dfleta/Python_ejercicios/blob/master/Procedimental/Unidad_3_%20Listas_y_%20operaciones_sobre_listas/problem_set_3/matriz_identidad.py

def esMatrizIdentidad(matrix):

    if len(matrix) < 3:
        return False
    
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return False
        else:

            if matrix[i][i] != 1:
                return False
            else: 

                for j in range(len(matrix)):
                    if j != i:
                        if matrix[i][j] != 0:
                            return False
                    else:
                        continue
    return True

print (esMatrizIdentidad([[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]))


