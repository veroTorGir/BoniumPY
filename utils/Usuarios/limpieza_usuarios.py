import pandas as pd
#from utils.orden.limpieza_usuarios import limpiar_datos_usuarios

# Cargar datos
df = pd.read_csv('usuarios.csv')

# Ejecutar limpieza (genera reporte automáticamente)
df_limpio, reporte = limpiar_datos_usuarios(df, guardar_reporte=True)

# Guardar
df_limpio.to_csv('usuarios_limpios.csv', index=False)

