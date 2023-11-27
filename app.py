#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
values = ['piedra', 'papel', 'tijera']
import random

# Pedir al usuario que ingrese un valor por consola en un blucle infinito hasta que ingrese la palabra "salir"
# y mostrar el valor ingresado por consola en cada iteración

while True:
    # Generar valor aleatorio entre 0 y 2 y asignarlo a la variable number
    number = random.randint(0, 2)

    maquina = values[number]
    
    valor = input("Escribe tu tiro o salir para terminar: ")
    # Si el valor es piedra
    if valor == "salir":
        break
    elif valor == "piedra":
        if maquina == "piedra":
            print(valor, "vs", maquina, "empate")
        elif maquina == "papel":
            print(valor, "vs", maquina, "perdiste")
        else:
            print(valor, "vs", maquina, "ganaste")
    elif valor == "papel":
        if maquina == "piedra":
            print(valor, "vs", maquina, "ganaste")
        elif maquina == "papel":
            print(valor, "vs", maquina, "empate")
        else:
            print(valor, "vs", maquina, "perdiste")
    elif valor == "tijera":
        if maquina == "piedra":
            print(valor, "vs", maquina, "perdiste")
        elif maquina == "papel":
            print(valor, "vs", maquina, "ganaste")
        else:
            print(valor, "vs", maquina, "empate")
    else:
        print('Valor no valido')




