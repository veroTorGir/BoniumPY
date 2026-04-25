import pandas as pd

def describir_datos(data_frame_limpio):
    print(f"numero de filas: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas: {data_frame_limpio.shape[1]}")
    print(f"columnas disponibles: {list(data_frame_limpio)}")
    print(f"estadisticas:\n{data_frame_limpio[['id', 'fk_user']].describe()}")
    print(f"valores modalidad:\n{data_frame_limpio['modalidad'].value_counts()}")
    print(f"fecha minima: {data_frame_limpio['fecha'].min()}")
    print(f"fecha maxima: {data_frame_limpio['fecha'].max()}")