from flask import Flask, jsonify
import sqlite3
from qrgen import qr

# file_name = qr.QR("data to be stored within QR", "information")
# print(file_name)

app = Flask(__name__)

# conn = sqlite3.connect('parking.db')
# cur = conn.cursor()
# # cur.execute("CREATE TABLE parkings (u_id integer, p_id integer, filled boolean)")
# cur.execute("insert into parkings values (3,4,0)")
# cur.close()

@app.route("/parking", methods = ['GET'])
def get_parking():
    conn = sqlite3.connect('parking.db')
    cur = conn.cursor()
    cur.execute("select * from parkings")
    # print(cur.execute("select * from parkings"))
    data = cur.fetchall()
    return jsonify(data)

@app.route("/parking/add/<int:parking_id>/<int:user_id>")
def add_parking(parking_id, user_id):
    pass
    # sqlite.query(update where p_id = parking_id, set filled = yes and set u_id = user_id)

@app.route("/parking/delete/<int:parking_id>", methods=['GET'])
def remove_parking(parking_id):
    pass
    # sqlite3.query(get id = parking, change filled = no and user id = null)

@app.route("/parking/find/<int:user_id>", methods=['GET'])
def find_parking(user_id, current_position = ""):
    pass
    # sqlite.query(get parking_id where user_id = user_id)
    # navigate current_position to parking_id

if __name__ == '__main__':
    app.run(debug=True, port=8080)
