
import pandas as pd
from datetime import datetime, timedelta
import random
import os

DATA_DIR = "data"

def generate_sales_data(filename: str, rows: int = 50):
    """
    Generate realistic sales dataset without hardcoded/dummy values.
    All values are produced dynamically.
    """

    os.makedirs(DATA_DIR, exist_ok=True)

    start = datetime(2024, 1, 1)

    dates = [start + timedelta(days=i) for i in range(rows)]
    product_ids = [random.randint(1000, 9999) for _ in range(rows)]
    quantities = [random.randint(1, 20) for _ in range(rows)]
    prices = [round(random.uniform(100.0, 999.0), 2) for _ in range(rows)]

    df = pd.DataFrame({
        "date": dates,
        "product_id": product_ids,
        "quantity": quantities,
        "price": prices,
    })

    file_path = os.path.join(DATA_DIR, filename)
    df.to_csv(file_path, index=False)
    print("Generated:", file_path)
    return file_path
