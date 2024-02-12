import sqlite3

# create a connection to the database
conn = sqlite3.connect('KRIS_CALLIER_join.sqlite3')

# create a cursor object
c = conn.cursor()

# create the tables
c.execute('''CREATE TABLE table1
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              foreign_key INTEGER,
              description TEXT)''')

c.execute('''CREATE TABLE table2
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              logical_key TEXT,
              foreign_key INTEGER,
              description TEXT)''')

c.execute('''CREATE TABLE table3
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              logical_key TEXT,
              foreign_key INTEGER,
              description TEXT)''')

# insert data into the tables
c.execute("INSERT INTO table1 (foreign_key, description) VALUES (1, 'Table 1 row 1')")
c.execute("INSERT INTO table1 (foreign_key, description) VALUES (2, 'Table 1 row 2')")
c.execute("INSERT INTO table1 (foreign_key, description) VALUES (3, 'Table 1 row 3')")

c.execute("INSERT INTO table2 (logical_key, foreign_key, description) VALUES ('key1', 1, 'Table 2 row 1')")
c.execute("INSERT INTO table2 (logical_key, foreign_key, description) VALUES ('key2', 2, 'Table 2 row 2')")
c.execute("INSERT INTO table2 (logical_key, foreign_key, description) VALUES ('key3', 3, 'Table 2 row 3')")

c.execute("INSERT INTO table3 (logical_key, foreign_key, description) VALUES ('key1', 1, 'Table 3 row 1')")
c.execute("INSERT INTO table3 (logical_key, foreign_key, description) VALUES ('key2', 2, 'Table 3 row 2')")
c.execute("INSERT INTO table3 (logical_key, foreign_key, description) VALUES ('key3', 3, 'Table 3 row 3')")

# display the rows of the three tables
print("Table 1:")
for row in c.execute("SELECT * FROM table1"):
    print(row)

print("Table 2:")
for row in c.execute("SELECT * FROM table2"):
    print(row)

print("Table 3:")
for row in c.execute("SELECT * FROM table3"):
    print(row)

# join two tables
print("Join table 1 and table 2:")
for row in c.execute("SELECT * FROM table1 JOIN table2 ON table1.id = table2.foreign_key"):
    print(row)

# join all three tables
print("Join all three tables:")
for row in c.execute("SELECT * FROM table1 JOIN table2 ON table1.id = table2.foreign_key JOIN table3 ON table2.id = "
                     "table3.foreign_key"):
    print(row)

# commit the changes and close the connection
conn.commit()
conn.close()
