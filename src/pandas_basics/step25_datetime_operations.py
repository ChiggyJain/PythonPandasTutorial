import pandas as pd
from src.utils.file_generator import generate_sales_data

# Step 0 — Generate dataset
csv_path = generate_sales_data("step25_sales.csv", rows=10)
df = pd.read_csv(csv_path, parse_dates=["date"])

print("\n--- ORIGINAL DATA ---")
print(df)

print("\nExtract year, month, day")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
print(df)

print("\nExtract weekday (0=Mon, 6=Sun)")
df["weekday"] = df["date"].dt.weekday
df["weekday_name"] = df["date"].dt.day_name()
print(df)

print("\nExtract hour, minute, second (when time exists)")
df.loc[0, "date"] = "2025-01-01 11:30:20"
df["hour"] = df["date"].dt.hour
df["minute"] = df["date"].dt.minute
df["seconds"] = df["date"].dt.second
print(df)

print("\n--- Start & End of Month/Year ---")
df.loc[1, "date"] = "2025-02-05 11:30:20"
#df["year_start"] = df["date"].dt.to_period("Y").dt.start_time
#df["year_end"] = df["date"].dt.to_period("Y").dt.end_time
df["month_start"] = df["date"].dt.to_period("M").dt.start_time
df["month_end"] = df["date"].dt.to_period("M").dt.end_time
print(df)

print("\n--- Days difference from max date ---")
print("Date difference — timedelta")
df["days_since"] = (df["date"].max() - df["date"]).dt.days
print(df)


