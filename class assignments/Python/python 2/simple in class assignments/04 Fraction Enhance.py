######################################################################################################################
# Name: Joshua Brack    
# Date: 12/18/2018
# Description: Fraction class that allows division, multiplication, addition, and subtraction
######################################################################################################################

# the fraction class
class Fraction(object):

    def __init__(self, num = 0, den = 1):
        self.num = num
        if (den == 0):
            den = 1
        self.den = den
        
    #accessor(getter) for the numerator
    @property
    def num(self):
        return self._num
    
    #mutator(setter) for the numerator
    @num.setter
    def num(self, value):
        self._num = value
        
    #accessor(getter) for the denominator
    @property
    def den(self):
        return self._den
    
    #mutator (setter) for the denominator
    @den.setter
    def den(self, value):
        #ignore if the value is zero
        if(value != 0):
            self._den = value

    def realValue(self):
        return float(self.num) / self.den

    #return the string representation of the fraction
    def __str__(self):
        self.reduce()
        return "{}/{}, ({})".format(self.num, self.den, self.realValue())

    #add two fractions
    def __add__(self, other):
        num = (self.num * other.den) + (self.den * other.num)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    #subtract two fractions
    def __sub__(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = (self.den * other.den)
        return Fraction(num, den)

    #multiply two fractions
    def __mul__(self, other):
        num = (self.num *other.num)
        den = (self.den * other.den)
        return Fraction(num, den)

    #divide two fractions
    def __div__(self, other):
        num = (self.num * other.den)
        den = (self.den * other.num)
        return Fraction(num, den)

    #reduce a fraction
    def reduce(self):
        #assume greatest common divisor is one
        gcd = 1
        #find the minimum from the numerator and denominator
        minimum = min(abs(self.num), abs(self.den))
        
        #if gcd is not one, look for gcd
        for i in range(2, minimum + 1):
            if (self.num % i == 0 and self.den % i == 0):
                    gcd = i
        
        #divide both the numerator and denominator by the gcd
        self.num /= gcd
        self.den /= gcd

        #setting the denominator to 1 if numerator is 0
        if(self.num == 0):
            self.den = 1


# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

