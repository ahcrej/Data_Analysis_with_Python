#!/usr/bin/env python3

import sys
import statistics


def summary(filename):
    numbers = []

    with open(filename, "r") as f:
        for line in f:
            try:
                numbers.append(float(line))
            except:
                pass

    (total, average, stddev) = (sum(numbers),
                                statistics.mean(numbers), statistics.stdev(numbers))

    return (total, average, stddev)


def main():
    # Adds all sys arguments into a list, except the current program's name which is sys.argv[0]
    files = sys.argv[1:]
    for file in files:
        total, average, stddev = summary(file)
        print(
            f"File: {file} Sum: {total:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")


if __name__ == "__main__":
    main()
