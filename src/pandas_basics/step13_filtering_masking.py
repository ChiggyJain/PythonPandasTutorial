
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step13_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nSimple Boolean Mask (Boolean Value:True/False)")
boolCond = df["quantity"]>10
print(boolCond)

print("\nBetween Range → between(startValue, endValue)")
print(df[df["quantity"].between(1,3)])

print("\n isin(listValues) → Filter using list of values. Similar like IN operator of mysql")
print(df[df["quantity"].isin([1,5])])

print("\n--- ~(price < 300)")
print(df[~(df["price"]<300)])

print("\nComplex Multi-Condition Filtering")
print(df[ (df["quantity"]>10) & (df["price"]>10) & (df["date"]>'2024-01-05')  ])

print("\nComplex Multi-Condition Filtering")
print(df[ ((df["quantity"]>10) | (df["price"]>10)) & (df["date"]>'2024-01-05')  ])


df["product_str"] = df["product_id"].astype(str)
print("\n--- product_id contains '5' ---")
print(df[df["product_str"].str.contains("5")])

print("\nFilter using .query(): SQL like syntax")
print(df.query("quantity>10 and price<700").head(2))


























