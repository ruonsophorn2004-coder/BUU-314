class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Airplane(Vehicle):
    def move(self):
        print("Airplane is flying")
class Ship(Vehicle):
    def move(self):
        print("Ship is sailing")