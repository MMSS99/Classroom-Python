#https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    
    final = ''
    
    date = [0, 0, 0, 0, 0]
    
    while seconds > 59:
        if seconds >= 31536000:
            date[0] = seconds//31536000
            seconds = seconds%31536000
            continue
        elif seconds >= 86400:
            date[1] = seconds//86400
            seconds = seconds%86400
            continue
        elif seconds >= 3600:
            date[2] = seconds//3600
            seconds = seconds%3600
            continue
        elif seconds >= 60:
            date[3] = seconds//60
            seconds = seconds%60
    
    date[4] = seconds
        
    print (date)
            
    
    if date[0] != 0:
        if date[0] == 1:
            date[0] = "1 year"
        else:
            date[0] = str(date[0])+" years"
    
    if date[1] != 0:
        if date[1] == 1:
            date[1] = "1 day"
        else:
            date[1] = str(date[1])+" days"
    
    if date[2] != 0:
        if date[2] == 1:
            date[2] = "1 hour"
        else:
            date[2] = str(date[2])+" hours"
    
    if date[3] != 0:
        if date[3] == 1:
            date[3] = "1 minute"
        else:
            date[3] = str(date[3])+" minutes"
        
    if date[4] != 0:
        if date[4] == 1:
            date[4] = "1 second"
        else:
            date[4] = str(date[4])+" seconds"
    
    if date.count(0) < 4:
        while 0 in date:
            date.remove(0)
        for i in range(len(date)-1):
            final += date[i]+", "
        return final[:-2] + " and " + date[-1]
        
    else:
        for i in range(len(date)):
            if date[i] != 0:
                return date[i]
    
    #print (date)