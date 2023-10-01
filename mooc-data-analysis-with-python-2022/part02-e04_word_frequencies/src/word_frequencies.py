#!/usr/bin/env python3

def word_frequencies(filename):
    d = {}

    with open(filename, "r") as f:
        raw = f.read().split()

    cleaned = [word.strip("""!"#$%&'()*,-./:;?@[]_""") for word in raw]

    for word in cleaned:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d


def main():
    print(word_frequencies("src/alice.txt"))


if __name__ == "__main__":
    main()
