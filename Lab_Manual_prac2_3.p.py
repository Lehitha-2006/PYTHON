class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
class Bird(Animal):
    def make_sound(self):
        print("Chirp")

animals = [Dog(), Cat(), Bird()]
for x in animals:
    x.make_sound()
