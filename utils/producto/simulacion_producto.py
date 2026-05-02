import random

def generar_simulacion_productos(numero_productos):
    """
    Genera productos sintéticos con datos sucios y errores controlados,
    para luego ser limpiados por la rutina correspondiente.
    """
    tipos_validos = ["bebida", "comida", "postre", "servicio"]
    estados_validos = ["activo", "inactivo", "agotado"]

    productos_base = [
        {"id": "PRD001", "nombre": "Café", "tipo": "bebida"},
        {"id": "PRD002", "nombre": "Hamburguesa", "tipo": "comida"},
        {"id": "PRD003", "nombre": "Helado", "tipo": "postre"},
        {"id": "PRD004", "nombre": "Internet", "tipo": "servicio"},
    ]

    data_frame_sucio = []
    for i in range(1, numero_productos + 1):
        base = random.choice(productos_base)
        producto_simulado = {
            "id": i,
            "nombre": base["nombre"],
            "precio": random.choice([5000, 15000, 30000, -1000, 0, None]),
            "tipo": base["tipo"],
            "estado": random.choice(estados_validos + [" ", "ACTIVO", None])
        }

        # Error controlado: duplicado
        if random.random() < 0.1 and data_frame_sucio:
            producto_simulado = data_frame_sucio[-1].copy()

        data_frame_sucio.append(producto_simulado)
    return data_frame_sucio
