from flask import Flask, request, jsonify
import mysql.connector
# import mysql.
from mysql.connector import Error
from mysql.connector import errorcode
app = Flask(__name__)

@app.route("/signup",methods=["POST"])
def sign():
 try:
    name = request.json.get('name')
    name1 = request.json.get('lastname')
    name2 = request.json.get('sex')
    conn = mysql.connector.connect(host='localhost',
    database='details', user='studentadmin',
    password='80123nicK#')
    query = 'INSERT INTO details VALUES('+'"'+ name +'","'+name1+'","'+ name2+'"'+')'
    print(query)
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(request.json)
    return "data entered"
 except mysql.connector.Error as error:
    print("Error :", error)

 finally:
  if(conn.is_connected()):
        conn.close()
        print("Database Connection Closed")
@app.route("/update",methods=["POST"])
def update():
 try:
    name = request.json.get('name')
    # name1 = request.json.get('lastname')
    # name2 = request.json.get('sex')
    conn1 = mysql.connector.connect(host='localhost',
    database='details', user='studentadmin',
    password='80123nicK#')
    query = 'UPDATE details SET fist_name="'+name+'" WHERE last_name="vin" '
    # UPDATE details SET fist_name=""+name1+"" WHERE last_name="vin"
    # UPDATE details SET("name"="data") WHERE last_name="vin" '
    print(query)
    cursor=conn1.cursor()
    cursor.execute(query)
    conn1.commit()
    conn1.close()
    print(request.json)
    return "data updated"
 except mysql.connector.Error as error:
    print("Error :", error)

 finally:
  if(conn1.is_connected()):
        conn1.close()
        print("Database Connection Closed")
@app.route("/delete",methods=["POST"])
def delete():
 try:
    # name = request.json.get()
    # name1 = request.json.get('lastname')
    # name2 = request.json.get('sex')
    conn1 = mysql.connector.connect(host='localhost',
    database='details', user='studentadmin',
    password='80123nicK#')
    query = 'DELETE FROM details where last_name="vin"'
    # DELETE FROM details where last_name="vin"
    # UPDATE details SET fist_name=""+name1+"" WHERE last_name="vin"
    # UPDATE details SET("name"="data") WHERE last_name="vin" '
    print(query)
    cursor=conn1.cursor()
    cursor.execute(query)
    conn1.commit()
    conn1.close()
    print(request.json)
    return "data delete"
 except mysql.connector.Error as error:
    print("Error :", error)

 finally:
  if(conn1.is_connected()):
        conn1.close()
        print("Database Connection Closed")
@app.route("/get",methods=["GET"])
def get():
 try:
    # name = request.json.get()
    # name1 = request.json.get('lastname')
    # name2 = request.json.get('sex')
    conn1 = mysql.connector.connect(host='localhost',
    database='details', user='studentadmin',
    password='80123nicK#')
    query = 'select * from details'
    # DELETE FROM details where last_name="vin"
    # UPDATE details SET fist_name=""+name1+"" WHERE last_name="vin"
    # UPDATE details SET("name"="data") WHERE last_name="vin" '
    print(query)
    cursor=conn1.cursor()
    cursor.execute(query)
    myresult = cursor.fetchall()

    # for x in myresult:
    #      print(x)
    return jsonify(myresult)
 except mysql.connector.Error as error:
    print("Error :", error)

 finally:
  if(conn1.is_connected()):
        conn1.close()
        print("Database Connection Closed")
app.run()

