#https://www.codewars.com/kata/59884371d1d8d3d9270000a5

def shake_tree(tree):
    
    # El array que devolveremos y mutaremos para conocer la posición de las bellotas en todo momento.
    bellotas = []
    
    # Buscamos las bellotas en la primera rama y creamos un array con ellas: si en una posición hay una bellota, le damos un 1 al array. Si no la hay, le damos un 0.
    for i in tree[0]:
        if i == ' ':
            bellotas.append(0)
        elif i == 'o':
            bellotas.append(1)
    
    # Dividimos el arbol en ramas (la lista de arrays en arrays)
    for rama in tree:
        
        # Como un mono, vamos rama por rama (o sea, visitamos todos los carácteres del array). Queremos saber en qué carácter nos encontramos, ya que tendremos que comparar las posiciones exactas de nuestro array "bellotas" y la "rama" en la que nos encontramos.
        for j in range(len(rama)):
            # Si nos encontramos un '/' en la misma posición de la rama en la que tenemos una 'o' (ahora un 1) en bellotas, movemos el valor de esa posición del array 'bellotas' a la anterior (se desplaza a la izquierda), y colocamos la posición actual en 0.
            # Esta filosofía de desplazamiento bellotil la utilizaremos para '\\' (importante colocar dos para que python no piense que es solo un carácter de escape) y para '_'
            if rama[j] == '/' and bellotas[j] > 0:
                bellotas[j-1] += bellotas[j]
                bellotas[j] = 0
            elif rama[j] == '\\' and bellotas[j] > 0:
                bellotas[j+1] += bellotas[j]
                bellotas[j] = 0
            elif rama[j] == '_' and bellotas[j] > 0:
                bellotas[j] = 0
    
    return bellotas