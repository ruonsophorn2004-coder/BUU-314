class Animal:
    def eat(self):
        print("Animal is Eating")

    def make_sound(self):
        print("Animal is Making Sound")
class dog(Animal):
    def make_sound(self):
        print("Woof Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
class Cow(Animal):
    def make_sound(self):
        print("Moo Moo")

dog= Dog()
Cat= Cat()
Cow= Cow()

