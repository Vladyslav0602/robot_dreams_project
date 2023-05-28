# Exercise 1
import sqlite3


def create_db():
    try:
        connection = sqlite3.connect(r'homework21/my_db.db')
        cursor = connection.cursor()
        print("Connected to Sqlite")
        create = """CREATE TABLE IF NOT EXISTS users(
                                                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                        first_name TEXT,
                                                        last_name TEXT, 
                                                        age INTEGER);"""
        cursor.execute(create)
        connection.commit()
        print("Database created")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed")


create_db()


def add_records():
    try:
        connection = sqlite3.connect(r'homework21/my_db.db')
        cursor = connection.cursor()
        print("Connected to Sqlite")

        sql_add_records = """INSERT INTO users(id, first_name, last_name, age)
                    VALUES('1', 'Alex', 'Smith', '22');
                INSERT INTO users(id, first_name, last_name, age)
                    VALUES('2', 'Anna', 'Grey', '20');
                INSERT INTO users(id, first_name, last_name, age)
                    VALUES('3', 'Vlad', 'Kutsyi', '23');
                INSERT INTO users(id, first_name, last_name, age)
                    VALUES('4', 'Tomas', 'One', '18');
                INSERT INTO users(id, first_name, last_name, age)
                    VALUES('5', 'Ivan', 'Fox', '20');
                INSERT INTO users(id, first_name, last_name, age)
                    VALUES('6', 'Roman', 'Good', '27');"""
        cursor.execute(sql_add_records)
        connection.commit()
        print("Recording done successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed")


add_records()


def delete_record(dev_id):
    try:
        connection = sqlite3.connect('sqlite_python.db')
        cursor = connection.cursor()
        print("Connected to Sqlite")

        sql_update_query = """DELETE from users where id = ?"""
        cursor.execute(sql_update_query, (dev_id,))
        connection.commit()
        print("Recording successfully deleted")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed")


delete_record(5)
