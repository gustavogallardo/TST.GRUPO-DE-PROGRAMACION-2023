import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="root", database="proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

# Leer los propietarios desde la tabla
propietarios = conexion_bd.leer_propietarios()
for propietario in propietarios:
    print(propietario)

print("Fin tabla propietarios")

conexion_bd.ingresar_propietario(id_propietario=1, nombre="Juan", apellido="Pérez", fecha_nacimiento="1990-01-01")

# Leer los propietarios desde la tabla
propietarios = conexion_bd.leer_propietarios()
for propietario in propietarios:
    print(propietario)

print("Fin tabla propietarios")

# Desconectar de la base de datos
conexion_bd.disconnect()