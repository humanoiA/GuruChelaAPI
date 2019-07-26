import mysql.connector
from flask import Flask,jsonify,request,render_template
from werkzeug.serving import WSGIRequestHandler
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS']='Content-Type'
@app.route('/')
@cross_origin()
def index():
   #return 'OK!'
    mydb= mysql.connector.connect(
    host="remotemysql.com",
    user="DcRR6aobND",
    passwd="xh7QRmkdzC",
    database="DcRR6aobND"
)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from teachers_arena INNER JOIN teachers_login where teachers_arena.TID=teachers_login.id and Time_Date>now()")
    myresult = mycursor.fetchall()
    print(myresult)
    return jsonify(a=myresult)
@app.route('/<sub>/<pre>/<ven>/<crc>/<all>/<tid>/<date>/<time>')
@cross_origin()
def teachers_detail(sub,pre,ven,crc,all,tid,date,time):
    mydb= mysql.connector.connect(
    host="remotemysql.com",
    user="DcRR6aobND",
    passwd="xh7QRmkdzC",
    database="DcRR6aobND"
)
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO teachers_arena (subject, prerequisite, venue, currency_requirement, allowance, TID, Time_Date, UniID) VALUES('"+sub+"',"+"'"+pre+"',"+"'"+ven+"',"+crc+","+all+","+tid+","+"'"+date+" "+time+"',NULL)")
    mydb.commit()
    return jsonify(ALPHA="OK")
   # myresult = mycursor.fetchall()
  #  return jsonify(ALPHA=myresult)
@app.route('/<Tmail>')
@cross_origin()
def teachers_dashboard(Tmail):
    mydb= mysql.connector.connect(
    host="remotemysql.com",
    user="DcRR6aobND",
    passwd="xh7QRmkdzC",
    database="DcRR6aobND"
)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from teachers_arena INNER JOIN teachers_login where teachers_arena.TID=teachers_login.id and Time_Date>now() and email=\""+Tmail+"\"")
    myresult = mycursor.fetchall()
    return jsonify(ALPHA=myresult)
if __name__ == '__main__':
   WSGIRequestHandler.protocol_version = "HTTP/1.1"
   app.run(debug = True)
#for x in myresult:
 # print(x)