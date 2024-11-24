import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Animal (Id INT PRIMARY KEY AUTOINCREMENT, Name TEXT, Type TEXT); ")
connection.commit()

# cur.execute(f"INSERT INTO Animal (id, Name, Type) VALUES (1, 'Лев', 'Ссавець');")
# cur.execute(f"INSERT INTO Animal (id, Name, Type) VALUES (2, 'Крокодил', 'Плазун');")
# cur.execute(f"INSERT INTO Animal (id, Name, Type) VALUES (3, 'Орел', 'Птах');")
# cur.execute(f"INSERT INTO Animal (id, Name, Type) VALUES (4, 'Морська черепаха', 'Плазун');")
# cur.execute(f"INSERT INTO Animal (id, Name, Type) VALUES (5, 'Мавпа', 'Ссавець');")
# connection.commit()

#cur.execute("SELECT * FROM Animal WHERE type='Ссавець'")
# cur.execute("SELECT * FROM Animal;")
# connection.commit()
# res = cur.fetchall()
# for row in res:
#     print(f"{row[0]}. {row[1]} - {row[2]}")

# ====== UPDATE ======
name_s = input("Old login:")
name_n = input("New login:")
cur.execute(f"SELECT rowid FROM Animal WHERE name='{name_s}';")
connection.commit()
res = cur.fetchall()
id = int(res[0][0])
cur.execute(f"UPDATE Animal SET name='{name_n}' WHERE rowid={id};")
connection.commit()

# cur.execute(f"DELETE FROM Animal WHERE rowid=6")
# connection.commit()