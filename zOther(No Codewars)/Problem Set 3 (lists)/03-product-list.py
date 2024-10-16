#https://github.com/dfleta/Python_ejercicios/blob/master/Procedimental/Unidad_3_%20Listas_y_%20operaciones_sobre_listas/problem_set_3/03-Product_List.py

def product_list(list):
    resultado = 1
    for i in list:
        resultado *= i
    return resultado

print (product_list([1,2,3,4]))
