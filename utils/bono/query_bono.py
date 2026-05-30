import pandas as pd

def obtener_bonos_activos(df):
    """Bonos con todos los campos obligatorios válidos y id/precio > 0."""
    activos = df.dropna(subset=["id", "nombre", "precio"])
    activos = activos[(activos["id"] > 0) & (activos["precio"] > 0)]
    return activos

def bonos_por_nombre(df, nombre):
    """Filtra todos los bonos de un nombre específico."""
    return df[df["nombre"] == nombre]

def bonos_por_precio_maximo(df, precio_max):
    """Filtra bonos cuyo precio es menor o igual al máximo indicado."""
    return df[df["precio"] <= precio_max]
