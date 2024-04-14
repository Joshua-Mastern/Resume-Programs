class Car(object):
    def __init__(self, name):
        self.name = name
        self.tires = 4
        self.engine = True

    def __str__(self):
        return "Name: {}\nTires: {}\nEngine: {}".format(self.name, self.tires, self.engine)
    
class Bicycle(object):
    def __init__(self, name):
        self.name = name
        self.tires = 2
        self.engine = False

    def __str__(self):
        return "Name: {}\nTires: {}\nEngine: {}".format(self.name, self.tires, self.engine)

class Motorcycle(object):
    def __init__(self, name):
        self.name = name
        self.tires = 2
        self.engine = True

    def __str__(self):
        return "Name: {}\nTires: {}\nEngine: {}".format(self.name, self.tires, self.engine)
        

#########################################################################################
c1 = Car("angel")
print c1
print "_" * 20
b1 = Bicycle("austin")
m1 = Motorcycle("zoe")
print b1
print "_"*20
print m1
print"_"*20
    
