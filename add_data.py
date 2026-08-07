#=======================================================================
#===================TO BE RUN TO CREATE=================================
#===================& ADD DATA ON NEW DEVICES===========================
#=======================================================================
# All imports
import mysql.connector as m
from data_tuple import laptops

con = m.connect(host = 'localhost', user = '<user>', passwd = '<passwd>')

if con.is_connected():
    cur = con.cursor()
    
    #cur.execute("CREATE DATABASE IF NOT EXISTS CS_PROJECT")
    print("Database created successfully")
    
    cur.execute("USE CS_PROJECT")
    cur.execute("""CREATE TABLE IF NOT EXISTS LAPTOPS(
        LAPTOP VARCHAR(100) PRIMARY KEY,
        RAM VARCHAR(10),
        STORAGE VARCHAR(10),
        COMPANY VARCHAR(50),
        YEAR INT,
        CPU VARCHAR(70),
        OS VARCHAR(60),
        LAST_OS VARCHAR(60),
        PRICE INT
        )""")
    print("Table created successfully")

    for data in laptops:
        QUERY = """INSERT INTO LAPTOPS
                    VALUES('%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', %s)"""%(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        cur.execute(QUERY)
        con.commit()
    print("Data added successfully")
