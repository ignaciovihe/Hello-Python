# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
from math import pi

def circle_area(radius):
    return pi * (radius ** 2)

def square_area(side_a, side_b):
    return side_a * side_b