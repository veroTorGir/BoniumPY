import pandas as pd
from utils.orden.simulacion_orden import generar_simulacion
from utils.orden.limpiar_orden import limpiar_simulacion
from utils.orden.exploracion_orden import explorar_ordenes
from utils.orden.query_orden import obtener_ordenes_activas, ordenes_por_usuario, ordenes_por_fecha
from utils.orden.groupby_orden import agrupar_por_usuario, agrupar_por_producto

from utils.bono.simulacion_bono import generar_simulacion_bono
from utils.bono.limpiar_bono import limpiar_bono
from utils.bono.exploracion_bono import explorar_bonos
from utils.bono.query_bono import obtener_bonos_activos, bonos_por_nombre, bonos_por_precio_maximo
from utils.bono.groupby_bono import agrupar_bonos_por_nombre, agrupar_bonos_por_precio

# ── ORDEN ──────────────────────────────────────────────
# HU3 — Simulación: +2000 órdenes con relaciones válidas y fechas coherentes
simulaciones = generar_simulacion(2000)
simulaciones_ordenadas = pd.DataFrame(simulaciones)

# HU1 — Limpieza
simulaciones_limpias = limpiar_simulacion(simulaciones_ordenadas)

# HU2 — Exploración
explorar_ordenes(simulaciones_limpias)

# HU4 — Query
print("=== QUERIES ORDEN ===\n")
activas = obtener_ordenes_activas(simulaciones_limpias)
print(f"Órdenes activas: {len(activas)}\n")

usuario_ejemplo = simulaciones_limpias["fk_user"].dropna().iloc[0]
print(f"Órdenes del usuario {int(usuario_ejemplo)}:")
print(ordenes_por_usuario(simulaciones_limpias, usuario_ejemplo).to_string(index=False))
print()

fecha_ejemplo = simulaciones_limpias["fecha"].dropna().iloc[0]
print(f"Órdenes del {fecha_ejemplo.date()}:")
print(ordenes_por_fecha(simulaciones_limpias, fecha_ejemplo).to_string(index=False))
print()

# HU5 — GroupBy
print("=== GROUPBY ORDEN ===\n")
print("Órdenes por usuario:")
print(agrupar_por_usuario(simulaciones_limpias).to_string(index=False))
print()
print("Órdenes por producto:")
print(agrupar_por_producto(simulaciones_limpias).to_string(index=False))
print()

# ── BONO ──────────────────────────────────────────────
# HU3 — Simulación: +2000 bonos
bonos_raw = generar_simulacion_bono(2000)
bonos_df = pd.DataFrame(bonos_raw)

# HU1 — Limpieza
bonos_limpios = limpiar_bono(bonos_df)

# HU2 — Exploración
explorar_bonos(bonos_limpios)

# HU4 — Query
print("=== QUERIES BONO ===\n")
activos = obtener_bonos_activos(bonos_limpios)
print(f"Bonos activos: {len(activos)}\n")

nombre_ejemplo = bonos_limpios["nombre"].dropna().iloc[0]
print(f"Bonos de tipo '{nombre_ejemplo}':")
print(bonos_por_nombre(bonos_limpios, nombre_ejemplo).to_string(index=False))
print()

print("Bonos con precio <= 15000:")
print(bonos_por_precio_maximo(bonos_limpios, 15000).to_string(index=False))
print()

# HU5 — GroupBy
print("=== GROUPBY BONO ===\n")
print("Bonos por nombre:")
print(agrupar_bonos_por_nombre(bonos_limpios).to_string(index=False))
print()
print("Bonos por precio:")
print(agrupar_bonos_por_precio(bonos_limpios).to_string(index=False))


# ── PRODUCTO ──────────────────────────────────────────────
from utils.producto.simulacion_producto import generar_simulacion_productos
from utils.producto.limpiar_producto import limpiar_productos
from utils.producto.descripcion_producto import describir_productos
from utils.producto.query_producto import (
    obtener_productos_activos,
    obtener_productos_por_tipo,
    obtener_productos_por_precio,
)
from utils.producto.groupby_producto import (
    calcular_promedio_precio_por_tipo,
    contar_productos_por_estado,
)

# HU3 — Simulación: +2000 productos
productos_sucios = generar_simulacion_productos(2000)
data_frame_sucio = pd.DataFrame(productos_sucios)

# HU1 — Limpieza
data_frame_limpio = limpiar_productos(data_frame_sucio)

# HU2 — Exploración / Descripción
print("=== DESCRIPCIÓN PRODUCTO ===\n")
describir_productos(data_frame_limpio)

# HU4 — Query
print("\n=== QUERIES PRODUCTO ===\n")
activos = obtener_productos_activos(data_frame_limpio)
print(f"Productos activos: {len(activos)}\n")

tipo_ejemplo = data_frame_limpio["tipo"].dropna().iloc[0]
print(f"Productos del tipo '{tipo_ejemplo}':")
print(obtener_productos_por_tipo(data_frame_limpio, tipo_ejemplo).to_string(index=False))
print()

print("Productos con precio entre 5000 y 20000:")
print(obtener_productos_por_precio(data_frame_limpio, 5000, 20000).to_string(index=False))
print()

# HU5 — GroupBy
print("=== GROUPBY PRODUCTO ===\n")
print("Promedio de precios por tipo:")
print(calcular_promedio_precio_por_tipo(data_frame_limpio).to_string(index=False))
print()
print("Conteo de productos por estado:")
print(contar_productos_por_estado(data_frame_limpio).to_string(index=False))
print()

