import mysql.connector
user = "root"
password = "colocar contraseña mysql"
host = "localhost"
port = "3306"
database = "proyectoIntegradorv01"

midb = mysql.connector.connect(
    user=user,
    password = password,
    host = host,
    port = port,
    database = database),
print (midb)
