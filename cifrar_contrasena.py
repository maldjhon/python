from cryptography.fernet import Fernet
import getpass

# Pedir al usuario que ingrese la contraseña
db_password = getpass.getpass("Introduce la contraseña de la base de datos: ")

# Generar una clave y guardarla en un archivo
key = Fernet.generate_key()
with open(r'D:\Documentos\Proyectos\python\clave.key', 'wb') as key_file:
    key_file.write(key)

# Cifrar la contraseña
cipher_suite = Fernet(key)
contraseña = db_password.encode()
contraseña_cifrada = cipher_suite.encrypt(contraseña)

# Guardar la contraseña cifrada en un archivo
with open(r'D:\Documentos\Proyectos\python\contraseña_cifrada.bin', 'wb') as archivo_cifrado:
    archivo_cifrado.write(contraseña_cifrada)