# Ya quedo el juego :))))

import time 
import os 
# Colorama es para ponerle color 
# pip install colorama / este es el comando para instalarlo 
# si no lo quieres instalar ponlo como comentario
from colorama import init, Fore, Style 

filas = 5
columnas = 5 
BARCO = "B"
mar = " "
Disparo_fallido = (Fore.RED +"x"+ Style.RESET_ALL)
Disparo_dado = (Fore.GREEN +"✔"+ Style.RESET_ALL)
jugador_1 = "J1"
jugador_2 = "J2"
Disparos_cont = 15
Barcos_ini = 4

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
    print(Fore.RED +f"\nIngresa las coordenadas de \
tus {cantidad_barcos} barcos, turno de {jugador}"+ Style.RESET_ALL)
    barcos_colocados = 0 
    while barcos_colocados < cantidad_barcos:
        y = None
        x = None
        # Obtener fila (letra)
        fila_valida= False # Sustituye el break
        while not fila_valida:
            letra_fila = input("\
Ingresa la letra para la fila (A-E): ").upper()
            if len(letra_fila) == 1 and 'A' <= letra_fila <= 'E':
                y = ord(letra_fila) - 65  
                fila_valida=True
            else:
                print(Fore.RED +"\
Fila inválida. Debes ingresar una letra entre A y E."+ Style.RESET_ALL) 
        # Obtener columna (número)
        columna_valida=False  #sustituye el break
        while not columna_valida: 
            x = input("Ingresa el número para la columna (1-5): ")
            if x.isdigit(): #Sustituye el try 
                x=int(x)
                if 1 <= x <= 5:
                    x = x - 1  # Convertir número a índice de columna
                    columna_valida= True 
                else:
                    print(Fore.RED +"\
Columna inválida. Debes ingresar un número entre 1 y 5."+ Style.RESET_ALL)
            else:
                print(Fore.RED +"\
Entrada inválida. Ingresa un número."+ Style.RESET_ALL)
        # Verificar si la posición está libre
        if el_mar(x, y, matriz):
            matriz[y][x] = BARCO
            barcos_colocados += 1
            print(Fore.LIGHTWHITE_EX +f"\
Barco {barcos_colocados} colocado en ({letra_fila}{x+1})"+ Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX +"\
Ya hay un barco en esa posición. Elige otra."+ Style.RESET_ALL)
    return matriz

def imprimir_con_disparos(cont_disparos,jugador):
    print(Fore.YELLOW +f"\
Disparos restantes de {jugador}: {cont_disparos} "+ Style.RESET_ALL)

def imprimir_matriz(matriz, mostra_barcos, jugador):
    print(f"\nEste es el mar del jugador {jugador}: ")
    letra = "A"
    for y in range(filas):
        divididor_H()
        print(f"| {letra} ", end=" ")
        for x in range(columnas):
            celda = matriz [y][x]
            valor_real = celda
            if (not mostra_barcos and valor_real != mar and valor_real != 
                Disparo_fallido and valor_real != Disparo_dado):
                valor_real = " "
            print(f"| {valor_real} ", end=" ")
        letra = letras_tablero(letra)
        print("|",) #Esto es un salto de linea
    divididor_H()
    numeros_tablero()
    divididor_H()

def coordenadas_disparos(jugador):
    print(Fore.MAGENTA +f"Ingresa las coordenadas,\
 turno {jugador}"+ Style.RESET_ALL)
    #Este es un ciclo infinito hasta que se confirma 
    y = None
    x = None 
    fila_valida=False #sustituye el break
    while not fila_valida: 
        letra_fila= input("Ingresa la letra para la fila (A-E): ").upper()
        #letra_fila = letra_fila.upper()
        if len(letra_fila) != 1: 
            print(Fore.YELLOW +"\
Debes ingresar unicamente la letra"+ Style.RESET_ALL)
            continue
        # A = 65, B = 66
# Hay que convertir las letras a indices, para eso le restamos 65 y queda en 0 
        y = ord(letra_fila)-65
        if coordenadas_en_rango(0,y):
            fila_valida=True
        else: 
            print(Fore.RED +"Fila invalida"+ Style.RESET_ALL)
    # Esto es para la columna
    columna_valida=False # Sustituye el brake
    while not columna_valida: 
        x = input("Ingresa el numero de columna (1-5): ")
        if x.isdigit():  #Sustituye el try 
            x=int(x)
            if coordenadas_en_rango(x-1, 0): 
                x = x-1 
                columna_valida=True
            else:
                print(Fore.RED +"Columna invalida"+ Style.RESET_ALL)
        else:     
            print(Fore.RED +"Ingresa un número valido"+ Style.RESET_ALL)
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
    # regresa un bool
    for y in range (filas): 
        for x in range (columnas): 
            celda=matriz[y][x]
            if (celda != mar and celda != Disparo_dado and 
                celda != Disparo_fallido):
                # Si no es mar ni un disparo todavia hay un barco 
                return False
    # Se recorre toda la matriz para ver si hay barcos aun 
    return True

def winner(jugador): 
    print(Fore.GREEN +f"Fin del juego\
\nEl jugador {jugador} es el ganador"+ Style.RESET_ALL)

def loser(jugador):
    print(Fore.RED +f"Fin del juego\nEl jugador {jugador} pierde\
\nYa no tienes disparos"+ Style.RESET_ALL)

def imprimir_barcos_en_matriz(matriz_j1, matriz_j2): 
    print(Fore.YELLOW +"Mostrando ubicacion de los barcos"+ Style.RESET_ALL)
    imprimir_matriz(matriz_j1, True, jugador_1)
    imprimir_matriz(matriz_j2, True, jugador_2)

def Juego(): 
    clearall()
    print(Fore.CYAN + "¡Bienvenidos a Battleship!" + Style.RESET_ALL)
    print(" ")
    print(Fore.LIGHTMAGENTA_EX + "Iniciando juego..." + Style.RESET_ALL)
    time.sleep(2)   
    global Disparos_cont
    disparos_restantesJ1 = Disparos_cont
    disparos_restantesJ2 = Disparos_cont
    cantidad_barcos = 4
    matriz_j1, matriz_j2 = Tablero(), Tablero()
    # Colocar los barcos por el jugador
    matriz_j1 = ingresar_barcos(matriz_j1, cantidad_barcos, jugador_1)
    time.sleep(3)
    clearall()
    time.sleep(1)
    matriz_j2 = ingresar_barcos(matriz_j2, cantidad_barcos, jugador_2)
    turno_actual = jugador_1
    fin_juego=False # sustituye un breake
    while not fin_juego: 
        time.sleep(3)
        clearall()
        time.sleep(1)
        print(Fore.BLUE +f"TURNO DE: {turno_actual}"+ Style.RESET_ALL)
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
            print(Fore.GREEN + "Le has dado a un barco"+ Style.RESET_ALL)
            print( "Espera unos segundos")

            if Ganador(matriz_oponente): 
                winner(turno_actual)
                imprimir_barcos_en_matriz(matriz_j1, matriz_j2)
                fin_juego=True 
        else: 
            print(Fore.YELLOW + "Disparo fallado" + Style.RESET_ALL)
            print("Espera unos segundos")
            if Disparos_cont-1 <=0: 
                loser(turno_actual)
                imprimir_barcos_en_matriz(matriz_j1, matriz_j2)
                fin_juego=True
            turno_actual= VS_Jugador(turno_actual)

Juego()