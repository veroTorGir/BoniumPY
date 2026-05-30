"""
Módulo de graficación para bonos - BoniumPY
Proporciona funciones para visualizar datos de bonos mediante gráficos
utilizando matplotlib y seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta por defecto para guardar gráficos de bonos
RUTA_GRAFICOS = os.path.join(os.path.dirname(__file__), "..", "..", "graficos")


def crear_ruta_si_no_existe(ruta_destino):
    """
    Crea la carpeta destino si no existe.
    
    Args:
        ruta_destino (str): Ruta de la carpeta a crear
    """
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_lineas(datos_agrupados, columna_eje_x, columna_eje_y,
                    titulo="Gráfico de líneas", color_linea="#2196F3",
                    nombre_archivo="lineas.png", ruta_destino=RUTA_GRAFICOS):
    """
    Dibuja un gráfico de líneas con marcadores, útil para mostrar tendencias
    en el tiempo (ej: bonos por fecha).
    
    Args:
        datos_agrupados (pd.DataFrame): DataFrame con datos agrupados
        columna_eje_x (str): Nombre de la columna para el eje X
        columna_eje_y (str): Nombre de la columna para el eje Y
        titulo (str): Título del gráfico
        color_linea (str): Color hex de la línea
        nombre_archivo (str): Nombre del archivo a guardar
        ruta_destino (str): Ruta donde guardar el gráfico
    """
    crear_ruta_si_no_existe(ruta_destino)
    
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    
    area_dibujo.plot(
        datos_agrupados[columna_eje_x],
        datos_agrupados[columna_eje_y],
        marker="o",
        color=color_linea,
        linewidth=2
    )
    
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_eje_x, fontsize=12)
    area_dibujo.set_ylabel(columna_eje_y, fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    
    print(f"Gráfico de líneas guardado en: {ruta_completa}")


def graficar_barras(datos_agrupados, columna_categorias, columna_valores,
                    titulo="Gráfico de barras", color_barras="#4CAF50",
                    nombre_archivo="barras.png", ruta_destino=RUTA_GRAFICOS):
    """
    Dibuja un gráfico de barras verticales, útil para comparar cantidades
    entre categorías (ej: bonos por nombre).
    
    Args:
        datos_agrupados (pd.DataFrame): DataFrame con datos agrupados
        columna_categorias (str): Nombre de la columna con categorías
        columna_valores (str): Nombre de la columna con valores
        titulo (str): Título del gráfico
        color_barras (str): Color hex de las barras
        nombre_archivo (str): Nombre del archivo a guardar
        ruta_destino (str): Ruta donde guardar el gráfico
    """
    crear_ruta_si_no_existe(ruta_destino)
    
    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    
    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )
    
    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    
    print(f"Gráfico de barras guardado en: {ruta_completa}")


def graficar_torta(datos_agrupados, columna_etiquetas, columna_valores,
                   titulo="Gráfico de torta", lista_colores=None,
                   nombre_archivo="torta.png", ruta_destino=RUTA_GRAFICOS):
    """
    Dibuja un gráfico de torta con porcentajes, útil para mostrar la
    proporción de cada categoría.
    
    Args:
        datos_agrupados (pd.DataFrame): DataFrame con datos agrupados
        columna_etiquetas (str): Nombre de la columna con etiquetas
        columna_valores (str): Nombre de la columna con valores
        titulo (str): Título del gráfico
        lista_colores (list): Lista de colores hex (opcional)
        nombre_archivo (str): Nombre del archivo a guardar
        ruta_destino (str): Ruta donde guardar el gráfico
    """
    crear_ruta_si_no_existe(ruta_destino)
    
    if lista_colores is None:
        lista_colores = ["#FF9800", "#2196F3", "#4CAF50", "#E91E63", "#9C27B0"]
    
    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    cantidad_categorias = len(datos_agrupados)
    
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5}
    )
    
    area_dibujo.set_title(titulo, fontsize=14)
    plt.tight_layout()
    
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    
    print(f"Gráfico de torta guardado en: {ruta_completa}")


def graficar_mapa_calor(datos_agrupados, columna_filas, columna_columnas, columna_valores,
                        titulo="Mapa de calor", paleta_color="YlOrRd",
                        nombre_archivo="mapa_calor.png", ruta_destino=RUTA_GRAFICOS):
    """
    Dibuja un mapa de calor pivotando los datos en filas y columnas con
    intensidad por valor.
    
    Args:
        datos_agrupados (pd.DataFrame): DataFrame con al menos 3 columnas
        columna_filas (str): Nombre de la columna para filas
        columna_columnas (str): Nombre de la columna para columnas
        columna_valores (str): Nombre de la columna con valores
        titulo (str): Título del gráfico
        paleta_color (str): Paleta de colores seaborn
        nombre_archivo (str): Nombre del archivo a guardar
        ruta_destino (str): Ruta donde guardar el gráfico
    """
    crear_ruta_si_no_existe(ruta_destino)
    
    tabla_pivote = datos_agrupados.pivot_table(
        index=columna_filas,
        columns=columna_columnas,
        values=columna_valores,
        aggfunc="sum",
        fill_value=0
    )
    
    figura, area_dibujo = plt.subplots(figsize=(10, 6))
    
    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap=paleta_color,
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )
    
    area_dibujo.set_title(titulo, fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)
    
    print(f"Mapa de calor guardado en: {ruta_completa}")
