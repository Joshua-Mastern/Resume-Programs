#########################################################
# Name: Joshua Brack
# Date: 1/19/2019
# Description: Implements vehicle, truck and car classes.
#########################################################

# the vehicle class
# a vehicle has a year, make, and model
# a vehicle is instantiated with a make and model
class Vehicle(object):
    def __init__(self, _make="", _model=""):
        self.make = _make
        self.model = _model
        self.year = 2000

    #accessor for make
    @property
    def make(self):
        return self._make

    #mutator for make
    @make.setter
    def make(self, value):
        self._make = value

    #accessor for model
    @property
    def model(self):
        return self._model

    #mutator for model
    @model.setter
    def model(self, value):
        self._model = value
    #accessor for year
    @property
    def year(self):
        return self._year

    #mutator for year
    @year.setter
    def year (self, value):
        #ignore if value is not 2000-2018
        if (value >= 2000 and value <= 2018):
            self._year = value
    def __str__(self):
        return "{} {} {}".format(self.year, self.make, self.model)

# the truck class
# a truck is a vehicle
# a truck is instantiated with a make and model
class Truck(Vehicle):
    def __init__(self, _make, _model):
        Vehicle.__init__(self, _make, _model)

# the car class
# a car is a vehicle
# a car is instantiated with a make and model
class Car(Vehicle):
    def __init__(self, _make, _model):
        Vehicle.__init__(self, _make, _model)

# the Dodge Ram class
# a Dodge Ram is a truck
# a Dodge Ram is instantiated with a year
# all Dodge Rams have the same make and model
class DodgeRam(Truck):
    make = "Dodge"
    model = "Ram"
    def __init__(self, _year):
        Truck.__init__(self, DodgeRam.make, DodgeRam.model)
        self.year = _year
    

# the Honda Civic class
# a Honda Civic is a car
# a Honda Civic is instantiated with a year
# all Honda Civics have the same make and model
class HondaCivic(Car):
    make = "Honda"
    model = "Civic"
    def __init__(self, _year):
        Car.__init__(self, HondaCivic.make, HondaCivic.model)
        self.year = _year
        

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print ram

civic1 = HondaCivic(2007)
print civic1

civic2 = HondaCivic(1999)
print civic2

