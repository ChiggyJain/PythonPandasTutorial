import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step21_sales.csv", rows=15)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df.head())

# ------------------------------------------------------------
# 1. map() — for Series only
# ------------------------------------------------------------
discount_map = {
    1001: "LowRange",
    1002: "MidRange",
    1003: "HighRange"
}

df.loc[0,"product_id"] = 1001
df["product_category"] = df["product_id"].map(discount_map)

print("\n--- map() applied on product_id ---")
print(df[["product_id", "product_category"]])

# ------------------------------------------------------------
# 2. apply() — can be used on Series OR DataFrame
# ------------------------------------------------------------
# Example: Row-wise discount rule
def calculate_discount(row):
    if row["price"] > 500:
        return "High Discount"
    elif row["price"] > 300:
        return "Medium Discount"
    else:
        return "Low Discount"

df["discount_label"] = df.apply(calculate_discount, axis=1)

print("\n--- apply() row-wise business logic ---")
print(df[["price", "discount_label"]].head())

# Column-wise apply
df["price_double"] = df["price"].apply(lambda x: x * 2)

print("\n--- apply() column-wise multiply price by 2 ---")
print(df[["price", "price_double"]].head())

# ------------------------------------------------------------
# 3. applymap() — applies to ENTIRE DataFrame
# ------------------------------------------------------------
df_small = df[["quantity", "price"]].head()

df_applymap = df_small.applymap(lambda v: v + 1)

print("\n--- applymap() adds +1 to entire DataFrame ---")
print(df_applymap)
