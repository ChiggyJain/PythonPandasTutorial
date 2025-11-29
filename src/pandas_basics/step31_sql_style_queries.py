import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 – Generate dataset
csv_path = generate_sales_data("step31_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\n--- SELECT * FROM TABLE ---")
print(df)

print("\n--- SELECT product_id, quantity FROM TABLE ---")
print(df[ ["product_id", "quantity"] ])

print("\n--- WHERE quantity > 10 ---")
print(df[ df["quantity"]>10 ])

print("\n--- WHERE price BETWEEN 300 AND 700 ---")
print(df[ (df["price"]>=300) & (df["price"]<=700)  ])

print("\n--- WHERE product_id IN (1001,1002) ---")
productId = df.loc[0:2, "product_id"].tolist()
# print(productId)
print(df[ df["product_id"].isin(productId)  ])

print("\n--- WHERE product_id LIKE '%5%' ---")
print(df[ df["product_id"].astype(str).str.contains("5")  ])

print("\n--- ORDER BY price DESC ---")
print(df.sort_values("price", ascending=False))

print("\n--- SELECT DISTINCT(product_id) ---")
print(df["product_id"].unique())

print("\n--- GROUP BY product_id SUM(quantity) ---")
print( df.groupby("product_id")["quantity"].sum())

print("\n--- LIMIT 5 ---")
print(df.head(5))

print("\n--- INNER JOIN product_id ---")
df2_path = generate_sales_data("step31_products.csv", rows=12)
df2 = pd.read_csv(df2_path, parse_dates=["date"])
inner_join = pd.merge(df, df2, on="product_id", how="inner")
print(inner_join)

print("\n--- HAVING SUM(quantity) > 20 ---")
print( df.groupby("product_id").filter(lambda g:g["quantity"].sum()>10) )

print("\n--- UPDATE quantity = quantity + 1 ---")
df["quantity"] = df["quantity"] + 1
print( df )












