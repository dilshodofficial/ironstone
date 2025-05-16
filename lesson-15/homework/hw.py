import sqlite3

conn = sqlite3.connect("eighth.db")

cursor = conn.cursor()

cursor.execute(
  """
  create table Roster(
  Name text,
  Species text,
  Age int
  )
  """
)

cursor.execute("insert into Roster values (?, ?, ?)", ('Benjamin Sisko', 'Human', 40))
cursor.execute("insert into Roster values (?, ?, ?)", ('Jadzia Dax', 'Trill', 300))
cursor.execute("insert into Roster values (?, ?, ?)", ('Kira Nerys', 'Bajoran', 29))

conn.commit()

cursor.execute("select * from Roster")
print(cursor.fetchall())

cursor.execute("""UPDATE Roster SET Name = ? WHERE Name = ?""", ('Ezri Dax', 'Jadzia Dax'))

conn.commit()

cursor.execute("select * from Roster")
print(cursor.fetchall())

nage = cursor.execute("""select name, age from Roster where Species = 'Bajoran'""")

nage.fetchall()
