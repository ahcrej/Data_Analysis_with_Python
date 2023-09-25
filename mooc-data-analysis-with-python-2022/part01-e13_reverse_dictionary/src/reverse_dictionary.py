#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}

    # for value in d.values():
    #     for word in value:
    #         result[word] = []

    for key, value in d.items():
        for word in value:
            if word in result:
                result[word].append(key)
            else:
                result[word] = [key]

    return result


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa',
                                         'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(d)
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
