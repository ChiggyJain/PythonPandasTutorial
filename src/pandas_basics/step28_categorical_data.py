import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step28_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\n--- Converted product_id to category data ---")
df["product_id_cat"] = df["product_id"].astype("category")
print(df)

print("\n--- List categories ---")
print(df["product_id_cat"].cat.categories)

print("\n--- After adding new category ---")
df["product_id_cat"] = df["product_id_cat"].cat.add_categories(["NEW-CAT1"])
print(df["product_id_cat"].cat.categories)

print("\n--- After removing unused categories ---")
df["product_id_cat"] = df["product_id_cat"].cat.remove_unused_categories()
print(df["product_id_cat"].cat.categories)

print("\n--- Renamed categories using lambda ---")
df["product_id_cat"] = df["product_id_cat"].cat.rename_categories(lambda x : f"ID-{x}")
print(df["product_id_cat"].cat.categories)

print("\n--- Memory usage comparison (bytes) and Compare memory usage (int vs category) ---")
print(df["product_id"].memory_usage(deep=True))
print(df["product_id_cat"].memory_usage(deep=True))