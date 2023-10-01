#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def __mul__(self, b):
        return Rational(self.numer * b.numer , self.denom * b.denom)
    
    def __truediv__(self, b):
        return Rational(self.numer * b.denom, self.denom * b.numer)
    
    def __add__(self, b):
        new_denom = self.denom * b.denom
        mult1 = b.denom
        mult2 = self.denom
        new_numer = self.numer * mult1 + b.numer * mult2
        return Rational(new_numer, new_denom)
    
    def __sub__(self, b):
        new_denom = self.denom * b.denom
        mult1 = b.denom
        mult2 = self.denom
        new_numer = self.numer * mult1 - b.numer * mult2
        return Rational(new_numer, new_denom)

    def __eq__(self, b):
        return self.numer == b.numer and self.denom == b.denom
    
    def __gt__(self, b):
        new_denom = self.denom * b.denom 
        mult1 = b.denom
        mult2 = self.denom
        new_numer_a = self.numer * mult1
        new_numer_b = b.numer * mult2
        return new_numer_a / new_denom > new_numer_b / new_denom

    def __lt__(self, b):
        new_denom = self.denom * b.denom 
        mult1 = b.denom
        mult2 = self.denom
        new_numer_a = self.numer * mult1
        new_numer_b = b.numer * mult2
        return new_numer_a / new_denom < new_numer_b / new_denom

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
