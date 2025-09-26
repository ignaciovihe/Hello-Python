# 1. Crea una función que reciba una función y un número, y devuelva el resultado de aplicar la función al número.

def apply_func(function, number):
    return function(number)

def add_ten(number):
    return number + 10

apply_func(print ,2)
print(apply_func(add_ten, 2))
print(apply_func(lambda n : n * 2, 2))

# 2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.

def sum_two_numbers_and_apply_func(number1, number2, function):
    return function(number1+ number2)

def add_five(number):
    return number + 5

sum_two_numbers_and_apply_func(5, 10, print)
print(sum_two_numbers_and_apply_func(5, 10, add_five))
print(sum_two_numbers_and_apply_func(5, 10, lambda n: n ** 2))

# 3. Crea una función que devuelva otra función que sume un número fijo.

def create_adder(fix_number):
    def sum(value): 
        return value + fix_number
    return sum #También se puede devolver directamente una lambda

sum_5 = create_adder(5)
print(sum_5(10))
sum_100 = create_adder(100)
print(sum_100(1))


# 4. Usa map() con lambda para multiplicar cada número de una lista por 10.

my_list =[2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda n: n * 10, my_list)))

# 5. Usa filter() con lambda para quedarte solo con los números pares.

print(list(filter(lambda n: n % 2 == 0, my_list)))

# 6. Usa reduce() con lambda para obtener la suma total de una lista.
from functools import reduce

print(reduce(lambda n1, n2: n1 + n2, my_list))

# 7. Escribe una función que devuelva una función que reciba un nombre y devuelva “Hola, ”.

def create_greet(salute):
    def greet(name):
        return f"{salute}, {name}"
    return greet

hello = create_greet("Hello")
print(hello("Peter"))
how_are_you = create_greet("How are you")
print(how_are_you("John"))
print(hello("Sarah"))

# 8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.

my_numbers =[2, 3, 4, 5, 6, 7, 8, 12]
my_names =["Ana", "Juan", "Pedro"]

def checker(function, values):
    counter = 0
    for value in values:
        if function(value):
            counter += 1
    return(counter)

print(checker(lambda n: n % 2 == 0, my_numbers))
print(checker(lambda n: len(n) > 3, my_names))

# 9. Crea una función que reciba dos funciones y un número, y las aplique en orden.

def apply_functions(function1, function2, number):
    return function2(function1(number))

print(apply_functions(lambda n: n * 10, lambda n: n + 10, 8))
print(apply_functions(lambda n: n + 10, lambda n: n * 10, 8))

# 10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).

def apply_function_to_list(function, iterable):
    result = []
    for element in iterable:
        result.append(function(element))

    return result

def make_lower(name):
    return name.lower()

print(apply_function_to_list(make_lower, my_names))
print(apply_function_to_list(lambda n: f"{n}%",my_numbers))
