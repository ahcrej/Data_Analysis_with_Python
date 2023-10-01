#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    # rows = []
    # num_rows, num_cols = a.shape

    # for i in range(num_rows):
    #     row = a[i,:]
    #     rows.append(row.reshape(1, num_cols))

    # return rows

    return np.split(a, a.shape[0], axis = 0)

def get_column_vectors(a):
    # cols = []
    # num_rows, num_cols = a.shape

    # for i in range(num_cols):
    #     col = a[:,i]
    #     cols.append(col.reshape(num_rows, 1))

    # return cols

    return np.split(a, a.shape[1], axis = 1)


def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
