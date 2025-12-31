import os
import sqlite3
from nba_api.stats.static import teams

# 🔹 Find the directory this file lives in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔹 Build absolute path to db/nba.db
DB_PATH = os.path.join(os.getcwd(), "db", "nba.db")


print("Database path:", DB_PATH)  # DEBUG LINE

# 1️⃣ Get NBA teams
nba_teams = teams.get_teams()

# 2️⃣ Connect to database
conn = sqlite3.connect("/Users/harisrana/nba/db/nba.db")
cursor = conn.cursor()

# 3️⃣ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY,
    full_name TEXT,
    abbreviation TEXT,
    city TEXT,
    nickname TEXT
)
""")

# 4️⃣ Insert data
for team in nba_teams:
    cursor.execute("""
        INSERT OR IGNORE INTO teams
        (team_id, full_name, abbreviation, city, nickname)
        VALUES (?, ?, ?, ?, ?)
    """, (
        team["id"],
        team["full_name"],
        team["abbreviation"],
        team["city"],
        team["nickname"]
    ))

conn.commit()
conn.close()

print("✅ NBA teams saved to database!")