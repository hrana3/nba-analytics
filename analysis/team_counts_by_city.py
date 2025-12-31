import sqlite3

conn = sqlite3.connect("/Users/harisrana/nba/db/nba.db")
cursor = conn.cursor()

cursor.execute("""
SELECT city, COUNT(*) AS team_count
FROM teams
GROUP BY city
ORDER BY team_count DESC;
""")

results = cursor.fetchall()

for city, count in results:
    print(f"{city}: {count}")

conn.close()
