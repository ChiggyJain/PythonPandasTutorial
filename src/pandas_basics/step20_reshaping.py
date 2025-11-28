
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step20_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

df_top = df.head(5)
df_bottom = df.tail(5)

print("\nVertical concat (rows stacked)")
print(pd.concat([df_top, df_bottom], axis=0))

print("\nHorizonatal concat (cols stacked. side by side columns)")
print(pd.concat([ df_top[["quantity"]], df_top[["price"]] ], axis=1))

print("\n--- Concat ignore_index=True ---")
concat_ignore_index = pd.concat([df_top, df_bottom], ignore_index=True)
print(concat_ignore_index)

print("\nConcat with keys (Hierarchical index)")
print(pd.concat({"TOP":df_top, "BOTTOM":df_bottom}))

df_small = df.head(3)[["product_id", "quantity", "price"]] #.set_index("product_id")
print(df_small)

print("\n--- STACK (columns -> rows) ---")
stacked = df_small.stack()
print(stacked)

print("\n--- UNSTACK (rows -> columns) ---")
print(stacked.unstack())

df_small2 = df.head(6).copy()
df_small2["day_name"] = df_small2["date"].dt.day_name()
print("\n")
print(df_small2)


print("\npivot()")
pivot_df = df_small2.pivot(index="product_id", columns="day_name", values="quantity")
print(pivot_df)

print("\pivot_table()")
print("\--- PIVOT TABLE (sum of qty per product_id per day) ---")
pivot_table_df = df_small2.pivot_table(index="product_id", columns="day_name", values="quantity", aggfunc="sum")
print(pivot_table_df)


print("\nmelt: unpivot")
print(df_small2.head(2))
print("\n")
melted = pd.melt(
    df_small2.head(2),
    id_vars=["product_id", "date"],
    value_vars=["quantity", "price"],
    var_name="metric",
    value_name="value"
)
print(melted)























