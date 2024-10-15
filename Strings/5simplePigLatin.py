#https://www.codewars.com/kata/520b9d2ad5c005041100000f — Easy to do because lacking tests about special characters imbeded onto the strings.

def pig_it(text):
    latinized = ''
    for i in text.split():
        if i.isalpha():
            latinized += (i+i[0]+'ay')[1:] + ' '
        else:
            latinized += i + ' '
    return (latinized[:-1])