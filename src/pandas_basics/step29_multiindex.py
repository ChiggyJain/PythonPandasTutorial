import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step29_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

df.loc[1, "date"] = df.loc[0, "date"]
df.loc[1, "product_id"] = df.loc[0, "product_id"]

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nCreate a MultiIndex using set_index()")
df_multi = df.set_index(["date", "product_id"])
print(df_multi)

print("\nIndex Names:", df_multi.index.names)

print("\n--- Selecting using MultiIndex .loc ---")
print(df_multi.loc[ ( df["date"].iloc[0], df["product_id"].iloc[0] ) ])

print("\nPartial index selection (powerful feature)")
print("Selecting all products for a date")
print(df_multi.loc[ df["date"].iloc[0] ])

print("\n--- Reset MultiIndex back to columns ---")
df_reset = df_multi.reset_index()
print(df_reset)

print("\n--- Sorted MultiIndex ---")
print(df_multi.sort_index())

print("\n--- GroupBy with MultiIndex output ---")
grouped = df.groupby(["date", "product_id"])["quantity"].sum()
print(grouped)

print("\n--- Unstack (MultiIndex → Columns) ---")
unstacked = grouped.unstack()
print(unstacked)

print("\n--- Stack (Columns → MultiIndex Rows) ---")
stacked = unstacked.stack()
print(stacked)