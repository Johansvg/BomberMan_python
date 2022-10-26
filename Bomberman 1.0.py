import random


def crear_matricula(i, j, matriz):
    for fila in range(i):
        matriz.append(['.'] * j)


def poner_bombas(i, j, matriz):
    for filas in range(i):
        for columnas in range (j):
            if random.randint(0, 2) == 0:
                matriz[filas][columnas] = "O"


def imprimir_cuadricula(i, j, matriz):
    for fila in range(i):
        for columna in range(j):
            print(matriz[fila][columna], end=" ")
        print("")


def poner_bombas(i, j, matriz):
    for filas in range(i):
        for columnas in range (j):
            if random.randint(0, 2) == 0:
                matriz[filas][columnas] = "O"


def es_esquina(i, j, fila, columna, matriz):
    if fila == 0 and columna == j-1:
        matriz[fila][columna] = 'o'
        if matriz[fila][columna - 1] != 'O':
            matriz[fila][columna - 1] = 'o'
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


def transformar_matriz(i, j, matriz):
    for fila in range(i):
        for columna in range(j):
            if matriz[fila][columna] == '.':
                matriz[fila][columna] = 'O'
    for fila in range(i):
        for columna in range(j):
            if matriz[fila][columna] == 'o':
                matriz[fila][columna] = '.'


def explotar_bombas(i, j, matriz):
    for fila in range(i):
        for columna in range(j):
            if matriz[fila][columna] == 'O':
                if not(es_esquina(i, j, fila, columna, matriz)):
                    if not(es_lado(i, j, fila, columna, matriz)):
                        matriz[fila][columna] = 'o'
                        if matriz[fila + 1][columna] != 'O':
                            matriz[fila + 1][columna] = 'o'
                        if matriz[fila - 1][columna] != 'O':
                            matriz[fila - 1][columna] = 'o'
                        if matriz[fila][columna + 1] != 'O':
                            matriz[fila][columna + 1] = 'o'
                        if matriz[fila][columna - 1] != 'O':
                            matriz[fila][columna - 1] = 'o'
    transformar_matriz(i, j, matriz)


def iniciar_juego(i, j, matriz, n, segundos, contadora):
    if n>0:
        if segundos == 3:
            segundos = 0
            contadora+=1
            explotar_bombas(i, j, matriz)
            '''print("Explosion numero: {0}".format(contadora))'''
            '''imprimir_cuadricula(i, j, matriz)'''
        return iniciar_juego(i, j, matriz, n-1, segundos+1, contadora)


n = int(input("Ingrese numero de segundos: "))
c = int(input("Ingrese numero de columnas: "))
r = int(input("Ingrese numero de filas: "))
contadora = 0
cuadricula = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.'], ['.', '.', '.', '.', 'O', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['O', 'O', '.', '.', '.', '.', '.'], ['O', 'O', '.', '.', '.', '.', '.']]
'''
crear_matricula(r, c, cuadricula)
poner_bombas(r, c, cuadricula)
'''
print("ANTES DE EXPLOTAR")
imprimir_cuadricula(r, c, cuadricula)
iniciar_juego(r, c, cuadricula, n, 1, contadora)
print("El juego ha terminado")
print("-------TABLERO FINAL-------")
imprimir_cuadricula(r, c, cuadricula)