
# day_69

#  open() function
f = open("hello.txt", "rt")

# Open a File on the Server
f = open("hello.txt", "r")
print(f.read())

# Read Only Parts of the File
print(f.read(5))

# Read Lines
print(f.readline())

# Close Files
f.close()

# Write to an Existing File

f = open("hello.txt", "a")
f.write("Now this file has more content!")
f.close()

f = open("hello.txt", "r")
print(f.read())

# Create a New File
f = open("myfile.txt", "x")

# Delete a File
import os
os.remove("myfile.txt")

# Check if File exist

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exite")

# Delete Folder

os.rmdir("myfolder")


# day_70

import mysql.connector

#creating a connection
mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="12345678",
    db="mydatabase"
)
print(mydb)

# Creating a Database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print (x)

# Creating a Table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if Table Exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print (x)

# Primary Key
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# Day_71

# Insert Into Table

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Insert Multiple Rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# Get Inserted ID
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Sundus", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

# Select From
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Selecting Columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# fetchone() Method
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# Select With a Filter
sql = "SELECT * FROM customers WHERE name = 'sundus'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Wildcard Characters
sql = "SELECT * FROM customers WHERE address Like '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Day_72

Sort the Result
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# ORDER BY DESC
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Delete Record
sql = "delete from customers where address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "records delete")

# Delete a Table
sql = "drop table customers"
mycursor.execute(sql)

# Day_73

# Update Table
sql = "update customers set address = 'Canyon 123' where address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "records affected")

# Limit the Result
sql = "SELECT * FROM customers limit 5"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Start From Another Position
sql = "SELECT * FROM customers limit 5 offset 2"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# day_74_75

# Task_1
txt = open("hello.txt", "rt")
print(txt.readline())
print(txt.readline())
print(txt.readline())

txt = open("hello.txt", "a")
txt.write("The best way we learn anything is by practice and exercise questions")

txt = open("hello.txt", "rt")
print(txt.readline())
print(txt.readline())
print(txt.readline())
print(txt.readline())
# Task_2

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="12345678",
    db="MyEmployee"
)

# Creating a Database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MyEmployee")

mycursor.execute("CREATE TABLE MyEmployee (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255),"
                 " Age INT(25), Gender VARCHAR(255), salary INT(25))")



sql = "INSERT INTO MyEmployee (fname, lname, Age, Gender, salary) " \
      "VALUES (%s, %s, %s, %s, %s )"
val = [
  ('Ahmad', 'Ali', 30, 'Male', 10000),
  ('Khalid', 'Muhammad', 34, 'Male', 7000),
  ('Norah', 'Saleh', 29, 'Female', 7000)
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM MyEmployee")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
mycursor.execute("SELECT fname, Gender, salary FROM MyEmployee ")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
mycursor.execute("SELECT * FROM MyEmployee order by fname DESC")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("delete FROM MyEmployee where Age = 34")
mycursor.execute("SELECT * FROM MyEmployee")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


# Task_3
with open("hello.txt", "r") as txt:
    array = []
    for line in txt:
        array.append(line)
print(array)