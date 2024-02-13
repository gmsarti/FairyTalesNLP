import sqlite3

conn = sqlite3.connect('fairytale.db')  # Create/connect to the database

cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animal_types (
        id INTEGER PRIMARY KEY,
        type TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professions (
        id INTEGER PRIMARY KEY,
        profession TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS human_names (
        id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT
    )
''')

# Sample data (add more as needed)
animal_types = ["Fox", "Owl", "Rabbit", "Bear", "Wolf"]  # Removed extra parentheses
professions = ["Farmer", "Blacksmith", "Baker", "Woodcutter", "Knight"]  # Removed extra parentheses
names = [
    ("Jack", "Male"), ("Finn", "Male"), ("Henry", "Male"),
    ("Alice", "Female"), ("Willow", "Female"), ("Emma", "Female"),
    ("Rowan", "Nonbinary"), ("Riley", "Nonbinary"), ("Alex", "Nonbinary")
]

# Corrected INSERT statements
cursor.executemany("INSERT OR IGNORE INTO animal_types (type) VALUES (?)", [(type,) for type in animal_types])
cursor.executemany("INSERT OR IGNORE INTO professions (profession) VALUES (?)", [(prof,) for prof in professions])
cursor.executemany("INSERT OR IGNORE INTO human_names (name, gender) VALUES (?, ?)", names)

conn.commit() 
conn.close() 
