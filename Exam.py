import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Website (Id INT PRIMARY KEY AUTOINCREMENT, Login TEXT, Password TEXT); ")
connection.commit()

login = input("Do you want to login or register:")
if login == 'login':
    name = input("Login:")
    name2 = input("Password:")
    cur.execute(f"SELECT rowid FROM Website WHERE login='{name}' and password='{name2}'")
    connection.commit()
    res = cur.fetchall()
    if res != []:
       cur.execute(f"INSERT INTO Website (Login, Password) VALUES ('{name}', '{name2}');")
       connection.commit()
       print("Succesfully Login!")
       connection.commit()
    if res == []:
        print("Invalid Login or Password")
if login == 'register':
    name = input("Register:")
    name2 = input("Password:")
    cur.execute(f"SELECT rowid FROM Website WHERE login='{name}'")
    connection.commit()
    res = cur.fetchall()
    if res == []:
       cur.execute(f"INSERT INTO Website (Login, Password) VALUES ('{name}', '{name2}');")
       connection.commit()
       print("Succesfully Register!")
       connection.commit()
    if res != []:
        print('This Login already exist')

# cur.execute(f"DELETE FROM Website WHERE rowid=2")
# connection.commit()