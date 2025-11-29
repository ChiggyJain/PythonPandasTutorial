import pandas as pd
import numpy as np
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step32_sales.csv", rows=5000)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL MEMORY USAGE ---")
print(df.memory_usage(deep=True))

print("\n--- Memory Usage After convert_dtypes() Let pandas automatically optimize ---")
df_auto = df.convert_dtypes()
print(df_auto.memory_usage(deep=True))

print("\n--- Memory Usage After converting product_id to category ---")
df_cat = df.copy()
df_cat["product_id"] = df["product_id"].astype("category")
print(df_cat.memory_usage(deep=True))

print("\n--- Downcasting int64 → smaller int ---")
df_down_int = df.copy()
df_down_int["quantity"] = pd.to_numeric(df_down_int["quantity"], downcast="integer")
print(df_down_int.memory_usage(deep=True))

print("\n--- Downcasting float64 → smaller float ---")
df_down_float = df.copy()
df_down_float["price"] = pd.to_numeric(df_down_int["price"], downcast="float")
print(df_down_float.memory_usage(deep=True))