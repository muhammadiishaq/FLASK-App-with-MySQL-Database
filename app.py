
from flask import Flask,render_template,request,url_for
from flask_mysqldb import MySQL 
from flask import redirect
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
def index():
    return render_template("index.html")

@app.route("/trainer")
def trainer():
    return render_template("trainer_form.html")


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
        return redirect(url_for('trainer'))


@app.route("/trainer_data",methods=['POST','GET'])
def trainer_data():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM trainer_details;"
        
    cursor.execute(sql)
    row = cursor.fetchall()

    return render_template("trainer_reports.html",output=row)




@app.route("/trainer_filter",methods=['POST','GET'])
def trainer_filter():
    if request.method == "POST":
        course_search = request.form["course"]
        cursor = mysql.connection.cursor()
        
        if course_search == "All":
                    
            sql = "SELECT * FROM trainer_details;"
            cursor.execute(sql)
            row = cursor.fetchall()

            return render_template("trainer_reports.html",output=row)


        else:    
            sql = "SELECT * FROM trainer_details where course=" + course_search
            cursor.execute(sql)
            row = cursor.fetchall()

            return render_template("trainer_reports.html",output=row)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')



