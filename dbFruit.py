import sqlite3

con = sqlite3.connect("fruits.db")
cur = con.cursor()

print("\n📌 Top 5 Low Sugar Fruits:")
cur.execute(
    """
    SELECT name, sugar
    FROM fruits
    ORDER BY sugar ASC
    LIMIT 5
"""
)
low_sugar = cur.fetchall()
for i, (name, sugar) in enumerate(low_sugar, start=1):
    print(f"{i}. {name}: {sugar} g sugar")

print("\n📌 Fruits with High Protein and Low Calories:")
cur.execute(
    """
    SELECT name, protein, calories
    FROM fruits
    ORDER BY protein DESC, calories ASC
    LIMIT 5
"""
)
high_protein_low_calories = cur.fetchall()
for i, (name, protein, calories) in enumerate(high_protein_low_calories, start=1):
    print(f"{i}. {name}: {protein} g protein, {calories} kcal")

print("\n📌 Fruits with Low Sugar, High Protein, and Low Calories :")
cur.execute(
    """
    SELECT f1.name, f1.protein, f1.calories, f2.sugar
    FROM (
        SELECT name, protein, calories
        FROM fruits
        ORDER BY protein DESC, calories ASC
        LIMIT 5
    ) AS f1
    INNER JOIN (
        SELECT name, sugar
        FROM fruits
        ORDER BY sugar ASC
        LIMIT 5
    ) AS f2
    ON f1.name = f2.name
"""
)
intersection = cur.fetchall()
if intersection:
    for i, (name, protein, calories, sugar) in enumerate(intersection, start=1):
        print(f"{i}. {name}: {protein} g protein, {calories} kcal, {sugar} g sugar")
else:
    print("No fruits found in both categories.")

con.close()
