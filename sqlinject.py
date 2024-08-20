import sqlite3

def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """)

def insert_patient(conn, name, age):
    with conn:
        conn.execute("INSERT INTO patients (name, age) VALUES (?, ?)", (name, age))

def search_patient(conn, name):
    with conn:
        cursor = conn.execute("SELECT * FROM patients WHERE name = ?", (name,))
        return cursor.fetchall()

def main():
    conn = connect_db('healthcare.db')
    create_table(conn)
    insert_patient(conn, 'John Doe', 30)
    patients = search_patient(conn, 'John Doe')
    for patient in patients:
        print(patient)

if __name__ == '__main__':
    main()
