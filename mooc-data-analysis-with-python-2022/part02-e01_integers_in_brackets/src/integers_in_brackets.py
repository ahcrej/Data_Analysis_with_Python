#!/usr/bin/env python3


def integers_in_brackets(s):
    import re

    result = re.findall(r'\[\s*[+-]?\d+\s*\]', s)
    #result = re.findall(r'\[\s*([\+\-]?\d+)\s*\]', s)

    # int function mapped to all integers in the passed list,
    # the passed list is all results with any character in the string "[ ]" stripped out 
    result = list(map(int,[s.strip("[ ]") for s in result]))

    return result


def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))
    print(integers_in_brackets(" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"))


if __name__ == "__main__":
    main()
