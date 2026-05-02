"""
HU 3: Simulación y exportación de datos (USUARIO)

Como desarrollador quiero simular datos de usuarios para pruebas

Módulo modularizado para generar, simular y exportar datos de usuarios
con +1000 registros, correos únicos y roles asignados.
"""

import pandas as pd
from utils.orden.simulacion_usuarios import simular_y_exportar_usuarios

# Opción 1: Función simplificada
df, reporte = simular_y_exportar_usuarios(
    cantidad=1500,
    directorio='datos',
    nombre_base='usuarios_test',
    semilla=42  # Para reproducibilidad
)

# Opción 2: Usar clase directamente
from utils.orden.simulacion_usuarios import SimulacionUsuarios

simulador = SimulacionUsuarios(cantidad_usuarios=2000, semilla=123)
df = simulador.simular_usuarios()
simulador.mostrar_muestra(n=10)
simulador.exportar_multiformato(directorio='datos')
