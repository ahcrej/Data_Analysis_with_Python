#!/usr/bin/env python3

def positive_list(L):
    # def is_positive(x):
    #     if x > 0:
    #         return True
    #     else:
    #         return False

    # return list(filter(is_positive, L))

    return list(filter(lambda x: x > 0, L))


def main():
    print(positive_list([2, -2, 0, 1, -7]))


if __name__ == "__main__":
    main()
