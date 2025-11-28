
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step10_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- Full Data Frame ---")
print(df)

print("\nArithmetic Vectorized Operations (+, -, *, /)")
df["quantity_plus_5"] = df["quantity"] + 5
df["quantity_times_2"] = df["quantity"] * 2
df["price_minus_50"] = df["price"] - 50
df["price_div_2"] = df["price"] / 2
print(df[["quantity", "quantity_plus_5", "quantity_times_2", "price", "price_minus_50", "price_div_2"]])


print("\nComparison Operations (> , < , == , !=)")
df["qty_more_than_10"] = df["quantity"]>10
df["price_less_than_300"] = df["price"]<300
print(df[["quantity", "qty_more_than_10", "price", "price_less_than_300"]])


print("\nLogical Operations (&, |, ~)")
df["qty_gt_10_and_price_gt_500"] = ((df["quantity"]>10) & (df["price"]>500))
df["qty_gt_10_or_price_lt_300"] = ((df["quantity"]>10) | (df["price"]<300))
print(df[["quantity", "price", "qty_gt_10_and_price_gt_500", "qty_gt_10_or_price_lt_300"]])

print("\nVectorized string operations (.str)")
df["product_id_str"] = df["product_id"].astype(str)
df["product_id_starts_with_1"] = df["product_id_str"].str.startswith("1")
df["product_id_end_with_1"] = df["product_id_str"].str.endswith("1")
df["product_id_contains_1"] = df["product_id_str"].str.contains("1")
print(df[["product_id", "product_id_starts_with_1", "product_id_end_with_1", "product_id_contains_1"]])


print("\nVectorized Date Operations (dt)")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()
print(df[["date", "year", "month", "day", "day_name"]])