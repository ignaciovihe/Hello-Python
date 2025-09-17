# 1. Genera una lista utilizando comprensión con los números del 0 al 10.
new_list = [i for i in range (11)]
print(new_list)
print()

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.
square_list = [i**2 for i in range(1,11)]
print(square_list)
print()

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.

even_list = [i for i in range(0, 21, 2)]
print(even_list)
print()


# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.

def celsius_to_farenheit(celsius_grads):
    return (celsius_grads * 9 / 5) + 32

celsius = [0 ,10, 20, 30, 40, 50, 100]

farenheit = [celsius_to_farenheit(i) for i in celsius]
print(f"Grados celsius: {celsius}")
print(f"Grados farenheit: {farenheit}")
print()

# 5. Crea una lista utilizando comprensión con los caracteres de una cadena.

my_word = "Hello Python"
my_list = [c for c in my_word]
print(my_list)
print()

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.

my_words = ["dog", "hause", "cat", "lamp", "computer", "bedroom", "map"]
filtered_list = [word for word in my_words if len(word) > 4]
print(filtered_list)
print()

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.
def sum_five(number):
    return number + 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_numbers = [sum_five(number) for number in numbers]
print(new_numbers)
print()

# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.

numbers= [23, 8, 3, 28, 19, 9 ,10]

bigger_than_ten = [number > 10 for number in numbers ]
print(bigger_than_ten)
print()

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = [number * 3 if number % 2 else number for number in numbers]
print(new_numbers)
print()

# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.
matrix = [[col + (3 * row) for col in range(1,4)] for row in range(3)]
for line in matrix:
    print(line)
