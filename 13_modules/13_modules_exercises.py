# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.

import calculator

print(calculator.add(3, 4))
print(calculator.divide(3, 0))
print(calculator.substract(3, 4))
print(calculator.multiply(3, 4))

# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.

from converter import celsius_to_farenheit, farenheit_to_celsius

celsius = 10
farenheit = 32

print(f"{celsius} grados Celsius son {celsius_to_farenheit(celsius)} grados Farenheit")
print(f"{farenheit} grados Farenheit son {farenheit_to_celsius(farenheit)} grados Celsius")

# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.

from students import print_students

print_students()

# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
import geometry

radius = 2.5
side_a = 4
side_b = 4

print(f"El área de un circulo con radio {radius} es : {geometry.circle_area(radius)}")
print(f"El area de cun cuadrado de lados {side_a} y {side_b} es: {geometry.square_area(side_a, side_b)}")

# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.

from sum_module import sum_all

print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".
from car_module import Car

new_car = Car("BMW", "320D", "2009")
new_car.display_info()

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

import file_module

file_module.append_file("mifichero.txt", "Esta es la primera linea que escribo en el fichero\n")
file_module.append_file("mifichero.txt", "y esta es la segunda\n")
print(file_module.read_file("mifichero.txt"))

# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.

from statistics import mean, median

list_of_numbers = [45,9,7,90,64,8]

print(mean(list_of_numbers))
print(median(list_of_numbers))

# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.

from word_count import count_word

print(count_word(" ", "Hola me llamo Nacho pero mis amigos me llaman Nacho"))

# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.

from dates import get_date, difference_of_dates

today = get_date()
print(today)

print(difference_of_dates((today.year, today.month, today.day),(1985, 2, 23)))