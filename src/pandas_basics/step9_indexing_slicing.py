
import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate real data
csv_path = generate_sales_data("step9_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- FULL DATAFRAME ---")
print(df)


print("\n--- df.loc[rowStartIndx : rowEndIndx, ['RespectiveColName1', 'RespectiveColName2', 'etc']] and labelBase ---")
print(df.loc[0:5, ["date", "quantity"]])