import sqlite3


def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                title TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """)
        connection.commit()

    except sqlite3.Error as error:
        return error
    
    finally:
        return "Table Created"

def add_data(connection, title, username, password):
    if title !="" and username!="" and password!="":
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO user (title, username, password)
                        VALUES
                        (?, ?, ?)
            """, (title, username, password))
            connection.commit()

        except sqlite3.Error as error:
            return error
        
        finally:
            return "Data Added Successfully"

def delete_data(connection, title):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM user
            WHERE title = ? ;
""", (title,))
        connection.commit()

    except sqlite3.Error as error:
        return error
    
    finally:
        return True

def all_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user;")
        rows = cursor.fetchall()
        connection.commit()

    except sqlite3.Error as error:
        return error
    
    finally:
        return rows