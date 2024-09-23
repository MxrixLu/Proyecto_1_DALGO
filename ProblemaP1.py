import math as m

def reliquias_sal(matriz, r, c ):
    sallah = (r, c//2 +1) 
    if sallah[0] == r//2 +1:
        return matriz[sallah[0]][sallah[1]]
    if sallah[0] != r//2 +1: 
        return max(reliquias_sal(matriz, r-1, c), reliquias_sal(matriz, r-1, c-1), reliquias_sal(matriz, r-1, c+1))
    if matriz[sallah[0]][sallah[1]] == -1: 
        return - m.inf
    
def reliquias_ind_mar(matriz, r, c ): 
    i = 0
    j = 0
    k = c
    indiana = (0,0)
    marion = (0, c)
    if indiana and indiana[1] != marion[1]: 
        return max(reliquias_ind_mar(matriz, c), reliquias_ind_mar)
        
    
    
    