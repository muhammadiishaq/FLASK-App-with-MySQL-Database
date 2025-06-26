from flask import Flask,render_template,request,url_for
import sqlite3
from datetime import *
import time as t


app = Flask(__name__)

# SQLite database file
DATABASE = 'alnafi.db'

def init_db():
    """Initialize the database with trainer_details table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trainer_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            design TEXT NOT NULL,
            course TEXT NOT NULL,
            datetime DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

home = "HOMe Pages!!!!!!!!!!"


@app.route("/")
def get_home():
    return render_template("home.html")

@app.route("/trainer")
def trainer():
    return render_template("trainer_details.html")


@app.route("/view_trainers")
def view_trainers():
    # connection to SQLite
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # execute sql query to get all trainers
    cursor.execute("SELECT * FROM trainer_details ORDER BY id DESC")
    trainers = cursor.fetchall()
    
    #close database
    cursor.close()
    conn.close()
    
    return render_template("view_trainers.html", trainers=trainers)


@app.route("/trainer_create",methods=['POST','GET'])
def trainer_create():
    if request.method == "POST":
        fname_data = request.form["fname"]
        lname_data = request.form["lname"]
        design_data = request.form["design"]
        course_data = request.form["course"]
        current_date = date.today()

        sql = "INSERT INTO trainer_details (fname,lname,design,course,datetime) VALUES (?,?,?,?,?)"
        val = (fname_data,lname_data,design_data,course_data,current_date)

        # connection to SQLite
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # execute sql query
        cursor.execute(sql,val)

        #commit
        conn.commit()

        #close database
        cursor.close()
        conn.close()
        
        return render_template("success.html", message="Trainer data has been added successfully!")


if __name__ == "__main__":
    init_db()  # Initialize database on startup
    app.run(debug=True,host='0.0.0.0')



