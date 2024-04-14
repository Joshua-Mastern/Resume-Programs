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
        return "{}/{}, {}".format(self.num, self.den, self.realValue())

    #add two fractions
    def __add__(self, other):
        num = (self.num * other.den) + (self.den * other.num)
        den = (self.den * other.den)
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
##main##

f1 = Fraction()
f2 = Fraction(2, 4)
f3 = Fraction(1, 3)
f4 = f2+f3

print f1
print f2
print f3
print f4
