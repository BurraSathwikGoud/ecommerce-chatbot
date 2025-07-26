import pandas as pd
import os

excel_files = [
    "distribution_centers.csv",
    "Inventory_items.csv",
    "order_items.csv",
    "orders.csv",
    "products.csv",
    "users.csv"
]

print("\n📂 Reading CSV Files:\n")
for file in excel_files:
    if os.path.exists(file):
        print(f"\n----- {file} -----")
        df = pd.read_csv(file)
        print(df.head())  # Show only first few rows
    else:
        print(f"⚠️ File not found: {file}")
