import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
csv_path = generate_sales_data("step16_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nBasic GroupBy → sum : Total-Quantity per product-id")
print(df.groupby("product_id")["quantity"].sum())

print("\nGroupBy → multiple aggregations on single column")
print("Price statistics per product_id")
print(df.groupby("product_id")["price"].agg(["min", "max", "mean", "std"]))

print("\nGroupBy on multiple columns")
print(df.groupby(["product_id", "date"])["quantity"].sum())

print("\nNamed aggregations (clean columns)")
print(df.groupby("product_id").agg(
    total_quantity=("quantity", "sum"),
    avg_quantity=("quantity", "mean"),
    min_quantity=("quantity", "min"),
    max_quantity=("quantity", "max")
))