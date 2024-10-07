# It's a dumpster fire. Needs refactoring in the future — but hey, as long as it works... Lots of scope workarounds, good for a begginer. 
# https://www.codewars.com/kata/585894545a8a07255e0002f1

def count_patterns_from(firstPoint, length):
    if length < 1 or length > 9:
        return 0
    elif length == 1:
        return 1
    
    def A(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('A')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            A_VISITADO = True
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == True:
                if C_VISITADO == False:
                    C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == True:
                if G_VISITADO == False:
                    G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if I_VISITADO == False:
                    I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
            
    def B(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('B')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            B_VISITADO = True
            if A_VISITADO == False:
                A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if C_VISITADO == False:
                C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if G_VISITADO == False:
                G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if H_VISITADO == False:
                    H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if I_VISITADO == False:
                I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
            
    def C(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('C')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            C_VISITADO = True
            if B_VISITADO == True:
                if A_VISITADO == False:
                    A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if G_VISITADO == False:
                    G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == True:
                if I_VISITADO == False:
                    I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
            
    def D(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('D')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            D_VISITADO = True
            if A_VISITADO == False:
                A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if C_VISITADO == False:
                C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if F_VISITADO == False:
                    F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if G_VISITADO == False:
                G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if I_VISITADO == False:
                I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
    def E(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('E')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            E_VISITADO = True
            if A_VISITADO == False:
                A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if C_VISITADO == False:
                C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if G_VISITADO == False:
                G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if I_VISITADO == False:
                I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
            
    def F(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('F')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            F_VISITADO = True
            if A_VISITADO == False:
                A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if C_VISITADO == False:
                C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if D_VISITADO == False:
                    D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if G_VISITADO == False:
                G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if I_VISITADO == False:
                I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
    def G(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('G')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            G_VISITADO = True
            if D_VISITADO == True:
                if A_VISITADO == False:
                    A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if C_VISITADO == False:
                    C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == True:
                if I_VISITADO == False:
                    I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
            
    def H(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('H')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            H_VISITADO = True
            if A_VISITADO == False:
                A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == True:
                if B_VISITADO == False:
                    B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if C_VISITADO == False:
                C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if G_VISITADO == False:
                G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if I_VISITADO == False:
                I(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
    def I(profundidad, A_VISITADO = False, B_VISITADO = False, C_VISITADO = False, D_VISITADO = False, E_VISITADO = False, F_VISITADO = False, G_VISITADO = False, H_VISITADO = False, I_VISITADO = False):
        nonlocal total
        #print ('I')
        if profundidad == length:
            total += 1
        else:
            profundidad += 1
            I_VISITADO = True
            if E_VISITADO == True:
                if A_VISITADO == False:
                    A(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if B_VISITADO == False:
                B(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == True:
                if C_VISITADO == False:
                    C(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if D_VISITADO == False:
                D(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if E_VISITADO == False:
                E(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if F_VISITADO == False:
                F(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == True:
                if G_VISITADO == False:
                    G(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            if H_VISITADO == False:
                H(profundidad, A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO)
            
    
    NODOS = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I}
    A_VISITADO, B_VISITADO, C_VISITADO, D_VISITADO, E_VISITADO, F_VISITADO, G_VISITADO, H_VISITADO, I_VISITADO = (False,)*9
    profundidad = 1
    total = 0
    
    #Length es nuestra profundidad:
    
    

            
    NODOS.get(firstPoint)(profundidad)
    #print (total)
    return total
    
    
            
        
    
    pass