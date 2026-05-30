import random

def generar_simulacion_bono(numeroSimulaciones):

    nombres_bonos = [
        "Bono Bienvenida",
        "Bono Cumpleaños",
        "Bono Fidelidad",
        "Bono Estudiante",
        "Bono Fin de Semana",
        "Bono Familiar",
        "Bono Ejecutivo",
        "Bono Premium",
    ]

    precios_validos = [5000, 10000, 15000, 20000, 25000, 30000, 50000]

    simulaciones = []
    for i in range(1, numeroSimulaciones + 1):

        simulacion = {
            "id": i,
            "nombre": random.choice(nombres_bonos),
            "precio": random.choice(precios_validos),
        }

        # Inyectando errores controlados
        probabilidadError = random.random()

        if probabilidadError < 0.10:
            # Error 1: id negativo o cero → inválido, será eliminado
            simulacion["id"] = random.choice([0, -1, -3])

        elif probabilidadError < 0.20:
            # Error 2: nombre nulo → campo obligatorio, registro será eliminado
            simulacion["nombre"] = None

        elif probabilidadError < 0.30:
            # Error 3: precio nulo → campo obligatorio, registro será eliminado
            simulacion["precio"] = None

        elif probabilidadError < 0.40:
            # Error 4: precio negativo o cero → inválido, será eliminado
            simulacion["precio"] = random.choice([0, -5000, -1000])

        elif probabilidadError < 0.50:
            # Error 5: nombre con espacios extra → .str.strip() lo corrige
            simulacion["nombre"] = "  " + simulacion["nombre"] + "  "

        elif probabilidadError < 0.60:
            # Error 6: nombre inválido (fuera del catálogo)
            simulacion["nombre"] = random.choice(["Bono Falso", "Descuento X", "Promo ???"])

        elif probabilidadError < 0.68:
            # Error 7: precio no numérico → pd.to_numeric lo convierte a NaN
            simulacion["precio"] = random.choice(["gratis", "N/A", "--"])

        elif probabilidadError < 0.74:
            # Error 8: registro duplicado del anterior
            if simulaciones:
                simulacion = simulaciones[-1].copy()

        # Sin error: ~26% de registros limpios

        simulaciones.append(simulacion)
    return simulaciones
