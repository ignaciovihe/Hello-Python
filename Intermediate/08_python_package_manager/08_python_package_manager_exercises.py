# 1. Importa el módulo math y muestra el valor de pi.
import math

print(math.pi)

# 2. Crea un array de números usando numpy y multiplícalo por 3.

import numpy

numpyarray = numpy.array([[2, 3], [4, 5]])
print(numpyarray)
print(numpyarray * 3)


# 3. Muestra la versión instalada de numpy.


import pandas as pd
print(f"numpy verion: {numpy.version.version}")
print(f"pandas version: {pd.__version__}")

# 4. Realiza una petición HTTP con requests a una API pública y muestra el código de estado.

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response.status_code)

if response.status_code == 200:
    print(response.json())


# 5. Importa una función llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilízala.

from mypackage import arithmetics

print(arithmetics.sum_two_values(2, 3))

# 6. Usa pandas para crear un DataFrame con nombres en español.
datos = {
    "Name" : ["Anna", "Peter", "John"],
    "Age" : [23, 34, 46]
}

df = pd.DataFrame(datos)
print(df)
print(df.loc[1, "Name"])
print(df.shape)

# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.

# pip install request

# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros Pokémon.
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
if response.status_code == 200:
    data = response.json()
    #print(json.dumps(data, indent=4)) para imprimir el json mas visualmente
    for item in data["results"]:
        print(item["name"])


# 9. Muestra todos los paquetes instalados con pip desde la terminal.

# pip list

# 10. Escribe una línea de código que muestre la ayuda sobre el paquete numpy desde Python.
help(numpy)
