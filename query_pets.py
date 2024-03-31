import sqlite3

def connect_to_db():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    return conn, cursor

def query_person(cursor):
    while True:
        person_id = int(input("Enter the ID number of the person you want to look up: "))
        if person_id == -1:
            close_connection(conn)
            print("Exiting program.")
            exit()
        elif person_id <= 0:
            print("Enter -1 if you want to quit. Enter an ID number greater than 0.")
        else:
            print_person(person_id, cursor)

def print_person(person_id, cursor):
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()
    if person is None:
        print("ERROR: No person with that ID number found.")
    else:
        print(f"\nName: {person[0]} {person[1]}, {person[2]} years old")
        cursor.execute("SELECT pet_id FROM person_pet WHERE person_id = ?", (person_id,))
        pet_ids = cursor.fetchall()
        for pet_id in pet_ids:
            cursor.execute("SELECT name, breed, age, dead FROM pet WHERE id = ?", pet_id)
            pet_info = cursor.fetchone()
            print(f"{person[0]} {person[1]} owned {pet_info[0]}, a {pet_info[1]}, that was {pet_info[2]} years old.")
            if pet_info[3] == 1:
                print("This pet has passed away.")

def close_connection(conn):
    conn.commit()
    conn.close()

if __name__ == "__main__":
    conn, cursor = connect_to_db()
    query_person(cursor)
    close_connection(conn)
