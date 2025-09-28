
import os
script_path = os.path.dirname(os.path.abspath(__file__))

# 1. Crea un archivo de texto y escribe en él la frase "Hola desde Python".
with open(f"{script_path}/hello_python.txt", "w") as f:
    f.write("Hola desde Python")

# 2. Abre un archivo y lee todo su contenido.
with open(f"{script_path}/hello_python.txt", "r") as f:
    print(f.read())

# 3. Añade una nueva línea al final del archivo con el texto "Línea añadida".
with open(f"{script_path}/hello_python.txt", "a") as f:
    f.write("\nLinea añadida")

# 4. Lee solo los primeros 10 caracteres del archivo.
with open(f"{script_path}/hello_python.txt", "r") as f:
    print(f.read(10))

# 5. Usa seek para volver al inicio del archivo y leer desde ahí.
    print(f.read())
    f.seek(0)
    print(f.read())

# 6. Lee e imprime el contenido línea por línea usando readline.
    f.seek(0)
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()
    

# 7. Lee todas las líneas del archivo en una lista y recórrelas con un bucle.
    f.seek(0)
    print()
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias líneas.
with open(f"{script_path}/hello_python.txt", "w") as f:
    f.write("Mi nombre el Pedro\nEstudio Python\ny alemán")



# 9. Usa una función para abrir un archivo, escribir texto y cerrarlo automáticamente con with.

with open(f"{script_path}/hello_python.txt", "w") as f:
    f.write("Este fichero se maneja con with")


# 10. Lee un archivo línea por línea y muestra solo las que contienen la palabra "Python".
print()
with open(f"{script_path}/filter_lines.txt", "r") as f:
    for linie in f:
        if "Python" in linie:
            print(linie.strip())