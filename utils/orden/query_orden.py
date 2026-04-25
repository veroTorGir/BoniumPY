import pandas as pd

def obtener_ordenes_activas(df):
    """Órdenes con todos los campos obligatorios válidos y id > 0."""
    activas = df.dropna(subset=["id", "fk_user", "fk_producto_plato", "modalidad"])
    activas = activas[activas["id"] > 0]
    return activas

def ordenes_por_usuario(df, fk_user):
    """Filtra todas las órdenes de un usuario específico."""
    return df[df["fk_user"] == fk_user]

def ordenes_por_fecha(df, fecha):
    """Filtra órdenes de una fecha específica (formato 'YYYY-MM-DD')."""
    return df[df["fecha"] == pd.to_datetime(fecha)]
