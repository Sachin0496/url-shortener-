import sqlite3

conn = sqlite3.connect("urls.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS urls (
        id integer primary key,
        short_url text,
        original_url text
    )
"""
)

conn.commit()
conn.close()

print("the tables have been sucessfully created")