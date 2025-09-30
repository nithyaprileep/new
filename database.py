
#Database

"""What is a Database?

A database is an organized collection 
of data that can be stored, managed, and retrieved easily.

Types of Databases

Relational Databases (RDBMS)

Data is stored in tables (rows & columns).

Examples: SQLite, MySQL, PostgreSQL, Oracle, SQL Server.

Uses SQL to manage data.

Example Table → students
-----------------------------------------
id	name	age
-------------------------------
1	Alice	21
--------------------------------
2	Bob	2
-----------------------------------

Non-relational Databases (NoSQL)

Data stored in different forms (documents, key-value, graph, etc.).

Examples: MongoDB, Redis, Cassandra.

Better for unstructured or flexible data."""
#CRUD fuctions

"""CREATE TABLE employee(
    id INT PRIMARY KEY,
    name CHAR(20),
    age INT,
    address VARCHAR(50)
    salary FLOAT 
);
INSERT INTO employee VALUES(1,'mohan',30,'olat',5000);
UPDATE employee SET age=2,salary=90000 where id=1;
ALTER TABLE employee ADD COLUMN designation varchar(50);
SELECT * FROM employee;
DELETE FROM employee WHERE id=1;#one row delete
ALTER TABLE employee DROP COLUMN age;#one column delete
DELETE FROM employee;#Delete all rows
DROP employee; #DELETE table"""


"""import sqlite3
con=sqlite3.connect("student.db")
print("Connected Successfully")

cursor=con.cursor()"""

"""import sqlite3

def create_db():
   conn=sqlite3.connect("student.db")
   print("database created successfully")
   cursor=conn.cursor()
   cursor.execute(""" 
        #CREATE TABLE IF NOT EXISTS Student_table(
             #   id INT PRIMARY KEY AUTOINCREMENT,
              #  name VARCHAR(50) NOT NULL,
              #  email VARCHAR(50) UNIQUE,
              #  age INT ) 
""")
   conn.commit()
   conn.close()
   print("successfull")

   
def add_students(name,email,age):
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute("""
    #INSERT INTO student (name,email,age) VALUES (?,?,?)
""" CREATE TABLE  Student_table(id INT PRIMARY KEY AUTOINCREMENT,name VARCHAR(50) NOT NULL,email VARCHAR(50) UNIQUE,
               age INT) )"""
""",(name,email,age))
   conn.commit()
   conn.close()
   print("successfull")

name=input("enter student name : ")
email=input("enter student email : ")
age=int(input("enter student age : "))
add_students(name,email,age)"""

"""import sqlite3

def create_db():
   conn=sqlite3.connect("student.db")
   print("database created successfully")
   cursor=conn.cursor()
   cursor.execute(""" 
    #CREATE TABLE IF NOT EXISTS Student_table(
               # id INT PRIMARY KEY AUTOINCREMENT,
              #  name VARCHAR(50) NOT NULL,
              #  email VARCHAR(50) UNIQUE,
              #  age INT ) 
""")
   conn.commit()
   conn.close()
   print("successfull")"""


import sqlite3

def create_db():
   conn=sqlite3.connect("student.db")
   print("database created successfully")
   cursor=conn.cursor()
   cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS Student10(
                id INTEGER PRIMARY KEY  ,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE,
                age INT ) """)
   conn.commit()
   conn.close()
   print("successfull")
create_db()

def add_students(name,email,age):
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute("""
   INSERT INTO student10(name,email,age) VALUES (?,?,?)
   """,(name,email,age))
   conn.commit()
   conn.close()
   print("successfull")

def view_students():
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute("""SELECT * FROM Student10""")
   rows=cursor.fetchall()
   conn.commit()
   conn.close()
   for i in rows:
      print(i)

#view_students()

"""name=input("enter student name : ")
email=input("enter student email : ")
age=int(input("enter student age : "))"""
#add_students(name,email,age)
from tabulate import tabulate

def view_students():
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute("""SELECT * FROM Student10""")
   rows=cursor.fetchall()
   conn.commit()
   conn.close()
   headers=["ID","NAME","EMAIL","AGE"]
   print(tabulate(rows,headers,tablefmt="double_grid")) #fancy_grid,grid

#view_students()

def update_students(new_name,new_email,new_age,student_id):
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute(""" 
         UPDATE  Student10 SET name=?,email=?,age=? WHERE id=?
""",(new_name,new_email,new_age,student_id))
   conn.commit()
   conn.close()
   print("Update successful")

"""student_id=int(input("enter student id : "))
new_name=input("enter student new name : ")
new_email=input("enter student new email : ")
new_age=int(input("enter student new age : "))"""

#update_students(new_name,new_email,new_age,student_id)

def update_students(new_name,new_email,new_age,student_id):
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute(""" 
         UPDATE  Student_table SET name=?,email=?,age=? WHERE id=?
""",(new_name,new_email,new_age,student_id))
   conn.commit()
   conn.close()
   print("Update successful")

"""student_id=int(input("enter student id : "))
new_name=input("enter student new name : ")
new_email=input("enter student new email : ")
new_age=int(input("enter student new age : "))"""

#update_students(new_name,new_email,new_age,student_id)
def delete_students(student_id):
   conn=sqlite3.connect("student.db")
   cursor=conn.cursor()
   cursor.execute("""
         DELETE FROM student10 WHERE id=?
""",(student_id,))
   conn.commit()
   conn.close()
   print("Deleted successful")

student_id=int(input("enter student id : "))
delete_students(student_id)