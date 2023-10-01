#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    # raw = []
    # results = []

    # with open(filename, "r") as f:
    #     next(f)
    #     raw = [line for line in f]

    # pattern = r'(\d+)\s*(\d+)\s*(\d+)\s*\s(.*)'

    # results = [f"{match[0][0]}\t{match[0][1]}\t{match[0][2]}\t{match[0][3]}"
    #            for match in (re.findall(pattern, line)
    #                          for line in raw)]

    results = []

    with open(filename, "r") as f:
        next(f)
        results = [f"{match[0][0]}\t{match[0][1]}\t{match[0][2]}\t{match[0][3]}"
                   for match in (re.findall(r'(\d+)\s*(\d+)\s*(\d+)\s*\s(.*)', line)
                                 for line in f)]

    return results


def main():
    for l in red_green_blue():
        print(l)


if __name__ == "__main__":
    main()
