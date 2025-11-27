import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data (not hardcoded)
csv_path = generate_sales_data("step6_sales.csv", rows=20)

df = pd.read_csv(csv_path, parse_dates=["date"])
print("\n--- Original Data ---")
print(df.head())


# Write CSV (Basic) without index-column
output_csv = "data/output_basic.csv"
df.to_csv(output_csv, index=False)
print("\nSaved:", output_csv)

# Write CSV with index-column
output_index_csv = "data/output_with_index.csv"
df.to_csv(output_index_csv, index=True)
print("\nSaved:", output_index_csv)

# Append mode (mode='a')
output_append_csv = "data/output_append.csv"
df.head(5).to_csv(output_append_csv, index=False)
df.tail(5).to_csv(output_append_csv, mode='a', header=False, index=False)
print("\nSaved (append mode):", output_append_csv)

# Write compressed file (gzip)
output_gzip = "data/output_compressed.csv.gz"
df.to_csv(output_gzip, index=False, compression="gzip")
print("\nSaved:", output_gzip)

# Write JSON file
output_json = "data/output.json"
df.head(2).to_json(output_json, orient="records", lines=True)
print("\nSaved:", output_json)

# Write Excel file
output_excel = "data/output.xlsx"
df.to_excel(output_excel, index=False, sheet_name="SalesData")
print("\nSaved:", output_excel)