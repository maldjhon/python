import mysql.connector
from cryptography.fernet import Fernet

# Leer la clave desde el archivo
with open(r'D:\Documentos\Proyectos\python\clave.key', 'rb') as key_file:
    key = key_file.read()

# Leer la contraseña cifrada desde el archivo
with open(r'D:\Documentos\Proyectos\python\contraseña_cifrada.bin', 'rb') as archivo_cifrado:
    contraseña_cifrada = archivo_cifrado.read()

# Descifrar la contraseña
cipher_suite = Fernet(key)
contraseña_descifrada = cipher_suite.decrypt(contraseña_cifrada).decode()

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=contraseña_descifrada,
    database="dev"
)

cursor = conexion.cursor()

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

# Cerrar la conexión
cursor.close()
conexion.close()
