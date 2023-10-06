#!/usr/bin/env python3

import pandas as pd

def cities():
    data = {"Helsinki": {"Population": 643272, "Total area": 715.48},
            "Espoo": {"Population": 279044, "Total area": 528.03},
            "Tampere": {"Population": 231853, "Total area": 689.59},
            "Vantaa": {"Population": 223027, "Total area": 240.35},
            "Oulu": {"Population": 201810, "Total area": 3817.52}}
    return pd.DataFrame(data).T
    
    # return pd.DataFrame([{"Population": 643272, "Total area": 715.48},
    #                      {"Population": 279044, "Total area": 528.03},
    #                      {"Population": 231853, "Total area": 689.59},
    #                      {"Population": 223027, "Total area": 240.35},
    #                      {"Population": 201810, "Total area": 3817.52}],
    #                      index=["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])
    
def main():
    df = cities()
    print(df["Population"][0])
    
if __name__ == "__main__":
    main()
