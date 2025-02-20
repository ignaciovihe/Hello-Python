# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).

def divide(number1, number2):
    try:
        result= number1 / number2
        print(f"El resultador es: {result}")
    except ZeroDivisionError:
        print("No se puede dividir por 0")

n1, n2 = map(int,input("Dame dos numeros para dividir: ").split())
divide(n1, n2)

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.

def convert_to_int(element):
    try:
        converted_elemen = int(element)
        print("Converión correcta")
    except ValueError as error:
        print(f"Ha habido un problema en la conversión {error}")

convert_to_int("YO")


# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def open_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as error:
        print(f"El archivo no exixste. {error}")

open_file("12_exceptions/archivo.txt")

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

def calculator(num1, operator, num2):
    try:    
        match operator:
            case "+":
                print(f"{num1} + {num2} = {num1 + num2}")
            case "-":
                print(f"{num1} - {num2} = {num1 - num2}")
            case "*":
                print(f"{num1} * {num2} = {num1 * num2}")
            case "/":
                print(f"{num1} / {num2} = {num1 / num2}")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except TypeError:
        print("Algun número no es del tipo correcto")
    else:
        print("Operacion realizada correctamente")
    finally:
        print("Se termina la ejecución")

n1, op, n2 = input("Introduce una operacion con espacios: ").split()
calculator(int(n1), op, int(n2))

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

def check_age():
    try:
        age = int(input("Introduce tu edad: "))
        if age < 0:
            raise ValueError("El número no puede ser negativo")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print("Has introducido bien tu edad")
    finally:
        print("Se termina la ejecucion")

check_age()  


# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango.

def get_element(index):
    names = ["Ignacio" , "Pedro", " Miguel"]
    try:
        print(names[index])
    except IndexError as error:
        print(f"El índice esta fuera de rango. {error}")

get_element(3)

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def handle_multiple_exceptions():
    input_ok = False
    while not input_ok:
        try:
            n1, n2 = map(int, input("Dame dos números separados por comas: ").split(","))
            input_ok = True
            print(f"{n1} / {n2} = {n1 / n2} --> Operación correcta")
            n3 = input("Dame otro número: ")
            print(n2 + n3)
            
        except ValueError as error:
            print(f"Has usado un formato incorrecto: {error} \nDebes usar este formato X,Y")
        except ZeroDivisionError:
            print("No se puede dividir por 0")
        except TypeError as error:
            print(error)
        finally:
            if input_ok:
                print("Ejecución terminda")

handle_multiple_exceptions()

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

#Defino una excepcion personalizada que hereda de Exception
class InsufficientFundsError(Exception):                    #Hereda de exception
    def __init__(self, mensaje, codigo_error):              #Se crea el contructor
        super().__init__(mensaje)                           #Se llama al contructor de la clase sup.
        self.codigo_error = codigo_error                    # Se crea un atributo personalizado         
    def __str__(self):                                      # Define el mensaje que se mostrara en "as error"
        return f"[Error {self.codigo_error}]: {self.args[0]}"

def transaction(funds, withdrawal_amount):
    try:
        if withdrawal_amount > funds:
            print(f"Saldo inicial: {funds}. Dinero a retirar: {withdrawal_amount}.")
            raise InsufficientFundsError("Saldo insuficiente", "InsufficientFundsError" )
        else:
            print(f"Saldo inicial: {funds}. Dinero a retirar: {withdrawal_amount}. Saldo final: {funds - withdrawal_amount}")
    except InsufficientFundsError as error:
        print(error)

transaction(200,125)



# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

def covert_list_to_integers(my_list):
    integers = []
    for element in my_list:
        try:
            integers.append(int(element))
        except ValueError as error:
            print(f"No se puede convertir el dato: {element} \n\t[{error}]")
            continue
        except TypeError as error:
            print(f"int() no puede convertir ese tipo de dato: {element} \n\t[{error}]")
            continue
    return integers

print(covert_list_to_integers([3, "3", "Hola", [1, 4]]))

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.

def square_root(number):
    try:
        if number < 0:
            raise ValueError("No se puede hacer la raiz cuadrada de un número negativo")
        return number ** 0.5
    except ValueError as error:
        print(f" Error: {error}")

print(square_root(-3))
