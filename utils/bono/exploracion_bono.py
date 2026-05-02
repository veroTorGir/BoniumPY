import pandas as pd

def explorar_bonos(df):
    print("=== EXPLORACIÓN DE BONOS ===\n")

    # Cantidad de bonos
    print(f"Total de bonos: {len(df)}\n")

    # Distribución por nombre
    print("Distribución por nombre de bono:")
    print(df["nombre"].value_counts().to_string())
    print()

    # Estadísticas de precio
    print("Estadísticas de precio:")
    print(df["precio"].describe().to_string())
    print()

    return df
