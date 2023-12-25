
import os
import platform
import sys

# Obtener directorio actual
directorio_actual = os.getcwd()

# Obtener información sobre la plataforma
sistema_operativo = platform.system()
nombre_de_maquina = platform.node()
version_del_sistema = platform.version()

# Obtener version de python
version_de_python = sys.version

#Obtener la ruta del ejecutable de python
ruta_de_ejecutable = sys.executable

# Colores para la mejor distincion

gris = "\033[30m"
rojo = "\033[31m"
verde = "\033[32m"
amarillo = "\033[33m"
magenta = "\033[34m"
rosa = "\033[35m"
aqua = "\033[36m"
blanco = "\033[37m"

# espacio
e = "\n\n"


print(f"{e}{rojo}{directorio_actual}{e}{verde}Sistema operativo: \t{magenta}{sistema_operativo}\n{verde}Version de Python: \t{magenta}{version_de_python}\n{verde}Nombre de la maquina: \t{magenta}{nombre_de_maquina}\n{verde}Ruta: \t\t\t{magenta}{ruta_de_ejecutable}\n{verde}Version del sistema: \t{magenta}{version_del_sistema}{e}{blanco}\tDescrifrado de redes wifi, con aircrack-ng, airodump-ng, aireplay-ng{e}")

