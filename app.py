
from flask import Flask,render_template,request,url_for
from flask_mysqldb import MySQL 
from datetime import *
import time as t


app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="ishaq"
app.config['MYSQL_PASSWORD']="ishaq123"
app.config['MYSQL_DB']="alnafi"

mysql = MySQL(app)

home = "HOMe Pages!!!!!!!!!!"


@app.route("/")
def get_home():
    return home

@app.route("/trainer")
def trainer():
    return render_template("trainer_details.html")


@app.route("/trainer_create",methods=['POST','GET'])
def trainer_create():
    if request.method == "POST":
        fname_data = request.form["fname"]
        lname_data = request.form["lname"]
        design_data = request.form["design"]
        course_data = request.form["course"]
        current_date = date.today()

        sql = "INSERT INTO trainer_details (fname,lname,design,course,datetime) VALUES (%s,%s,%s,%s,%s)"
        val = (fname_data,lname_data,design_data,course_data,current_date)

        # connection to mysql
        cursor = mysql.connection.cursor()

        # execute sql query
        cursor.execute(sql,val)

        #commit
        mysql.connection.commit()

        #close database

        cursor.close()
        return "Done, Data has been add"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')



