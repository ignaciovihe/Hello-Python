# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.

def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9 / 5) + 32
    return farenheit

def farenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * 5 / 9
    return celsius