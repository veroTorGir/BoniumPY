def calcular_promedio_precio_por_tipo(data_frame_limpio):
    """Calcula el precio promedio agrupado por tipo de producto."""
    return data_frame_limpio.groupby("tipo")["precio"].mean().reset_index(name="precio_promedio")

def contar_productos_por_estado(data_frame_limpio):
    """Cuenta cuántos productos hay en cada estado."""
    return data_frame_limpio.groupby("estado").size().reset_index(name="total_productos")
