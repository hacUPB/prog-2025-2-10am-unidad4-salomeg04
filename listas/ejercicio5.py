#generar una lista con 100 numeros aleatorios entre 100 y 1000, calcular el promedio de los valores de la lista, calcular el mayor y menos de los numeros

import random 

numeros = []

for i in range(100):
    aleatorio = random.randint(100,1000)
numeros.append(aleatorio)

suma = 0 
for i in numeros: 
    suma += i 


#tambien se puede hacer asi:

import random 

numeros = []

suma = 0 
for i in numeros: 
    suma += i 

for i in range(len(numeros)):
     suma += numeros [i]

# tambien: 

prom = suma / len(numeros) 
print("promedio = {prom}")

mayor = max(numeros)
menor = min(numeros)