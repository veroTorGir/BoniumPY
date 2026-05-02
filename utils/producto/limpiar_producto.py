import pandas as pd

def limpiar_productos(data_frame_sucio):
    """
    Limpieza de productos simulados:
    - Normaliza texto en nombre, tipo y estado
    - Valida estados permitidos
    - Convierte precios a numéricos y elimina inválidos
    - Elimina registros nulos en campos obligatorios
    - Elimina duplicados
    """
    data_frame_limpio = data_frame_sucio.copy()

    # Normalizar texto
    for columna in ["nombre", "tipo", "estado"]:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # Validar estados
    estados_validos = ["activo", "inactivo", "agotado"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(estados_validos), pd.NA
    )

    # Validar precios
    data_frame_limpio["precio"] = pd.to_numeric(data_frame_limpio["precio"], errors="coerce")
    data_frame_limpio = data_frame_limpio[data_frame_limpio["precio"] > 0]

    # Campos obligatorios
    columnas_obligatorias = ["id", "nombre", "precio", "estado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
