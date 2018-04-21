import sqlite3

conn = sqlite3.connect('./../parking.db')
cur = conn.cursor()
print(cur)

# cur.execute("insert into parkings values (3,4,0)")
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())

conn.commit()
conn.close()