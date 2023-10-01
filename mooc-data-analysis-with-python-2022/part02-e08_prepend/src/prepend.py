#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, param1):
        self.a = param1

    def write(self, s):
        print(f"{self.a}{s}")


def main():
    #pass
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
