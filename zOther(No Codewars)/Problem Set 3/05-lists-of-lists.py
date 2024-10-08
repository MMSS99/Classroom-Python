#https://github.com/dfleta/Python_ejercicios/blob/master/Procedimental/Unidad_3_%20Listas_y_%20operaciones_sobre_listas/problem_set_3/05-Lists_Of_Lists.py

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(listoflist):
    estudiantestotal = 0
    becastotal = 0
    for i in listoflist:
        estudiantestotal += i[1]
        becastotal += i[1] * i[2]
    return estudiantestotal, becastotal

print (total_enrollment(usa_univs))


