# Cambios - BoniumPY

## Resumen

Se han añadido módulos de graficación a BoniumPY basados en las funcionalidades de `muestraintegrador`. Los cambios permiten generar visualizaciones de los datos de órdenes, bonos y productos.

---

## Cambios Realizados

### 1. Actualización de `requirements.txt`

**Fecha:** 2026-05-30

Se agregaron dos nuevas dependencias para soporte de graficación:

- `matplotlib==3.10.3` - Biblioteca para crear gráficos estáticos, animados e interactivos
- `seaborn==0.13.2` - Biblioteca para visualización de datos estadísticos basada en matplotlib

**Archivo:** [requirements.txt](requirements.txt)

```
+ matplotlib==3.10.3
+ seaborn==0.13.2
```

---

### 2. Nuevo Módulo: `graficacion_orden.py`

**Ubicación:** [utils/orden/graficacion_orden.py](utils/orden/graficacion_orden.py)

Módulo para crear visualizaciones de datos de órdenes. Incluye 4 funciones:

#### Funciones disponibles:

- **`graficar_lineas()`** - Gráficos de líneas con marcadores (tendencias por fecha)
- **`graficar_barras()`** - Gráficos de barras (comparación entre categorías)
- **`graficar_torta()`** - Gráficos circulares con porcentajes (proporciones)
- **`graficar_mapa_calor()`** - Mapas de calor con pivotes (relaciones multidimensionales)

#### Parámetros comunes:

- `datos_agrupados`: DataFrame con datos agrupados
- `titulo`: Título personalizado del gráfico
- `nombre_archivo`: Nombre del archivo PNG a guardar
- `ruta_destino`: Ruta donde guardar (default: `graficos/`)

#### Ejemplo de uso:

```python
from utils.orden.graficacion_orden import graficar_barras
from utils.orden.groupby_orden import agrupar_por_usuario

# Agrupar datos
datos = agrupar_por_usuario(df_ordenes)

# Crear gráfico
graficar_barras(
    datos,
    columna_categorias="fk_user",
    columna_valores="cantidad",
    titulo="Órdenes por Usuario",
    color_barras="#2196F3",
    nombre_archivo="ordenes_por_usuario.png"
)
```

---

### 3. Nuevo Módulo: `graficacion_bono.py`

**Ubicación:** [utils/bono/graficacion_bono.py](utils/bono/graficacion_bono.py)

Módulo para crear visualizaciones de datos de bonos. Incluye las mismas 4 funciones que `graficacion_orden.py`, adaptadas para bonos:

- **`graficar_lineas()`** - Tendencias de bonos por fecha
- **`graficar_barras()`** - Comparación de bonos por nombre o tipo
- **`graficar_torta()`** - Proporción de tipos de bono
- **`graficar_mapa_calor()`** - Relaciones entre bonos y atributos

---

### 4. Nuevo Módulo: `graficacion_producto.py`

**Ubicación:** [utils/producto/graficacion_producto.py](utils/producto/graficacion_producto.py)

Módulo para crear visualizaciones de datos de productos. Incluye las mismas 4 funciones que los módulos anteriores, adaptadas para productos:

- **`graficar_lineas()`** - Tendencias de productos por fecha
- **`graficar_barras()`** - Comparación de productos por tipo
- **`graficar_torta()`** - Proporción de categorías de producto
- **`graficar_mapa_calor()`** - Relaciones entre productos y atributos

---

## Características de los Módulos de Graficación

### Estilos y Colores

- Los gráficos utilizan colores profesionales por defecto
- Soportan personalización de colores
- Incluyen etiquetas y títulos claros
- Tienen cuadrículas y marcadores para mejor legibilidad

### Almacenamiento

- Los gráficos se guardan en formato PNG
- Se crean automáticamente en la carpeta `graficos/` en la raíz del proyecto
- Los nombres de archivo son personalizables
- Se imprime en consola la ubicación exacta del archivo guardado

### Escalabilidad

- Soportan diferentes tamaños de datos
- Adaptan el tamaño de figura automáticamente
- Las etiquetas se rotan para evitar superposición

---

## Cómo Usar

### Instalación de dependencias

```powershell
pip install -r requirements.txt
```

### Integración en `main.py`

Se pueden importar los módulos de graficación para crear visualizaciones después de procesar los datos:

```python
from utils.orden.graficacion_orden import graficar_barras
from utils.bono.graficacion_bono import graficar_torta
from utils.producto.graficacion_producto import graficar_mapa_calor

# Después de limpiar y agrupar los datos...
graficar_barras(datos_orden_agrupados, ...)
graficar_torta(datos_bono_agrupados, ...)
graficar_mapa_calor(datos_producto_agrupados, ...)
```

---

## Diferencias con `muestraintegrador`

| Aspecto            | muestraintegrador             | BoniumPY (Actualizado)                          |
| ------------------ | ----------------------------- | ----------------------------------------------- |
| **Graficación**    | Centralizado en 1 módulo      | Distribuido por entidad (orden, bono, producto) |
| **Datos**          | Consume desde API REST        | Genera por simulación                           |
| **Transformación** | Filtros y groupby específicos | Módulos groupby reutilizables                   |
| **Entidades**      | Servicios                     | Órdenes, Bonos, Productos                       |

---

## Próximos Pasos (Recomendaciones)

1. **Integrar en `main.py`**: Agregar llamadas a funciones de graficación para visualizar resultados
2. **Crear ejemplos**: Archivos como `ejemplo_uso_graficacion_*.py`
3. **Documentación visual**: Incluir screenshots de gráficos en el README
4. **Validación de datos**: Asegurar que los datos estén limpios antes de graficar

---

## Notas Técnicas

- Las rutas se crean automáticamente si no existen
- Los gráficos se cierran correctamente después de guardarse (liberan memoria)
- Compatible con Jupyter Notebooks y scripts Python regulares
- Las funciones incluyen docstrings completos para facilitar el desarrollo

---

**Documento generado:** 2026-05-30
