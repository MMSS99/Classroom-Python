#https://www.codewars.com/kata/55722d67355421ab510001ac

def loose_change(coins_list, change):
    print (coins_list, change)
    
    # Hacer que change llegue a 0 siendo dividido por List lo antes posible. 
    
    coins = 0
    coincounter = []
    
    while change > 0:
        
        for i in sorted(coins_list)[::-1]:
            if change%i == 0:
                coincounter.append(coins + change//i)
                
        
        for j in sorted(coins_list)[::-1]:
            if change >= j:
                coins += 1
                change += -j
                break
                
        
    for k in coincounter:
        if k < coins:
            coins = k
    
    return coins