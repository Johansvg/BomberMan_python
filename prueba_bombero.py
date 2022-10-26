import random

def crear_matricula(i, j, matriz):
    for fila in range(i):
        matriz.append(['.'] * j)


def imprimir_cuadricula(i, j, matriz):
    for fila in range(i):
        for columna in range(j):
            print(matriz[fila][columna], end=" ")
        print("")


def es_esquina(i, j, fila, columna, matriz):
    if fila == 0 and columna == j-1:
        matriz[fila][columna] = 'o'
        print("QUE PUTAS HAY")
        print(matriz[fila][columna - 2])
        imprimir_cuadricula(i, j, matriz)
        if matriz[fila][columna - 2] != 'O':
            matriz[fila][columna - 2] = 'o'
        if matriz[fila + 1][columna] != 'O':
            matriz[fila + 1][columna] = 'o'
        return True
    elif fila == 0 and columna == 0:
        matriz[fila][columna] = 'o'
        if matriz[fila + 1][columna] != 'O':
            matriz[fila + 1][columna] = 'o'
        if matriz[fila][columna + 1] != 'O':
            matriz[fila][columna + 1] = 'o'
        return True
    elif fila == i-1 and columna == 0:
        matriz[fila][columna] = 'o'
        if matriz[fila][columna + 1] != 'O':
            matriz[fila][columna + 1] = 'o'
        if matriz[fila - 1][columna] != 'O':
            matriz[fila - 1][columna] = 'o'
        return True
    elif fila == i-1 and columna == j-1:
        matriz[fila][columna] = 'o'
        if matriz[fila - 1][columna] != 'O':
            matriz[fila - 1][columna] = 'o'
        if matriz[fila][columna - 1] != 'O':
            matriz[fila][columna - 1] = 'o'
        return True
    else:
        return False


def es_lado(i, j, fila, columna, matriz):
    if fila == 0 and columna != 0 and columna != j-1:
        matriz[fila][columna] = 'o'
        if matriz[fila][columna + 1] != 'O':
            matriz[fila][columna + 1] = 'o'
        if matriz[fila][columna - 1] != 'O':
            matriz[fila][columna - 1] = 'o'
        if matriz[fila + 1][columna] != 'O':
            matriz[fila + 1][columna] = 'o'
        return True
    elif fila == i-1 and columna != 0 and columna != j-1:
        matriz[fila][columna] = 'o'
        if matriz[fila][columna + 1] != 'O':
            matriz[fila][columna + 1] = 'o'
        if matriz[fila][columna - 1] != 'O':
            matriz[fila][columna - 1] = 'o'
        if matriz[fila - 1][columna] != 'O':
            matriz[fila - 1][columna] = 'o'
        return True
    elif columna == 0 and fila != 0 and fila != i-1:
        matriz[fila][columna] = 'o'
        if matriz[fila][columna + 1] != 'O':
            matriz[fila][columna + 1] = 'o'
        if matriz[fila - 1][columna] != 'O':
            matriz[fila - 1][columna] = 'o'
        if matriz[fila + 1][columna] != 'O':
            matriz[fila + 1][columna] = 'o'
        return True
    elif columna == j-1 and fila != 0 and fila != i-1:
        matriz[fila][columna] = 'o'
        if matriz[fila][columna - 1] != 'O':
            matriz[fila][columna - 1] = 'o'
        if matriz[fila - 1][columna] != 'O':
            matriz[fila - 1][columna] = 'o'
        if matriz[fila + 1][columna] != 'O':
            matriz[fila + 1][columna] = 'o'
        return True
    else:
        return False


def poner_bombas(i, j, matriz):
    for filas in range(i):
        for columnas in range (j):
            if random.randint(0, 2) == 0:
                matriz[filas][columnas] = "O"


def llenar_bombas_faltantes(i, j, matriz):
    for filas in range(i):
        for columnas in range (j):
            if matriz[filas][columnas] == ".":
                matriz[filas][columnas] = "O"


def explotar_bombas(i, j, matriz):
    for fila in range(i):
        for columna in range(j):
            if matriz[fila][columna] == 'O':
                if not(es_esquina(i, j, fila, columna, matriz)):
                    if not(es_lado(i, j, fila, columna, matriz)):
                        matriz[fila][columna] = 'o'
                        matriz[fila][columna - 1] = 'o'
                        matriz[fila - 1][columna] = 'o'
                        matriz[fila + 1][columna] = 'o'
                        matriz[fila][columna + 1] = 'o'
            else:
                if matriz[fila][columna] != 'o':
                    matriz[fila][columna]='O'
    for fila in range(i):
        for columna in range(j):
            if matriz[fila][columna] == 'o':
                matriz[fila][columna] = '.'



def iniciar_juego(i, j, matriz, n, segundos):
    if n>0:
        if segundos == 3:
            segundos = 0
            explotar_bombas(i, j, matriz)
            print("Tablero despues de explotar")
            imprimir_cuadricula(i, j, matriz)
        return iniciar_juego(i, j, matriz, n-1, segundos+1)


'''n = int(input("ingrese numero de segundos: "))'''
n = 3
c = int(input("Ingrese numero de columnas: "))
r = int(input("Ingrese numero de filas: "))
cuadricula = [['O', '.', '.', '.', '.', 'O'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', 'O']]


print("Antes de explotar")

imprimir_cuadricula(r, c, cuadricula)

explotar_bombas(r, c, cuadricula)

print("Despues de explotar")

imprimir_cuadricula(r, c, cuadricula)



'''iniciar_juego(r, c, cuadricula, n, 1)'''

'''explotar_bombas(r, c, cuadricula)'''

'''print("Tablero despues de explotar")'''

'''imprimir_cuadricula(r, c, cuadricula)'''

'''poner_bombas(r, c, cuadricula)'''

'''print("Despues de poner bombas aleatorias: ")'''

'''imprimir_cuadricula(r, c, cuadricula)'''

'''
llenar_bombas_faltantes(r, c, cuadricula)

print("Despues de llenar con bombas")

imprimir_cuadricula(r, c, cuadricula)

'''






