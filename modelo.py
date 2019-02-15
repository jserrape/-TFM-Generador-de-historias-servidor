import sqlite3

def crear_modelo():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    # delete
    cursor.execute("""DROP TABLE historia;""")

    sql_command = """
    CREATE TABLE historia ( id INTEGER PRIMARY KEY, nombre VARCHAR(20), latitud VARCHAR(20), longitud VARCHAR(20), zoom INTEGER, descripcion VARCHAR(200));"""
    cursor.execute(sql_command)

    #sql_command = """INSERT INTO historia (staff_number, fname, lname, gender, birth_date) VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
    #cursor.execute(sql_command)

    # never forget this, if you want the changes to be saved:
    connection.commit()
    connection.close()
    print("Hola mundo")

def select_employee():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM historia")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)
    print("\n\n\n\n")
    cursor.execute("SELECT * FROM historia")
    print("\nfetch one:")
    res = cursor.fetchone()
    print(res)
