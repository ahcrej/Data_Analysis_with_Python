#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    print(triangle.hypotenuse(4, 5))
    print(triangle.area(4,5))

if __name__ == "__main__":
    main()
