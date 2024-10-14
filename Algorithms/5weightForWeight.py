#https://www.codewars.com/kata/55c6126177c9441a570000cc/ — Should've used (sorted, x key='ARGUMENT, probably the array I called pesosnuevos')

def order_weight(pesos):
    if not pesos:
        return ''
    
    pesos = pesos.split()
    pesosnuevos = pesos[:]
    buffer = []
    
    for i in range(len(pesos)):
        pesosnuevos[i] = 0
        for j in pesos[i]:
            pesosnuevos[i] += int(j)
        buffer.append( [pesosnuevos[i], int(pesos[i])] )
            

    buffer2 = []
    paso = []
    max = sorted(buffer, reverse=True)[0][0]
    cont = 0    
    while cont <= max:
        for i in range(len(buffer)):
            if buffer[i][0] == cont:
                paso.append(str(buffer[i][1]))
        if paso:
            buffer2.append(sorted(paso))
        paso.clear()
        cont += 1
        
    final = ''
    for i in buffer2:
        for j in i:
            print (j)
            final += j + ' '
    
    return final[:-1]