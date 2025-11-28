
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Generate real data
csv_path = generate_sales_data("step7_sales.csv", rows=10)

df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- FULL DATAFRAME ---")
print(df)

# ----------------------------------------------------
# 1. head(): Show top rows
# ----------------------------------------------------
print("\n--- df.head(5) First 5 rows ---")
print(df.head(5))

# ----------------------------------------------------
# 2. tail(): Last rows
# ----------------------------------------------------
print("\n--- df.tail(3) Last 3 rows ---")
print(df.tail(3))

# ----------------------------------------------------
# 3. shape: (rows, columns)
# ----------------------------------------------------
print("\n--- df.shape and return (totalRows, totalCols)---")
print(df.shape)

# ----------------------------------------------------
# 4. size: total cells
# ----------------------------------------------------
print("\n--- df.size and return (totalRows * totalCols) ---")
print(df.size)

# ----------------------------------------------------
# 5. columns: list of column names
# ----------------------------------------------------
print("\n--- df.columns and return all column-names in list ---")
print(df.columns)

# ----------------------------------------------------
# 6. index: row index
# ----------------------------------------------------
print("\n--- df.index and return rows-index-range(startIndex, endIndex, stepRange) ---")
print(df.index)

# ----------------------------------------------------
# 7. dtypes: data types of each column
# ----------------------------------------------------
print("\n--- df.dtypes and return data-types of each columns ---")
print(df.dtypes)

# ----------------------------------------------------
# 8. info(): Full summary
# ----------------------------------------------------
print("\n--- df.info() and return (IndexRange, Total-Columns-Count, Column-Names, Data-Types of Each Column, Total-Memory-Consumed in bytes by Data-Frame) ---")
print(df.info())

# ----------------------------------------------------
# 9. describe(): Numeric summary statistics
# ----------------------------------------------------
print("\n--- df.describe() ---")
print("Count: Total-Rows of Each Column-Level")
print("Mean: Average value of each total-column-data")
print("Min: Minimum value from of each total-column-data")
print("Max: Maximum value from of each total-column-data")
print("STD: sqrt( Σ(x-mean)²/(n-1))")
print("25%: minValue + 0.25 * (maxVal - minValue)")
print("50%: minValue + 0.50 * (maxVal - minValue)")
print("75%: minValue + 0.75 * (maxVal - minValue)")
print(df.describe())

# ----------------------------------------------------
# 10. memory_usage()
# ----------------------------------------------------
print("\n--- df.memory_usage() and show how much ram memory is used data-frame for each-column + indexes etc in bytes ---")
print(df.memory_usage())

# ----------------------------------------------------
# 11. Selecting a single column
# ----------------------------------------------------
print("\n--- df['quantity'] and showing one-column from data-frame ---")
print(df["quantity"].head())

# ----------------------------------------------------
# 12. Selecting multiple columns
# ----------------------------------------------------
print("\n--- df[['date', 'price']] and showing multiple-column from data-frame ---")
print(df[["date", "price"]].head())

# ----------------------------------------------------
# 13. Selecting rows using .loc (label-based)
# df.loc[rowStartIndx : rowEndIndx, ['RespectiveColName1', 'RespectiveColName2', 'etc']]
# ----------------------------------------------------
print("\n--- df.loc[rowStartIndx : rowEndIndx, ['RespectiveColName1', 'RespectiveColName2', 'etc']] ---")
print(df.loc[0:2, ["date", "product_id"]])

# ----------------------------------------------------
# 14. Selecting rows using .iloc (position-based)
# ----------------------------------------------------
print("\n--- df.loc[rowStartIndx : rowEndIndx, colStartIndx : colEndIndx] ---")
print(df.iloc[0:2, 0:10])
