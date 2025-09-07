# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.

class Animal:
    def __init__(self, species = "Nueva especie"):
        self.species = species

    def make_sound(self):
        print("Sonido animal generico")

my_animal = Animal()
my_animal.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.

class Animal:
    def __init__(self, species = "Nueva especie"):
        self.species = species

    def make_sound(self):
        if self.species == "Dog":
            print("Guau")
        elif self.species == "Cat":
            print("Miau")
        else:
            print("Sonido animal generico")

my_animal = Animal()
my_animal.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.

class Car:
    def __init__(self, brand = "Sin especificar", model = "Sin especificar"):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10
        print(f"Velocidad actual: {self.__speed}")

    def brake(self):
        self.__speed = max(0, self.__speed - 10)
        print(f"Velocidad actual: {self.__speed}")


my_car = Car()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_car.brake()
my_car.brake()
my_car.brake()



# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    
    def get_author(self):
        return self.__author
    
    def change_title(self, new_title):
        self.title = new_title

my_book = Book("LOTR: The fellowship of the ring.", "J.R.R Tolkien")
print(my_book.get_author())
print(my_book.title)
my_book.change_title("LOTR: The two towers.")
print(my_book.get_author())
print(my_book.title)

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self, name, surname, notas):
        self.name = name
        self.surname = surname
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
new_student = Estudiante("Ignacio" , "Vidal", [6, 8, 9, 10])
print(f" {new_student.name} {new_student.surname} tiene una nota media de {new_student.calcular_media()}")

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        print(f"Nueva cuenta de {self.owner}. Saldo actual: {self.balance}")
    
    def deposit(self, quantity: float):
        self.balance += quantity
        print(f"Has depositado {quantity}€. Balance total: {self.balance}")

    def withdraw(self, quantity: float):
        if quantity > self.balance:
            print(f"Insuficiente saldo: Se retira: {self.balance}. Saldo actual 0") 
            self.balance = max(0, self.balance - quantity)
        else:
            self.balance -=  quantity
            print(f"Has retirado {quantity}€. Saldo Actual: {self.balance}")

my_account = BankAccount("Ignacio")
my_account.deposit(300)
my_account.deposit(250)
my_account.withdraw(500)
my_account.deposit(135)
my_account.withdraw(400)
my_account.deposit(15.5)
my_account.withdraw(15.5)        

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self , newx, newy):
        catetoa = abs(newx - self.x)
        catetob = abs(newy - self.y)        
        return ((catetoa ** 2) + (catetob ** 2)) ** 0.5
    
my_location = Point(-1, 4)
print(my_location.distance(3, 2))


# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def total_salary(self):
        return self.hours_worked * self.hourly_wage


new_person = Employee("Pedro", 18, 160)
print(new_person.total_salary())

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self):
        self.inventory = ["HDD", "SDD", "Graphic Card", "RAM", "Processor"]
    
    def add_item(self, new_item):
        self.inventory.append(new_item)

    def show_inventory(self):
        for product in self.inventory:
            print(product)

my_store = Store()
my_store.add_item("Motherboard")
my_store.show_inventory()