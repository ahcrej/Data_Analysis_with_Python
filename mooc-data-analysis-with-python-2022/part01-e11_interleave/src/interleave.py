#!/usr/bin/env python3

def interleave(*lists):
    results_list = []

    for item in zip(*lists):
        results_list.extend(item)

    return results_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
