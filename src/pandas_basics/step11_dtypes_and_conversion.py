
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real dataset
csv_path = generate_sales_data("step11_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\n--- df.dtypes and returning data-types of each columns of data-frame ---")
print(df.dtypes)

print("\nConvert numeric column to float using astype()")
df["quantity_numeric_to_float"] = df["quantity"].astype(float)
print(df[["quantity", "quantity_numeric_to_float"]].head(2))

print("\nConvert numeric column to string using astype()")
df["quantity_numeric_to_string"] = df["quantity"].astype(str)
print(df[["quantity", "quantity_numeric_to_string"]].head(2))

print("\nConvert float column to integer using astype()")
df["price_float_to_integer"] = df["price"].astype(int)
print(df[["price", "price_float_to_integer"]].head(2))

print("\nto_numeric() with error handling. errors='coerce' converts invalid values to NaN")
sample_series = pd.Series(["100", "ABC", "200"])
converted_to_numeric = pd.to_numeric(sample_series, errors="coerce")
print(converted_to_numeric)

print("\nto_datetime() with error handling. errors='coerce' converts invalid values to NaN")
sample_series = pd.Series(["2025-01-01", "ABC"])
converted_to_datetime = pd.to_datetime(sample_series, errors="coerce")
print(converted_to_datetime)

print("\nto_timedelta() with error handling. errors='coerce' converts invalid values to NaN")
sample_series = pd.Series(["1 Days", "ABC", "1 days", "1 Days 10 hours"])
converted_to_timedelta = pd.to_timedelta(sample_series, errors="coerce")
print(converted_to_timedelta)


print("\nChanging multiple column types at once using astype(dict)")
print(df.dtypes)
df = df.astype({"quantity":"int32", "price":"float32"})
print(df.dtypes)


print("\nMixed data-types of any single-column")
df = pd.DataFrame({
    "colName1": [123, "2025-01-01"]
})
print(df.dtypes)