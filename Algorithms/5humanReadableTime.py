# https://www.codewars.com/kata/52685f7382004e774f0001f7/python

def make_readable(seconds):
    horas = 0
    minutos = 0
    
    while seconds > 59:
        if seconds >= 3600:
            horas = seconds//3600
            seconds = seconds%3600
            continue
        elif seconds >= 60:
            minutos = seconds//60
            seconds = seconds%60
            continue
            
    horas = str(horas)
    minutos = str(minutos)
    seconds = str(seconds)
    
    if len(horas) == 1:
        horas = '0' + str(horas)
    
        
    if len(minutos) == 1:
        minutos = '0' + str(minutos)
    
        
    if len(seconds) == 1:
        seconds = '0' + str(seconds)
    
    return horas+':'+minutos+':'+seconds