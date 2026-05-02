"""

HU 1: Limpieza del set de datos (USUARIO)

Como analista de datos quiero limpiar el conjunto de datos de la tabla usuario
para asegurar que la información sea confiable antes del análisis.

Módulo modularizado para la limpieza de datos de usuarios con pandas.
"""

import pandas as pd
import re
from datetime import datetime
from typing import Tuple, Dict, List


class LimpiezaUsuarios:
    """
    Clase para gestionar la limpieza y validación del dataset de usuarios.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa la clase con el DataFrame de usuarios.
        
        Args:
            df (pd.DataFrame): DataFrame con datos de usuarios
        """
        self.df_original = df.copy()
        self.df_limpio = df.copy()
        self.reporte_cambios = {
            'fecha_proceso': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'registros_iniciales': len(df),
            'cambios_realizados': []
        }
    
    def identificar_nulos(self) -> Dict[str, int]:
        """
        Identifica valores nulos en campos críticos.
        
        Campos validados: nombre, correo, clave, fk_rol
        
        Returns:
            Dict[str, int]: Diccionario con conteo de nulos por campo
        """
        campos_criticos = ['nombre', 'correo', 'clave', 'fk_rol']
        nulos_encontrados = {}
        
        for campo in campos_criticos:
            if campo in self.df_limpio.columns:
                cantidad_nulos = self.df_limpio[campo].isnull().sum()
                nulos_encontrados[campo] = cantidad_nulos
                
                if cantidad_nulos > 0:
                    self.reporte_cambios['cambios_realizados'].append({
                        'tipo': 'NULOS_IDENTIFICADOS',
                        'campo': campo,
                        'cantidad': cantidad_nulos
                    })
        
        return nulos_encontrados
    
    def eliminar_registros_con_nulos(self) -> int:
        """
        Elimina registros que contienen valores nulos en campos críticos.
        
        Returns:
            int: Cantidad de registros eliminados
        """
        campos_criticos = ['nombre', 'correo', 'clave', 'fk_rol']
        registros_antes = len(self.df_limpio)
        
        # Filtrar solo los campos que existen en el DataFrame
        campos_validos = [c for c in campos_criticos if c in self.df_limpio.columns]
        self.df_limpio = self.df_limpio.dropna(subset=campos_validos)
        
        registros_eliminados = registros_antes - len(self.df_limpio)
        
        if registros_eliminados > 0:
            self.reporte_cambios['cambios_realizados'].append({
                'tipo': 'REGISTROS_ELIMINADOS',
                'cantidad': registros_eliminados,
                'razon': 'Contienen valores nulos en campos críticos'
            })
        
        return registros_eliminados
    
    def corregir_formato_correo(self) -> int:
        """
        Corrige y valida el formato de los correos electrónicos.
        
        - Convierte a minúsculas
        - Elimina espacios en blanco
        - Valida formato básico de email
        
        Returns:
            int: Cantidad de correos corregidos
        """
        if 'correo' not in self.df_limpio.columns:
            return 0
        
        correos_corregidos = 0
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        for idx, correo in enumerate(self.df_limpio['correo']):
            if isinstance(correo, str):
                # Limpiar y normalizar
                correo_limpio = correo.strip().lower()
                
                # Validar formato
                if not re.match(patron_email, correo_limpio):
                    self.df_limpio.at[idx, 'correo'] = correo_limpio
                    correos_corregidos += 1
                elif correo != correo_limpio:
                    self.df_limpio.at[idx, 'correo'] = correo_limpio
                    correos_corregidos += 1
        
        if correos_corregidos > 0:
            self.reporte_cambios['cambios_realizados'].append({
                'tipo': 'CORREOS_CORREGIDOS',
                'cantidad': correos_corregidos,
                'acciones': ['Conversión a minúsculas', 'Eliminación de espacios', 'Validación de formato']
            })
        
        return correos_corregidos
    
    def eliminar_correos_duplicados(self) -> int:
        """
        Identifica y elimina registros con correos electrónicos duplicados.
        
        Mantiene la primera ocurrencia y elimina las posteriores.
        
        Returns:
            int: Cantidad de duplicados eliminados
        """
        if 'correo' not in self.df_limpio.columns:
            return 0
        
        registros_antes = len(self.df_limpio)
        self.df_limpio = self.df_limpio.drop_duplicates(subset=['correo'], keep='first')
        duplicados_eliminados = registros_antes - len(self.df_limpio)
        
        if duplicados_eliminados > 0:
            self.reporte_cambios['cambios_realizados'].append({
                'tipo': 'CORREOS_DUPLICADOS_ELIMINADOS',
                'cantidad': duplicados_eliminados,
                'criterio': 'Mantener primera ocurrencia'
            })
        
        return duplicados_eliminados
    
    def normalizar_nombres(self) -> int:
        """
        Normaliza los nombres de usuarios.
        
        - Convierte a formato Title Case (Primeras mayúsculas)
        - Elimina espacios múltiples
        - Elimina espacios al inicio y final
        
        Returns:
            int: Cantidad de nombres normalizados
        """
        if 'nombre' not in self.df_limpio.columns:
            return 0
        
        nombres_normalizados = 0
        
        for idx, nombre in enumerate(self.df_limpio['nombre']):
            if isinstance(nombre, str):
                # Limpiar espacios múltiples
                nombre_limpio = ' '.join(nombre.split())
                # Convertir a Title Case
                nombre_normalizado = nombre_limpio.title()
                
                if nombre != nombre_normalizado:
                    self.df_limpio.at[idx, 'nombre'] = nombre_normalizado
                    nombres_normalizados += 1
        
        if nombres_normalizados > 0:
            self.reporte_cambios['cambios_realizados'].append({
                'tipo': 'NOMBRES_NORMALIZADOS',
                'cantidad': nombres_normalizados,
                'acciones': ['Title Case', 'Eliminación de espacios múltiples']
            })
        
        return nombres_normalizados
    
    def obtener_reporte_cambios(self) -> Dict:
        """
        Retorna el reporte detallado de todos los cambios realizados.
        
        Returns:
            Dict: Reporte con registro de cambios
        """
        self.reporte_cambios['registros_finales'] = len(self.df_limpio)
        self.reporte_cambios['registros_eliminados_total'] = (
            self.reporte_cambios['registros_iniciales'] - 
            self.reporte_cambios['registros_finales']
        )
        
        return self.reporte_cambios
    
    def guardar_reporte_cambios(self, ruta_archivo: str = 'reporte_limpieza_usuarios.txt') -> None:
        """
        Guarda el reporte de cambios en un archivo de texto.
        
        Args:
            ruta_archivo (str): Ruta donde guardar el reporte
        """
        reporte = self.obtener_reporte_cambios()
        
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("=" * 80 + "\n")
            archivo.write("REPORTE DE LIMPIEZA - DATASET DE USUARIOS\n")
            archivo.write("=" * 80 + "\n\n")
            
            archivo.write(f"Fecha de Proceso: {reporte['fecha_proceso']}\n")
            archivo.write(f"Registros Iniciales: {reporte['registros_iniciales']}\n")
            archivo.write(f"Registros Finales: {reporte['registros_finales']}\n")
            archivo.write(f"Registros Eliminados: {reporte['registros_eliminados_total']}\n\n")
            
            archivo.write("DETALLE DE CAMBIOS REALIZADOS:\n")
            archivo.write("-" * 80 + "\n")
            
            for i, cambio in enumerate(reporte['cambios_realizados'], 1):
                archivo.write(f"\n{i}. {cambio['tipo']}\n")
                for clave, valor in cambio.items():
                    if clave != 'tipo':
                        archivo.write(f"   - {clave}: {valor}\n")
    
    def ejecutar_limpieza_completa(self) -> Tuple[pd.DataFrame, Dict]:
        """
        Ejecuta el proceso completo de limpieza de datos.
        
        Orden de ejecución:
        1. Identificar nulos
        2. Eliminar registros con nulos
        3. Corregir formato de correos
        4. Eliminar correos duplicados
        5. Normalizar nombres
        
        Returns:
            Tuple[pd.DataFrame, Dict]: DataFrame limpio y reporte de cambios
        """
        print("Iniciando limpieza del dataset de usuarios...")
        
        # Paso 1: Identificar nulos
        print("\n1. Identificando valores nulos...")
        nulos = self.identificar_nulos()
        print(f"   Nulos encontrados: {nulos}")
        
        # Paso 2: Eliminar registros con nulos
        print("\n2. Eliminando registros con valores nulos...")
        eliminados = self.eliminar_registros_con_nulos()
        print(f"   Registros eliminados: {eliminados}")
        
        # Paso 3: Corregir formato de correos
        print("\n3. Corrigiendo formatos de correo...")
        correos_corregidos = self.corregir_formato_correo()
        print(f"   Correos corregidos: {correos_corregidos}")
        
        # Paso 4: Eliminar correos duplicados
        print("\n4. Eliminando correos duplicados...")
        duplicados = self.eliminar_correos_duplicados()
        print(f"   Duplicados eliminados: {duplicados}")
        
        # Paso 5: Normalizar nombres
        print("\n5. Normalizando nombres...")
        nombres_normalizados = self.normalizar_nombres()
        print(f"   Nombres normalizados: {nombres_normalizados}")
        
        print("\n" + "=" * 80)
        print("LIMPIEZA COMPLETADA")
        print("=" * 80)
        
        return self.df_limpio, self.obtener_reporte_cambios()


# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def limpiar_datos_usuarios(df: pd.DataFrame, guardar_reporte: bool = True) -> Tuple[pd.DataFrame, Dict]:
    """
    Función principal para limpiar el dataset de usuarios.
    
    Args:
        df (pd.DataFrame): DataFrame con datos de usuarios
        guardar_reporte (bool): Si True, guarda el reporte en archivo
    
    Returns:
        Tuple[pd.DataFrame, Dict]: DataFrame limpio y reporte de cambios
    
    Ejemplo:
        >>> df_usuarios = pd.read_csv('usuarios.csv')
        >>> df_limpio, reporte = limpiar_datos_usuarios(df_usuarios)
    """
    limpiador = LimpiezaUsuarios(df)
    df_limpio, reporte = limpiador.ejecutar_limpieza_completa()
    
    if guardar_reporte:
        limpiador.guardar_reporte_cambios()
        print("\nReporte guardado en 'reporte_limpieza_usuarios.txt'")
    
    return df_limpio, reporte


def mostrar_reporte_cambios(reporte: Dict) -> None:
    """
    Muestra el reporte de cambios en formato legible.
    
    Args:
        reporte (Dict): Diccionario con el reporte de cambios
    """
    print("\n" + "=" * 80)
    print("RESUMEN DEL REPORTE DE LIMPIEZA")
    print("=" * 80)
    print(f"\nFecha: {reporte['fecha_proceso']}")
    print(f"Registros iniciales: {reporte['registros_iniciales']}")
    print(f"Registros finales: {reporte['registros_finales']}")
    print(f"Registros eliminados: {reporte['registros_eliminados_total']}")
    print(f"\nTotal de cambios realizados: {len(reporte['cambios_realizados'])}")
    print("\nDetalle de cambios:")
    
    for cambio in reporte['cambios_realizados']:
        print(f"  ✓ {cambio['tipo']}")


# ============================================================================
# EJEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Crear datos de ejemplo
    datos_ejemplo = {
        'id': [1, 2, 3, 4, 5, 6, 7],
        'nombre': ['juan perez', 'MARIA GARCIA', 'carlos  lopez', None, 'ana martinez', 'juan perez', 'luis rodriguez'],
        'correo': ['JUAN@EMAIL.COM', 'maria@email.com', 'carlos@email.com', 'test@email.com', 'ana@EMAIL.COM', 'juan@email.com', '   luis@email.com   '],
        'clave': ['pass123', 'pass456', None, 'pass789', 'pass101', 'pass123', 'pass202'],
        'fk_rol': [1, 2, 1, 2, None, 1, 1]
    }
    
    df_ejemplo = pd.DataFrame(datos_ejemplo)
    
    print("DATASET ORIGINAL:")
    print(df_ejemplo)
    print(f"\nTotal registros: {len(df_ejemplo)}\n")
    
    # Ejecutar limpieza
    df_limpio, reporte = limpiar_datos_usuarios(df_ejemplo)
    
    print("\n\nDATASET LIMPIO:")
    print(df_limpio)
    
    # Mostrar reporte
    mostrar_reporte_cambios(reporte)