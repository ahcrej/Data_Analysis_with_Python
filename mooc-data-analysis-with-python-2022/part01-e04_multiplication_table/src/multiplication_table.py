#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            number = '{:4d}'.format(i*j)
            if j == 10:
                print(number)
            else: 
                print(number, end="")
    #pass

if __name__ == "__main__":
    main()
