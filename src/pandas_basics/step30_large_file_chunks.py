import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate a bigger dataset (simulate large file)
csv_path = generate_sales_data("step30_sales.csv", rows=10000)

print("\nRead CSV in chunks of 1000 rows of total-rows:10000. Show total quantity")
chunk_iter = pd.read_csv(csv_path, chunksize=1000)
total_quantity = 0
chunk_count = 0
for chunk in chunk_iter:
    chunk_count+= 1
    total_quantity+= chunk["quantity"].sum()
    print(f"Processed chunk: {chunk_count}, Rows: {len(chunk)}")
print(f"Total quantity from all chunks: {total_quantity}")


print("\nRead CSV in chunks of 1000 rows of total-rows:10000. Combine specific rows from all chunks whose price>500")
chunk_iter = pd.read_csv(csv_path, chunksize=1000)
filteredRows = []
for chunk in chunk_iter:
    filteredRows.append(chunk[chunk["price"]>500])
df_filtered = pd.concat(filteredRows)    
print(df_filtered.head(5))

print("\nCompute groupby using chunks")
chunk_iter = pd.read_csv(csv_path, chunksize=1000)
productIdWiseTotQuantity = {}
for chunk in chunk_iter:
    result = chunk.groupby("product_id")["quantity"].sum()
    for productId, totQuantity in result.items():
        productIdWiseTotQuantity[productId] = productIdWiseTotQuantity.get(productId, 0) + totQuantity
print(f"productIdWiseTotQuantity: {productIdWiseTotQuantity}")