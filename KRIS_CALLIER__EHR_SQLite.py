import sqlite3

# create a connection to the database
conn = sqlite3.connect('ehr_database.db')
c = conn.cursor()


def create_table():
    # create the patients table
    c.execute('''CREATE TABLE IF NOT EXISTS patients
                (name TEXT, age INTEGER, weight REAL, gender TEXT)''')
    print("Table created successfully")


def insert_data():
    # insert 10 existing patients
    patients = [('Alice', 25, 130.0, 'F'),
                ('Bob', 35, 175.0, 'M'),
                ('Charlie', 45, 200.0, 'M'),
                ('Dave', 50, 180.0, 'M'),
                ('Eve', 28, 120.0, 'F'),
                ('Frank', 40, 190.0, 'M'),
                ('Grace', 30, 140.0, 'F'),
                ('Harry', 55, 170.0, 'M'),
                ('Ivy', 20, 110.0, 'F'),
                ('Jack', 32, 160.0, 'M')]

    c.executemany("INSERT INTO patients VALUES (?, ?, ?, ?)", patients)
    conn.commit()
    print("Data inserted successfully")


def add_patient(name, age, weight, gender):
    # add a new patient to the table
    c.execute("INSERT INTO patients VALUES (?, ?, ?, ?)", (name, age, weight, gender))
    conn.commit()
    print("New patient added successfully")


def get_weight(name):
    # retrieve a patient's weight based on their name
    c.execute("SELECT weight FROM patients WHERE name=?", (name,))
    weight = c.fetchone()
    if weight:
        print(f"{name}'s weight is {weight[0]}")
    else:
        print(f"{name} not found in the database")


def display_over_age(age):
    # display all patients over a certain age
    c.execute("SELECT * FROM patients WHERE age > ?", (age,))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print(f"No patients found over age {age}")


def display_all():
    # display all rows and columns in the table
    c.execute("SELECT * FROM patients")
    rows = c.fetchall()
    for row in rows:
        print(row)


def update_patient(name, age, weight):
    # update a patient's weight and age based on their name
    c.execute("UPDATE patients SET age=?, weight=? WHERE name=?", (age, weight, name))
    conn.commit()
    print(f"{name}'s age and weight updated successfully")


def remove_patient(name):
    # remove a patient based on their name
    c.execute("DELETE FROM patients WHERE name=?", (name,))
    conn.commit()
    print(f"{name} removed successfully")


if __name__ == '__main__':
    create_table()
    insert_data()

    # call each function to demonstrate functionality
    add_patient('Karen', 42, 150.0, 'F')
    get_weight('Alice')
    display_over_age(30)
    display_all()
    update_patient('Bob', 40, 180.0)
    remove_patient('Charlie')

    # close the database connection
    conn.close()
