
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Generate real data
csv_path = generate_sales_data("step7_sales.csv", rows=20)

df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- FULL DATAFRAME ---")
print(df)

# ----------------------------------------------------
# 1. head(): Show top rows
# ----------------------------------------------------
print("\n--- df.head(5) ---")
print(df.head(5))

# ----------------------------------------------------
# 2. tail(): Last rows
# ----------------------------------------------------
print("\n--- df.tail(3) ---")
print(df.tail(3))

# ----------------------------------------------------
# 3. shape: (rows, columns)
# ----------------------------------------------------
print("\n--- df.shape ---")
print(df.shape)

# ----------------------------------------------------
# 4. size: total cells
# ----------------------------------------------------
print("\n--- df.size ---")
print(df.size)

# ----------------------------------------------------
# 5. columns: list of column names
# ----------------------------------------------------
print("\n--- df.columns ---")
print(df.columns)

# ----------------------------------------------------
# 6. index: row index
# ----------------------------------------------------
print("\n--- df.index ---")
print(df.index)

# ----------------------------------------------------
# 7. dtypes: data types of each column
# ----------------------------------------------------
print("\n--- df.dtypes ---")
print(df.dtypes)

# ----------------------------------------------------
# 8. info(): Full summary
# ----------------------------------------------------
print("\n--- df.info() ---")
print(df.info())

# ----------------------------------------------------
# 9. describe(): Numeric summary statistics
# ----------------------------------------------------
print("\n--- df.describe() ---")
print(df.describe())

# ----------------------------------------------------
# 10. memory_usage()
# ----------------------------------------------------
print("\n--- df.memory_usage() ---")
print(df.memory_usage())

# ----------------------------------------------------
# 11. Selecting a single column
# ----------------------------------------------------
print("\n--- df['quantity'] ---")
print(df["quantity"].head())

# ----------------------------------------------------
# 12. Selecting multiple columns
# ----------------------------------------------------
print("\n--- df[['date', 'price']] ---")
print(df[["date", "price"]].head())

# ----------------------------------------------------
# 13. Selecting rows using .loc (label-based)
# ----------------------------------------------------
print("\n--- df.loc[0:5, ['date', 'price']] ---")
print(df.loc[0:5, ["date", "price"]])

# ----------------------------------------------------
# 14. Selecting rows using .iloc (position-based)
# ----------------------------------------------------
print("\n--- df.iloc[0:5, 0:2] ---")
print(df.iloc[0:5, 0:2])
