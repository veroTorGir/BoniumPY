"""
EJEMPLO DE INTEGRACIÓN - Transformación y Filtrado de Usuarios
"""

import pandas as pd
import numpy as np
from utils.orden.simulacion_usuarios import simular_y_exportar_usuarios
from utils.orden.transformacion_usuarios import (
    TransformacionUsuarios,
    mostrar_resultado_filtro,
    crear_vista_personalizada
)


def ejemplo_1_filtros_basicos():
    """
    Ejemplo 1: Filtros básicos de usuarios.
    """
    print("\n" + "=" * 80)
    print("EJEMPLO 1: FILTROS BÁSICOS")
    print("=" * 80)
    
    # Simular datos
    print("\n📥 Generando datos de ejemplo...")
    df, _ = simular_y_exportar_usuarios(cantidad=500, mostrar_muestra=False)
    
    # Crear transformador
    transformador = TransformacionUsuarios(df)
    transformador.extraer_dominio_correo()
    
    # Filtro 1: Por rol
    print("\n1️⃣  Filtrando usuarios por Rol ID=2...")
    df_rol_2 = transformador.filtrar_por_rol(rol_id=2)
    print(f"   ✓ {len(df_rol_2)} usuarios encontrados")
    
    # Filtro 2: Por dominio
    print("\n2️⃣  Filtrando usuarios por dominio 'gmail.com'...")
    df_gmail = transformador.filtrar_por_dominio_correo('gmail.com')
    print(f"   ✓ {len(df_gmail)} usuarios encontrados")
    
    # Filtro 3: Por estado
    print("\n3️⃣  Filtrando usuarios activos...")
    df_activos = transformador.filtrar_por_estado('activo')
    print(f"   ✓ {len(df_activos)} usuarios encontrados")
    
    print(f"\n✅ Ejemplo 1 completado\n")
    return df, transformador


def ejemplo_2_filtros_avanzados():
    """
    Ejemplo 2: Filtros avanzados y combinados.
    """
    print("\n" + "=" * 80)
    print("EJEMPLO 2: FILTROS AVANZADOS")
    print("=" * 80)
    
    # Simular datos
    print("\n📥 Generando datos de ejemplo...")
    df, _ = simular_y_exportar_usuarios(cantidad=500, mostrar_muestra=False)
    
    # Crear transformador
    transformador = TransformacionUsuarios(df)
    transformador.extraer_dominio_correo()
    
    # Filtro 1: Múltiples roles
    print("\n1️⃣  Filtrando usuarios con Roles 1, 2 o 3...")
    df_multiples_roles = transformador.filtrar_multiples_roles([1, 2, 3])
    print(f"   ✓ {len(df_multiples_roles)} usuarios encontrados")
    
    # Filtro 2: Múltiples dominios
    print("\n2️⃣  Filtrando usuarios de dominios 'gmail.com' o 'hotmail.com'...")
    df_multiples_dominios = transformador.filtrar_multiples_dominios(['gmail.com', 'hotmail.com'])
    print(f"   ✓ {len(df_multiples_dominios)} usuarios encontrados")
    
    # Filtro 3: Criterios múltiples
    print("\n3️⃣  Filtrando usuarios activos del Rol 1...")
    criterios = {'fk_rol': 1, 'estado': 'activo'}
    df_criterios = transformador.filtrar_por_criterios_multiples(criterios)
    print(f"   ✓ {len(df_criterios)} usuarios encontrados")
    
    # Filtro 4: Rango de IDs
    print("\n4️⃣  Filtrando usuarios con IDs entre 50 y 150...")
    df_rango = transformador.filtrar_por_rango_ids(50, 150)
    print(f"   ✓ {len(df_rango)} usuarios encontrados")
    
    print(f"\n✅ Ejemplo 2 completado\n")
    return df, transformador


def ejemplo_3_distribucion():
    """
    Ejemplo 3: Análisis de distribuciones.
    """
    print("\n" + "=" * 80)
    print("EJEMPLO 3: ANÁLISIS DE DISTRIBUCIONES")
    print("=" * 80)
    
    # Simular datos
    print("\n📥 Generando datos de ejemplo...")
    df, _ = simular_y_exportar_usuarios(cantidad=500, mostrar_muestra=False)
    
    # Crear transformador
    transformador = TransformacionUsuarios(df)
    transformador.extraer_dominio_correo()
    
    # Distribución 1: Roles
    print("\n1️⃣  Distribución de Usuarios por Rol:")
    print("-" * 80)
    dist_roles = transformador.obtener_distribucion_roles()
    print(dist_roles)
    
    # Distribución 2: Dominios (Top 5)
    print("\n2️⃣  Top 5 Dominios de Correo:")
    print("-" * 80)
    dist_dominios = transformador.obtener_distribucion_dominios(top=5)
    print(dist_dominios)
    
    # Distribución 3: Cruzada rol x estado
    print("\n3️⃣  Tabla Cruzada Rol x Estado:")
    print("-" * 80)
    tabla_cruzada = transformador.agrupar_por_rol_y_estado()
    print(tabla_cruzada)
    
    # Resumen ejecutivo
    print("\n4️⃣  Resumen Ejecutivo:")
    print("-" * 80)
    resumen = transformador.crear_resumen_ejecutivo()
    for clave, valor in resumen.items():
        print(f"   {clave}: {valor}")
    
    print(f"\n✅ Ejemplo 3 completado\n")
    return df, transformador


def ejemplo_4_busqueda_especifica():
    """
    Ejemplo 4: Búsqueda de usuarios específicos.
    """
    print("\n" + "=" * 80)
    print("EJEMPLO 4: BÚSQUEDA DE USUARIOS ESPECÍFICOS")
    print("=" * 80)
    
    # Simular datos
    print("\n📥 Generando datos de ejemplo...")
    df, _ = simular_y_exportar_usuarios(cantidad=500, mostrar_muestra=False)
    
    # Crear transformador
    transformador = TransformacionUsuarios(df)
    
    # Búsqueda 1: Por patrón de nombre
    print("\n1️⃣  Buscando usuarios con 'Garcia' en el nombre...")
    df_garcia = transformador.filtrar_por_nombre('Garcia')
    mostrar_resultado_filtro(df_garcia, "Usuarios con 'Garcia' en el nombre")
    
    # Búsqueda 2: Por patrón de correo
    print("\n2️⃣  Buscando usuarios con correos que contienen 'sofia'...")
    df_sofia = transformador.filtrar_por_correo('sofia')
    mostrar_resultado_filtro(df_sofia, "Usuarios con 'sofia' en el correo")
    
    # Búsqueda 3: Por IDs específicos
    print("\n3️⃣  Buscando usuarios con IDs específicos [10, 25, 42, 88]...")
    df_ids = transformador.filtrar_por_ids([10, 25, 42, 88])
    mostrar_resultado_filtro(df_ids, "Usuarios con IDs específicos")
    
    print(f"\n✅ Ejemplo 4 completado\n")
    return df, transformador


def ejemplo_5_vistas_personalizadas():
    """
    Ejemplo 5: Crear vistas personalizadas.
    """
    print("\n" + "=" * 80)
    print("EJEMPLO 5: VISTAS PERSONALIZADAS")
    print("=" * 80)
    
    # Simular datos
    print("\n📥 Generando datos de ejemplo...")
    df, _ = simular_y_exportar_usuarios(cantidad=500, mostrar_muestra=False)
    
    # Vista 1: Solo información personal
    print("\n1️⃣  Vista: Información Personal")
    print("-" * 80)
    vista_personal = crear_vista_personalizada(df, ['id', 'nombre', 'correo'])
    print(vista_personal.head(5))
    
    # Vista 2: Solo información de seguridad
    print("\n2️⃣  Vista: Información de Seguridad")
    print("-" * 80)
    vista_seguridad = crear_vista_personalizada(df, ['id', 'clave', 'fk_rol', 'estado'])
    print(vista_seguridad.head(5))
    
    # Vista 3: Con filtro + personalización
    print("\n3️⃣  Vista: Usuarios Activos (Personal + Rol + Estado)")
    print("-" * 80)
    transformador = TransformacionUsuarios(df)
    df_activos = transformador.filtrar_por_estado('activo')
    vista_activos = crear_vista_personalizada(df_activos, ['id', 'nombre', 'correo', 'fk_rol', 'estado'])
    print(f"   Total registros: {len(vista_activos)}")
    print(vista_activos.head(5))
    
    print(f"\n✅ Ejemplo 5 completado\n")


def ejemplo_6_pipeline_completo():
    """
    Ejemplo 6: Pipeline completo de análisis.
    """
    print("\n" + "=" * 80)
    print("EJEMPLO 6: PIPELINE COMPLETO DE ANÁLISIS")
    print("=" * 80)
    
    # Paso 1: Simular
    print("\n📥 PASO 1: GENERAR DATOS")
    print("-" * 80)
    df, _ = simular_y_exportar_usuarios(cantidad=1000, mostrar_muestra=False)
    print(f"✓ {len(df)} usuarios generados")
    
    # Paso 2: Transformar
    print("\n🔄 PASO 2: TRANSFORMAR DATOS")
    print("-" * 80)
    transformador = TransformacionUsuarios(df)
    transformador.extraer_dominio_correo()
    print("✓ Dominio de correo extraído")
    
    # Paso 3: Filtrar y analizar
    print("\n🔍 PASO 3: ANÁLISIS Y FILTRADO")
    print("-" * 80)
    
    # Usuarios activos
    df_activos = transformador.filtrar_por_estado('activo')
    print(f"✓ Usuarios activos: {len(df_activos)} ({len(df_activos)/len(df)*100:.1f}%)")
    
    # Usuarios por rol
    dist_roles = transformador.obtener_distribucion_roles()
    print(f"✓ Distribución de roles calculada")
    
    # Dominios principales
    dist_dominios = transformador.obtener_distribucion_dominios(top=3)
    print(f"✓ Top 3 dominios identificados")
    
    # Paso 4: Exportar resultados
    print("\n💾 PASO 4: EXPORTAR RESULTADOS")
    print("-" * 80)
    
    # Exportar usuarios activos
    df_activos.to_csv('datos/usuarios_activos.csv', index=False)
    print("✓ usuarios_activos.csv")
    
    # Exportar distribución de roles
    dist_roles.to_csv('datos/distribucion_roles.csv')
    print("✓ distribucion_roles.csv")
    
    # Exportar distribución de dominios
    dist_dominios.to_csv('datos/distribucion_dominios.csv')
    print("✓ distribucion_dominios.csv")
    
    # Exportar resumen
    resumen = transformador.crear_resumen_ejecutivo()
    df_resumen = pd.DataFrame([resumen])
    df_resumen.to_csv('datos/resumen_ejecutivo.csv', index=False)
    print("✓ resumen_ejecutivo.csv")
    
    # Exportar reporte
    transformador.guardar_reporte_transformaciones('datos/reporte_transformaciones.txt')
    print("✓ reporte_transformaciones.txt")
    
    print(f"\n✅ Pipeline completado\n")


def main():
    """
    Menú interactivo para ejecutar ejemplos.
    """
    print("\n" + "=" * 80)
    print("🎯 EJEMPLOS DE USO - TRANSFORMACIÓN DE USUARIOS")
    print("=" * 80)
    
    # Crear directorio de datos si no existe
    import os
    if not os.path.exists('datos'):
        os.makedirs('datos')
    
    print("\n📌 Selecciona un ejemplo a ejecutar:")
    print("   1. Filtros Básicos")
    print("   2. Filtros Avanzados")
    print("   3. Análisis de Distribuciones")
    print("   4. Búsqueda de Usuarios Específicos")
    print("   5. Vistas Personalizadas")
    print("   6. Pipeline Completo")
    print("   7. Ejecutar Todos")
    
    opcion = input("\nOpción (1-7): ").strip()
    
    if opcion == '1':
        ejemplo_1_filtros_basicos()
    elif opcion == '2':
        ejemplo_2_filtros_avanzados()
    elif opcion == '3':
        ejemplo_3_distribucion()
    elif opcion == '4':
        ejemplo_4_busqueda_especifica()
    elif opcion == '5':
        ejemplo_5_vistas_personalizadas()
    elif opcion == '6':
        ejemplo_6_pipeline_completo()
    elif opcion == '7':
        ejemplo_1_filtros_basicos()
        ejemplo_2_filtros_avanzados()
        ejemplo_3_distribucion()
        ejemplo_4_busqueda_especifica()
        ejemplo_5_vistas_personalizadas()
        ejemplo_6_pipeline_completo()
    else:
        print("Opción inválida")
        return
    
    print("\n✅ Ejemplos ejecutados correctamente")


if __name__ == "__main__":
    # Ejecutar ejemplo por defecto
    # ejemplo_6_pipeline_completo()
    
    # O ejecutar menú interactivo
    main()
