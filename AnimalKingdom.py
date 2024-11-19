import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ====== CREATE ======
# cur.execute("CREATE TABLE animal (login TEXT); ")
# connection.commit()

name = input("Тип звіра:")
name2 = input("Звір:")
cur.execute(f"INSERT INTO animal (login) VALUES ('{name}, {name2}');")
connection.commit()
print("Login added!")

# ====== SELECT ======
# cur.execute(f"SELECT * FROM animal WHITE rowid=2;")
# cur.execute(f"SELECT * FROM animal WHITE login='admin234234';")
# connection.commit()
# res = cur.fetchall()
# print(res)

connection.close()