import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os


def preprocessing(df):
    print(
        "Dataset loaded successfully!\n"
    )
    print("Preview:")
    print(df.head())
    print("\nColumns in dataset:")
    print(df.columns.tolist())

    # Filter relevant columns to focus on
    relevant_columns = [
        "Player", "Age", "Pos", "Squad", "Comp", "Nation", "Gls", "Ast", "Min"
    ]
    
    # Create a copy of the dataframe for safe manipulation
    df = df[relevant_columns].copy()

    # Drop rows with NaN values in the relevant columns
    df.dropna(subset=relevant_columns, inplace=True)
    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Ensure correct data types for numerical columns
    df.loc[:, "Gls"] = pd.to_numeric(df["Gls"], errors="coerce")
    df.loc[:, "Ast"] = pd.to_numeric(df["Ast"], errors="coerce")
    df.loc[:, "Age"] = pd.to_numeric(df["Age"], errors="coerce")

    print(f"\nAfter cleaning, dataset has {len(df)} rows and {len(df.columns)} columns.")
    print("\nBasic statistical summary:")
    print(df.describe())
    return df


def plot_relational_plot(df):
    if {"Gls", "Ast"}.issubset(df.columns):
        sns.set(style="whitegrid")
        sns.relplot(
            x="Ast", y="Gls", kind="scatter", data=df
        )
        plt.title("Relationship between Assists and Goals")
        plt.xlabel("Assists")
        plt.ylabel("Goals")
        plt.tight_layout()
        plt.savefig("relational_plot.png")
        plt.show()


def plot_categorical_plot(df):
    if {"Comp", "Gls"}.issubset(df.columns):
        plt.figure(figsize=(8, 5))
        sns.barplot(
            x="Comp", y="Gls", data=df, estimator=np.mean
        )
        plt.title("Average Goals by Competition")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("categorical_plot.png")
        plt.show()


def plot_statistical_plot(df):
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            df[num_cols].corr(), annot=True, cmap="coolwarm"
        )
        plt.title("Correlation Heatmap of Numeric Stats")
        plt.tight_layout()
        plt.savefig("statistical_plot.png")
        plt.show()

    if "Gls" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(
            df["Gls"], bins=20, kde=True, color="green"
        )
        plt.title("Distribution of Player Goals")
        plt.xlabel("Goals Scored")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = df[col].skew()
    excess_kurtosis = df[col].kurt()
    return mean, stddev, skew, excess_kurtosis


def writing(moments, col):
    print(f'\nFor the attribute "{col}":')
    print(
        f"Mean = {moments[0]:.2f}, "
        f"Standard Deviation = {moments[1]:.2f}, "
        f"Skewness = {moments[2]:.2f}, and "
        f"Excess Kurtosis = {moments[3]:.2f}."
    )

    if moments[2] > 0.5:
        skewness_type = "right-skewed"
    elif moments[2] < -0.5:
        skewness_type = "left-skewed"
    else:
        skewness_type = "approximately symmetric"

    if moments[3] > 0:
        kurtosis_type = "leptokurtic (heavy-tailed)"
    elif moments[3] < 0:
        kurtosis_type = "platykurtic (light-tailed)"
    else:
        kurtosis_type = "mesokurtic (normal-like)"

    print(f"The data is {skewness_type} and {kurtosis_type}.")


def main():
    # Default file path (for non-interactive environments)
    file_path = "players_data-2024_2025.csv"

    if not os.path.exists(file_path):
        print(
            f"Error: The file '{file_path}' does not exist in the "
            "current directory."
        )
        print("Please make sure the CSV file is present and rerun the script.")
        return

    df = pd.read_csv(file_path)
    df = preprocessing(df)

    if "Gls" in df.columns:
        col = "Gls"
    else:
        col = df.select_dtypes(include=[np.number]).columns[0]

    plot_relational_plot(df)
    plot_categorical_plot(df)
    plot_statistical_plot(df)

    moments = statistical_analysis(df, col)
    writing(moments, col)

    df.to_csv("cleaned_football_data.csv", index=False)
    print("\nCleaned data saved as 'cleaned_football_data.csv'.")


if __name__ == "__main__":
    main()
