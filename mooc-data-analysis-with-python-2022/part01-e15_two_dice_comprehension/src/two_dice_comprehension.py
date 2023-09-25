#!/usr/bin/env python3

def main():
    # results = [(i, j) for i in range(1, 7) for j in range(1, 7) if (i + j == 5)]
    
    # for pair in results:
    #     print(pair)

    print("\n".join(f"({a}, {b})" for a in range(1, 7) for b in range(1, 7) \
                    if (a + b == 5)))

if __name__ == "__main__":
    main()
