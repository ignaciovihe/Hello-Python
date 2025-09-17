### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    labels = [
        "fizzbuzz" if n % 15 == 0
        else "fizz" if n % 3 == 0
        else "buzz" if n % 5 == 0
        else str(n)
        for n in range(1,101)
    ]
    
    for l in labels:
        print(l)

fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagramm(word1, word2):
    if word1 == word2 or len(word1) != len(word2):
        return False
    else:
        for char in word1:
            if word1.count(char) != word2.count(char):
                return False
            
        return True
    
print(is_anagramm("conservar", "conversan"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():

    sequence = [0, 1]
    for _ in range(48):
        sequence.append(sequence[-1]+ sequence[-2])

    for number in sequence:
        print(f"{number},",end="")

fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
import math
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True
        
for i in range(1,101):
    if is_prime(i):
        print(f"{i}, ",end="")


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
my_string = "Hello World"
reversed_string = ""

for i in range(1, len(my_string) + 1):
    reversed_string +=  my_string[-i]

print(my_string)
print(reversed_string)


