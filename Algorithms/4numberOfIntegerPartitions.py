# https://www.codewars.com/kata/546d5028ddbcbd4b8d001254/
# El algoritmo también resuelve este kata: https://www.codewars.com/kata/52ec24228a515e620b0005ef
# Secuencia relevante para solución (matriz inversa): https://oeis.org/A000041

def partitions(number):
    sequence = [1] + [0]*number

    for indexBase in range(1,number+1):
        for indexOperation in range(indexBase,number+1):
            sequence[indexOperation] += sequence[indexOperation-indexBase]

    return sequence[-1]

if __name__ == "__main__":
    assert partitions(5) == 7
    assert partitions(10) == 42
    assert partitions(25) == 1958