# Ejercicio seleccionado 
Ascenso hasta altitud objetivo

simula como un avion asciende hacia una altitud establecida
- el usuario decide si aumenta, mantiene o disminuye la velocidad de ascenso cada segundo.
- el usuario cada 5 minutos ingresa el angulo de ascenso.
- ecuacion: altitud = velocidad_ascenso . seno(angulo_ataque) . tiempo_transcurrido

# En que se van a usar diccionarios?
# En que se van a usar listas?

Buneo primero debemos saber que son diccionarios y que son listas y para que se utilizan

- ## Listas
**Las listas son colecciones ordenadas y mutables de elementos. Pueden contener objetos de diferentes tipos y admiten la duplicación de elementos**

**La lista la vamos a utilizar para almacenar la altitud en cada movimiento que realice el piloto, el append que se va a utilizar en el codigo funciona para registrar cada cambio y hacer un guardado de eso para la impresion final muestre el historial de la simulacion.**

## Metodos principales de listas utillizados: 
|Metodo|Descripcion|
|------|-----------|
|append|Añadir un elemento al final|
|insert()|insertar un nuevo elemento|
|extend|a;ade elementos de otra iterable|

- ## Diccionarios:
Los diccionarios son colecciones no ordenadas y mutables de pares clave-valor. Las claves deben ser únicas e inmutables (como strings, números o tuplas), mientras que los valores pueden ser de cualquier tipo.

**En este trabajo se va a trabajar con diccionarios para añadir mediante claves en nuestro cogido original las variables como velocidad de ascenso, altitud objetivo, angulo de ataque, etc.**
**Cada variable va a llevar un nombre en el cual en el diccionario va a ser un tipo de clave para identificarlo**

- Si queremos saber el valor de esa clave en especifico lo que debemos hacer es lo siguiente: Debemos primero la funcion print. despues llamar el diccionario que seria avion y despues la clave que deseamos saber, ejemplo: print(avion["va"])

## Modificación de valores
- **avion["va"] = 260**

## Añadir nuevo par clave-valor
- **avion["ao"] = 10000** 


## Calculos estadisticos
- **Por ultimo en los calculos estadisticos nos hemos ayudado investigando, aprendimos que para calcular los registros de las altitudes, primero antes en el codigo creamos una lista vacia [ ], la cual nos sirve para añadir otros elementos de despues del codigo a medida que vamos trabajando como  en el caso de las estadisiticas, en este caso el promedio actual seria la suma del registro de altitudes sobre el codigo de (len) que sirve para contar cuantos elementos tenemos guardados en esa lista calculando asi el promedio.**