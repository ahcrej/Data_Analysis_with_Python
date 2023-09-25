#!/usr/bin/env python3

def merge(L1, L2):
    sorted_list = L1 + L2

    # Bubble sort algorithm
    for i in range(len(sorted_list)):
        for i in range(len(sorted_list) - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                # temp = sorted_list[i]
                # sorted_list[i] = sorted_list[i + 1]
                # sorted_list[i + 1] = temp
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]

    return sorted_list

def main():
    L1 = [1, 3, 5, 7]
    L2 = [1, 3, 6, 6, 7]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
