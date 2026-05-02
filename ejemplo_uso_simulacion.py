"""
EJEMPLO DE INTEGRACIÓN - Simulación y Exportación de Usuarios
"""

import pandas as pd
from utils.orden.simulacion_usuarios import simular_y_exportar_usuarios, SimulacionUsuarios


def ejemplo_basico():
    """
    Ejemplo básico: Simular y exportar usuarios.
    """
    print("=" * 80)
    print("EJEMPLO BÁSICO - SIMULACIÓN Y EXPORTACIÓN")
    print("=" * 80)
    
    # Simular 1500 usuarios
    df, reporte = simular_y_exportar_usuarios(
        cantidad=1500,
        directorio='datos',
        nombre_base='usuarios_test',
        semilla=42,
        mostrar_muestra=True
    )
    
    print("\n✅ Simulación completada")
    return df, reporte


def ejemplo_avanzado():
    """
    Ejemplo avanzado: Simulación con opciones personalizadas.
    """
    print("\n\n" + "=" * 80)
    print("EJEMPLO AVANZADO - SIMULACIÓN PERSONALIZADA")
    print("=" * 80)
    
    # Crear simulador
    simulador = SimulacionUsuarios(cantidad_usuarios=2000, semilla=123)
    
    # Paso 1: Simular
    print("\n1️⃣  Generando datos...")
    df = simulador.simular_usuarios()
    
    # Paso 2: Mostrar estadísticas
    print("\n2️⃣  Estadísticas de la simulación:")
    stats = simulador.obtener_estadisticas()
    print(f"   Total: {stats['total_usuarios']}")
    print(f"   Correos únicos: {stats['correos_unicos']}")
    
    # Paso 3: Mostrar muestra
    print("\n3️⃣  Muestra de datos:")
    simulador.mostrar_muestra(n=10)
    
    # Paso 4: Exportar
    print("\n4️⃣  Exportando en múltiples formatos...")
    archivos = simulador.exportar_multiformato(
        directorio='datos',
        nombre_base='usuarios_avanzado'
    )
    
    print("\n   Archivos generados:")
    for formato, ruta in archivos.items():
        print(f"   ✓ {formato.upper()}: {ruta}")
    
    # Paso 5: Reporte
    print("\n5️⃣  Guardando reporte...")
    simulador.guardar_reporte('datos/reporte_simulacion_avanzado.txt')
    print("   ✓ Reporte guardado")
    
    return df, simulador.obtener_reporte()


def ejemplo_comparativa():
    """
    Ejemplo comparativo: Generar múltiples simulaciones para análisis.
    """
    print("\n\n" + "=" * 80)
    print("EJEMPLO COMPARATIVO - MÚLTIPLES SIMULACIONES")
    print("=" * 80)
    
    tamaños = [500, 1000, 2000]
    resultados = {}
    
    for tamaño in tamaños:
        print(f"\n🎲 Generando {tamaño} usuarios...")
        simulador = SimulacionUsuarios(cantidad_usuarios=tamaño)
        df = simulador.simular_usuarios()
        stats = simulador.obtener_estadisticas()
        
        resultados[tamaño] = {
            'dataframe': df,
            'estadisticas': stats
        }
        
        print(f"   ✓ Total: {stats['total_usuarios']}")
        print(f"   ✓ Correos únicos: {stats['correos_unicos']}")
    
    # Comparativa
    print("\n\n📊 COMPARATIVA DE SIMULACIONES:")
    print("=" * 80)
    print(f"{'Tamaño':<15} {'Usuarios':<15} {'Correos Únicos':<20} {'Cobertura'}")
    print("-" * 80)
    
    for tamaño, datos in resultados.items():
        stats = datos['estadisticas']
        cobertura = (stats['correos_unicos'] / stats['total_usuarios']) * 100
        print(f"{tamaño:<15} {stats['total_usuarios']:<15} {stats['correos_unicos']:<20} {cobertura:.1f}%")
    
    return resultados


def ejemplo_integracion_completa():
    """
    Ejemplo completo: Simular, limpiar y describir en una sola ejecución.
    """
    print("\n\n" + "=" * 80)
    print("EJEMPLO INTEGRACIÓN COMPLETA - SIMULAR → LIMPIAR → DESCRIBIR")
    print("=" * 80)
    
    # Importar módulos de limpieza y descripción
    from utils.orden.limpieza_usuarios import limpiar_datos_usuarios
    from utils.orden.descripcion_usuarios import describir_usuarios
    
    # Paso 1: Simular
    print("\n📥 FASE 1: SIMULAR USUARIOS")
    print("-" * 80)
    df_simulado, _ = simular_y_exportar_usuarios(
        cantidad=1200,
        mostrar_muestra=False
    )
    print(f"✓ {len(df_simulado)} usuarios simulados")
    
    # Paso 2: Describir antes
    print("\n📊 FASE 2: ANÁLISIS ANTES DE LIMPIAR")
    print("-" * 80)
    resumen_antes = describir_usuarios(df_simulado, mostrar_reporte=False)
    print(f"✓ Análisis completado")
    
    # Paso 3: Limpiar
    print("\n🧹 FASE 3: LIMPIAR DATOS")
    print("-" * 80)
    df_limpio, _ = limpiar_datos_usuarios(df_simulado, guardar_reporte=False)
    print(f"✓ Datos limpios: {len(df_limpio)} registros")
    
    # Paso 4: Describir después
    print("\n📊 FASE 4: ANÁLISIS DESPUÉS DE LIMPIAR")
    print("-" * 80)
    resumen_despues = describir_usuarios(df_limpio, mostrar_reporte=False)
    print(f"✓ Análisis completado")
    
    # Paso 5: Exportar limpios
    print("\n💾 FASE 5: EXPORTAR DATOS LIMPIOS")
    print("-" * 80)
    df_limpio.to_csv('datos/usuarios_limpios_finales.csv', index=False)
    df_limpio.to_json('datos/usuarios_limpios_finales.json', orient='records')
    print(f"✓ Datos exportados")
    
    print("\n✅ PIPELINE COMPLETADO EXITOSAMENTE\n")
    
    return df_simulado, df_limpio


def main():
    """
    Función principal que ejecuta todos los ejemplos.
    """
    print("\n" + "🎯 EJEMPLOS DE USO - SIMULACIÓN DE USUARIOS\n")
    
    # Crear directorio de datos si no existe
    import os
    if not os.path.exists('datos'):
        os.makedirs('datos')
    
    # Ejecutar ejemplos
    print("\n📌 Selecciona un ejemplo a ejecutar:")
    print("   1. Ejemplo Básico")
    print("   2. Ejemplo Avanzado")
    print("   3. Ejemplo Comparativo")
    print("   4. Ejemplo Integración Completa")
    print("   5. Ejecutar Todos")
    
    opcion = input("\nOpción (1-5): ").strip()
    
    if opcion == '1':
        ejemplo_basico()
    elif opcion == '2':
        ejemplo_avanzado()
    elif opcion == '3':
        ejemplo_comparativa()
    elif opcion == '4':
        ejemplo_integracion_completa()
    elif opcion == '5':
        ejemplo_basico()
        ejemplo_avanzado()
        ejemplo_comparativa()
        ejemplo_integracion_completa()
    else:
        print("Opción inválida")
        return
    
    print("\n✅ Ejemplos ejecutados correctamente")


if __name__ == "__main__":
    # Ejecutar ejemplo por defecto (integración completa)
    # resultado = ejemplo_integracion_completa()
    
    # O ejecutar menú interactivo
    main()
