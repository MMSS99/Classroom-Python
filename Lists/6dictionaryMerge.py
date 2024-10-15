#https://www.codewars.com/kata/5ae840b8783bb4ef79000094/

def merge(*dicts):
    megadict = {}
    for dict in dicts:
        for i in dict:
            if i not in megadict:
                megadict[i] = [dict.get(i)]
            else:
                megadict[i].append(dict.get(i))  
    return megadict