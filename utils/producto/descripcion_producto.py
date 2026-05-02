def describir_productos(data_frame_limpio):

    print(f"Filas: {data_frame_limpio.shape[0]}")
    print(f"Columnas: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(data_frame_limpio)}")
    print("\nEstadísticas de precios:")
    print(data_frame_limpio["precio"].describe())
    print("\nDistribución de tipos:")
    print(data_frame_limpio["tipo"].value_counts())
    print("\nDistribución de estados:")
    print(data_frame_limpio["estado"].value_counts())
