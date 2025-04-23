import sqlite3

conn = None
# baza relacyjna
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    print("Baza danych zosytała podłączona")

    query = """
    CREATE TABLE company (
    id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    age INT NOT NULL,
    salary REAL);
    """

    # cursor.execute(query)
    # conn.commit()

    insert = """
    INSERT INTO company (id,name,age,salary) 
    VALUES (1,'Radek',31,15000);"""

    cursor.execute(insert)
    conn.commit()

except sqlite3.Error as e:
    print("Bład", e)
finally:
    if conn:
        conn.close()
