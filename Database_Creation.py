import requests
import sqlite3


def create_database():
    """Creates the database for main.py"""
    activities = []
    for i in range(150):
        response = requests.get("https://www.boredapi.com/api/activity/")
        activity = response.json()
        activities.append(activity)

    # Connect to the database
    conn = sqlite3.connect('activities.db')

    # Create a new table for the activities
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS activities''')
    c.execute('''CREATE TABLE IF NOT EXISTS activities
                (activity TEXT,
                activity_type TEXT,
                participants INTEGER,
                price REAL,
                link TEXT,
                key INTEGER)''')

    # Insert each activity into the table
    for activity in activities:
        activity_type = activity['type']
        participants = activity['participants']
        price = activity['price']
        link = activity['link']
        key = activity['key']
        c.execute(
            "INSERT OR IGNORE INTO activities (activity, activity_type, participants, price, link, key) VALUES (?, "
            "?, ?, ?, ?, ?)",
            (activity['activity'], activity_type, participants, price, link, key))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
