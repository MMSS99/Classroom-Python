#https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    # Assing value to letter -> Sum value of all letters and / 10
    print (walk)
    latitude = 0
    altitude = 0
    if len(walk) != 10:
        return False
    
    for x in walk:
        if x == "n":
            altitude += 1
        if x == "s":
            altitude += -1
        if x == "w":
            latitude += 1
        if x == "e":
            latitude += -1
    if altitude == 0 and latitude == 0:
        return True
    else:
        return False