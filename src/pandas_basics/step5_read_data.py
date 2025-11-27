import pandas as pd
from src.utils.file_generator import generate_sales_data

# generate real data csv file
csv_path = generate_sales_data(filename="step5_sales.csv", rows=30)

# reading csv file all contents
df = pd.read_csv(csv_path)
print("Printing full data-frame (csv file contents)\n")
print(df)
print("\n")


# reading csv file contents with specific columns
df_subset = pd.read_csv(csv_path, usecols=["date", "quantity"])
print("Printing data-frame (csv file contents) with specifi columns\n")
print(df_subset)
print("\n")

# Parse date column properly
df_dates = pd.read_csv(csv_path, parse_dates=["date"])
print("date-column is parsed with dates and showing all data-types of respective columns\n")
print(df_dates.dtypes)
print("\n")

# Read CSV with index column
df_indexed = pd.read_csv(csv_path, index_col="product_id")
print("Column product_id added as Index to identify each row-unique and showing only 5 records with the help head()\n")
print(df_indexed.head())
print("\n")


# Reading Large Files with Chunksize
print("Reading file in Chunks (chunksize=10). Here each chuncks will have 10-rows-records-data only\n")
chunk_iter = pd.read_csv(csv_path, chunksize=10)
for i, chunk in enumerate(chunk_iter):
    print(f"\nChunk {i+1}")
    print(chunk)
print("\n")    