import math as m

def reliquias_sal(matriz, i, j, r , c):
    if i == r // 2:  # Caso base: Sallah llega a la fila central
        return matriz[i][j], [(i, j)] 

    if matriz[i][j] == -1:  # Caso base: Celda con maldición
        return -m.inf, [] 

    if i != r // 2: 
        # Llamadas recursivas 
        valor_arriba, camino_arriba = reliquias_sal(matriz, i - 1, j, r, c)
        valor_izquierda, camino_izquierda = reliquias_sal(matriz, i - 1, j - 1, r ,c ) if j > 0 else (-m.inf, []) # Evitar salir de la matriz
        valor_derecha, camino_derecha = reliquias_sal(matriz, i - 1, j + 1, r,c) if j < len(matriz[0]) - 1 else (-m.inf, []) # Evitar salir de la matriz

        # Encontrar el máximo y su camino correspondiente
        max_valor = max(valor_arriba, valor_izquierda, valor_derecha)
        if max_valor == valor_arriba:
            camino = camino_arriba
        elif max_valor == valor_izquierda:
            camino = camino_izquierda
        else:
            camino = camino_derecha

        # Agregar la coordenada actual al camino y sumar el valor de la reliquia
        camino.append((i, j))
        return max_valor + matriz[i][j], camino
        
def reliquias_ind_mar(matriz, i, j, k, R, C, coordenadas_sal):
    if any(coord in coordenadas_sal for coord in [(i, j), (i, k)]):
        return 0 # Celda inválida
    if matriz[i][j] == -1 or matriz[i][k] == -1:
        return -m.inf  # Celda con maldición

    if i == R // 2:
        return matriz[i][j] + matriz[i][k]

    max_reliquias = -m.inf
    return max_reliquias            
    
def reliquias(matriz, R, C):
    reliquias_saal, coordenadas_sal = reliquias_sal(matriz, R - 1, C // 2, R, C)
    #reliquias_ind_mare = reliquias_ind_mar(matriz, 0, 0, C - 1, R, C, coordenadas_sal) 
    return reliquias_saal
    
# Ejemplo de uso (mismo que antes)
matriz = [
    [0, 9, 1, 10, 0],
    [-1, -1, 5, -1, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]

R = 5
C = 5
print(reliquias(matriz, R, C))
