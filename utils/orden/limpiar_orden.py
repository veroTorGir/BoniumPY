import pandas as pd
from datetime import datetime

def limpiar_simulacion(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Limpiar columnas de texto
    columnas_texto = ["fk_producto_plato", "fk_producto_adicional", "modalidad"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    # 2. Validar modalidad: solo valores permitidos
    modalidades_validas = ["en_mesa", "para_llevar"]
    data_frame_limpio["modalidad"] = data_frame_limpio["modalidad"].where(
        data_frame_limpio["modalidad"].isin(modalidades_validas), pd.NA
    )

    # 3. Evaluar columna numérica id
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])

    # 4. Evaluar columna de fecha
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"])

    # 5. Reemplazar fechas y horas nulas por valores por defecto
    fecha_default = pd.to_datetime("2026-01-01")
    hora_default = "00:00:00"
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_default)
    data_frame_limpio["hora"] = data_frame_limpio["hora"].fillna(hora_default)

    # 6. Eliminar registros nulos en campos obligatorios
    columnas_obligatorias = ["id", "fk_user", "fk_producto_plato", "modalidad"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 7. Eliminar ids inválidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    # 8. Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
