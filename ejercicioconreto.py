#utilizar diccionarios y listas dentro del codigo de un ejercicio del reto anterior

import math
import random


def simulacion1():
    avion = {
    "velocidad_ascenso": 200 ,
    "altitud_objetivo": 10000,
    "angulo_ataque": 15,
    "altitud_actual": 0, 
    "tiempo_transcurrido": 0
    }

    historial_de_altitudes = [ ]

    while avion["altitud_actual"] < avion ["altitud_objetivo"]:
        print(f"\nTiempo: {avion["tiempo_transcurrido"]} segundos")
        print(f"Altitud actual: {avion["altitud_actual"]:.2f}")

        print("Opciones:\n 1 = Aumentar velocidad \n 2 = Mantener \n 3 = Disminuir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            avion ["velocidad_ascenso"] += 10
        elif opcion == "3":
            avion ["velocidad_ascenso"] -= 10
            if  avion ["velocidad_ascenso"] < 0:  
                 avion ["velocidad_ascenso"] = 0

        if avion["tiempo_transcurrido"] % 300 == 0 and avion["tiempo_transcurrido"] != 0:
            avion["angulo_ataque"] = float(input("Ingrese nuevo ángulo de ascenso (en grados): "))

        avion["altitud_actual"] = avion["velocidad_ascenso"] * math.sin(math.radians(avion["angulo_ataque"])) * avion["tiempo_transcurrido"]
        avion["tiempo_transcurrido"] += 1

    print("\n¡El avión alcanzó la altitud objetivo!")
    print(f"Altitud final: {avion["altitud_actual"]:.2f}")
    print(historial_de_altitudes)

simulacion1()