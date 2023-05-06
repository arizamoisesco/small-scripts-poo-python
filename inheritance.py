class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Vehiculo):
    def __init__(self, marca, modelo, precio):
        super().__init__(marca, modelo)
        self.precio = precio

carro = Carro("Ford", "Mustang", 50000)
print(carro.marca) # Ford
print(carro.modelo) # Mustang
print(carro.precio) # 50000