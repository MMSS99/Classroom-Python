#https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    zeros = lst.count(0)
    for i in range(zeros):
        lst.remove(0)
        lst.append(0)
    return lst