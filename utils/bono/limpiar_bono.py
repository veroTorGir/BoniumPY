import pandas as pd

def limpiar_bono(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Limpiar espacios en columna de texto
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].astype("string").str.strip()

    # 2. Validar nombre: solo valores del catálogo permitidos
    nombres_validos = [
        "Bono Bienvenida",
        "Bono Cumpleaños",
        "Bono Fidelidad",
        "Bono Estudiante",
        "Bono Fin de Semana",
        "Bono Familiar",
        "Bono Ejecutivo",
        "Bono Premium",
    ]
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].where(
        data_frame_limpio["nombre"].isin(nombres_validos), pd.NA
    )

    # 3. Convertir id y precio a numérico
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["precio"] = pd.to_numeric(data_frame_limpio["precio"], errors="coerce")

    # 4. Eliminar registros nulos en campos obligatorios
    columnas_obligatorias = ["id", "nombre", "precio"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 5. Eliminar ids y precios inválidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["precio"] > 0]

    # 6. Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
