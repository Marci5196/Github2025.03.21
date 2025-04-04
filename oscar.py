from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='oscar')

cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print("-------------")

cursor.execute("USE oscar;")

cursor.execute("SELECT film.ev, film.cim FROM film WHERE nyert ORDER BY ev;")
for film in cursor:
    print(film)
print("-------------")

cursor.execute("SELECT film.ev FROM film GROUP BY ev HAVING Count(id)>=10;")
for film in cursor:
    print(film)
print("-------------")

cursor.execute("SELECT film.cim FROM film WHERE ev AND bemutato BETWEEN 1939 AND 1945")
for film in cursor:
    print(film)
print("-------------")

    
    
   
