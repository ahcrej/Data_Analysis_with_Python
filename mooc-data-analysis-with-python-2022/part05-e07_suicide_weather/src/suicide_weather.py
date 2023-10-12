#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    # Read the suicide data from a CSV file into a Pandas DataFrame.
    df = pd.read_csv("src/who_suicide_statistics.csv")

    # Remove unecessary columns from the DataFrame.
    df = df.drop(["year", "sex", "age"], axis=1)

    # Add and calculate the 'suicide_ratio' column by dividing the 'suicides_no' by the 'population' for each row.
    df["suicide_ratio"] = df["suicides_no"] / df["population"]

    # Group the data in 'df' by the 'country' column.
    results = df.groupby("country")

    # Calculate the mean of the 'suicide_ratio' for each country.
    return results["suicide_ratio"].mean()


def suicide_weather():
    # Call the 'suicide_fractions' function to get a DataFrame with suicide data.
    df_mean = suicide_fractions()

    # Read a HTML table from a web page, setting 'Country' as the index.
    df_weather = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html", index_col="Country")

    # Select the first DataFrame from the list of DataFrames read from the web page.
    df_weather = df_weather[0]

    # Convert a specific column to float by replacing unicode minus sign (−) with a regular minus sign (-).
    df_weather.iloc[:, 0] = df_weather.iloc[:, 0].str.replace("\u2212", "-").astype(float)
    
    # # '.apply' is generally slower than above as it uses elementwise operations rather than vectorized operations.
    # df_weather.iloc[:, 0] = df_weather.iloc[:, 0].apply(
    #     lambda x: float(x.replace("\u2212", "-")))

    # Merge the suicide DataFrame and the weather DataFrame using the common index 'Country'.
    df_common = pd.merge(df_weather, df_mean,
                         left_index=True, right_index=True)

    suicide_rows = df_mean.shape[0]
    temperature_rows = df_weather.shape[0]
    common_rows = df_common.shape[0]
    correlation = df_common.corr(method='spearman').iloc[0][1]
    #correlation = df_weather.corrwith(df_mean, method="spearman", axis=0)[0]

    return (suicide_rows, temperature_rows, common_rows, correlation)


def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")


if __name__ == "__main__":
    main()
