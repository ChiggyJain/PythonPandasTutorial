import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step26_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\n--- Filter price > 500 AND sort by price DESC ---")
print(df[df["price"]>500].sort_values("price", ascending=False))

print("\n--- Filter qty>=10 + sort by date + select columns ---")
print(df[df["quantity"]>10].sort_values("date", ascending=True)[["product_id", "quantity", "date"]])

print("\n--- quantity > 10 AND price < 700 + multi-sort ---")
print(df[ (df["quantity"]>10) & (df["price"]<700) ].sort_values(["quantity", "price"], ascending=[False, True])[["product_id", "quantity", "date"]])

print("\n--- TOP 5 highest priced rows ---")
print(df.sort_values("price", ascending=False).head(5))

print("\n--- Lowest 3 quantity rows ---")
print(df.sort_values("quantity", ascending=False).tail(3))

print("\n--- Unique products sorted by frequency (descending) ---")
print(df["price"].value_counts().sort_values(ascending=False))