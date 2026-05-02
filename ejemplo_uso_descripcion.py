"""
EJEMPLO DE INTEGRACIÓN - Análisis Exploratorio de Usuarios en el pipeline
"""

import pandas as pd
from utils.orden.limpieza_usuarios import limpiar_datos_usuarios
from utils.orden.descripcion_usuarios import describir_usuarios, comparar_antes_despues


def main():
    """
    Ejemplo completo: Cargar → Limpiar → Describir
    """
    
    # 1. CREAR DATOS DE EJEMPLO
    print("📥 Creando dataset de ejemplo...\n")
    datos_ejemplo = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'nombre': ['juan perez', 'MARIA GARCIA', 'carlos  lopez', None, 'ana martinez', 
                   'juan perez', 'luis rodriguez', 'Sofia  Fernandez', 'DIEGO sanchez', 
                   'laura gomez', 'marco ruiz', 'elena torres'],
        'correo': ['JUAN@EMAIL.COM', 'maria@email.com', 'carlos@email.com', 'test@email.com', 
                   'ana@EMAIL.COM', 'juan@email.com', '   luis@email.com   ', 'sofia@email.com',
                   'diego@email.com', 'laura@email.com', 'marco@email.com', 'elena@email.com'],
        'clave': ['pass123', 'pass456', None, 'pass789', 'pass101', 'pass123', 
                  'pass202', 'pass303', 'pass404', 'pass505', 'pass606', 'pass707'],
        'fk_rol': [1, 2, 1, 2, None, 1, 1, 2, 1, 2, 3, 1]
    }
    
    df_original = pd.DataFrame(datos_ejemplo)
    
    print(f"✓ Dataset de ejemplo creado: {len(df_original)} registros\n")
    
    # 2. ANÁLISIS ANTES DE LIMPIAR
    print("\n" + "=" * 80)
    print("FASE 1: ANÁLISIS EXPLORATORIO - ANTES DE LIMPIAR")
    print("=" * 80)
    
    resumen_antes = describir_usuarios(df_original, mostrar_reporte=True, guardar_reporte=False)
    
    # 3. LIMPIAR DATOS
    print("\n\n" + "=" * 80)
    print("FASE 2: LIMPIEZA DE DATOS")
    print("=" * 80)
    
    df_limpio, reporte_limpieza = limpiar_datos_usuarios(df_original, guardar_reporte=False)
    
    # 4. ANÁLISIS DESPUÉS DE LIMPIAR
    print("\n\n" + "=" * 80)
    print("FASE 3: ANÁLISIS EXPLORATORIO - DESPUÉS DE LIMPIAR")
    print("=" * 80)
    
    resumen_despues = describir_usuarios(df_limpio, mostrar_reporte=True, guardar_reporte=False)
    
    # 5. COMPARACIÓN
    print("\n\n" + "=" * 80)
    print("FASE 4: COMPARACIÓN ANTES vs DESPUÉS")
    print("=" * 80)
    
    comparar_antes_despues(df_original, df_limpio)
    
    # 6. GUARDAR RESULTADOS
    print("\n\n" + "=" * 80)
    print("FASE 5: GUARDAR RESULTADOS")
    print("=" * 80)
    
    print("\n💾 Guardando datos...")
    # df_limpio.to_csv('datos/usuarios_limpios.csv', index=False, encoding='utf-8')
    # df_limpio.to_excel('datos/usuarios_limpios.xlsx', index=False)
    print("✓ Datos guardados exitosamente")
    
    print("\n✅ PROCESO COMPLETADO\n")
    
    return {
        'df_original': df_original,
        'df_limpio': df_limpio,
        'resumen_antes': resumen_antes,
        'resumen_despues': resumen_despues,
        'reporte_limpieza': reporte_limpieza
    }


if __name__ == "__main__":
    resultados = main()
