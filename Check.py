import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('healthcare.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS patients
                  (id INTEGER PRIMARY KEY, name TEXT, heart_rate INTEGER)''')
conn.commit()

# Safely inserting data using parameterized queries
def add_patient(name, heart_rate):
    cursor.execute("INSERT INTO patients (name, heart_rate) VALUES (?, ?)", (name, heart_rate))
    conn.commit()

# Example usage
add_patient("John Doe", 75)

# Fetching data safely
def get_patient(name):
    cursor.execute("SELECT * FROM patients WHERE name=?", (name,))
    return cursor.fetchone()

print(get_patient("John Doe"))

conn.close()
