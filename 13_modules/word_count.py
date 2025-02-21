# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.

def count_word(word, text: str):
    return text.lower().split().count(word.lower())