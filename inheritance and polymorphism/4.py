class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo")

class Lion(Animal):
    def sound(self):
        print("Lion: Roar")

d = Dog()
c = Cat()
w = Cow()
l = Lion()

d.sound()
c.sound()
w.sound()
l.sound()