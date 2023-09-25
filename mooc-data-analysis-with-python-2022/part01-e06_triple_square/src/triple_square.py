#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        a = triple(i)
        b = square(i)
        if (b > a):
            break
        else:
            print(f"triple({i})=={a} square({i})=={b}")

def triple(num):
    return num*3

def square(num):
    return num*num

if __name__ == "__main__":
    main()
