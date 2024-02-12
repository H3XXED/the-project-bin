import sqlite3

# create a connection to the database
conn = sqlite3.connect('KRIS_CALLIER_Sports.sqlite3')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# create a table called "baseball_players"
cursor.execute('''CREATE TABLE baseball_players (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_name TEXT,
                    home_runs INTEGER,
                    batting_avg REAL,
                    rbi INTEGER
                )''')

# insert sample data into the table
cursor.execute("INSERT INTO baseball_players (player_name, home_runs, batting_avg, rbi) VALUES ('Babe Ruth', 714, 0.342, 2214)")
cursor.execute("INSERT INTO baseball_players (player_name, home_runs, batting_avg, rbi) VALUES ('Hank Aaron', 755, 0.305, 2297)")
cursor.execute("INSERT INTO baseball_players (player_name, home_runs, batting_avg, rbi) VALUES ('Lou Gehrig', 493, 0.34, 1995)")
cursor.execute("INSERT INTO baseball_players (player_name, home_runs, batting_avg, rbi) VALUES ('Ty Cobb', 117, 0.366, 1944)")
cursor.execute("INSERT INTO baseball_players (player_name, home_runs, batting_avg, rbi) VALUES ('Willie Mays', 660, 0.302, 1903)")

# commit changes to the database
conn.commit()

# select all rows and columns from the table
cursor.execute("SELECT * FROM baseball_players")
print(cursor.fetchall())

# select only the players with a batting average above .320
cursor.execute("SELECT * FROM baseball_players WHERE batting_avg > 0.32")
print(cursor.fetchall())

# select only the players with more than 2000 RBI
cursor.execute("SELECT * FROM baseball_players WHERE rbi > 2000")
print(cursor.fetchall())

# select only Babe Ruth's stats
cursor.execute("SELECT * FROM baseball_players WHERE player_name = 'Babe Ruth'")
print(cursor.fetchall())

# update Ty Cobb's number of home runs to 118
cursor.execute("UPDATE baseball_players SET home_runs = 118 WHERE player_name = 'Ty Cobb'")

# delete Willie Mays from the table
cursor.execute("DELETE FROM baseball_players WHERE player_name = 'Willie Mays'")

# commit changes to the database
conn.commit()

# close the cursor and database connection
cursor.close()
conn.close()
