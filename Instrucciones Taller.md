# 📊 TALLER: DASHBOARD DE VISUALIZACIÓN CON MATPLOTLIB

## 🎯 Objetivo
Crear un dashboard básico con 4 visualizaciones usando matplotlib, demostrando comprensión de los conceptos de graficación y visualización de datos.

## 📁 Archivos Proporcionados

1. **`dashboard_simple.py`** - Plantilla con código guiado (70% completo)
2. **`sales_data_2024.csv`** - Dataset de ventas con 50+ registros

## 🚀 Inicio Rápido

### Opción A: Para Principiantes (Recomendado)
Usa `dashboard_simple.py` - tiene el código casi completo con instrucciones claras.

```bash
# 1. Instalar librerías necesarias
pip install matplotlib pandas numpy

# 2. Abrir el archivo dashboard_simple.py
# 3. Seguir las instrucciones TODO
# 4. Ejecutar el código
python dashboard_simple.py
```

## 📝 Tareas a Completar

### Nivel Básico (dashboard_simple.py)
- [ ] Cargar el archivo CSV correctamente
- [ ] Completar el cálculo de ventas por producto
- [ ] Terminar la gráfica de distribución regional
- [ ] Implementar la línea de tendencia temporal
- [ ] Crear el top 5 de productos

### Nivel Intermedio (Personalización)
- [ ] Cambiar al menos 3 colores
- [ ] Modificar títulos para mayor claridad
- [ ] Ajustar el tamaño de la figura
- [ ] Agregar etiquetas a los ejes

## 🎨 Código de Ejemplo

### Cargar datos:
```python
import pandas as pd
df = pd.read_csv('sales_data_2024.csv')
```

### Crear gráfica de barras:
```python
import matplotlib.pyplot as plt
ventas = df.groupby('Product')['Sales'].sum()
plt.bar(ventas.index, ventas.values)
plt.show()
```

### Crear gráfica de pastel:
```python
regiones = df.groupby('Region')['Sales'].sum()
plt.pie(regiones.values, labels=regiones.index, autopct='%1.1f%%')
plt.show()
```

## ✅ Criterios de Evaluación

### Funcionamiento (40%)
- El código ejecuta sin errores
- Las 4 gráficas se muestran correctamente
- El dashboard se guarda como imagen

### Comprensión (30%)
- Uso correcto de `groupby()`
- Implementación adecuada de cada tipo de gráfica
- Datos calculados correctamente

### Presentación (20%)
- Títulos descriptivos
- Colores apropiados
- Layout organizado

### Creatividad (10%)
- Personalización adicional
- Mejoras visuales
- Elementos extra

## 💡 Tips y Trucos

1. **Si te atascas:** Lee los comentarios con pistas en el código
2. **Para depurar:** Usa `print()` para ver los datos intermedios
3. **Colores:** Usa códigos hex como `'#C5282F'` para rojo FESC
4. **Tamaños:** `figsize=(14, 8)` crea una figura de 14x8 pulgadas

## ⏱️ Tiempo Estimado

- **Versión Simple:** 30-45 minutos
- **Versión Completa:** 60-90 minutos

## 📤 Entrega

1. Código Python completado (`mi_dashboard.py`)
2. Dashboard guardado (`mi_dashboard_ventas.png`)
3. Captura de pantalla del código ejecutándose

## 🆘 Ayuda Rápida

### Error: "No module named 'pandas'"
```bash
pip install pandas matplotlib numpy
```

### Error: "File not found"
Asegúrate de estar en la carpeta correcta con el archivo CSV.

### Las gráficas se ven muy juntas
Usa `plt.tight_layout()` antes de mostrar.

## 🏆 Reto Extra (Opcional)

Si terminas antes, intenta:
1. Agregar una quinta gráfica
2. Implementar un filtro por fechas
3. Crear una animación de la tendencia
4. Exportar a PDF además de PNG

---

**¡Éxito en tu taller! Recuerda que el objetivo es aprender, no la perfección.** 🚀