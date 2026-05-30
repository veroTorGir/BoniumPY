"""
HU 4: Transformación con query() (USUARIO)

Como analista quiero filtrar usuarios para análisis

Módulo modularizado para transformaciones, filtrados y consultas de usuarios
utilizando pandas query() y otras técnicas de filtrado.
"""

import pandas as pd
from utils.orden.simulacion_usuarios import simular_y_exportar_usuarios
from utils.orden.transformacion_usuarios import TransformacionUsuarios

# Simular datos
df, _ = simular_y_exportar_usuarios(cantidad=1000)

# Crear transformador
transformador = TransformacionUsuarios(df)
transformador.extraer_dominio_correo()

# Ejemplos de filtrado
df_rol_1 = transformador.filtrar_por_rol(rol_id=1)
df_gmail = transformador.filtrar_por_dominio_correo('gmail.com')
df_activos = transformador.filtrar_por_estado('activo')

# Análisis
distribucion_roles = transformador.obtener_distribucion_roles()
distribucion_dominios = transformador.obtener_distribucion_dominios(top=5)
resumen = transformador.crear_resumen_ejecutivo()

# Filtrado combinado
df_filtrado = transformador.filtrar_por_criterios_multiples({
    'fk_rol': 1,
    'estado': 'activo'
})
