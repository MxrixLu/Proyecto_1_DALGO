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

def leer_casos_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        num_casos = int(archivo.readline().strip())
        casos = []
        
        for _ in range(num_casos):
            R, C = map(int, archivo.readline().strip().split())
            matriz = [list(map(int, archivo.readline().strip().split())) for _ in range(R)]
            casos.append({'R': R, 'C': C, 'matriz': matriz})
        
        return casos

# Función para procesar cada caso
def procesar_caso(caso):
    R, C, matriz = caso['R'], caso['C'], caso['matriz']
    return reliquias(matriz, R, C)

def main(): 
    opcion = int(input("Ingrese 1 para leer archivo o 2 para escribirlo en consola o 3 para la matriz por defecto: "))
    if opcion == 1:
        nombre_archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
        casos = leer_casos_desde_archivo(nombre_archivo_entrada)
        
        # Procesar cada caso
        resultados = [procesar_caso(caso) for caso in casos]
        contador = 1
        for resultado in resultados:
            print(f"Máximo de reliquias: {resultado} , caso {contador}")
            contador += 1
        
    elif opcion == 2:
        R, C = map(int, input().strip().split())
        matriz = [list(map(int, input().strip().split())) for _ in range(R)]
        print(f"Procesando caso con matriz de tamaño {R}x{C}:")
        resultado = reliquias(matriz, R, C)
        print(f"Máximo de reliquias: {resultado}")
        
    elif opcion == 3:
        print(reliquias(matriz, R, C))
    
    

if __name__ == "__main__":
    main()