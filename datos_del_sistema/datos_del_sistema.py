import sys 
import os
import platform


# Colores para la mejor distincion
gris = "\033[30m"
rojo = "\033[31m"
verde = "\033[32m"
amarillo = "\033[33m"
magenta = "\033[34m"
rosa = "\033[35m"
aqua = "\033[36m"
blanco = "\033[37m"

# Obtener ruta actual
directorio_actual = os.getcwd()

# Obtener ruta del archivo actual
ruta_de_archivo_actual = sys.executable

# Obtener el sistema
sistema = platform.system()

# Obtener version de sistema
version_de_sistema = platform.version()

# Obtener maquina
maquina = platform.node()

print(f"""
{blanco}Sistema:    {gris}{sistema}
{blanco}Version:    {gris}{version_de_sistema}
{blanco}Maquina:    {gris}{maquina}
{blanco}Directorio: {gris}{directorio_actual}
{blanco}Ejecutable: {gris}{ruta_de_archivo_actual}
""")