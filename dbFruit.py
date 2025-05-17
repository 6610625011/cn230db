import sqlite3

con = sqlite3.connect("fruits.db")
cur = con.cursor()


def print_title(title):
    print("\n" + "📌 " + title)
    print("-" * (len(title) + 4))


# Top 5 Low Sugar Fruits
print_title("Top 5 Low Sugar Fruits")
cur.execute(
    """
    SELECT name, sugar
    FROM fruits
    ORDER BY sugar ASC
    LIMIT 5
"""
)
for i, (name, sugar) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {name}: {sugar} g")

# Top 5 High Protein Fruits
print_title("Top 5 High Protein Fruits")
cur.execute(
    """
    SELECT name, protein
    FROM fruits
    ORDER BY protein DESC
    LIMIT 5
"""
)
for i, (name, protein) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {name}: {protein} g")

# Top 5 Lowest Calorie Fruits
print_title("Top 5 Lowest Calorie Fruits")
cur.execute(
    """
    SELECT name, calories
    FROM fruits
    ORDER BY calories ASC
    LIMIT 5
"""
)
for i, (name, calories) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {name}: {calories} kcal")

# Average nutrition per fruit family
print_title("Average Sugar & Protein by Fruit Family")
cur.execute(
    """
    SELECT family, ROUND(AVG(sugar), 2), ROUND(AVG(protein), 2)
    FROM fruits
    GROUP BY family
    ORDER BY AVG(sugar) ASC
"""
)
for family, sugar_avg, protein_avg in cur.fetchall():
    print(f"🍃 {family}: {sugar_avg} g sugar avg, {protein_avg} g protein avg")

# Fruits that are low sugar + low calories + high protein
print_title("Smart Choice Fruits (Low Sugar + Low Cal + High Protein)")
cur.execute(
    """
    SELECT name, sugar, calories, protein
    FROM fruits
    WHERE sugar < 10 AND calories < 60 AND protein > 0.5
    ORDER BY protein DESC
"""
)
results = cur.fetchall()
if results:
    for i, (name, sugar, calories, protein) in enumerate(results, 1):
        print(f"{i}. {name}: {sugar}g sugar, {calories} kcal, {protein}g protein")
else:
    print("No fruits matched the criteria.")

con.close()
