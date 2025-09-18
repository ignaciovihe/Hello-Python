# 1. Crea una lambda que sume dos números.

sum = lambda a, b : a + b
print(sum(1, 2))
print()

# 2. Crea una lambda que calcule el cuadrado de un número.

square = lambda a : a ** 2
print(square(2))
print()

# 3. Crea una lambda que devuelva el mayor de dos números.

bigger = lambda a , b : a if a > b else b
print(bigger(12, 17))
print()

# 4. Crea una lambda que sume 10 a un número dado.

sum_10 = lambda a : a + 10
print(sum_10(10))
print()

# 5. Crea una lambda que devuelva el último carácter de una cadena.

last_char = lambda s : s[-1]
print(last_char("Hello"))
print()

# 6. Crea una lambda que indique si una palabra tiene más de 6 letras.

check_len = lambda w : len(w) > 6
print(check_len("Hello"))
print()

# 7. Crea una lambda que convierta una cadena a minúsculas.

lowercase = lambda w : w.lower()
print(lowercase("PYTHON"))
print()

# 8. Crea una lambda que devuelva True si un número es positivo.

positive = lambda n : n > 0
print(positive(1))
print()

# 9. Crea una lambda que devuelva "Cadena vacía" si el string está vacío.

empty_str = lambda s : "Cadena vacía" if len(s) == 0 else "Cadena no vacía"
print(empty_str(""))
print()

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.

price_with_tax = lambda price : price * 1.21
print(price_with_tax(80))
print()


# EJEMPLO DE CLOSURES USANDO LAMBDAS

def make_checker(condition, value):
    if condition == "greater":
        return lambda x: x > value
    elif condition == "less":
        return lambda x: x < value
    elif condition == "divisible":
        return lambda x: x % value == 0
    else:
        return lambda x: True  # por defecto, siempre cierto

# Creamos funciones dinámicas en tiempo de ejecución:
greater_than_10 = make_checker("greater", 10)
less_than_5 = make_checker("less", 5)
divisible_by_3 = make_checker("divisible", 3)

print(greater_than_10(12))  # True
print(less_than_5(7))       # False
print(divisible_by_3(9))    # True