Cifrador:

El cifrador utiliza la biblioteca Fernet en Python para generar una clave secreta única. Esta clave se guarda en un archivo llamado "clave.key". Luego, se utiliza esta clave para cifrar archivos específicos (PDF, DOC, TXT) en el directorio actual. El contenido de los archivos se lee en modo binario, se cifra y se guarda en nuevos archivos con la extensión ".cifrado". Los archivos originales se eliminan para preservar la seguridad de la información.

Descifrador:

El descifrador carga la clave desde el archivo "clave.key". Utiliza esta clave para descifrar archivos cifrados en el directorio actual. Lee el contenido cifrado, lo descifra y lo guarda en nuevos archivos sin la extensión ".cifrado". Los archivos cifrados originales se eliminan. La gestión segura de la clave es esencial para garantizar el éxito del descifrado. Este proceso sigue principios de cifrado simétrico, donde la misma clave se utiliza tanto para cifrar como para descifrar.


OJO, NO ESTÁ ORIENTADO COMO #RANSOMWARE, SOLO ES UN CIFRADOR PARA NUESTROS ARCHIVOS, no lo uséis para cosas de malos.
