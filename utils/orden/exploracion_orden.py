import pandas as pd

def explorar_ordenes(df):
    print("=== EXPLORACIÓN DE ÓRDENES ===\n")

    # Cantidad de órdenes
    print(f"Total de órdenes: {len(df)}\n")

    # Estados (distribución por modalidad)
    print("Distribución por modalidad:")
    print(df["modalidad"].value_counts().to_string())
    print()

    # Frecuencia por fecha
    print("Frecuencia de órdenes por fecha:")
    print(df["fecha"].value_counts().sort_index().to_string())
    print()

    return df
