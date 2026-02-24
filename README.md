# Football Player Data Analysis

This Python project performs data preprocessing, visualization, and statistical analysis on football player performance data. It uses `pandas` for data manipulation, `numpy` for numerical operations, `matplotlib` and `seaborn` for visualization.

## Features

- **Data Cleaning:** Handles missing values, duplicates, and ensures correct data types.
- **Visualizations:**
  - Scatter plot of Assists vs Goals.
  - Bar plot showing average goals by competition.
  - Correlation heatmap of numeric stats.
  - Histogram of player goals distribution.
- **Statistical Analysis:** Computes mean, standard deviation, skewness, and excess kurtosis for numeric attributes.
- **Outputs:** Saves cleaned dataset as `cleaned_football_data.csv` and plots as PNG files.

## Usage

1. Place the dataset CSV file `players_data-2024_2025.csv` in the same directory.
2. Run the script:
   `python football_analysis.py`
3. View generated plots and cleaned data.
   
### Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
