#superclass vehicle
class Vehicle(object):
    def __init__(self, name):
        self.name = name
        self.tires = None
        self.engine = None

    def __str__(self):
        return "Name: {}\nTires: {}\nEngine: {}".format(self.name, self.tires, self.engine)
    
class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 4
        self.engine = True
    def __str__(self):
        return "Car:\n" + Vehicle.__str__(self)
        
class Cycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2
class Bicycle(Cycle):
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = False

    def makeSound(self):
        print "Squeak squeak"

    def __str__(self):
        return "Bicycle:\n" + Cycle.__str__(self)

class Motorcycle(Cycle):
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.tires = 2
        self.engine = True
    def makeSound(self):
        print "Vroom Vroom"
    def __str__(self):
        return "Motorcycle:\n" + Cycle.__str__(self)

        

    ##############################################################################
c1 = Car("angel")
print c1
print "_" * 20
b1 = Bicycle("austin")
m1 = Motorcycle("zoe")
print b1
print "_"*20
print m1
print"_"*20
    
m1.makeSound()
b1.makeSound()
