#!/usr/bin/env python3

def detect_ranges(L):
    sorted_list = sorted(L)
    result_list = []
    seq_start = 0
    seq_end = 0

    for i in range(1, len(sorted_list)):
        if sorted_list[i] - 1 == sorted_list[i - 1]:
            seq_end = i

            if i == len(sorted_list) - 1:
                t = (sorted_list[seq_start], sorted_list[seq_end] + 1)
                result_list.append(t)

        else:
            if seq_start == seq_end:
                result_list.append(sorted_list[seq_start])

            else:
                t = (sorted_list[seq_start], sorted_list[seq_end] + 1)
                result_list.append(t)

            seq_start = seq_end = i

            if i == len(sorted_list) - 1:
                result_list.append(sorted_list[-1])

    return result_list


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
