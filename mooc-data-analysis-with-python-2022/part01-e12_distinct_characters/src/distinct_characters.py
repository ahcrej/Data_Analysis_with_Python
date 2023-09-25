#!/usr/bin/env python3

def distinct_characters(L):
    # temp = []
    d = {}

    for word in L:
        d[word] = len(set(word))
        # chars = len(set(word))
        # temp = list(word)
        # chars = set(temp)
        # d[word] = len(chars)
        # temp.clear()
    return d


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
