#https://www.codewars.com/kata/5208f99aee097e6552000148

def solution(s):
    # -> When cap is detected, insert space before+ç
    camel = ""
    for x in s:
        if x.isupper():
            camel += " " + "".join(x)
        else:
            camel += "".join(x)
    return camel