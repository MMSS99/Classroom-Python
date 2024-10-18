#https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    
    hexadecimal = ''
    tonos = [r, g, b]
    for indiceColor in range(len(tonos)):
        if int(tonos[indiceColor]) < 0:
            tonos[indiceColor] = 0
        elif int(tonos[indiceColor]) > 255:
            tonos[indiceColor] = 255
        
        tonos[indiceColor] = hex(tonos[indiceColor])[2:]
        if len(tonos[indiceColor]) < 2:
            tonos[indiceColor] = '0' + tonos[indiceColor]

        hexadecimal += tonos[indiceColor].upper()   

    return hexadecimal
            
        
if __name__ == '__main__':
    assert (rgb(0, 0, 0)) == "000000"
    assert (rgb(1, 2, 3)) == "010203"
    assert (rgb(255, 255, 255)) == "FFFFFF"
    assert (rgb(254, 253, 252)) == "FEFDFC"
    assert (rgb(-20, 275, 125)) == "00FF7D"