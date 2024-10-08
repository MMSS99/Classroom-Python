#https://github.com/dfleta/Python_ejercicios/blob/master/Procedimental/Unidad_3_%20Listas_y_%20operaciones_sobre_listas/problem_set_3/04-Greatest.py

def greatest (list):
    if not list:
        return 0
    else:
        list.sort()
        return list[-1]
    
print (greatest([4,23,1]))
