# Proyecto Integrador — Gestión de Órdenes

Simulación de una base de datos de órdenes de restaurante con datos sucios, y su posterior proceso de limpieza usando pandas.

---

## Estructura del proyecto

```
muestraintegradornt20261/
├── main.py                        # Punto de entrada
├── requirements.txt               # Dependencias
└── utils/
    ├── simulacion.py              # Generación de datos (BD sucia)
    └── notebook/
        └── limpieza.py            # Limpieza y validación de datos
```

---

## Cómo ejecutar

```powershell
cd "c:\Users\Windows 11\Documents\hoy\muestraintegradornt20261"
& "C:\Users\Windows 11\AppData\Local\Programs\Python\Python310\python.exe" main.py
```

---

## Paso a paso

### Paso 1 — Punto de entrada ([main.py](main.py#L1))

[`main.py`](main.py) orquesta todo el flujo:

1. [`generar_simulacion(10)`](main.py#L6) — genera 10 órdenes con errores aleatorios
2. [`pd.DataFrame(...)`](main.py#L7) — convierte la lista en un DataFrame de pandas
3. [`limpiar_simulacion(...)`](main.py#L8) — aplica todas las reglas de limpieza
4. [`print(...)`](main.py#L10) — muestra el resultado limpio en consola

---

### Paso 2 — Modelo de la Orden ([simulacion.py L1–L35](utils/simulacion.py#L1-L35))

La función `generar_simulacion()` define la estructura de la BD de Órdenes:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | int | Auto-incremental, generado en el bucle |
| `fk_user` | int | Referencia al usuario (101–108) |
| `fk_producto_plato` | str | Plato obligatorio (PLT001–PLT008) |
| `fk_producto_adicional` | str / None | Adicional opcional (ADC001–ADC006 o None) |
| `modalidad` | str | `en_mesa` o `para_llevar` |
| `fecha` | date | Se genera automáticamente al crear la orden |
| `hora` | str | Se genera automáticamente al crear la orden |

**Catálogo de platos** → ver [`simulacion.py` líneas 9–18](utils/simulacion.py#L9-L18)

**Catálogo de adicionales** → ver [`simulacion.py` líneas 20–28](utils/simulacion.py#L20-L28)

---

### Paso 3 — Inyección de errores ([simulacion.py L50–L84](utils/simulacion.py#L50-L84))

Cada orden tiene una probabilidad aleatoria de recibir uno de estos errores:

| Probabilidad | Error inyectado | Campo afectado |
|---|---|---|
| 0–10% | `fk_user = None` | [`línea 55`](utils/simulacion.py#L55) |
| 10–20% | `fk_producto_plato = None` | [`línea 59`](utils/simulacion.py#L59) |
| 20–30% | Modalidad inválida (`domicilio`, `delivery`…) | [`línea 63`](utils/simulacion.py#L63) |
| 30–38% | `fecha = None`, `hora = None` | [`línea 67`](utils/simulacion.py#L67-L68) |
| 38–46% | `id` negativo o cero | [`línea 72`](utils/simulacion.py#L72) |
| 46–54% | Modalidad con espacios o mayúsculas | [`línea 76`](utils/simulacion.py#L76) |
| 54–70% | `fk_producto_plato` con espacios extra | [`línea 80`](utils/simulacion.py#L80) |
| 70–76% | Registro duplicado del anterior | [`línea 84`](utils/simulacion.py#L84) |
| 76–100% | Sin error | — |

---

### Paso 4 — Limpieza de datos ([limpieza.py](utils/notebook/limpieza.py))

La función `limpiar_simulacion(df)` aplica 8 pasos en orden:

#### Paso 4.1 — Limpiar espacios en columnas de texto → [`línea 8`](utils/notebook/limpieza.py#L8-L10)
Aplica `.str.strip()` a `fk_producto_plato`, `fk_producto_adicional` y `modalidad`.
Corrige errores como `"  PLT003  "` → `"PLT003"`.

#### Paso 4.2 — Validar modalidad → [`línea 13`](utils/notebook/limpieza.py#L13-L16)
Solo acepta `"en_mesa"` o `"para_llevar"`. Cualquier otro valor se convierte a `NA`.

#### Paso 4.3 — Convertir `id` a numérico → [`línea 19`](utils/notebook/limpieza.py#L19)
Usa `pd.to_numeric()` para asegurar que el campo `id` sea un número válido.

#### Paso 4.4 — Convertir `fecha` a tipo datetime → [`línea 22`](utils/notebook/limpieza.py#L22)
Usa `pd.to_datetime()` para normalizar el formato de fecha.

#### Paso 4.5 — Rellenar fechas y horas nulas → [`línea 25`](utils/notebook/limpieza.py#L25-L28)
Si `fecha` es nula se reemplaza por `2026-01-01`. Si `hora` es nula se reemplaza por `00:00:00`.

#### Paso 4.6 — Eliminar registros con campos obligatorios nulos → [`línea 31`](utils/notebook/limpieza.py#L31-L32)
Elimina filas donde `id`, `fk_user`, `fk_producto_plato` o `modalidad` sean `NA`.

#### Paso 4.7 — Eliminar `id` inválidos → [`línea 35`](utils/notebook/limpieza.py#L35)
Elimina registros donde `id <= 0`.

#### Paso 4.8 — Eliminar duplicados → [`línea 38`](utils/notebook/limpieza.py#L38)
Usa `drop_duplicates()` para eliminar filas idénticas.

---

## Dependencias

Ver [`requirements.txt`](requirements.txt)

```
numpy==1.26.4
pandas==2.2.3        # Versión compatible con Python 3.10
python-dateutil==2.9.0.post0
six==1.17.0
tzdata==2026.1
```

Instalar con:
```powershell
pip install -r requirements.txt
```
