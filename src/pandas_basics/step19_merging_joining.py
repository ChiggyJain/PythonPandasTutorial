
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
sales_path = generate_sales_data("step19_sales.csv", rows=12)
products_path = generate_sales_data("step19_products.csv", rows=12)

df_sales = pd.read_csv(sales_path, parse_dates=["date"])
df_products = pd.read_csv(products_path, parse_dates=["date"])

# Add additional product details (not from generator)
df_products["product_name"] = ["Item_" + str(i) for i in range(len(df_products))]
df_products["category"] = ["Category_A" if i % 2 == 0 else "Category_B" for i in range(len(df_products))]

print("\n--- SALES DATA ---")
print(df_sales)

print("\n--- PRODUCTS DATA ---")
print(df_products)

print("\nINNER/FULL JOIN (Most used). Only matching rows based on given columns")
inner_join = pd.merge(df_sales, df_products, on="product_id", how="inner")
print(inner_join)

print("\nLEFT JOIN (Most used)")
df_products.loc[0,"product_id"] = df_sales["product_id"][0]
df_products.loc[1,"product_id"] = df_sales["product_id"][0]
left_join = pd.merge(df_sales, df_products, on="product_id", how="left")
print(left_join)

print("\RIGHT JOIN (Most used)")
df_products.loc[0,"product_id"] = df_sales["product_id"][0]
df_products.loc[1,"product_id"] = df_sales["product_id"][0]
right_join = pd.merge(df_sales, df_products, on="product_id", how="right")
print(right_join)

print("\nFULL OUTER JOIN (Most used)")
full_outer_join = pd.merge(df_sales, df_products, on="product_id", how="outer")
print(full_outer_join)