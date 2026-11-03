class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with an ignition key")

c = Car()
b = Bike()
bus = Bus()

c.start()
b.start()
bus.start()