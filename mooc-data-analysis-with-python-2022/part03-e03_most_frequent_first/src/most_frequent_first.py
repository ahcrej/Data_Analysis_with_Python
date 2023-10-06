#!/usr/bin/env python3

import numpy as np


def most_frequent_first(a, c):
    # Step 1: Extract the specified column (column c)
    column_c = a[:, c]

    # Step 2: Find unique values and their counts in column_c
    unique_values, inverse_indices, value_counts = np.unique(
        column_c, return_inverse=True, return_counts=True)
    
    print(unique_values, inverse_indices, value_counts)

    # Step 3: Sort the unique values by their counts
    sorted_indices = np.argsort(value_counts[inverse_indices])

    # Step 4: Rearrange the original array based on sorted indices
    sorted_a = a[sorted_indices][::-1]

    return sorted_a


def main():
    input_array = np.array([[3, 2, 7],
                            [1, 2, 5],
                            [3, 1, 3],
                            [2, 4, 3],
                            [1, 3, 5]])

    column_index = 2  # Index of the column to sort by (column c)
    result = most_frequent_first(input_array, column_index)
    print(result)



if __name__ == "__main__":
    main()
