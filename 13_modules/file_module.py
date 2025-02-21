# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

def read_file(name):
    try:
        with open(name , "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return ("El archivo no existe")
    except Exception as e:
        return(f"Ocurrio un error al lerr el archivo {e}")


def append_file(name, message):
    try:
        with open(name, "a") as file:
            file.write(message)
    except Exception as e:
        return(f"Ocurrio un error al escribir en el archivo: {e}")