import math as m

points = {"X":0,"Y":0,"Z":0}

already_been = set()

def recursive_board_game(Xi,Xj,Yi,Yj,Zi,Zj,Board , points , already_been ): 
    r = len(Board) -1
  
    c = len(Board[0]) -1
    
    #----------- Movimiento de Z
    if not(Zi <0):
        if Zj == -1 or Zj > c or Board[Zi][Zj] == -1 : 
            points["Z"] = 0
            Zi = - m.inf
        elif Zi == r//2:
            if (Zi,Zj) not in already_been :
                points["Z"] += Board[Zi][Zj]
            else: 
                already_been.add((Zi,Zj))
            Zi = - m.inf
        else:
            if (Zi,Zj) not in already_been:
                points["Z"] += Board[Zi][Zj]
                already_been.add((Zi,Zj))
            
    
    #-----------Movimiento de X
    if not(Xi <0):       
        if Xj == -1 or Xj > c or Board[Xi][Xj] == -1: 
            points["X"] = 0
            Xi = - m.inf
        elif Xi == r//2:
            if (Xi,Xj) not in already_been:
                points["X"] += Board[Xi][Xj]
                already_been.add((Xi,Xj))
            Xi = - m.inf
        else:
            if (Xi,Xj) not in already_been:
                points["X"] += Board[Xi][Xj]
                already_been.add((Xi,Xj))
        
    #----------- Movimiento de Y
    if (not Yi <0):
        if Yj == -1 or Yj > c or Board[Yi][Yj] == -1: 
            points["Y"] = 0
            Yi = - m.inf
        elif Yi == r//2:
            if (Yi,Yj) not in already_been:
                points["Y"] += Board[Yi][Yj]
                already_been.add((Yi,Yj))
            Yi = - m.inf
        else:
            if (Yi,Yj) not in already_been:
                
                points["Y"] += Board[Yi][Yj]
                already_been.add((Yi,Yj))      
    
    #----------- Recursión
    if Xi <0 or Yi <0 or Zi <0:
        return points
    else:
        maxim = {'max': max(
            sum(list(recursive_board_game(Xi+1, Xj-1, Yi+1, Yj-1, Zi-1, Zj-1, Board , points , already_been ).values())),  # X izq, Y izq, Z izq
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
        # print(f"X: {Xi},{Xj} Y: {Yi},{Yj} Z: {Zi},{Zj}")
        # print(f"Already been: {already_been}")
        # print("Points: ",points)
        # print("Maxim: ",maxim)
        # print("r: ",r, "c: ",c)
        # print("-------------------------------------------------")
        
        return maxim



matriz = [
    [0, 9, 1, 10, 0],
    [-1, 5, 5, 25, 5],
    [1, 5, 1, 5, 7],
    [5, 5, 5, 15, 2],
    [55, 3, 0, 4, 1]
]
#Z : 22
#X : 10
#Y : 30
#Total : 40

print(recursive_board_game(0,0,0,4,4,2,matriz,points, already_been))

