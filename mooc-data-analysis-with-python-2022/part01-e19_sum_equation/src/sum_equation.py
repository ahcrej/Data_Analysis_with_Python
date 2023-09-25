#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        result = "0 = 0"
    else:
        result = " + ".join(map(str, L)) + f" = {sum(L)}"

    return result

def main():
    print(sum_equation([1,5,7]))
    #L = [1, 5, 7]
    #result = " + ".join(map(str, L)) + f" = {sum(L)}"
    #print(result)

if __name__ == "__main__":
    main()
