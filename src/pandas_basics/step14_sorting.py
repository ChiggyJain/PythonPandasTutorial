import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
csv_path = generate_sales_data("step14_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nsort_values() — Sort by one column (Ascending)")
print(df.sort_values(by="price", ascending=True))

print("\nsort_values() — Sort by one column (Descending)")
print(df.sort_values(by="price", ascending=False))

print("\nMulti-column sorting")
print(df.sort_values(by=["price", "quantity"], ascending=[True, False]))

print("\nSorting by date")
print(df.sort_values(by="date", ascending=False))

print("\nsort_index() — Sort rows by index")
print(df.sort_index(ascending=False))

print("\nSorting with inplace=True. Its always return None and modified data-frame")
df.sort_values(by="price", inplace=True)
print(df)