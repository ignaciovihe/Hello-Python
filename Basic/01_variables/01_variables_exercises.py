# 1. Declara y asigna valores a las siguientes variables:
# •	name: una cadena que contenga tu nombre.
name = "Ignacio"
# •	age: un número entero que represente tu edad.
age = 39
# •	height: un número flotante que represente tu altura.
height = 1.87
# •	Imprime cada variable en una línea separada.
print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
age = str(age)
print(f"Tengo {age} años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = False
print(is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
name = "Ignacio Vidal Hernando"
print(f"tu nombre tiene {len(name)} caracteres")

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, surname, city = "Ignacio", "Vidal", "Madrid"
print(f"Me llamo {name} {surname} y vengo de {city}.") 

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
color = input("¿Cuál es tu color favorito?")
print(f"Tu color favorito es el {color}.")

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "platano"
print(fruit)
fruit = "naranja"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 12.9
print(price)
price = int(price)
print(price)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address = "Calle falsa, 123"
address_len = len(address)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone : int = 676776875
print(f"El número {phone} es de tipo {type(phone)}.")
phone = 111111111
print(f"El número {phone} es de tipo {type(phone)}.")
