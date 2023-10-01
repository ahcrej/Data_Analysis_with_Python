#!/usr/bin/env python3
import re

def file_extensions(filename):
    no_ext = []
    matches = []
    types = {}

    with open(filename, "r") as f:
        raw = [line.strip() for line in f]

    for file in raw:
        if "." not in file:
            no_ext.append(file)
        else:
            matches.append(re.findall(r'(.*)\.(.*)', file))

    for match in matches:
        name, extension = match[0][0], match[0][1]
        if extension in types:
            types[extension].append(f"{name}.{extension}")
        else:
            types[extension] = [f"{name}.{extension}"]
        
    return (no_ext, types)

def main():
    no_ext, d  = file_extensions("src/filenames.txt")

    print(f"{len(no_ext)} files with no extension")

    for key in sorted(d):
        print(f"{key} {len(d[key])}")

if __name__ == "__main__":
    main()
