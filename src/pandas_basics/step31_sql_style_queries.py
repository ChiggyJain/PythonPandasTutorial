import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 – Generate dataset
csv_path = generate_sales_data("step31_sales.csv", rows=12)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)