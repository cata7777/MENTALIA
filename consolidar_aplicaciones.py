#!/usr/bin/env python3
"""
Script de Consolidación Inteligente - MENTALIA Ecosystem
Extrae y analiza todas las aplicaciones para crear versiones consolidadas
preservando las mejores características de cada una.
"""

import os
import zipfile
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

class ConsolidadorMentalia:
    def __init__(self, workspace_path: str):
        self.workspace = Path(workspace_path)
        self.temp_dir = Path("/tmp/mentalia_consolidacion")
        self.production_dir = self.workspace / "MENTALIA_PRODUCTION"
        
        # Crear directorios de trabajo
        self.temp_dir.mkdir(exist_ok=True, parents=True)
        self.production_dir.mkdir(exist_ok=True, parents=True)
        
        # Mapeo de aplicaciones por categoría
        self.aplicaciones = {
            'agenda_clinica': [],
            'formacion_laboral': [],
            'modulacion_emocional': [],
            'agenda_personal': [],
            'comunicacion': [],
            'despacho': [],
            'otros': []
        }
        
    def buscar_zips(self) -> List[Path]:
        """Busca todos los ZIPs en el workspace"""
        zips = []
        for zip_file in self.workspace.rglob("*.zip"):
            if zip_file.is_file():
                zips.append(zip_file)
        return zips
    
    def categorizar_aplicacion(self, zip_path: Path) -> str:
        """Categoriza una aplicación basada en su nombre"""
        nombre = zip_path.name.lower()
        
        if 'agenda' in nombre and ('clinica' in nombre or 'profesional' in nombre):
            return 'agenda_clinica'
        elif 'otec' in nombre or 'formacion' in nombre or 'laboral' in nombre:
            return 'formacion_laboral'
        elif 'blu' in nombre or 'modulacion' in nombre or 'emocional' in nombre:
            return 'modulacion_emocional'
        elif 'agenda' in nombre and 'personal' in nombre:
            return 'agenda_personal'
        elif 'comunicacion' in nombre or 'whatsapp' in nombre:
            return 'comunicacion'
        elif 'despacho' in nombre:
            return 'despacho'
        else:
            return 'otros'
    
    def extraer_zip(self, zip_path: Path) -> Tuple[Path, bool]:
        """Extrae un ZIP y retorna la ruta de extracción"""
        try:
            nombre_limpio = zip_path.stem.replace(' ', '_').replace('-', '_')
            extract_dir = self.temp_dir / nombre_limpio
            
            if extract_dir.exists():
                shutil.rmtree(extract_dir)
            
            extract_dir.mkdir(parents=True, exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            
            return extract_dir, True
            
        except Exception as e:
            print(f"Error extrayendo {zip_path}: {e}")
            return zip_path.parent, False
    
    def analizar_contenido(self, extract_dir: Path) -> Dict:
        """Analiza el contenido extraído para identificar características únicas"""
        caracteristicas = {
            'archivos': [],
            'tecnologias': set(),
            'funcionalidades': set(),
            'tamaño': 0
        }
        
        for archivo in extract_dir.rglob("*"):
            if archivo.is_file():
                caracteristicas['archivos'].append(archivo.name)
                caracteristicas['tamaño'] += archivo.stat().st_size
                
                # Detectar tecnologías
                ext = archivo.suffix.lower()
                if ext in ['.ts', '.tsx']:
                    caracteristicas['tecnologias'].add('TypeScript')
                elif ext in ['.js', '.jsx']:
                    caracteristicas['tecnologias'].add('JavaScript')
                elif ext == '.py':
                    caracteristicas['tecnologias'].add('Python')
                elif ext == '.vue':
                    caracteristicas['tecnologias'].add('Vue')
                elif ext in ['.html', '.css']:
                    caracteristicas['tecnologias'].add('Web')
                
                # Detectar funcionalidades por nombre de archivo
                nombre = archivo.name.lower()
                if 'login' in nombre:
                    caracteristicas['funcionalidades'].add('Autenticación')
                elif 'factur' in nombre or 'boleta' in nombre:
                    caracteristicas['funcionalidades'].add('Facturación')
                elif 'whatsapp' in nombre:
                    caracteristicas['funcionalidades'].add('WhatsApp')
                elif 'dsm' in nombre or 'cie10' in nombre:
                    caracteristicas['funcionalidades'].add('Diagnósticos')
                elif 'paciente' in nombre:
                    caracteristicas['funcionalidades'].add('Gestión_Pacientes')
                elif 'admin' in nombre:
                    caracteristicas['funcionalidades'].add('Panel_Admin')
                elif 'consentimiento' in nombre:
                    caracteristicas['funcionalidades'].add('Consentimiento_Digital')
        
        return caracteristicas
    
    def generar_matriz_consolidacion(self) -> Dict:
        """Genera matriz de características para consolidación inteligente"""
        print("🔍 Iniciando análisis de aplicaciones MENTALIA...")
        
        zips = self.buscar_zips()
        matriz = {}
        
        for zip_path in zips:
            categoria = self.categorizar_aplicacion(zip_path)
            print(f"📦 Procesando: {zip_path.name} → {categoria}")
            
            extract_dir, exito = self.extraer_zip(zip_path)
            if exito:
                caracteristicas = self.analizar_contenido(extract_dir)
                
                if categoria not in matriz:
                    matriz[categoria] = []
                
                matriz[categoria].append({
                    'nombre': zip_path.name,
                    'ruta': str(zip_path),
                    'ruta_extraida': str(extract_dir),
                    'caracteristicas': caracteristicas
                })
        
        return matriz
    
    def mostrar_matriz(self, matriz: Dict):
        """Muestra la matriz de consolidación"""
        print("\n" + "="*80)
        print("📊 MATRIZ DE CONSOLIDACIÓN MENTALIA")
        print("="*80)
        
        for categoria, apps in matriz.items():
            if apps:
                print(f"\n🏗️  CATEGORÍA: {categoria.upper()}")
                print("-" * 60)
                
                for i, app in enumerate(apps, 1):
                    carac = app['caracteristicas']
                    print(f"  {i}. {app['nombre']}")
                    print(f"     📁 Archivos: {len(carac['archivos'])}")
                    print(f"     💻 Tecnologías: {', '.join(carac['tecnologias'])}")
                    print(f"     ⚙️  Funcionalidades: {', '.join(carac['funcionalidades'])}")
                    print(f"     📏 Tamaño: {carac['tamaño']//1024} KB")
                    print()
    
    def recomendar_consolidacion(self, matriz: Dict) -> Dict:
        """Recomienda estrategia de consolidación por categoría"""
        recomendaciones = {}
        
        for categoria, apps in matriz.items():
            if not apps:
                continue
            
            # Encontrar la app más completa por funcionalidades
            app_principal = max(apps, key=lambda x: len(x['caracteristicas']['funcionalidades']))
            
            # Identificar funcionalidades únicas en otras apps
            funcionalidades_principal = app_principal['caracteristicas']['funcionalidades']
            funcionalidades_extras = set()
            
            for app in apps:
                if app != app_principal:
                    extras = app['caracteristicas']['funcionalidades'] - funcionalidades_principal
                    funcionalidades_extras.update(extras)
            
            recomendaciones[categoria] = {
                'app_base': app_principal['nombre'],
                'funcionalidades_a_integrar': list(funcionalidades_extras),
                'apps_total': len(apps),
                'consolidacion_requerida': len(apps) > 1
            }
        
        return recomendaciones
    
    def ejecutar_consolidacion(self):
        """Ejecuta el proceso completo de consolidación"""
        print("🚀 Iniciando Consolidación Inteligente MENTALIA")
        print("="*60)
        
        # Generar matriz
        matriz = self.generar_matriz_consolidacion()
        
        # Mostrar matriz
        self.mostrar_matriz(matriz)
        
        # Generar recomendaciones
        recomendaciones = self.recomendar_consolidacion(matriz)
        
        print("\n" + "="*80)
        print("💡 RECOMENDACIONES DE CONSOLIDACIÓN")
        print("="*80)
        
        for categoria, rec in recomendaciones.items():
            if rec['consolidacion_requerida']:
                print(f"\n🎯 {categoria.upper()}:")
                print(f"   📌 App Base: {rec['app_base']}")
                print(f"   🔧 Apps a consolidar: {rec['apps_total']}")
                print(f"   ➕ Funcionalidades a integrar: {', '.join(rec['funcionalidades_a_integrar'])}")
        
        # Guardar matriz para uso futuro
        with open(self.workspace / 'matriz_consolidacion.json', 'w', encoding='utf-8') as f:
            json.dump(matriz, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n✅ Matriz guardada en: matriz_consolidacion.json")
        print(f"📁 Archivos extraídos en: {self.temp_dir}")
        
        return matriz, recomendaciones

if __name__ == "__main__":
    consolidador = ConsolidadorMentalia("/workspaces/MENTALIA")
    matriz, recomendaciones = consolidador.ejecutar_consolidacion()
