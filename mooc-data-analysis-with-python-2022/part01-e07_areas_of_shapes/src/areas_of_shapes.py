#!/usr/bin/env python3
import math


def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape != "triangle" and shape != "rectangle" and shape != "circle":
            print("Unknown shape!")
            continue
        elif shape == "triangle":
            triangle()
        elif shape == "rectangle":
            rectangle()
        elif shape == "circle":
            circle()


def triangle():
    base = float(input("Give base of the triangle: "))
    height = float(input("Give height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area is {area}")

def rectangle():
    width = float(input("Give width of the rectangle: "))
    height = float(input("Give height of the rectangle: "))
    area = width * height
    print(f"The area is {area}")

def circle():
    radius = float(input("Give radius of the circle: "))
    area = math.pi * pow(radius, 2)
    print(f"The area is {area}")

if __name__ == "__main__":
    main()
