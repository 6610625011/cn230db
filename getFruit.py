import requests
import sqlite3

url = "https://www.fruityvice.com/api/fruit/all"
response = requests.get(url)
fruits = response.json()

conn = sqlite3.connect("fruits.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS fruits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        family TEXT,
        genus TEXT,
        order_name TEXT,
        carbohydrates REAL,
        protein REAL,
        fat REAL,
        calories REAL,
        sugar REAL
    )
"""
)

cursor.execute("DELETE FROM fruits")
for fruit in fruits:
    cursor.execute(
        """
        INSERT INTO fruits (name, family, genus, order_name, carbohydrates, protein, fat, calories, sugar)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            fruit["name"],
            fruit["family"],
            fruit["genus"],
            fruit["order"],
            fruit["nutritions"]["carbohydrates"],
            fruit["nutritions"]["protein"],
            fruit["nutritions"]["fat"],
            fruit["nutritions"]["calories"],
            fruit["nutritions"]["sugar"],
        ),
    )

conn.commit()
conn.close()
