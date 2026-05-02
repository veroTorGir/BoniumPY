import random

from datetime import datetime, timedelta

def generar_simulacion(numeroSimulaciones):

    ids_usuarios = [101, 102, 103, 104, 105, 106, 107, 108]

    platos = [
        {"id": "PLT001", "nombre": "Pollo asado"},
        {"id": "PLT002", "nombre": "Chuleta asada"},
        {"id": "PLT003", "nombre": "Carne guisada"},
        {"id": "PLT004", "nombre": "Bandeja paisa"},
        {"id": "PLT005", "nombre": "Filete de tilapia"},
        {"id": "PLT006", "nombre": "Pechuga a la plancha"},
        {"id": "PLT007", "nombre": "Costilla BBQ"},
        {"id": "PLT008", "nombre": "Lomo de cerdo"},
    ]

    adicionales = [
        {"id": "ADC001", "nombre": "Porción de arroz"},
        {"id": "ADC002", "nombre": "Porción de papa cocida"},
        {"id": "ADC003", "nombre": "Porción de ensalada"},
        {"id": "ADC004", "nombre": "Porción de frijoles"},
        {"id": "ADC005", "nombre": "Porción de plátano maduro"},
        {"id": "ADC006", "nombre": "Porción de yuca frita"},
        None, None, None,  # Sin adicional (opcional)
    ]

    ids_platos = [p["id"] for p in platos]
    ids_adicionales = [a["id"] if a else None for a in adicionales]
    modalidades = ["en_mesa", "para_llevar"]

    # Rango de fechas coherente: enero–marzo 2026 (90 días)
    fechaInicio = datetime(2026, 1, 1)
    RANGO_DIAS = 90

    # Horas coherentes con horario de restaurante (10:00–22:00)
    horas_validas = [f"{h:02d}:{m:02d}:00" for h in range(10, 23) for m in (0, 15, 30, 45)]

    simulaciones = []
    for i in range(1, numeroSimulaciones + 1):

        fecha_orden = fechaInicio + timedelta(days=random.randint(0, RANGO_DIAS))

        simulacion = {
            "id": i,
            "fk_user": random.choice(ids_usuarios),
            "fk_producto_plato": random.choice(ids_platos),
            "fk_producto_adicional": random.choice(ids_adicionales),
            "modalidad": random.choice(modalidades),
            "fecha": fecha_orden.date(),
            "hora": random.choice(horas_validas)
        }

        # Inyectando errores controlados (cubre todos los casos que maneja limpieza.py)
        probabilidadError = random.random()

        if probabilidadError < 0.10:
            # Error 1: fk_user nulo → campo obligatorio, registro será eliminado
            simulacion["fk_user"] = None

        elif probabilidadError < 0.20:
            # Error 2: fk_producto_plato nulo → campo obligatorio, registro será eliminado
            simulacion["fk_producto_plato"] = None

        elif probabilidadError < 0.30:
            # Error 3: modalidad inválida → será convertida a NA y el registro eliminado
            simulacion["modalidad"] = random.choice(["domicilio", "drive-thru", "express", "delivery"])

        elif probabilidadError < 0.38:
            # Error 4: fecha y hora nulas → se rellenan con valores por defecto
            simulacion["fecha"] = None
            simulacion["hora"] = None

        elif probabilidadError < 0.46:
            # Error 5: id negativo o cero → registro inválido, será eliminado
            simulacion["id"] = random.choice([0, -1, -5])

        elif probabilidadError < 0.54:
            # Error 6: modalidad con espacios o mayúsculas → .str.strip() la limpiará pero sigue inválida
            simulacion["modalidad"] = random.choice(["  en_mesa  ", "  PARA_LLEVAR  ", " En_Mesa "])

        elif probabilidadError < 0.70:
            # Error 8: fk_producto_plato con espacios extra → .str.strip() la limpiará
            simulacion["fk_producto_plato"] = "  " + random.choice(ids_platos) + "  "

        elif probabilidadError < 0.76:
            # Error 9: registro duplicado completo → drop_duplicates() lo eliminará
            if simulaciones:
                simulacion = simulaciones[-1].copy()

        # Sin error: ~24% de registros limpios

        simulaciones.append(simulacion)
    return simulaciones
