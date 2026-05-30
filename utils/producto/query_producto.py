def obtener_productos_activos(data_frame_limpio):
    """Filtra productos con estado 'activo'."""
    return data_frame_limpio[data_frame_limpio["estado"] == "activo"]

def obtener_productos_por_tipo(data_frame_limpio, tipo_producto):
    """Filtra productos según su tipo (ejemplo: 'bebida')."""
    return data_frame_limpio[data_frame_limpio["tipo"] == tipo_producto]

def obtener_productos_por_precio(data_frame_limpio, precio_minimo, precio_maximo):
    """Filtra productos dentro de un rango de precios."""
    return data_frame_limpio[
        (data_frame_limpio["precio"] >= precio_minimo) & (data_frame_limpio["precio"] <= precio_maximo)
    ]
