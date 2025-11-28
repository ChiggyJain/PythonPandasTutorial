import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step18_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

df = df.sort_values("date")  # sorting is important for rolling windows

print("\n--- ORIGINAL SORTED DATA ---")
print(df)

print("\nRolling window (size=3) — rolling mean of quantity. Formula: (curRowColValue+prevRowCol1Value+prevRowCol2Value)")
df["qty_rolling_mean_3"] = df["quantity"].rolling(window=3).mean()
print(df)

print("\nRolling window (size=3) — rolling sum of quantity")
df["qty_rolling_sum_3"] = df["quantity"].rolling(window=3).sum()
print(df)

print("\nRolling window (size=3) — rolling min of quantity")
df["qty_rolling_min_3"] = df["quantity"].rolling(window=3).min()
print(df)

print("\nRolling window (size=3) — rolling max of quantity")
df["qty_rolling_max_3"] = df["quantity"].rolling(window=3).max()
print(df)

print("\nRolling window (size=3, center=True) — rolling mean of quantity. Formula: (curRowColValue+prevRowCol1Value+nextRowCol1Value)")
df["qty_center_mean"] = df["quantity"].rolling(window=3, center=True).mean()
print(df)

print("\nExpanding Window — cumulative growing window. Formula: fromFirstRowColIndxVal to curRowColIndVal at each row-level")
df["qty_expanding_mean"] = df["quantity"].expanding().mean()
print(df)

print("\nCumulative Functions. Example running total sales etc.")
df["qty_cumsum"] = df["quantity"].cumsum()
print(df)

print("\nTime-based Rolling Window (important)")
df = df.set_index("date")
df["price_roll_mean_7D"] = df["price"].rolling("7D").mean()
print(df)