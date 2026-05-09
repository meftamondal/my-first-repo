import pandas as pd

# Read CSV
df = pd.read_csv('g:/GableGrid/data.csv')

# Total customers
print("=" * 40)
print("DATASET INFO")
print("=" * 40)
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Column names:", list(df.columns))

# Show first 5 rows
print("\n" + "=" * 40)
print("FIRST 5 ROWS")
print("=" * 40)
print(df.head())

# Basic statistics
print("\n" + "=" * 40)
print("BASIC STATISTICS")
print("=" * 40)
print(df.describe())