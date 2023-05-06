class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        pass

#Clase Carro
class Car(Vehicle):
    def drive(self):
        print("Conduciendo el " + self.make + " " + self.model)

#Clase Camion
class Truck(Vehicle):
    def drive(self):
        print("Conduciendo el " + self.make + " " + self.model)


car = Car("Toyota", "Corolla")
truck = Truck("Ford", "F-150")

car.drive() 
truck.drive()  