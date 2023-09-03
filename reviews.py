import pandas as pd

# Read the CSV data
data = pd.read_csv("data/reviews-per-country.csv")

# Group data by country and calculate summary statistics
summary = data.groupby('country').agg({
    'points': ['count', 'mean']
}).reset_index()

# Rename columns for clarity
summary.columns = ['country', 'num_reviews', 'avg_points']

# Save the summary data to a new CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data saved to 'data/reviews-per-country.csv'")





