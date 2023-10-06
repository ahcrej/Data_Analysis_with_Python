#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values


def lengths():
    df = load()
    # Slices the sepal_lengths column into a new list
    sepal_lengths = df[:,0]

    # Slices the petal_lengtsh column into a new list
    petal_lengths = df[:,2]

    # Calculate the Pearson correlation coefficient and p-value
    correlation_coefficient, p_value = scipy.stats.pearsonr(
        sepal_lengths, petal_lengths)

    return correlation_coefficient


def correlations():
    # Set 'rowvar=False' as each column represents a variable, while the rows contain observations
    correlation_arr = np.corrcoef(load(), rowvar=False)
    return correlation_arr


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
