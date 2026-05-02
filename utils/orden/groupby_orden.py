import pandas as pd

def agrupar_por_usuario(df):
    """Total de órdenes agrupadas por usuario."""
    return (
        df.groupby("fk_user")
        .size()
        .reset_index(name="total_ordenes")
        .sort_values("total_ordenes", ascending=False)
    )

def agrupar_por_producto(df):
    """Total de órdenes agrupadas por plato principal."""
    return (
        df.groupby("fk_producto_plato")
        .size()
        .reset_index(name="total_ordenes")
        .sort_values("total_ordenes", ascending=False)
    )
