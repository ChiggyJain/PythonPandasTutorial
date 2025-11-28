import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step15_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATAFRAME ---")
print(df)

print("\nrename() — Rename columns")
print(df.rename(columns={"product_id" : "product_code", "quantity":"qty"}))

print("\nrename_axis(indexName) — Rename index of row-label only")
print(df.rename_axis("RowIndex"))

print("\nrename_axis(indexName, axis=1) — Rename index of column-label only")
print(df.rename_axis("ColIndex", axis=1))

print("\nset_index() — Move a column to index")
df_indexed = df.set_index("product_id")
print(df_indexed)

print("\nreset_index() — Move index back to a column. Original form")
df_reset = df_indexed.reset_index()
print(df_reset)

print("\n--- reset_index(drop=True) ---")
df_reset_drop = df_indexed.reset_index(drop=True)
print(df_reset_drop)

print("\nreindex() — Reorder rows or fill missing rows")
print(df.reindex(list(range(0,15)), fill_value="Missing"))