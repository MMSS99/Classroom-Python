#https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
    counter = 0
    for x in arr:
        if len(x) == 2:
            if x[0] == ":" or x[0] == ";":
                if x[1] == ")" or x[1] == "D":
                    counter += 1
                else:
                    counter += 0
            else:
                counter += 0
        
        elif len(x) == 3:
            if x[0] == ":" or x[0] == ";":
                if x[1] == "-" or x[1] == "~":
                    if x[2] == ")" or x[2] == "D":
                        counter += 1
                    else:
                        counter += 0
                    
                else:
                    counter += 0
            else:
                counter += 0
            
    return counter