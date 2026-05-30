"""
HU 5: Agrupación de datos (USUARIO)

Como analista quiero agrupar usuarios para obtener métricas

Módulo modularizado para agrupación, análisis de métricas y comparaciones
utilizando pandas groupby() y agregaciones.
"""

import pandas as pd
from utils.orden.simulacion_usuarios import simular_y_exportar_usuarios
from utils.orden.agrupacion_usuarios import AgrupacionUsuarios

# Simular datos
df, _ = simular_y_exportar_usuarios(cantidad=1000)

# Crear agrupador
agrupador = AgrupacionUsuarios(df)

# GROUPBY POR ROL
conteo_rol = agrupador.contar_usuarios_por_rol()
print(conteo_rol)
# Output:
#    fk_rol  cantidad_usuarios  porcentaje
#        1              100        10.00
#        2              150        15.00
#        ...

# CONTEO DE USUARIOS
metricas = agrupador.metricas_comparativas_roles()
print(metricas)
# Output:
#        total_usuarios  activos  inactivos  pct_del_total  pct_activos
# fk_rol
#     1              100       85         15          10.00        85.00
#     ...

# COMPARACIÓN ENTRE ROLES
ranking = agrupador.ranking_roles()
print(ranking)
# Output:
#    ranking  rol_id  cantidad_usuarios  porcentaje
#        1       2              150        15.00
#        2       3              140        14.00
#        ...

# Análisis específicos
rol_max = agrupador.rol_con_mas_usuarios()
actividad = agrupador.usuarios_activos_por_rol()
resumen = agrupador.crear_resumen_agrupaciones()
