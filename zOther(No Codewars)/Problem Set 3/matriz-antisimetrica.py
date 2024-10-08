#https://github.com/dfleta/Python_ejercicios/blob/master/Procedimental/Unidad_3_%20Listas_y_%20operaciones_sobre_listas/problem_set_3/matriz_antisimetrica.py

def esAntisimetrica(matriz):
    
    if len(matriz) < 3:
        return False
    
    for i in range(len(matriz)):
        if len(matriz) != len(matriz[i]):
            print ("Soy Concha, entro", len(matriz), len(matriz[i]))
            return False
        else:
            for j in range(len(matriz[i])):
                if matriz[i][j] + matriz[j][i] !=0:
                    print ("Soy Concha, entro", matriz[i][j], matriz[j][i])
                    return False
    return True

print (esAntisimetrica([[1,0,0,0,0,0,0,0,0]]))  

