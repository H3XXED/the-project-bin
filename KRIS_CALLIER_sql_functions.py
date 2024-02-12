import sqlite3

# Connect to the database
conn = sqlite3.connect(r'C:\Users\Kris\Desktop\Classes\CSC 2017 Python\census2000names.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Get the list of table names in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()

# Print the table names
for name in table_names:
    print(name[0])

# Print the schema for each table
for name in table_names:
    print(f"Table: {name[0]}")
    cursor.execute(f"PRAGMA table_info('{name[0]}')")
    columns = cursor.fetchall()
    for column in columns:
        print(f"  Column: {column[1]} ({column[2]})")

# Print the number of rows for each table
for name in table_names:
    cursor.execute(f"SELECT COUNT(*) FROM {name[0]}")
    count = cursor.fetchone()[0]
    print(f"Table: {name[0]}, Rows: {count}")

# Retrieve the maximum count from the 'surname' table
cursor.execute('SELECT MAX(count) FROM surnames')
max_name = cursor.fetchone()[0]
print(f"The largest name count in the database is {max_name}.")

# Retrieve the average percent of white in the 'surname' table
cursor.execute('SELECT AVG(pctwhite) FROM surnames')
avg_pct = cursor.fetchone()[0]
print(f"The average percent of white in the database is {avg_pct}.")

# Retrieve the count of 'prop100k' in the 'surname' table
cursor.execute('SELECT COUNT(prop100k) FROM surnames')
count_prop = cursor.fetchone()[0]
print(f"The count of prop100k in the database is {count_prop}.")

# Retrieve the maximum count of names in the top 10 ranks
cursor.execute('SELECT MAX(count) FROM surnames WHERE rank <= 10')
max_name = cursor.fetchone()[0]
print(f"The largest name count in the top 10 ranks is {max_name}.")

# Retrieve the smallest count of names in the bottom 10 ranks
cursor.execute('SELECT MIN(count) FROM surnames WHERE rank >= 90')
min_name = cursor.fetchone()[0]
print(f"The smallest name count in the bottom 10 ranks is {min_name}.")

# Retrieve the total count of names in the rank range of 50 to 100
cursor.execute('SELECT SUM(count) FROM surnames WHERE rank BETWEEN 50 AND 100')
sum_count = cursor.fetchone()[0]
print(f"The total count of names in the rank range of 50 to 100 is {sum_count}.")

# Close the database connection
conn.close()
