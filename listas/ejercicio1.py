import random
# Lista vacía
componentes = []
#creamos un elemento por agregar a la lista
elemento = input("ingrese el componente del avion: ")
#agregamos el elemento a la lista con .append()
componentes.append(elemento)
print(componentes)

#lista de numeros
numeros = []
aleatorio = random.randint(0,100)

#agregamos el elemento del numero aleatorio a la lista
numeros.append(aleatorio)
#agregamos el numero 10 a la lista
numeros.append(10)
#agregamos 10 numeros aleatorios a la lista
for i in range(10):
    aleatorio = random.randint(0,100)
    numeros.append(aleatorio)

print(numeros)

# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Lista con diferentes tipos de datos
datos_vuelo = [202, "Boeing 737", True, 10500.5]

# Listas anidadas
matriz_rotacion = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
