# 1. Usa un bucle while para imprimir los números del 1 al 10.
number = 1
while number < 11:
    print(number)
    number += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
number = 1
total = 0
while number < 101:
    print(f"Number = {number}")
    total += number
    number += 1
else: print(f"EL total es {total}")

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
word = "Python"
for letter in word:
    print(letter)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
number = 1
while number < 50:
    print(f"Numero: {number}")
    if number % 7 == 0:
        print(f"El primer numero divisible por 7 es {number}")
        break
    number += 1


# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
for element in my_dict.keys():
    print(element)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
number = 1
while number < 21:
    if number % 2 == 0:
        print (number)
    number += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for i in range(10,0,-1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
my_list = [30, 10, 30, 20, 30, 40]
total = 0
for element in my_list:
    if element == 30:
        total += 1
print(f"30 aparece {total} veces en la lista")


# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
my_list = ["Pepe", "Nacho", "Jose", "Miguel", "Lore", "Maria", "Brais", "Manuel"]
for name in my_list:
    if name == "Brais":
        break
    else:
        print (name)
