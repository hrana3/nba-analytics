import sqlite3

conn = sqlite3.connect("/Users/harisrana/nba/db/test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO test (name) VALUES (?)", ("example",))

conn.commit()
conn.close()

print("✅ SQLite test succeeded!")

