
import pandas as pd
import numpy as np
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step12_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nInject some missing values for practice (NO hardcoded data)")
df.loc[2, "price"] = None
df.loc[5, "quantity"] = None
df.loc[7, "date"] = None

print("\n--- DATA WITH MISSING VALUES ---")
print(df)

print("\nCheck missing values → isna()")
print(df.isna())

print("\nCount missing in each column: df.isna().sum()")
print(df.isna().sum())

print("\nCheck not-null values → notna()")
print(df.notna())

print("\nCount nont-value in each column: df.notna().sum()")
print(df.notna().sum())

print("\ndropna() → drop rows with missing values in any column of each row")
df_drop_rows = df.dropna()
print(df_drop_rows)

print("\nKeep rows where at least 'n' non-null values exist in overall (columsn) of each row")
df_thresh = df.dropna(thresh=4)
print(df_thresh)

print("\nfillna() → fill missing values")
df_fill_price_mean = df.copy()
df_fill_price_mean["price"] = df["price"].fillna(df["price"].mean())
print(df_fill_price_mean["price"])

print("\nfillna() → fill missing values")
df_fill_zero = df.copy()
df_fill_zero["quantity"] = df_fill_zero["quantity"].fillna(0)
print(df_fill_zero["quantity"])


print("\n--- fillna(method='ffill') date ---")
df_fill_date = df.copy()
df_fill_date["date"] = df_fill_date["date"].ffill()
print(df_fill_date["date"])

print("\nreplace() → replace values instead of NA")
df_replace = df.replace({"quantity" : {np.nan:99999.99}})
print(df_replace["quantity"])

print("\n--- interpolate() quantity working on integer/float data-types only. Return estimate value only ---")
print("x0=previous known value, x1=next known value, n=total missing points between them, k=which missing point we are filling (1,2,...n)")
df_interpolate = df.copy()
df_interpolate["quantity"] = df_interpolate["quantity"].interpolate()
print(df_interpolate["quantity"])



