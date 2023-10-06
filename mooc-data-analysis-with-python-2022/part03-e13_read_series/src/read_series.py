#!/usr/bin/env python3

import pandas as pd


def read_series():
    indices = []
    values = []

    # while True:
    #     line = input("Enter an index then value: ")
    #     if line == "":
    #         break
    #     if len(line.split()) != 2:
    #         raise Exception
    #     indices.append(line.split()[0])
    #     values.append(line.split()[1])

    while True:
        line = input("Enter an index then value: ")
        if line == "":
            break
        try:
            if len(line.split()) != 2:
                raise ValueError
            indices.append(line.split()[0])
            values.append(line.split()[1])
        except ValueError:
            print("Not a valid line, please re-enter.")
    
    ser = pd.Series(values, index=indices)

    return ser


def main():
    read_series()


if __name__ == "__main__":
    main()
