from flask import Flask, jsonify
import sqlite3
from qrgen import qr

# file_name = qr.QR("data to be stored within QR", "information")
# print(file_name)

app = Flask(__name__)

# conn = sqlite3.connect('parking.db')
# cur = conn.cursor()
# # cur.execute("CREATE TABLE parkings (u_id integer, p_id integer, filled boolean)")
# cur.close()

@app.route("/")
def hello():
    return "Hi"

@app.route("/parking", methods = ['GET'])
def get_parking():
    conn = sqlite3.connect('parking.db')
    cur = conn.cursor()
    cur.execute("select * from parkings")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/parking/add/<int:p>/<int:u>")
def add(p, u = -1):
    conn = sqlite3.connect('parking.db')
    cur = conn.cursor()
    cur.execute("select * from parkings where p_id = ?", (p,))
    data = cur.fetchone()
    if data:
        if len(data) > 0:
            return "Already exists"
    cur.execute("insert into parkings(u_id, p_id, filled) values(?,?,?)", (u, p, 0,))
    conn.commit()
    conn.close()
    return "Success"

@app.route("/parking/fill/<int:parking_id>/<int:user_id>")
def fill_parking(parking_id, user_id):
    conn = sqlite3.connect('parking.db')
    cur = conn.cursor()
    cur.execute("select * from parkings where u_id = ?", (user_id,))
    data = cur.fetchone()
    if data:
        if len(data) > 0:
            return "Already have a car parked"
    cur.execute("select * from parkings where p_id = ?", (parking_id,))
    data = cur.fetchone()
    if data:
        if data[2] == 1:
            return "Already filled"
    cur.execute("update parkings set u_id = ?, filled = ? where p_id = ?", (user_id, 1, parking_id,))
    conn.commit()
    conn.close()
    return "Success"

@app.route("/parking/delete/<int:parking_id>", methods=['GET'])
def remove_parking(parking_id):
    conn = sqlite3.connect('parking.db')
    cur = conn.cursor()
    cur.execute("update parkings set u_id = ?, filled = ? where u_id = ?", (-1, 0, u_id,))
    conn.commit()
    conn.close()
    return "Success"

@app.route("/parking/find/<int:user_id>", methods=['GET'])
def find_parking(user_id, current_position = ""):
    conn = sqlite3.connect('parking.db')
    cur = conn.cursor()
    cur.execute("select * from parkings where u_id = ?", (user_id,))
    conn.commit()
    data = cur.fetchone()
    conn.close()
    if len(data) > 0:
        return jsonify(data)
    # navigate current_position to parking_id

if __name__ == '__main__':
    app.run(debug=True, port=8080)
