import pandas as pd
import numpy as np
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate large dataset
csv_path = generate_sales_data("step33_sales.csv", rows=20000)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df.head())

print("\n--- apply() tag example (slow) ---")
def price_tag(price):
    if price>500:
        return "Costly"
    else:
        return "Inbduget"
df["price_tag_apply"] = df["price"].apply(price_tag)
print(df.head(10))

print("\n--- Vectorized np.where() (fast) ---")
df["tag_where"] = np.where(
    df["price"]>700, "Expensive",
    np.where(
        df["price"]>400, "MidRange", "Cheap"
    )
)
print(df.head(10))

print("\n--- np.select() Multi-condition ---")
conditions = [
    df["price"]>700,
    df["price"]>400
]
choices = ["Expensive", "MidRange"]
df["tag_select"] = np.select(conditions, choices, default="Cheap")
print(df)

print("\n--- map() instead of apply() ---")
productCtgryMapping = {
    1001 : "Low1", 1002 : "Low2", 1003 : "Low3"
}
df.loc[0, "product_id"] = 1001
df["discount_map"] = df["product_id"].map(productCtgryMapping)
print(df.head(10))

print("\n--- Multiprocessing parallel apply ---")
from multiprocessing import Pool, cpu_count
print(f"Total-Core-Cpu: {cpu_count()}")
def parallel_apply(colSeriesDataList, funcName, cntOfBatches=4):
    col_series_data_list_split = np.array_split(colSeriesDataList, cntOfBatches)
    pool = Pool(processes=4)
    result = pool.map(funcName, col_series_data_list_split)
    pool.close()
    pool.join()
    return pd.concat(result)
def tag_chunk(colSeriesDataList):
    return colSeriesDataList.apply(price_tag)

df["price_tag_apply_parallel"] = parallel_apply(df["price"], tag_chunk, 4)
print(df)















