import pandas as pd

# Load Kaggle dataset
kaggle_data = pd.read_csv(r"C:\Users\Rawaa\Downloads\DEV _ March Madness.csv")

# Load ESPN dataset (we will fix headers later)
espn_data = pd.read_csv(r"C:\Users\Rawaa\Downloads\espn-mens-college-basketball-bpi.csv")

# Print first few rows
print("Kaggle Data Preview:")
print(kaggle_data.head())

print("\nESPN BPI Data Preview:")
print(espn_data.head())
