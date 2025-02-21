# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.

def add(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    if number2 == 0:
        print("No se puede dividir entre 0")
    else:
        return number1 / number2

def multiply(number1, number2):
    return number1 * number2