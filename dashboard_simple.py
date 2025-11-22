#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard de Análisis de Ventas - Versión Simplificada
Curso: Diseño Funcional - Semestre VIII
FESC - Ingeniería de Software
Fecha: 21 de Noviembre de 2025

INSTRUCCIONES:
-------------
1. Lee todo el código antes de empezar
2. Completa las secciones marcadas con TODO
3. Ejecuta el código paso a paso para verificar
4. Personaliza colores y estilos al final
"""

from pathlib import Path
from textwrap import wrap

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.patches import FancyBboxPatch
import pandas as pd

# ============================================================================
# PASO 1: CARGAR LOS DATOS
# ============================================================================
print("=" * 60)
print("PASO 1: CARGANDO DATOS")
print("=" * 60)

data_path = Path(__file__).with_name('sales_data_2024.csv')
df = pd.read_csv(data_path, parse_dates=['Date'])
df.sort_values('Date', inplace=True)

print("✅ Datos cargados")
print(f"   Total de registros: {len(df)}")
print(f"   Columnas: {df.columns.tolist()}")

# ============================================================================
# PASO 2: PREPARAR LA FIGURA PRINCIPAL
# ============================================================================
print("\n" + "=" * 60)
print("PASO 2: CREANDO DASHBOARD")
print("=" * 60)

plt.style.use('seaborn-v0_8-whitegrid')
palette = ['#283845', '#33658A', '#86BBD8', '#F6AE2D', '#F26419', '#7EBDC2']
accent_color = '#F26419'

# Crear una figura grande para nuestro dashboard
fig = plt.figure(figsize=(16, 9.5))
fig.patch.set_facecolor('#f6f7fb')
fig.suptitle('Dashboard de Ventas 2024 • Diseño Funcional',
             fontsize=18, fontweight='bold', color='#1f2a44')
gs = fig.add_gridspec(3, 3, width_ratios=[1.2, 1, 0.9], height_ratios=[0.7, 1, 0.45],
                      wspace=0.3, hspace=0.35)

# ============================================================================
# PASO 3: CREAR 4 GRÁFICAS BÁSICAS
# ============================================================================

# ------------------------------------
# GRÁFICA 1: Ventas por Producto (Superior Izquierda)
# ------------------------------------
ax1 = fig.add_subplot(gs[0, :2])  # fila superior, primeras dos columnas

# TODO: Calcula las ventas totales por producto
# Pista: usa df.groupby('Product')['Sales'].sum()
ventas_por_producto = (
    df.groupby('Product')['Sales']
    .sum()
    .sort_values(ascending=False)
)
categorias_por_producto = (
    df.drop_duplicates('Product')
    .set_index('Product')['Category']
)
category_palette = {
    'Electronics': '#33658A',
    'Accessories': '#86BBD8',
    'Software': '#F6AE2D'
}
bar_colors = [category_palette.get(categorias_por_producto.get(prod, ''), palette[0])
              for prod in ventas_por_producto.index]

# TODO: Crea una gráfica de barras
# Pista: usa ax1.bar(x_posiciones, y_valores)
x_pos = range(len(ventas_por_producto))
wrapped_labels = ['\n'.join(wrap(prod, width=14)) for prod in ventas_por_producto.index]
bars1 = ax1.bar(x_pos, ventas_por_producto.values, color=bar_colors,
                edgecolor='#1f2a44', linewidth=0.5)
ax1.set_xticks(x_pos)
ax1.set_xticklabels(wrapped_labels, rotation=35, ha='right', fontsize=5)
ax1.set_title('Ventas totales por producto (Pareto)', fontsize=10)
ax1.set_ylabel('Ventas ($)', fontsize=7.5)
ax1.yaxis.set_major_formatter(mtick.StrMethodFormatter('$ {x:,.0f}'))
ax1.grid(axis='y', alpha=0.2)
ax1.margins(x=0.01)
ax1.tick_params(axis='y', labelsize=6)
ax1.bar_label(bars1, labels=[f"$ {v:,.0f}" for v in ventas_por_producto.values],
              padding=0.6, fontsize=4.2, rotation=90, label_type='edge')

cumulative_pct = ventas_por_producto.cumsum() / ventas_por_producto.sum() * 100
ax1b = ax1.twinx()
ax1b.plot(x_pos, cumulative_pct.values, color=accent_color,
          marker='o', linewidth=1.8)
ax1b.fill_between(x_pos, cumulative_pct.values, color=accent_color, alpha=0.07)
ax1b.set_ylabel('% acumulado', fontsize=7.3)
ax1b.set_ylim(0, 110)
ax1b.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1b.tick_params(axis='y', colors=accent_color, labelsize=5.7)
ax1b.spines['right'].set_color(accent_color)
ax1b.grid(False)

legend_handles = []
for categoria, color in category_palette.items():
    if categoria in categorias_por_producto.values:
        legend_handles.append(
            plt.Line2D([0], [0], marker='s', color='none', label=categoria,
                       markerfacecolor=color, markersize=10)
        )
if legend_handles:
    ax1.legend(handles=legend_handles, loc='upper right', fontsize=5,
               frameon=False, title='Categoría', title_fontsize=5.8)

print("✅ Gráfica 1: Ventas por Producto creada")

# ------------------------------------
# GRÁFICA 2: Distribución por Región (Superior Derecha)
# ------------------------------------
ax2 = fig.add_subplot(gs[0, 2])

# TODO: Calcula las ventas por región
ventas_por_region = (
    df.groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

# TODO: Crea una gráfica de pastel
# Pista: usa ax2.pie(valores, labels=etiquetas, autopct='%1.1f%%')
colores = palette[:len(ventas_por_region)]
wedges, texts, autotexts = ax2.pie(
    ventas_por_region.values,
    labels=ventas_por_region.index,
    colors=colores,
    autopct='%1.1f%%',
    pctdistance=0.8,
    startangle=90,
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)
plt.setp(autotexts, color='white', fontweight='bold')
ax2.set_title('Distribución porcentual de ventas por región')
# efecto dona
centre_circle = plt.Circle((0, 0), 0.55, fc='#f6f7fb')
ax2.add_artist(centre_circle)

print("✅ Gráfica 2: Distribución por Región creada")

# ------------------------------------
# GRÁFICA 3: Tendencia de Ventas (Inferior Izquierda)
# ------------------------------------
ax3 = fig.add_subplot(gs[1, 1:])

# TODO: Calcula las ventas diarias
ventas_diarias = df.groupby('Date')['Sales'].sum().sort_index()

# TODO: Crea una gráfica de líneas
# Pista: usa ax3.plot(x_fechas, y_valores)
ax3.plot(ventas_diarias.index, ventas_diarias.values,
         color=accent_color, linewidth=2.5, marker='o', markersize=4)
ax3.fill_between(ventas_diarias.index, ventas_diarias.values,
                 color=accent_color, alpha=0.15)
ax3.set_title('Tendencia diaria de ventas acumuladas')
ax3.set_xlabel('Fecha')
ax3.set_ylabel('Ventas ($)')
ax3.yaxis.set_major_formatter(mtick.StrMethodFormatter('$ {x:,.0f}'))
ax3.grid(True, alpha=0.3)
# Rotar fechas para mejor visualización
ax3.tick_params(axis='x', rotation=45)

print("✅ Gráfica 3: Tendencia de Ventas creada")

# ------------------------------------a
# GRÁFICA 4: Top 5 Productos (Inferior Derecha)
# ------------------------------------
ax4 = fig.add_subplot(gs[2, 1:])

# TODO: Obtén el top 5 de productos más vendidos
# Pista: usa .nlargest(5) después de agrupar
top_5_productos = ventas_por_producto.head(5)

# TODO: Crea una gráfica de barras horizontales
# Pista: usa ax4.barh(posiciones, valores)
y_pos = range(len(top_5_productos))
bars4 = ax4.barh(y_pos, top_5_productos.values,
                 color=palette[3], edgecolor='#1f2a44')
ax4.set_yticks(y_pos)
ax4.set_yticklabels(top_5_productos.index)
ax4.set_title('Top 5 productos más vendidos')
ax4.set_xlabel('Ventas ($)')
ax4.xaxis.set_major_formatter(mtick.StrMethodFormatter('$ {x:,.0f}'))
ax4.bar_label(bars4, labels=[f"$ {v:,.0f}" for v in top_5_productos.values],
              padding=3, fontsize=8)

print("✅ Gráfica 4: Top 5 Productos creada")

# ============================================================================
# PASO 4: AJUSTAR EL LAYOUT
# ============================================================================
for ax in (ax1, ax3, ax4):
    ax.set_facecolor('#ffffff')
    for spine in ax.spines.values():
        spine.set_visible(False)

total_sales = df['Sales'].sum()
total_units = df['Quantity'].sum()
avg_discount = df['Discount'].mean() * 100 if 'Discount' in df else 0
avg_ticket = total_sales / total_units if total_units else 0

ax_resumen = fig.add_subplot(gs[1:, 0])
ax_resumen.set_facecolor('#ffffff')
ax_resumen.set_xticks([])
ax_resumen.set_yticks([])
ax_resumen.set_xlim(0, 1)
ax_resumen.set_ylim(0, 1)
for spine in ax_resumen.spines.values():
    spine.set_visible(False)

ax_resumen.text(0.05, 0.9, 'Resumen 2024', fontsize=13, fontweight='bold',
                color='#1f2a44')
ax_resumen.text(0.05, 0.82, 'Indicadores clave del periodo', fontsize=8.5,
                color='#65738c')

kpi_data = [
    ('Ventas totales', f"$ {total_sales:,.0f}", '#33658A'),
    ('Unidades vendidas', f"{total_units:,.0f}", '#86BBD8'),
    ('Ticket promedio', f"$ {avg_ticket:,.0f}", '#F6AE2D'),
    ('Descuento promedio', f"{avg_discount:.1f}%", '#F26419'),
]

for idx, (label, value, color) in enumerate(kpi_data):
    y_center = 0.65 - idx * 0.18
    card = FancyBboxPatch((0.03, y_center - 0.07), 0.92, 0.12,
                          boxstyle="round,pad=0.02", linewidth=0,
                          facecolor=color, alpha=0.12)
    ax_resumen.add_patch(card)
    ax_resumen.text(0.06, y_center + 0.025, label.upper(), fontsize=8.5,
                    color='#1f2a44', fontweight='bold')
    ax_resumen.text(0.06, y_center - 0.015, value, fontsize=12,
                    color=color, fontweight='bold')

ax_resumen.text(0.05, 0.08,
                'Fuente: sales_data_2024.csv  •  Actualizado automáticamente',
                fontsize=7.5, color='#5c5c5c')

plt.subplots_adjust(left=0.04, right=0.98, top=0.9, bottom=0.05,
                    wspace=0.32, hspace=0.4)

# ============================================================================
# PASO 5: GUARDAR Y MOSTRAR
# ============================================================================
print("\n" + "=" * 60)
print("PASO 5: GUARDANDO DASHBOARD")
print("=" * 60)

# TODO: Guarda el dashboard como imagen
# Pista: usa plt.savefig('nombre_archivo.png', dpi=150)
plt.savefig('mi_dashboard_ventas.png', dpi=150, bbox_inches='tight')
print("✅ Dashboard guardado como 'mi_dashboard_ventas.png'")

# Mostrar el dashboard
plt.show()

print("\n" + "=" * 60)
print("¡FELICITACIONES! HAS COMPLETADO TU PRIMER DASHBOARD")
print("=" * 60)

# ============================================================================
# EJERCICIOS ADICIONALES (OPCIONAL)
# ============================================================================
"""
RETOS PARA MEJORAR TU DASHBOARD:
--------------------------------
1. Cambia los colores de las gráficas
2. Agrega más información a los títulos
3. Modifica el tamaño de la figura
4. Experimenta con diferentes tipos de gráficas
5. Agrega una quinta gráfica con información adicional

PREGUNTAS DE COMPRENSIÓN:
-------------------------
1. ¿Qué hace la función groupby()?
2. ¿Para qué sirve tight_layout()?
3. ¿Cómo cambiarías el tamaño de la figura?
4. ¿Qué diferencia hay entre plot() y bar()?
5. ¿Cómo agregarías una leyenda a las gráficas?
"""