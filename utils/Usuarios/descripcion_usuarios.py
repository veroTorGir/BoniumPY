"""
HU 2: Descripción exploratoria con Pandas (USUARIO)

Como analista de datos quiero usar Pandas para describir la tabla usuario
para entender su estructura y calidad.

Módulo modularizado para análisis exploratorio de datos de usuarios.
"""

import pandas as pd
from utils.orden.descripcion_usuarios import describir_usuarios

# Cargar datos
df = pd.read_csv('usuarios.csv')

# Ejecutar análisis completo
resumen = describir_usuarios(df, mostrar_reporte=True, guardar_reporte=True)

# Acceder a información específica
print(resumen['roles'])           # Info de roles
print(resumen['conteo'])          # Conteo de usuarios
print(resumen['estructura'])      # Estructura de columnas
