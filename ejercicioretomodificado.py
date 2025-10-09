import math
import random

# Función para solicitar al usuario los datos iniciales del vuelo
def pedir_datos():
    va = float(input("Ingrese la velocidad de ascenso de la aeronave: "))
    ao = float(input("Ingrese la altitud objetivo: "))
    aa = float(input("Ingrese el ángulo inicial de ascenso (en grados): "))
    avion = {
        "velocidad_ascenso": va,
        "altitud_objetivo": ao,
        "angulo_ataque": aa,
        "altitud_actual": 0,
        "tiempo_transcurrido": 1
    }
    return avion

# Función principal que simula el ascenso del avión con control manual del usuario
def simular_ascenso(avion):
    registro_altitud = []

    while avion["altitud_actual"] < avion["altitud_objetivo"]:
        print(f"\nTiempo: {avion['tiempo_transcurrido']} segundos")
        print(f"Altitud actual: {avion['altitud_actual']:.2f}")

        print("Opciones:\n 1 = Aumentar velocidad \n 2 = Mantener \n 3 = Disminuir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            avion["velocidad_ascenso"] += 10
        elif opcion == "3":
            avion["velocidad_ascenso"] = max(0, avion["velocidad_ascenso"] - 10)

        if avion["tiempo_transcurrido"] % 300 == 0:
            avion["angulo_ataque"] = float(input("Ingrese nuevo ángulo de ascenso (en grados): "))

        avion["altitud_actual"] = avion["velocidad_ascenso"] * math.sin(math.radians(avion["angulo_ataque"])) * avion["tiempo_transcurrido"]
        registro_altitud.append(avion["altitud_actual"])
        avion["tiempo_transcurrido"] += 1

    return registro_altitud

# Función para mostrar estadísticas finales del vuelo (altitud final, promedio, máximo, mínimo)
def mostrar_resultados(registro_altitud):
    print("\n¡El avión alcanzó la altitud objetivo!")
    print(f"Altitud final: {registro_altitud[-1]:.2f}")

    promedio_altitud = sum(registro_altitud) / len(registro_altitud)
    mayor_altitud = max(registro_altitud)
    menor_altitud = min(registro_altitud)

    print(f"\nPromedio de altitudes: {promedio_altitud:.2f} m")
    print(f"Mayor altitud: {mayor_altitud:.2f} m")
    print(f"Menor altitud: {menor_altitud:.2f} m")

# funcion para imprimir listas y diccionarios
def imprimir_datos(avion, registro):
    print("datos del avion")
    for clave, valor in avion.items():
        print(f"{clave}: {valor}", end="  ")
    print("\n")

    print("registro de altitudes")
    for altitud in registro:
        print(f"{altitud:.2f}", end="  ")
    print("\n")

# Función principal que maneja el menú del simulador y orquesta todas las demás funciones
def simulacion1():
    control = True

    while control:
        opcion = int(input("Seleccione una opción:\n1. Simulador\n2. listas y diccionarios\n3. salir\n1"))
        match opcion:
            case 1:
            #Aca llamos a las funciones pedir_datos, simular_ascenso y mostrar_resultados
                avion = pedir_datos()
                registro = simular_ascenso(avion)
                mostrar_resultados(registro)
            case 2:
              if avion and registro:
                   imprimir_datos(avion, registro)
              else:
                    print("Primero debe ejecutar el simulador (opción 1).")

            case 3:
                control = False
                print("Ya saliste del menú.")
            case _:
                print("Opción no válida.")

simulacion1()

