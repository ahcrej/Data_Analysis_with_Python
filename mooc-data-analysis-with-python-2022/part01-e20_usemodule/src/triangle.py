# Enter you module contents here
'''This module defines basic functions for a triangle.'''
from math import sqrt
__author__ = "Jeremy"
__version__ = "1"

def hypotenuse(a, b):
    '''This function returns the length of the hypothenuse 
	when given the lengths of two other sides of a right-angled triangle.'''
    return sqrt(a**2 + b**2)


def area(a, b):
    '''This function returns the area of the right-angled triangle,
	when two sides, perpendicular to each other, are given as parameters.'''
    return 0.5 * a * b
