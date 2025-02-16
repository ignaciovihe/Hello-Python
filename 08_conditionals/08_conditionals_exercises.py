# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.

number = int(input("Dame un número: "))
if number < 0:
    print("El número es negativo")
elif number > 0:
    print("El número es positivo")
else:
    print("El número es 0")


# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
edad = int(input("Introcude tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
my_string = "Mi cadena"
if my_string:
    print("La cadena esta llena")
else:
    print("La cadena esta vacia")
# Otra forma de hacer el if:   
print("La cadena esta llena") if my_string else print("La cadena esta vacia")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
number1, number2 = map(int,input("Dame dos numeros separados por un espacio: ").split())
if number1 == number2:
    print("Los números son iguales ")
elif number1 > number2:
    print(f"{number1} es mayor que {number2}")
else:
    print(f"{number2} es mayor que {number1}")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
number = int(input("Introduce un número: "))
if not(number % 3) and not(number % 5):
    print("El numero es divisible por 3 y 5")
else:
    print("El número no es divisible por 3 y 5")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
number = int(input("Introduce un número: "))
if not(number % 2):
    print("El número es par")
else:
    print("El número es impar")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
edad = int(input("Introduce tu edad: "))
if edad < 16:
    print("No puedes votar")
elif 16 <= edad < 18:
    print("Puedes votar con un permiso especial")
else:
    print("Puedes votar")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
password = "qwerty"
my_pass = input("Introduce tu contraseña: ")
if my_pass == password:
    print("Contraseña correcta, bienvenido")
else:
    print("Contraseña incorrecta.")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
number = int(input("Introduce un número: "))
if 10 <= number <= 20:
    print("El numero esta entre 10 y 20") 
else: 
    print("El número es menor que 10 o mayor que 20")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
color = input("Introduce un color: verde, amarillo o rojo: ").lower()
match color:
    case "rojo":
        print("Debes detenerte")
    case "amarillo":
        print("Debes estar alerta")
    case "verde":
        print("Avanza")
    case _:
        print("Color no valido")