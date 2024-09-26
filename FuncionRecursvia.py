points = {"X":0,"Y":0,"Z":0}

def recursive_board_game(Xi,Xj,Yi,Yj,Zi,Zj,Board, points, allready_been ):   

    # Movimiento de X
    if Xi <0:
        points["X"] = 0
        return points
    elif Xj == -1 or Xj > len(Board[0]) -1 or Board[Xi][Xj] == -1: 
        points["X"] = 0
        Xi = -99999

    elif Xi == len(Board)//2:
        points["X"] += Board[Xi][Xj]
        allready_been.add((Xi,Xj))
        Xi = -99999
    else:
        points["X"] += Board[Xi][Xj]
        allready_been.add((Xi,Xj))
    # Movimiento de Y
    if Yi <0:
        points["Y"] = 0
        return points
    elif Yj == -1 or Yj > len(Board[0]) -1: 
        points["Y"] = 0
        Yi = -99999

    elif Board[Yi][Yj] == -1:
        points["Y"] = 0
        Yi = -99999
    elif Yi == len(Board)//2:
        if (Yi,Yj) not in allready_been:
            points["Y"] += Board[Yi][Yj]
        allready_been.add((Yi,Yj))
        Yi = -99999
    else:
        if (Yi,Yj) not in allready_been:
            points["Y"] += Board[Yi][Yj]
        allready_been.add((Yi,Yj))
    # Movimiento de Z
    if Zi <0:
        points["Z"] = 0
        return points
    elif Zj == -1 or Zj > len(Board[0]) -1: 
            points["Z"] = 0
            Zi = -99999
            
    elif Board[Zi][Zj] == -1:
        
        points["Z"] = 0
        Zi = -99999
    elif Zi == len(Board)//2:
        if (Zi,Zj) not in allready_been:
            points["Z"] += Board[Zi][Zj]
        allready_been.add((Zi,Zj))
        Zi = -99999
    else:
        if (Zi,Zj) not in allready_been:
            points["Z"] += Board[Zi][Zj]
        allready_been.add((Zi,Zj))
    # Recursión
    if Xi <0 and Yi <0 and Zi <0:
        return points
    
    else:
        maxim = {'max': max(
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj-1, Zi-1, Zj-1, Board, points, allready_been).values())),  # X izq, Y izq, Z izq
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj-1, Zi-1, Zj, Board, points, allready_been).values())),    # X izq, Y izq, Z recto
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj-1, Zi-1, Zj+1, Board, points, allready_been).values())),  # X izq, Y izq, Z der
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj, Zi-1, Zj-1, Board, points, allready_been).values())),    # X izq, Y recto, Z izq
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj, Zi-1, Zj, Board, points, allready_been).values())),      # X izq, Y recto, Z recto
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj, Zi-1, Zj+1, Board, points, allready_been).values())),    # X izq, Y recto, Z der
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj+1, Zi-1, Zj-1, Board, points, allready_been).values())),  # X izq, Y der, Z izq
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj+1, Zi-1, Zj, Board, points, allready_been).values())),    # X izq, Y der, Z recto
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj+1, Zi-1, Zj+1, Board, points, allready_been).values())),  # X izq, Y der, Z der
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj-1, Zi-1, Zj-1, Board, points, allready_been).values())),    # X recto, Y izq, Z izq
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj-1, Zi-1, Zj, Board, points, allready_been).values())),      # X recto, Y izq, Z recto
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj-1, Zi-1, Zj+1, Board, points, allready_been).values())),    # X recto, Y izq, Z der
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj, Zi-1, Zj-1, Board, points, allready_been).values())),      # X recto, Y recto, Z izq
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj, Zi-1, Zj, Board, points, allready_been).values())),        # X recto, Y recto, Z recto
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj, Zi-1, Zj+1, Board, points, allready_been).values())),      # X recto, Y recto, Z der
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj+1, Zi-1, Zj-1, Board, points, allready_been).values())),    # X recto, Y der, Z izq
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj+1, Zi-1, Zj, Board, points, allready_been).values())),      # X recto, Y der, Z recto
            sum(list(recursive_board_game(Xi+1, Xj, Yi+1, Yj+1, Zi-1, Zj+1, Board, points, allready_been).values())),    # X recto, Y der, Z der
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj-1, Zi-1, Zj-1, Board, points, allready_been).values())),  # X der, Y izq, Z izq
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj-1, Zi-1, Zj, Board, points, allready_been).values())),    # X der, Y izq, Z recto
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj-1, Zi-1, Zj+1, Board, points, allready_been).values())),  # X der, Y izq, Z der
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj, Zi-1, Zj-1, Board, points, allready_been).values())),    # X der, Y recto, Z izq
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj, Zi-1, Zj, Board, points, allready_been).values())),      # X der, Y recto, Z recto
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj, Zi-1, Zj+1, Board, points, allready_been).values())),    # X der, Y recto, Z der
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj+1, Zi-1, Zj-1, Board, points, allready_been).values())),  # X der, Y der, Z izq
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj+1, Zi-1, Zj, Board, points, allready_been).values())),    # X der, Y der, Z recto
            sum(list(recursive_board_game(Xi+1, Xj+1, Yi+1, Yj+1, Zi-1, Zj+1, Board, points, allready_been).values()))   # X der, Y der, Z der
                    )}
        return maxim
matriz = [
    [0, 9, 1, 10, 0],
    [-1, -1, 5, -1, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]

print(recursive_board_game(0,0,0,4,4,2,matriz,points, set()))

