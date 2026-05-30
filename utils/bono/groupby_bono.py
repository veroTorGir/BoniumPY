import pandas as pd

def agrupar_bonos_por_nombre(df):
    """Total de bonos agrupados por nombre."""
    return (
        df.groupby("nombre")
        .size()
        .reset_index(name="total_bonos")
        .sort_values("total_bonos", ascending=False)
    )

def agrupar_bonos_por_precio(df):
    """Total de bonos agrupados por precio."""
    return (
        df.groupby("precio")
        .size()
        .reset_index(name="total_bonos")
        .sort_values("precio")
    )
