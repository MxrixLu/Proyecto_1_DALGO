import math as m

r = 5
c= 5
def reliquias_sal(matriz, i, j):
    if i== r//2 : 
        return matriz[i][j]
    if matriz[i][j] == -1:
        return -m.inf
    if i != r//2 : 
        valor = max(reliquias_sal(matriz, i-1, j), reliquias_sal(matriz, i-1, j-1), reliquias_sal(matriz, i-1, j+1)) + matriz[i][j]
        return valor

    contador = 0

def reliquias_ind_mar(matriz, i, j, k):
    
    if j == -1 or k == -1 or j == c or k == 5:
        return -m.inf
    
    if i == r//2  and j!= k and k < c and j < c: 
        return matriz[i][j] + matriz[i][k]
    
    if matriz[i][j] == -1 or matriz[i][k] == -1:
        return -m.inf
    
    
    indiana =  i
    marion =  0
    
    if indiana >  marion and j != k:
        print("marion", marion)
        print("indiana", indiana)
        marion += 1
        return max(reliquias_ind_mar(matriz, i+1, j, k), reliquias_ind_mar(matriz, i+1, j, k-1), reliquias_ind_mar(matriz, i+1, j, k+1)) + matriz[i][k]
    
    if marion >= indiana and j != k: 
        print("marion", marion)
        print("indiana", indiana)
        indiana += 1
        return max(reliquias_ind_mar(matriz, i+1, j, k), reliquias_ind_mar(matriz, i+1, j-1, k), reliquias_ind_mar(matriz, i+1, j+1, k)) + matriz[i][j] 
        
    if j == k and matriz[j-1] and matriz[j-2] == -1 and matriz[k+1] and matriz[k+2] == -1:
        print("j = k 1")
        return matriz[i][j] 
    
    if j == k and matriz[j-1]and matriz[j-2] == -1:
        print("j = k 2") 
        return max(reliquias_ind_mar(matriz,i, j, k + 1), reliquias_ind_mar(matriz,i, j, k + 2)) + matriz[i][j]
    
    if j == k and matriz[k+1]and matriz[k+2] == -1:
        print("j = k 3")
        return  max(reliquias_ind_mar(matriz,i, j -2, k), reliquias_ind_mar(matriz,i, j-1, k )) + matriz[i][k]
    
    if j == k: 
        print("j = k 4")
        return max(reliquias_ind_mar(matriz, i, j-2, k), reliquias_ind_mar(matriz, i, j- 1, k), 
                   reliquias_ind_mar(matriz, i, j, k+1), reliquias_ind_mar(matriz,i, j, k + 2)) +  matriz[i][k]

def reliquias(matriz, R, C):
    reliquias_sal_resultado = reliquias_sal(matriz, r-1, (c//2))
    reliquias_ind_mar_resultado = reliquias_ind_mar(matriz, 0, 0, c-1)
    
    if  reliquias_sal_resultado == -m.inf and reliquias_ind_mar_resultado == -m.inf:
        return -1
    elif reliquias_sal_resultado == -m.inf:
        return reliquias_ind_mar_resultado
    elif reliquias_ind_mar_resultado == -m.inf:
        return reliquias_sal_resultado
    else:
        return reliquias_sal_resultado + reliquias_ind_mar_resultado

# Función para leer los casos de prueba desde un archivo
def leer_casos_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        num_casos = int(archivo.readline().strip())
        casos = []
        
        for _ in range(num_casos):
            R, C = map(int, archivo.readline().strip().split())
            r = R
            c = C
            matriz = [list(map(int, archivo.readline().strip().split())) for _ in range(R)]
            casos.append({'R': R, 'C': C, 'matriz': matriz})
        
        return casos

# Función para procesar cada caso
def procesar_caso(caso):
    R, C, matriz = caso['R'], caso['C'], caso['matriz']
    r = R
    c = C
    return reliquias(matriz, R, C)

# Función principal que puede leer desde archivo o consola
def main():
    archivo = int(input("Quieres leer un archivo (1) o ingresarlo por consola (2)? "))
    
    if archivo == 2:
        num_casos = int(input("Número de casos de prueba: ").strip())
        for _ in range(num_casos):
            R, C = map(int, input().strip().split())
            r = R
            c = C
            matriz = [list(map(int, input().strip().split())) for _ in range(R)]
            print(f"Procesando caso con matriz de tamaño {R}x{C}:")
            resultado = reliquias(matriz, R, C)
            print(f"Máximo de reliquias: {resultado}")
    else:
        nombre_archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
        casos = leer_casos_desde_archivo(nombre_archivo_entrada)
        
        # Procesar cada caso
        resultados = [procesar_caso(caso) for caso in casos]
        contador =1
        for resultado in resultados:
            print(f"Máximo de reliquias : {resultado}" )
            contador+=1

if __name__ == "__main__":
    main()
