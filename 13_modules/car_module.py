# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.brand} - {self.model} - {self.year}")

