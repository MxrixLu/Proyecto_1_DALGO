import math as m

points = {"X":0,"Y":0,"Z":0}

already_set = set()
def recursive_board_game(Xi, Xj, Yi, Yj, Zi, Zj, Board, points, already_been):
    r = len(Board) - 1
    c = len(Board[0]) - 1
    
    points = points.copy()
    already_been = already_been.copy()
    
    # ----------- Movimiento de Z
    if not (Zi < 0):
        if Zj == -1 or Zj > c or Board[Zi][Zj] == -1 :
            points["Z"] = 0
            Zi = None
        elif Zi == r // 2:
            if (Zi, Zj) not in already_been:
                points["Z"] += Board[Zi][Zj]
                already_been.add((Zi, Zj))
            Zi = None
        else:
            if (Zi, Zj) not in already_been:
                points["Z"] += Board[Zi][Zj]
                already_been.add((Zi, Zj))

    # ----------- Movimiento de X
    if not (Xi < 0):
        
        if Xj == -1 or Xj > c or Board[Xi][Xj] == -1 :
            points["X"] = 0
            Xi = None
        elif Xi == r // 2:
            if (Xi, Xj) not in already_been:
                points["X"] += Board[Xi][Xj]
                already_been.add((Xi, Xj))
            Xi = None
        else:
            if (Xi, Xj) not in already_been:
                points["X"] += Board[Xi][Xj]
                already_been.add((Xi, Xj))

    # ----------- Movimiento de Y
    if not (Yi < 0):
        if Yj == -1 or Yj > c or Board[Yi][Yj] == -1 :
            points["Y"] = 0
            Yi = None
        elif Yi == r // 2:
            if (Yi, Yj) not in already_been:
                points["Y"] += Board[Yi][Yj]
                already_been.add((Yi, Yj))
            Yi = None
        else:
            if (Yi, Yj) not in already_been:
                points["Y"] += Board[Yi][Yj]
                already_been.add((Yi, Yj))

    # ----------- Recursión
    if Xi is None or Yi is None or Zi is None:
        return points
    else:
        maxim = {'max': max(
            sum(list(recursive_board_game(Xi + 1, Xj - 1, Yi + 1, Yj - 1, Zi - 1, Zj - 1, Board, points, already_been).values())),
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj-1, Zi-1, Zj, Board , points , already_been ).values())),    # X izq, Y izq, Z recto
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj-1, Zi-1, Zj+1, Board , points , already_been ).values())),  # X izq, Y izq, Z der
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj, Zi-1, Zj-1, Board , points , already_been ).values())),    # X izq, Y recto, Z izq
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj, Zi-1, Zj, Board , points , already_been ).values())),      # X izq, Y recto, Z recto
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj, Zi-1, Zj+1, Board , points , already_been ).values())),    # X izq, Y recto, Z der
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj+1, Zi-1, Zj-1, Board , points , already_been ).values())),  # X izq, Y der, Z izq
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj+1, Zi-1, Zj, Board , points , already_been ).values())),    # X izq, Y der, Z recto
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj+1, Zi-1, Zj+1, Board , points , already_been ).values())),  # X izq, Y der, Z der
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj-1, Zi-1, Zj-1, Board , points , already_been ).values())),    # X recto, Y izq, Z izq
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj-1, Zi-1, Zj, Board , points , already_been ).values())),      # X recto, Y izq, Z recto
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj-1, Zi-1, Zj+1, Board , points , already_been ).values())),    # X recto, Y izq, Z der
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj, Zi-1, Zj-1, Board , points , already_been ).values())),      # X recto, Y recto, Z izq
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj, Zi-1, Zj, Board , points , already_been ).values())),        # X recto, Y recto, Z recto
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj, Zi-1, Zj+1, Board , points , already_been ).values())),      # X recto, Y recto, Z der
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj+1, Zi-1, Zj-1, Board , points , already_been ).values())),    # X recto, Y der, Z izq
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj+1, Zi-1, Zj, Board , points , already_been ).values())),      # X recto, Y der, Z recto
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj+1, Zi-1, Zj+1, Board , points , already_been ).values())),    # X recto, Y der, Z der
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj-1, Zi-1, Zj-1, Board , points , already_been ).values())),  # X der, Y izq, Z izq
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj-1, Zi-1, Zj, Board , points , already_been ).values())),    # X der, Y izq, Z recto
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj-1, Zi-1, Zj+1, Board , points , already_been ).values())),  # X der, Y izq, Z der
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj, Zi-1, Zj-1, Board , points , already_been ).values())),    # X der, Y recto, Z izq
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj, Zi-1, Zj, Board , points , already_been ).values())),      # X der, Y recto, Z recto
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj, Zi-1, Zj+1, Board , points , already_been ).values())),    # X der, Y recto, Z der
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj+1, Zi-1, Zj-1, Board , points , already_been ).values())),  # X der, Y der, Z izq
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj+1, Zi-1, Zj, Board , points , already_been ).values())),    # X der, Y der, Z recto
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj+1, Zi-1, Zj+1, Board , points , already_been ).values()))   # X der, Y der, Z der
        )}
        return maxim

def reliquias(matriz, r, c): 
    indianaXi = 0
    indianaXj = 0
    marionYi = 0
    marionYj = c-1
    SallahZi = r-1
    SallahZj = c//2
    return recursive_board_game(indianaXi, indianaXj, marionYi, marionYj, SallahZi, SallahZj, matriz, points, already_set)

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
            print(f"Máximo de recursive_board_game: {resultado} , caso {contador}")
            contador += 1
        
    elif opcion == 2:
        R, C = map(int, input().strip().split())
        matriz = [list(map(int, input().strip().split())) for _ in range(R)]
        print(f"Procesando caso con matriz de tamaño {R}x{C}:")
        resultado = reliquias(matriz, R, C)
        print(f"Máximo de recursive_board_game: {resultado}")
        
    elif opcion == 3:
        print(reliquias(matriz, R, C))
    
if __name__ == "__main__":
    main()
    

