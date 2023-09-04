import pandas as pd

# Read the CSV data
data = pd.read_csv('wine-reviews-exercise-FariH004/data/winemag-data-130k-v2.csv.zip')

# Group data by country and calculate summary statistics
summary = data.groupby('country').agg({
    'points': ['count', 'mean']
}).reset_index().round(1)

# Rename columns for clarity
summary.columns = ['country', 'count', 'points']

# Save the summary data to a new CSV file
summary.to_csv('wine-reviews-exercise-FariH004/data/reviews-per-country.csv', index=False)







