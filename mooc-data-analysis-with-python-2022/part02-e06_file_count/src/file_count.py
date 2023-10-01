#!/usr/bin/env python3

import sys

def file_count(filename):
    # with open(filename, "r") as f:
    #     lines = [line for line in f]
    
    # text = " ".join(lines)
    # words = text.split()

    # return (len(lines), len(words), len(text) - 7)
    lines = 0
    words = 0
    characters = 0
    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
    return (lines, words, characters)

def main():
    files = sys.argv[1:]
    for file in files:
        lines, words, characters = file_count(file)
        print(f"{lines}\t{words}\t{characters}\t{file}")
        

if __name__ == "__main__":
    main()
