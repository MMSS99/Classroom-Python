#https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python

def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    
    cents = int(cents)
    
    while cents > 0:
        if cents >= 25:
            change_dict['Quarters'] = cents // 25
            cents = cents%25
        elif cents >= 10:
            change_dict['Dimes'] = cents // 10
            cents = cents%10
        elif cents >= 5:
            change_dict['Nickels'] = cents//5
            cents = cents%5
        elif cents >= 1:
            change_dict['Pennies'] += 1
            cents += -1
            
    return change_dict