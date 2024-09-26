import math as m

points = {"X":0,"Y":0,"Z":0}

copy_al = set()
def recursive_board_game(Xi, Xj, Yi, Yj, Zi, Zj, Board, points, already_been):
    r = len(Board) - 1
    c = len(Board[0]) - 1
    
    # Copia de puntos y posiciones visitadas para evitar mutación
    points = points.copy()
    already_been = already_been.copy()
    
    # ----------- Movimiento de Z
    if not (Zi < 0):
        if Zj == -1 or Zj > c or (Board[Zi][Zj] == -1 and Zi < r // 2):
            points["Z"] = 0
            Zi = None  # Mejor uso de None en lugar de -inf
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
        if Xj == -1 or Xj > c or Board[Xi][Xj] == -1 or Xi > r // 2:
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
        if Yj == -1 or Yj > c or Board[Yi][Yj] == -1 or Yi > r // 2:
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

matriz = [
    [0, 9, 1, 10, 0],
    [-1, 1, 5, 25, 5],
    [1, -1, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]
#Z : 22
#X : 10
#Y : 30
#Total : 40

print(recursive_board_game(0,0,0,4,4,2,matriz,points, copy_al))

