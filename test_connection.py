from scripts.database_connection import get_connection


connection = get_connection()


if connection:
    print("Connected successfully!")
    connection.close()
else:
    print("Connection failed")