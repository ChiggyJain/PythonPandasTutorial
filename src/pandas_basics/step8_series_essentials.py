
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
csv_path = generate_sales_data("step8_sales.csv", rows=10)

df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- FULL DATAFRAME ---")
print(df)

print("\n--- Printing data frame with specific columns only ---")
quantity_series = df["quantity"]
print(quantity_series)

print("\n--- anySeriesName.index and return row-indexes(rowStartIndx, rowEndIndx, stepRange) ---")
print(quantity_series.index)

print("\n--- anySeriesName.values and return value in 1DArray ---")
print(quantity_series.values)

print("\n--- vectorized operations (anySeriesName + anyNumber) ---")
print(quantity_series + 10)

print("\n--- anySeriesName.describe() ---")
print("Count: Total-Rows of Each Column-Level")
print("Mean: Average value of each total-column-data")
print("Min: Minimum value from of each total-column-data")
print("Max: Maximum value from of each total-column-data")
print("STD: sqrt( Σ(x-mean)²/(n-1))")
print("25%: minValue + 0.25 * (maxVal - minValue)")
print("50%: minValue + 0.50 * (maxVal - minValue)")
print("75%: minValue + 0.75 * (maxVal - minValue)")
print(quantity_series.describe())


print("\n--- anySeriesName (sum/mean/min/max/std) ---")
print("Sum:", quantity_series.sum())
print("Mean:", quantity_series.mean())
print("Min:", quantity_series.min())
print("Max:", quantity_series.max())
print("Std:", quantity_series.std())


print("\n--- anySeriesName.unique() and return unique value ---")
print(quantity_series)
print(quantity_series.unique())


print("\n--- anySeriesName.nunique() and return unique value count ---")
print(quantity_series)
print(quantity_series.nunique())

print("\n--- anySeriesName.value_counts() and return count of each column-data ---")
print(quantity_series.head(2))
print(quantity_series.head(2).value_counts())

print("\n--- anySeriesName > 12. Doing filtering part ---")
print(quantity_series)
print(quantity_series[quantity_series > 12])

print("\n--- anySeriesName.apply(lambda x: x - 2) and using lambda adding our business logic as per business usecases ---")
print(quantity_series)
discount_series = quantity_series.apply(lambda x: x - 2)
print(discount_series)
















