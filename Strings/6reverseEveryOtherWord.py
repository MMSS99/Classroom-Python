#https://www.codewars.com/kata/58d76854024c72c3e20000de
# Should've used a while loop.

def reverse_alternate(st):
    words = st.split()
    #print (words)
    counter = 0
    converter1 = ""
    converter2 = ""
    final = ""
    for x in words:
        #print (x)
        counter += 1
        
        if counter%2 == 0:
            #print (x)
            converter1 = list(x)
            
            for i in range((len(x)-1), -1 ,-1):
                #print (converter1[i])
                converter2 += "".join(converter1[i])
                
            #print (converter2)
            x = converter2
            converter2 = ""
            
        final += x + " "
        #print (final)
        
    return final[:-1]
            #print (converter)