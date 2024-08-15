import sqlite3

connection = sqlite3.connect('autopujcovna.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cisloOP INTEGER NOT NULL,
    Adresa TEXT NOT NULL,
    telefon INTEGER NOT NULL,
    mail TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    znacka TEXT NOT NULL,
    typ TEXT NOT NULL,
    rokV INTEGER NOT NULL,
    SPZ TEXT NOT NULL
)
''')


cursor.execute('''
INSERT INTO users (name, cisloOP, Adresa, telefon, mail) 
VALUES 
    ("Michal", "123456", "Doma 14", "789123456", "mojejmeno@michal.cz" ), 
    ("Alena", "242342424", "U mostu 15", "147258369", "jejimail@alena.cz")
''')

cursor.execute('''
INSERT INTO cars (znacka, typ, rokV, SPZ) 
VALUES 
    ("Škoda", "Octavia4", "2023", "1AAY147" ), 
    ("Škoda", "Octavia3", "2014", "1A11515")
''')


connection.commit()

cursor.execute("SELECT * FROM users, cars")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()