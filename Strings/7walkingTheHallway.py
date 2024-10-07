#https://www.codewars.com/kata/6368426ec94f16a1e7e137fc

import math
# Necesitaremos math más tarde; quizás se pueda hacer con .round() pero no he probado.

def contact(hallway):
    
    # Se crea un Array en el que guardar los valores de las distancias entre > y < en un string.
    distancia = []
    
    # Observamos todos los carácteres de hallway buscando un '>':
    for i in range(len(hallway)):
        if hallway[i] == '>':
            # Cuando encontramos '>', medimos la distancia al siguiente '<' y lo guardamos en el Array.
            distancia.append(hallway[i:].find('<'))
    
    # Ordenamos el Array de menor a mayor, ya que nos interesa usar el menor número.
    distancia.sort()
    
    # Comprobamos que el Array sea positivo (tiene más que -1 dentro) y que por lo menos tenga 1 objeto en su interior. Si no cumple uno de esos dos casos, devolvemos -1 (<> no existen o nunca se van a encontrar)
    if sum(distancia) < 0 or len(distancia) == 0:
        return -1
    
    # Ya sin Arrays de sólo -1 o negativos, observamos en [0] del Array.
    elif distancia[0] == -1:
        # Eliminamos todo caso de -1 (> que nunca encuentra un <).
        while -1 in distancia: distancia.remove(-1)
        # Y devolvemos el valor del objeto en [0] del Array (distancia mínima entre > y < en el string) dividido entre 2 (ya que ambos > y < avanzan hacia el otro) redondeado hacia arriba para evitar inexactitudes.
        return math.ceil(distancia[0]/2)
    
    else:
        # Si en el Array todos los valores son positivos, simplemente dividimos el caso [0] del Array/2 con redondeo hacia arriba.
        return math.ceil(distancia[0]/2)