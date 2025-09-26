# 1. Genera un SyntaxError al imprimir una cadena sin paréntesis.

#print "Hello Python"

# 2. Genera un NameError intentando usar una variable no definida.

#print(name)

# 3. Genera un IndexError accediendo a un índice inexistente de una lista.

my_list = [1, 2, 3, 4]
#print(my_list[4])

# 4. Genera un ModuleNotFoundError al importar un módulo inexistente.

#import maths

# 5. Genera un AttributeError accediendo a un atributo que no existe.

import datetime

#print(datetime.dates)

# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.

my_dict = {"name": "Leonardo", "lastname": "Da Vinci"}
#print(my_dict["firstname"])

# 7. Genera un TypeError usando tipos incorrectos (índice string en lista).

my_list = ["a", "b"]
#print(my_list["1"])

# 8. Genera un ImportError al importar una función que no existe desde un módulo.

#from datetime import dates

# 9. Genera un ValueError intentando convertir un string no numérico a entero.

#edad = int("12 años")
#print(edad)


# 10. Intenta detectar si un error ocurre usando try-except con un KeyError.
try:
    my_dict["firstname"]
except KeyError as e:
    print(f"La clave no existe: {e}")
