import sqlite3

i = 0

for i in range(0,100):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("insert into parkings values (?, ?, ?)", (i, -1, 0))
    conn.commit()
    conn.close()