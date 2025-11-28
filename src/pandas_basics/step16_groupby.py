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

print("\ntransform() — Returns series same length as original")
print("--- transform(): quantity / total_quantity_per_product_id ---")
df["qty_percent"] = df["quantity"] / df.groupby("product_id")["quantity"].transform("sum")
print(df)

print("\napply() — Custom function on each group")
def range_of_price(group):
    return group["price"].max() - group["price"].min()
print(df.groupby("product_id").apply(range_of_price))

print("\nFiltering groups using filter()")
print("Keep only those product_ids whose total quantity > 10")
print(df.groupby("product_id").filter(lambda g:g["quantity"].sum()>10))