# create_db.py
import sqlite3
import os

def create_database():
    # Connect to the database (this will create it if it doesn't exist)
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    
    # Create the user table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(150) UNIQUE NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            password VARCHAR(256) NOT NULL
        )
    ''')
    
    # Create the resume table with all the new fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resume (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            address TEXT NOT NULL,
            education TEXT NOT NULL,
            skills TEXT NOT NULL,
            interpersonal_skills TEXT NOT NULL,
            experience TEXT NOT NULL,
            certificates TEXT,
            github VARCHAR(200),
            linkedin VARCHAR(200),
            layout VARCHAR(20) DEFAULT 'layout1',
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (id)
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print("Database created successfully with the new schema!")
    print("All new fields have been added to the resume table.")

if __name__ == '__main__':
    create_database() 