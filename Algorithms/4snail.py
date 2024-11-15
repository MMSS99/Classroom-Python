# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/

def snail(snailMap):
    x, y = 0, 0
    mapHeight = len(snailMap)
    mapWidth = len(snailMap[0])
    snailPath = []


    def snailRight(x, y):
        while x < mapWidth:
            if isinstance(snailMap[y][x], int):
                snailPath.append(snailMap[y][x])
                snailMap[y][x] = 'BABA'
                x += 1
            else:
                x -= 1
                break

        if len(snailPath) < (mapHeight * mapWidth):
            if x == mapWidth:
                x -= 1
            y += 1
            snailDown(x, y)

    def snailDown(x, y):
        while y < mapHeight:
            if isinstance(snailMap[y][x], int):
                snailPath.append(snailMap[y][x])
                snailMap[y][x] = 'BABA'
                y += 1
            else:
                y -= 1
                break

        if len(snailPath) < (mapHeight * mapWidth):
            if y == mapHeight:
                y -= 1
            x -= 1
            snailLeft(x, y)

    def snailLeft(x, y):
        while x >= 0:
            if isinstance(snailMap[y][x], int):
                snailPath.append(snailMap[y][x])
                snailMap[y][x] = 'BABA'
                x -= 1
            else:
                x += 1
                break

        if len(snailPath) < (mapHeight * mapWidth):
            if x < 0:
                x = 0
            y -= 1
            snailUp(x, y)

    def snailUp(x, y):
        while y >= 0:
            if isinstance(snailMap[y][x], int):
                snailPath.append(snailMap[y][x])
                snailMap[y][x] = 'BABA'
                y -= 1
            else:
                y += 1
                break

        if len(snailPath) < (mapHeight * mapWidth):
            if y < 0:
                y = 0
            x += 1
            snailRight(x, y)

    snailRight(x, y)

    return snailPath
        


if __name__ == "__main__":
    assert  snail([[1,2,3],
             [4,5,6],
             [7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    
