
import re
# 1. Busca si una cadena empieza por "Hola".
pattern = re.compile(r"Hola")
print("Encontrado") if pattern.match("Buenos dias ,me llamo Ignacio") else print("No encontrado")


# 2. Busca la palabra "Python" en una cadena aunque esté en minúsculas.
pattern = re.compile(r"Python", re.I) # el flag I hace que ignore las minúsculas o mayusculas
match = pattern.search("Estoy estudiando python")
print("Encontrado") if match else print("No encontrado")


# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
pattern = re.compile(r"curso", re.I)
print(pattern.findall("Curso de Python. En este curso encontraras todo lo que buscas sobre python. Apuntate al CURSO ya."))


# 4. Reemplaza todas las apariciones de "lección" por "LECCIÓN".

print(re.sub("[L|l]ección","LECCIÓN", "En esta lección revisamos las expresiones regulares"))

# 5. Divide un texto en partes separadas por comas.
my_string = "Hoy empiezo una nueva etapa, en todos los sentidos, sera dificil al principio, pero se que lo conseguiré."
print(re.split(",", my_string))

# 6. Busca la primera palabra que comience con "A" o "a".
pattern = re.compile(r"\ba[\w]*", re.I)
i,f = re.search(pattern, my_string).span()
print(my_string[i:f])


# 7. Encuentra todas las palabras en una cadena que terminen en "ción".
my_string = "Tarta, ración, maratón, canción, marciano"
pattern = re.compile(r"[\w]*ción\b")
print(pattern.findall(my_string))

# 8. Verifica si una cadena contiene solo números.
my_string = "a2"
if re.search(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ]", my_string):
    print("No son todo dígitos")
elif re.search(r"\d", my_string):
    print("Son todo dígitos")
else:
    print("Cadena vacía")

print("Son todo dígitos") if re.fullmatch(r"\d+", my_string) else print("No son todo dígitos.")

# 9. Reemplaza todos los números de una cadena por el texto "[número]".
numbers = {
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
}

my_string = "1, 2, 3, 4, 5"
digits = re.findall(r"\d", my_string)
for digit in digits:
    my_string = re.sub(digit, numbers[digit], my_string)
print(my_string)

my_string = "El curso tendra lugar desde la 18 a las 20 horas"
my_string = re.sub(r"\d+", "[Número]", my_string)
print(my_string)


# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
my_string = "amigo, casa, loro, perro, mama"
pattern = re.compile(r"\b....\b")
print(pattern.findall(my_string))