# Codigo para experimentar

import random
import time 
import os 
# Colorama es para ponerle color 
# pip install colorama / este es el comando para instalarlo 
# si no lo quieres instalar ponlo como comentario
from colorama import init, Fore, Style 

filas = 1
columnas = 1
BARCO = "B"
mar = " "
Disparo_fallido = "X"
Disparo_dado = "O"
jugador_1 = "J1"
jugador_2 = "J2"
Disparos_cont = 3
Barcos_ini = 1

init()

def clearall(): 
        os.system('cls' if os.name == "nt" else 'clear')

def Tablero():
    matriz = []
    for y in range (filas):
        matriz.append([])
        for x in range (columnas):
            matriz[y].append(mar)
    #print(matriz)
    return matriz 

def divididor_H():
    for _ in range (columnas + 1):
        print(Fore.CYAN +"*---",end=" "+ Style.RESET_ALL)
    print(Fore.CYAN +"*"+ Style.RESET_ALL)

def letras_tablero(letra):
    return chr(ord(letra)+1)

def numeros_tablero():   
    print("|    ", end="")
    for x in range(columnas):
        print(f"| {x+1} ", end=" ")
    print("|")

def el_mar(x, y, matriz):
    return matriz[y][x]== mar

def coordenadas_en_rango(x,y): 
    return x >= 0 and x <= columnas-1 and y >= 0 and y <= filas-1

def ingresar_barcos(matriz, cantidad_barcos, jugador):
    print(Fore.RED +f"Ingresa las coordenadas de tus {cantidad_barcos} barcos, turno de {jugador}"+ Style.RESET_ALL)
    barcos_colocados = 0 
    while barcos_colocados < cantidad_barcos:
        y = None
        x = None
        # Obtener fila (letra)
        fila_valida= False 
        while not fila_valida:
            letra_fila = input("Ingresa la letra para la fila (A-E): ").upper()
            if len(letra_fila) == 1 and 'A' <= letra_fila <= 'E':
                y = ord(letra_fila) - 65  
                fila_valida=True
            else:
                print("Fila inválida. Debes ingresar una letra entre A y E.") 
        # Obtener columna (número)
        columna_valida=False
        while not columna_valida:
            x = input("Ingresa el número para la columna (1-5): ")
            if x.isdigit():
                x=int(x)
                if 1 <= x <= 5:
                    x = x - 1  # Convertir número a índice de columna
                    columna_valida= True 
                else:
                    print("Columna inválida. Debes ingresar un número entre 1 y 5.")
            else:
                print("Entrada inválida. Ingresa un número.")
        # Verificar si la posición está libre
        if el_mar(x, y, matriz):
            matriz[y][x] = BARCO
            barcos_colocados += 1
            print(f"Barco {barcos_colocados} colocado en ({letra_fila}{x+1})")
        else:
            print("Ya hay un barco en esa posición. Elige otra.")
    return matriz

#     columna_valida = False
#   while not columna_valida: 
#     x = input("Ingresa el número para la columna (1-5): ")
#     if x.isdigit():  # Verifica si la entrada es un número
#         x = int(x)  # Convierte la cadena en número
#         if coordenadas_en_rango(x - 1, 0): 
#             x = x - 1  # Ajustar la columna al índice de la matriz
#             columna_valida = True  # Se encontró una columna válida
#         else:
#             print("Columna inválida")
#     else:
#         print("Debes ingresar un número válido")
# return x, y

def imprimir_con_disparos(cont_disparos,jugador):
    print(Fore.YELLOW +f"Disparos restantes de {jugador}: {cont_disparos} "+ Style.RESET_ALL)

def imprimir_matriz(matriz, mostra_barcos, jugador):
    print(f"Este es el mar del jugador {jugador}: ")
    letra = "A"
    for y in range(filas):
        divididor_H()
        print(f"| {letra} ", end=" ")
        for x in range(columnas):
            celda = matriz [y][x]
            valor_real = celda
            if (not mostra_barcos and valor_real != mar  and valor_real != Disparo_fallido and valor_real != Disparo_dado):
                valor_real = " "
            print(f"| {valor_real} ", end=" ")
        letra = letras_tablero(letra)
        print("|",) #Esto es un salto de linea
    divididor_H()
    numeros_tablero()
    divididor_H()

# Sin breaks
# def coordenadas_disparos(jugador):
#     print(f"Ingresa las coordenadas, turno {jugador}")   
#     # Variables para almacenar coordenadas
#     y = None
#     x = None    
#     # Bandera de control para la fila
#     fila_valida = False
#     while not fila_valida: 
#         letra_fila = input("Ingresa la letra para la fila (A-E): ").upper()
#         if len(letra_fila) != 1: 
#             print("Debes ingresar unicamente una letra")
#             continue
#         # Convertir letra a índice de fila (A = 65)
#         y = ord(letra_fila) - 65
#         if coordenadas_en_rango(0, y):
#             fila_valida = True  # Se encontró una fila válida
#         else: 
#             print("Fila inválida")    
#     # Bandera de control para la columna
#     columna_valida = False
#   while not columna_valida: 
#     x = input("Ingresa el número para la columna (1-5): ")
#     if x.isdigit():  # Verifica si la entrada es un número
#         x = int(x)  # Convierte la cadena en número
#         if coordenadas_en_rango(x - 1, 0): 
#             x = x - 1  # Ajustar la columna al índice de la matriz
#             columna_valida = True  # Se encontró una columna válida
#         else:
#             print("Columna inválida")
#     else:
#         print("Debes ingresar un número válido")
# return x, y

def coordenadas_disparos(jugador):
    print(f"Ingresa las coordenadas, turno {jugador}")
    #Este es un ciclo infinito hasta que se confirma 
    y = None
    x = None 
    fila_valida=False
    while not fila_valida: 
        letra_fila= input("Ingresa la letra para la fila (A-E): ").upper()
        #letra_fila = letra_fila.upper()
        if len(letra_fila) != 1: 
            print("Debes ingresar unicamente la letra")
            continue
        # A = 65, B = 66
        # Hay que convertir las letras a indices, para eso le restamos 65 y queda en 0 
        y = ord(letra_fila)-65
        if coordenadas_en_rango(0,y):
            fila_valida=True
        else: 
            print("Fila invalida")
    # Esto es para la columna
    columna_valida=False
    while not columna_valida: 
        x = input("Ingresa el numero de columna (1-5): ")
        if x.isdigit():
            x=int(x)
            if coordenadas_en_rango(x-1, 0): 
                x = x-1 
                columna_valida=True
            else:
                print("Columna invalida")
        else:     
            print("Ingresa un número valido")
    return x, y

def disparos(x, y, matriz):
    # Regresa un bool 
    if el_mar(x, y, matriz): 
        matriz [y][x]= Disparo_fallido
        return False
    elif matriz[y][x] == Disparo_fallido or matriz[y][x] == Disparo_dado: 
        return False
    else: 
        matriz[y][x] = Disparo_dado
        return True

def VS_Jugador(jugador): 
    if jugador == jugador_1: 
        return jugador_2
    else: 
        return jugador_1

def Ganador(matriz): 
    for y in range (filas): 
        for x in range (columnas): 
            celda=matriz[y][x]
            if celda != mar and celda != Disparo_dado and celda != Disparo_fallido:
                # Si no es mar ni un disparo todavia hay un barco 
                return False
    # Se recorre toda la matriz para ver si hay barcos aun 
    return True

def winner(jugador): 
    print(Fore.RED +f"Fin del juego\nEl jugador {jugador} es el ganador"+ Style.RESET_ALL)

def loser(jugador):
    print(Fore.RED +f"Fin del juego\nEl jugador{jugador} pierde\nYa no tienes disparos"+ Style.RESET_ALL)

def imprimir_barcos_en_matriz(matriz_j1, matriz_j2): 
    print("Mostrando ubicacion de los barcos")
    imprimir_matriz(matriz_j1, True, jugador_1)
    imprimir_matriz(matriz_j2, True, jugador_2)

def Juego(): 
    global Disparos_cont
    disparos_restantesJ1 = Disparos_cont
    disparos_restantesJ2 = Disparos_cont
    cantidad_barcos = 1
    matriz_j1, matriz_j2 = Tablero(), Tablero()
    # Colocar los barcos por el jugador
    matriz_j1 = ingresar_barcos(matriz_j1, cantidad_barcos, jugador_1)
    #time.sleep(1)
    clearall()
    #time.sleep(1)
    matriz_j2 = ingresar_barcos(matriz_j2, cantidad_barcos, jugador_2)
    turno_actual = jugador_1
    fin_juego=False 
    print("------------------")
    while not fin_juego: 
        #time.sleep(1)
        clearall()
        #time.sleep(1)
        print(Fore.RED +f"TURNO DE: {turno_actual}"+ Style.RESET_ALL)
        Disparos_cont=disparos_restantesJ2
        if turno_actual == jugador_1:
            Disparos_cont= disparos_restantesJ1
        imprimir_con_disparos(Disparos_cont, turno_actual)
        matriz_oponente=matriz_j1
        if turno_actual== jugador_1: 
            matriz_oponente= matriz_j2
        imprimir_matriz(matriz_oponente, False, VS_Jugador(turno_actual))
        x,y = coordenadas_disparos(turno_actual)
        acertado= disparos(x,y,matriz_oponente)
        if turno_actual == jugador_1: 
            disparos_restantesJ1 -= 1
        else: 
            disparos_restantesJ2 -= 1
        imprimir_matriz(matriz_oponente, False, VS_Jugador(turno_actual))
        if acertado: 
            print(Fore.YELLOW + "Le has dado a un barco"+ Style.RESET_ALL)
            if Ganador(matriz_oponente): 
                winner(turno_actual)
                imprimir_barcos_en_matriz(matriz_j1, matriz_j2)
                fin_juego=True
        else: 
            print(Fore.YELLOW + "Disparo fallado" + Style.RESET_ALL)
            if Disparos_cont-1 <=0: 
                loser(turno_actual)
                imprimir_barcos_en_matriz(matriz_j1, matriz_j2)
                fin_juego=True
            turno_actual= VS_Jugador(turno_actual)

Juego()