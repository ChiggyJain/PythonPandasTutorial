
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
csv_path = generate_sales_data("step9_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- FULL DATAFRAME ---")
print(df)


print("\n--- df.loc[rowStartIndx : rowEndIndx, ['RespectiveColName1', 'RespectiveColName2', 'etc']] and labelBase ---")
print(df.loc[0:2, ["date", "quantity"]])

print("\n--- df.loc[rowStartIndx : rowEndIndx, colStartIndx : colEndIndx] and integer positionBase ---")
print(df.iloc[0:5, 0:2])

print("\n--- quantity > 10. Doing filtering part means extracting rows based on some conditions ---")
print(df)
print(df[df["quantity"] > 10])

print("\n--- quantity > 10 & price > 500. Doing filtering part means extracting rows based on some conditions ---")
print(df)
print(df[(df["quantity"]>10) & (df["price"]>500)])

print("\n--- quantity > 10 | price > 500. Doing filtering part means extracting rows based on some conditions ---")
print(df)
print(df[(df["quantity"]>10) | (df["price"]>500)])


print("\n--- ~(quantity > 10). Doing filtering part means extracting rows based on some conditions ---")
print(df[~(df["price"]>600)])

print("\n--- Only date & price for quantity > 10 ---")
print(df.loc[df["price"]>600, ["quantity", "price"]])

print("\n--- df[rowStartIndx:rowEndIndx]. Doing slicing rows ---")
print(df[0:5])


print("\n--- Rows rowStartIndx to rowEndIndx, columns ['colName1', 'colName2'] ---")
print(df.loc[5:7, ["date", "price"]])