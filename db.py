import mysql.connector
from flask import Flask, jsonify, request, render_template
from werkzeug.serving import WSGIRequestHandler
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/all')
@cross_origin()
def index():
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="6fmKMRyVWv",
        passwd="li0yQeOzCa",
        database="6fmKMRyVWv"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * from teachers_arena INNER JOIN teachers_login where teachers_arena.TID=teachers_login.id and Time_Date>now()")
    myresult = mycursor.fetchall()
    return jsonify(a=myresult)


@app.route('/api/search/<query>')
@cross_origin()
def search(query):
   # return 'OK!'
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="6fmKMRyVWv",
        passwd="li0yQeOzCa",
        database="6fmKMRyVWv"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM teachers_arena INNER JOIN teachers_login WHERE " + "teachers_arena.TID=teachers_login.id AND Time_Date>now() AND (teachers_login.name LIKE '%" + query
                     + "%' OR teachers_arena.subject LIKE '%" + query + "%')")
    myresult = mycursor.fetchall()
    return jsonify(a=myresult)


@app.route('/api/register', methods=['POST'])
@cross_origin()
def register():
    if request.method == 'POST':
        if len(request.form) > 0:
            data = request.form
            mydb = mysql.connector.connect(
                host="remotemysql.com",
                user="6fmKMRyVWv",
                passwd="li0yQeOzCa",
                database="6fmKMRyVWv"
            )
            mycursor = mydb.cursor()
            query = "INSERT INTO teachers_login (name, email, pass, dept, gender) VALUES(%s, %s, %s, %s, %s)"
            val = (data['name'], data['email'], data['pass'],
                   data['dept'], data['gender'])
            mycursor.execute(query, val)
            mydb.commit()
            return jsonify(True)
        else:
            return jsonify("bad request")
    else:
        return None


@app.route('/api/<sub>/<pre>/<ven>/<crc>/<all>/<tid>/<date>/<time>')
@cross_origin()
def teachers_detail(sub, pre, ven, crc, all, tid, date, time):
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="6fmKMRyVWv",
        passwd="li0yQeOzCa",
        database="6fmKMRyVWv"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO teachers_arena (subject, prerequisite, venue, currency_requirement, allowance, TID, Time_Date, UniID) VALUES('" +
                     sub+"',"+"'"+pre+"',"+"'"+ven+"',"+crc+","+all+","+tid+","+"'"+date+" "+time+"',NULL)")
    mydb.commit()
    return jsonify(ALPHA="OK")
   # myresult = mycursor.fetchall()
  #  return jsonify(ALPHA=myresult)


@app.route('/api/<Tmail>', methods=['GET'])
@cross_origin()
def teachers_dashboard(Tmail):
    mydb = mysql.connector.connect(
        host="remotemysql.com",
        user="6fmKMRyVWv",
        passwd="li0yQeOzCa",
        database="6fmKMRyVWv"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from teachers_arena INNER JOIN teachers_login where " + "teachers_arena.TID=teachers_login.id and teachers_arena.Time_Date>now() and teachers_login.email=\""+Tmail+"\"")
    myresult = mycursor.fetchall()
    return jsonify(ALPHA=myresult)


if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True)
