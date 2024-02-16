#Registro de Vehiculos en una clase con herencia


class Vehicle:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Vehicle):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

class Barco(Vehicle):
    def __init__(self, marca, modelo, eslora):
        super().__init__(marca, modelo)
        self.eslora = eslora

class Avion(Vehicle):
    def __init__(self, marca, modelo, capacidad_pasajeros):
        super().__init__(marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros

# Objetos de cada tipo de vehículo
carro1 = Carro(marca="Toyota", modelo="Corolla", color="Rojo")
carro2 = Carro(marca="Honda", modelo="Civic", color="Azul")

barco1 = Barco(marca="Yamaha", modelo="123", eslora=10.5)
barco2 = Barco(marca="Mercury", modelo="456", eslora=8.2)

avion1 = Avion(marca="Boeing", modelo="747", capacidad_pasajeros=400)
avion2 = Avion(marca="Airbus", modelo="A320", capacidad_pasajeros=200)


print(f"Carro 1: {carro1.marca} {carro1.modelo}, Color: {carro1.color}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Color: {carro2.color}")

print(f"Barco 1: {barco1.marca} {barco1.modelo}, Eslora: {barco1.eslora} metros")
print(f"Barco 2: {barco2.marca} {barco2.modelo}, Eslora: {barco2.eslora} metros")

print(f"Avión 1: {avion1.marca} {avion1.modelo}, Capacidad de pasajeros: {avion1.capacidad_pasajeros}")
print(f"Avión 2: {avion2.marca} {avion2.modelo}, Capacidad de pasajeros: {avion2.capacidad_pasajeros}")