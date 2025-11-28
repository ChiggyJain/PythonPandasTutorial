import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
csv_path = generate_sales_data("step17_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nColumn-level aggregations")
print(f"Total-Quantity-Sum: {df["quantity"].sum()}")
print(f"Min-Quantity: {df["quantity"].min()}")
print(f"Max-Quantity: {df["quantity"].max()}")
print(f"Std-Quantity: {df["quantity"].std()}")
print(f"Mean-Quantity: {df["quantity"].mean()}")
print(f"Var-Quantity: {df["quantity"].var()}")

print("\n--- price 25th & 75th percentile ---")
print("25th:", df["price"].quantile(0.25))
print("75th:", df["price"].quantile(0.75))

print("\nidxmin() & idxmax() → row index of min/max values")
minPriceRowIndx = df["price"].idxmin()
print(df.loc[minPriceRowIndx])

print("\nidxmin() & idxmax() → row index of min/max values")
maxPriceRowIndx = df["price"].idxmax()
print(df.loc[maxPriceRowIndx])

print("\n--- df.sum(axis=0) (single/multiple column-wise sum) ---")
print(df[["quantity", "price", "product_id"]].sum())

print("\nRow-wise aggregation (axis=1) of single/multiple columns")
df["row_total"] = df[["quantity", "price"]].sum(axis=1)
print(df)

print("\nUsing apply() for custom row-level aggregations")
df["qty_price_difference"] = df.apply(lambda r: r["price"] - r["quantity"], axis=1)
print(df)