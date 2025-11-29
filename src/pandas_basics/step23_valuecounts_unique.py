import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step23_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nunique() — Get all unique values/data in a column")
print(df["product_id"].unique())

print("\nnunique() — Count of unique values/data in a column")
print(df["product_id"].nunique())

print("\n--- value_counts() product_id frequency ---")
# df.loc[1, "product_id"] = df.loc[0, "product_id"]
print(df["product_id"].value_counts())

print("\n--- value_counts() sorted by frequency ASC ---")
# df.loc[1, "product_id"] = df.loc[0, "product_id"]
print(df["product_id"].value_counts(ascending=True))

print("\n--- value_counts(normalize=True) % distribution: countValue//totalRows ---")
df.loc[1, "product_id"] = df.loc[0, "product_id"]
print(df["product_id"].value_counts(normalize=True)*100)