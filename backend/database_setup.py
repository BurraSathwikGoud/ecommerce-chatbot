import sqlite3
import pandas as pd
import os

# Connect to SQLite DB (it creates ecommerce.db if not exists)
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Define table creation queries
create_tables = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            gender TEXT,
            age INTEGER,
            street_address TEXT,
            email TEXT,
            postal_code TEXT,
            country TEXT,
            state TEXT,
            city TEXT,
            pincode TEXT,
            latitude REAL,
            longitude REAL,
            signup_date TEXT,
            traffic_source TEXT,
            created_at TEXT
        )
    """,
    "products": """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            cost REAL,
            category TEXT,
            name TEXT,
            brand TEXT,
            retail_price REAL,
            department TEXT,
            sku TEXT,
            distribution_center_id INTEGER
        )
    """,
    "orders": """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            user_id TEXT,
            status TEXT,
            gender TEXT,
            created_at TEXT,
            returned_at TEXT,
            shipped_at TEXT,
            delivered_at TEXT,
            num_of_item INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """,
    "order_items": """
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY,
            order_id TEXT,
            user_id TEXT,
            product_id TEXT,
            inventory_item_id TEXT,
            status TEXT,
            created_at TEXT,
            shipped_at TEXT,
            delivered_at TEXT,
            returned_at TEXT,
            sale_price REAL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (inventory_item_id) REFERENCES inventory_items(id)
        )
    """,
    "distribution_centers": """
        CREATE TABLE IF NOT EXISTS distribution_centers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            latitude REAL,
            longitude REAL
        )
    """,
    "inventory_items": """
        CREATE TABLE IF NOT EXISTS inventory_items (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            created_at TEXT,
            sold_at TEXT,
            cost REAL,
            product_category TEXT,
            product_name TEXT,
            product_brand TEXT,
            product_retail_price REAL,
            product_department TEXT,
            product_sku TEXT,
            product_distribution_center_id INTEGER
        )
    """
}

# Execute the queries to create tables
for table, query in create_tables.items():
    cursor.execute(query)
    print(f"✅ Created table: {table}")

conn.commit()


import os

# Mapping table names to their CSV file names
csv_to_table = {
    "users": "users.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "distribution_centers": "distribution_centers.csv",
    "inventory_items": "inventory_items.csv"
}

# Load each CSV file into the corresponding SQL table
for table, file in csv_to_table.items():
    if os.path.exists(file):
        df = pd.read_csv(file)
        df.to_sql(table, conn, if_exists='append', index=False)
        print(f"📥 Inserted data into {table}")
    else:
        print(f"⚠️ CSV not found: {file}")

# Close DB connection
conn.close()

