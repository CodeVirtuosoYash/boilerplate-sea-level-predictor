import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data from 1880 onwards)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Predicting from 1880 to 2050
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Best Fit Line (All data)', color='blue')

    # Create second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = range(2000, 2051)  # Predicting from 2000 to 2050
    plt.plot(years_recent_extended, [slope_recent * year + intercept_recent for year in years_recent_extended], label='Best Fit Line (2000-Current)', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Show legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
