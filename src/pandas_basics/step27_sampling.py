import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step27_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\n--- Random sample of any 5 rows without random_state. Always return random rows ---")
print(df.sample(n=5))

print("\n--- Random sample of any 5 rows with random_state=42 bcz output can be reproducible ---")
print(df.sample(n=5, random_state=42))

print("\n--- Random 30%/50%/10% sample without random_state. Always return random rows ---")
print(df.sample(frac=0.3))

print("\n--- Random 30%/50%/10% sample with random_state=42 bcz output can be reproducible ---")
print(df.sample(frac=0.3, random_state=42))

print("\n--- Shuffled DataFrame without random_state. Always return random rows ---")
shuffled = df.sample(frac=1).reset_index(drop=True)
print(shuffled)

print("\n--- Shuffled DataFrame with random_state=42 bcz output can be reproducible ---")
shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
print(shuffled)

print("\n--- Sampling with replacement (bootstrap) ---")
shuffled = df.sample(n=15, replace=True, random_state=42).reset_index(drop=True)
print(shuffled)

print("\n--- Group-wise sample (1 row per product_id) ---")
shuffled = df.groupby("product_id").sample(n=5, replace=True)
print(shuffled)
