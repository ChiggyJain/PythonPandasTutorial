import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step24_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

df["product_str"] = df["product_id"].astype(str)

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nstr.lower()")
df["product_str_lower"] = df["product_str"].str.lower()
print(df)

print("\nstr.upper()")
df["product_str_upper"] = df["product_str"].str.upper()
print(df)

print("\n--- str.contains('5') ---")
df["product_str_contain_5"] = df["product_str"].str.contains("5")
print(df)

print("\nstr.startswith()")
df["product_str_startswith_1"] = df["product_str"].str.startswith("1")
print(df)

print("\nstr.endwendswithith()")
df["product_str_endswith_1"] = df["product_str"].str.endswith("1")
print(df)

print("\n--- str.replace('1', 'X') ---")
df["product_str_replace(1, 'X')"] = df["product_str"].str.replace("1", "X")
print(df)

print("\n--- str.len() ---")
df["product_str_len"] = df["product_str"].str.len()
print(df)

print("\n--- str.extract() digits ---")
df["product_str_digits_only"] = df["product_str_replace(1, 'X')"].str.extract(r"(\d+)", expand=True)
print(df)
