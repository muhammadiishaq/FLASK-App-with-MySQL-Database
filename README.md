# 🐍 Flask + MySQL Trainer Details App

This project is a basic **Flask web application** that interacts with a **MySQL** database to collect and display trainer details.

---

## 📁 Project Structure

```
trainer-app/
│
├── templates/
│   ├── trainer_details.html        # Trainer input form (not shown in above code)
│   └── display_trainer.html        # Trainer data display
│
├── app.py                          # Main Flask application
└── README.md                       # Project documentation (this file)
```

---

## 🚀 Features

- Submit trainer details via web form
- Save data in MySQL database
- Display all stored records in table format

---

## 🧰 Requirements

- Python 3.x
- MySQL Server
- Virtualenv (recommended)

---

## 🔧 Setup Instructions

### 1. ✅ Install MySQL Server (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install mysql-server
```

### 2. ✅ Login to MySQL

```bash
sudo mysql -u root -p
```

---

## 🛠️ MySQL Setup

### 3. ✅ Create a New User and Database

```sql
-- Create user
CREATE USER 'ishaq'@'localhost' IDENTIFIED BY 'ishaq123';

-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'ishaq'@'localhost';

-- Create database
CREATE DATABASE alnafi;

-- Use database
USE alnafi;
```

### 4. ✅ Create `trainer_details` Table

```sql
CREATE TABLE trainer_details (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(100),
    lname VARCHAR(100),
    design VARCHAR(100),
    course VARCHAR(100),
    datetime DATE
);

SHOW TABLES;
DESCRIBE trainer_details;
```

---

## 🐍 Python Setup

### 5. ✅ Create a Virtual Environment

```bash
python3 -m venv myproject
cd myproject
source bin/activate
```

### 6. ✅ Install Flask and MySQL library

```bash
pip install flask flask-mysqldb
```

---

## 📄 Flask App Code (`app.py`)

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import date

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "ishaq"
app.config['MYSQL_PASSWORD'] = "ishaq123"
app.config['MYSQL_DB'] = "alnafi"

mysql = MySQL(app)

@app.route("/")
def get_home():
    return "Home Page!"

@app.route("/trainer")
def trainer():
    return render_template("trainer_details.html")

@app.route("/trainer_create", methods=['POST', 'GET'])
def trainer_create():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        design = request.form["design"]
        course = request.form["course"]
        current_date = date.today()

        query = "INSERT INTO trainer_details (fname, lname, design, course, datetime) VALUES (%s, %s, %s, %s, %s)"
        values = (fname, lname, design, course, current_date)

        cursor = mysql.connection.cursor()
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("trainer"))

@app.route("/trainer_data", methods=['GET'])
def trainer_data():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM trainer_details")
    data = cursor.fetchall()
    cursor.close()
    return render_template("display_trainer.html", output=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
```

---

## 📄 Template: `display_trainer.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trainer Data</title>
</head>
<body>
    <table border="2">
        <tr><th colspan="5">Trainer Course Details</th></tr>
        <tr>
            <th>Sr.no</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Designation</th>
            <th>Course</th>
        </tr>
        {% for i in output %}
        <tr>
            <td>{{ i[0] }}</td>
            <td>{{ i[1] }}</td>
            <td>{{ i[2] }}</td>
            <td>{{ i[3] }}</td>
            <td>{{ i[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

---

## ▶️ Running the App

```bash
python app.py
```

Visit:
- `http://localhost:5000/trainer` → Form
- `http://localhost:5000/trainer_data` → View Data

---

## 💡 Useful MySQL Commands

| Action | Command |
|--------|---------|
| Start MySQL | `sudo systemctl start mysql` |
| Login as root | `sudo mysql -u root -p` |
| Login as user | `mysql -u ishaq -p` |
| List databases | `SHOW DATABASES;` |
| Use database | `USE alnafi;` |
| List tables | `SHOW TABLES;` |
| Describe table | `DESCRIBE trainer_details;` |
| Insert manually | `INSERT INTO trainer_details (fname, lname, design, course, datetime) VALUES ('Ali', 'Khan', 'Trainer', 'DevOps', CURDATE());` |

---

## 📦 Freeze Python Dependencies

```bash
pip freeze > requirements.txt
```

---

## ⚖️ License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---
