import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step22_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

# Inject duplicate rows for practice
print("\n--- DATA WITH DUPLICATES ---")
df.loc[2] = df.loc[1]
df.loc[3] = df.loc[1]
df.loc[7, "quantity"] = df.loc[4, "quantity"]
print(df)

print("\n--- detect duplicated() (True = duplicate) all rows ---")
print(df.duplicated())

print("\n--- Count of duplicate rows ---")
print(df.duplicated().sum())

print("\n--- drop_duplicates(): All duplicate rows removed and return non-duplicate-rows only ---")
df_non_duplicated_rows = df.drop_duplicates()
print(df_non_duplicated_rows)

print("\n--- drop_duplicates(subset=['product_id']). Means removed duplicate rows based on give column ---")
df_non_duplicated_rows = df.drop_duplicates(subset=["product_id"])
print(df_non_duplicated_rows)

print("\n--- keep='first' (default) [If any duplicate rows found keep first wala and removed others] ---")
print(df.drop_duplicates(keep="first"))

print("\n--- keep='last' [If any duplicate rows found then removed all previous wala and keep only last one] ---")
print(df.drop_duplicates(keep="last"))

print("\n--- keep=False (Removed all Duplicates rows) ---")
print(df.drop_duplicates(keep=False))

print("\n--- FILTER/Showing ONLY DUPLICATE ROWS ---")
only_duplicates = df[df.duplicated(keep=False)]
print(df)
print("\n")
print(only_duplicates)