#utilizar diccionarios y listas dentro del codigo de un ejercicio del reto anterior

import math
import random


def simulacion1():
    va = float(input("Ingrese la velocidad de ascenso de la aeronave: "))
    ao = float(input("Ingrese la altitud objetivo: "))
    aa = float(input("Ingrese el ángulo inicial de ascenso (en grados): "))
    avion = {
    "velocidad_ascenso": va ,
    "altitud_objetivo":ao ,
    "angulo_ataque":aa ,
    "altitud_actual": 0, 
    "tiempo_transcurrido": 0
    }

    registro_altitud = [ ]

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
            registro_altitud.append(avion["altitud_actual"])
            
            avion["tiempo_transcurrido"] += 1


    print("\n¡El avión alcanzó la altitud objetivo!")
    print(f"Altitud final: {avion["altitud_actual"]}")
    print(f" Registro de altitudes: {registro_altitud}")

    promedio_altitud = sum(registro_altitud) / len(registro_altitud)
    mayor_altitud = max(registro_altitud)
    menor_altitud = min(registro_altitud)

    print(f"\nPromedio de altitudes registradas: {promedio_altitud:.2f} m")
    print(f"Mayor altitud alcanzada: {mayor_altitud:.2f} m")
    print(f"Menor altitud registrada: {menor_altitud:.2f} m")

simulacion1()