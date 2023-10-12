#!/usr/bin/env python3
import pandas as pd
from sklearn.linear_model import LinearRegression


def split_date(df):
    weekdays = {"ma": "Mon", "ti": "Tue", "ke": "Wed",
                "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
              "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
              "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    df_split = df["Päivämäärä"]
    df_split = df_split.dropna(how='all')
    df_split = df_split.str.split(expand=True)
    df_split.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df_split["Hour"] = df_split["Hour"].str.split(":").str[0]
    df_split["Weekday"] = df_split["Weekday"].map(weekdays)
    df_split["Month"] = df_split["Month"].map(months)

    df_split = df_split.astype({"Weekday": object, "Day": int, "Year": int, "Hour": int})

    return df_split


def split_date_continues():
    # Read data from .csv
    df1 = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Declare df2 using the 'split_date(df)' function
    df2 = split_date(df1)

    # Drop unnecessary rows and columns
    df1 = df1.dropna(how="all", axis=1).dropna(how="all", axis=0).drop("Päivämäärä", axis=1)

    # Join the dataframes side by side by stating 'axis=1'
    joined_df = pd.concat([df2, df1], axis=1)

    return joined_df


def cycling_weather_continues(station):
    # Read weather data from a CSV file into a DataFrame.
    df_weather = pd.read_csv("src/kumpula-weather-2017.csv")

    # Process cycling data, including filtering for the year 2017 and grouping by month and day.
    df_cycling = split_date_continues()
    mask = df_cycling["Year"] == 2017
    df_cycling = df_cycling[mask].groupby(['Month', 'Day']).sum()

    # Merge weather and cycling data on day and month, remove unnecessary columns, and rename columns.
    df = pd.merge(df_weather, df_cycling, right_on=["Day", "Month"], left_on=["d", "m"]).drop(
        ["Time", "Time zone", "Year_y"], axis=1).rename(columns={"Year_x": "Year"})
    
    # Fill missing values in the merged DataFrame using forward fill (ffill).
    df = df.fillna(method='ffill')

    # Select predictor variables (weather data) and target variable (cycling data for the specified station).
    x = df.loc[:, "Precipitation amount (mm)": "Air temperature (degC)"]
    y = df.loc[:, station]

    # Train a linear regression model with the selected data.
    model = LinearRegression(fit_intercept=True).fit(x, y)

    # Return the model coefficients and the R-squared (coefficient of determination) score.
    return model.coef_, model.score(x, y)


def main():
    station = "Ratapihantie"
    coefficients, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coefficients[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coefficients[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coefficients[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
