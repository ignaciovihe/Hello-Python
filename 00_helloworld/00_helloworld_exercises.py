# 1. Imprime "¡Hola Mundo!" por consola.
print("¡Hola Mundo!")

# 2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.
# El ejercicio 1 imprime una cadena por pantalla

# 3. Imprime tu nombre y edad en la misma línea utilizando la función print.
print("Ignacio - 39 anos")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
print(type("cadena"))
print(type(1))
print(type(1.5))

# 5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
"""
Los tipos de datos son los diferentes tipos de valores que pueden tomar las variables en un lenguaje
de programacion: cadena, número entero, numero decimal, booleano, etc
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("Hola" + " " + "Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
name = "Ignacio"
age = 39
print( f"Mi nombre es {name} y mi tegno {age} años")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
name = input("¿Cuál es tu nombre? ")
print(f"Bienvenido {name}!")

# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.

result = 4 + 7       
print(f"El resultado de la suma es {result}")         
print(f"El tipo de dato del resultado es {type(result)}")   

# 10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
#Suma dos numeros enteros
result = 4 + 7 

#Imprime el resultado de la suma
print(f"El resultado de la suma es {result}")

#Imprime el tipo de dato del resultado
print(f"El tipo de dato del resultado es {type(result)}")

