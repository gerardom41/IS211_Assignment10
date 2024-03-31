import sqlite3

def connect_to_db():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS person_pet (person_id INTEGER, pet_id INTEGER)")

def clear_tables(cursor):
    cursor.execute("DELETE FROM person")
    cursor.execute("DELETE FROM pet")
    cursor.execute("DELETE FROM person_pet")

person_table = [
    (1, "James", "Smith", 41),
    (2, "Diana", "Greene", 23),
    (3, "Sara", "White", 27),
    (4, "William", "Gibson", 23),
]

pet_table = [
    (1, "Rusty", "Dalmatian", 4, 1),
    (2, "Bella", "Alaskan Malamute", 3, 0),
    (3, "Max", "Cocker Spaniel", 1, 0),
    (4, "Rocky", "Beagle", 7, 0),
    (5, "Rufus", "Cocker Spaniel", 1, 0),
    (6, "Spot", "Bloodhound", 2, 1)
]

person_pet_table = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

def insert_data(cursor):
    cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", person_table)
    cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pet_table)
    cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pet_table)

def print_all_data(cursor):
    for table in ["Person", "Pet", "Person_pet"]:
        print(f"Data from {table} table:")
        cursor.execute(f"SELECT * FROM {table}")
        print(cursor.fetchall())

def close_connection(conn):
    conn.commit()
    conn.close()

if __name__ == "__main__":
    conn, cursor = connect_to_db()
    create_tables(cursor)
    clear_tables(cursor)
    insert_data(cursor)
    print_all_data(cursor)
    close_connection(conn)
