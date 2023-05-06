class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Cow(Animal):
    def make_sound(self):
        return "moo"
    

animals = [Dog("Gala"), Cat("Manet"), Cow("Betsy")]


for animal in animals:
    print(animal.name + " dice " + animal.make_sound())