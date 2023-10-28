from cryptography.fernet import Fernet
import os
import glob

def cargar_clave(nombre_archivo="clave.key"):
    return open(nombre_archivo, "rb").read()

def descifrar_archivo(nombre_archivo_cifrado, clave):
    cipher_suite = Fernet(clave)

    with open(nombre_archivo_cifrado, "rb") as archivo_cifrado:
        contenido_cifrado = archivo_cifrado.read()
        contenido_descifrado = cipher_suite.decrypt(contenido_cifrado)

    # Guardar el archivo descifrado
    nombre_archivo_descifrado = nombre_archivo_cifrado.replace(".cifrado", "")
    with open(nombre_archivo_descifrado, "wb") as archivo_descifrado:
        archivo_descifrado.write(contenido_descifrado)

    # Eliminar el archivo cifrado
    os.remove(nombre_archivo_cifrado)

# Cargar la clave
clave = cargar_clave()

# Obtener todos los archivos cifrados en el directorio actual
archivos_cifrados = glob.glob("*.cifrado")

# Descifrar todos los archivos cifrados
for archivo_cifrado in archivos_cifrados:
    descifrar_archivo(archivo_cifrado, clave)
