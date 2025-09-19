---
title: "Resumen del Script Processing"
author: "Miguel"
date: "`r Sys.Date()`"
output: html_document
---

# Propósito del Script

El script **`processing.py`** procesa los CSV descargados desde la API de Yahoo Finance (ETFs/fondos) y calcula métricas financieras para análisis y reportes.

- Lee todos los CSVs de la carpeta `data/`.
- Ignora filas innecesarias que contienen solo nombres repetidos.
- Convierte la columna `Date` a tipo datetime.
- Calcula métricas financieras importantes y guarda un CSV procesado en `data/processed/`.

---

# Revisión de Datos

Antes de calcular métricas, el script revisa cada CSV:

- Muestra **primeras filas**.
- Muestra **estadísticas básicas** (`mean`, `min`, `max`, etc.).
- Muestra **tipos de columnas** para asegurar que están correctos.

---

# Métricas Financieras Calculadas

Cada CSV procesado contiene estas columnas nuevas:

| Columna                  | Descripción |
|---------------------------|-------------|
| Daily_Return             | Retorno diario: `(Close / Close_anterior - 1)` |
| Cumulative_Return        | Retorno acumulado desde la primera fecha |
| Volatility_Annual        | Volatilidad anualizada basada en retorno diario (252 días de trading) |
| Rolling_30D_Volatility   | Volatilidad móvil de 30 días |
| Drawdown                 | Caída máxima desde un pico histórico |
| Rolling_30D_Return       | Retorno acumulado móvil de 30 días |

> Nota: Las métricas basadas en ventanas (`Volatility_Annual`, `Rolling_30D_Volatility`, `Drawdown`, `Rolling_30D_Return`) **pueden tener NaN en los primeros días**, lo cual es normal porque no hay suficientes datos aún.

---

# Resultado Final

- Cada ETF/fondo tiene un **CSV procesado** en `data/processed/` listo para:
  - Análisis financiero.
  - Gráficos comparativos.
  - Reportes PDF corporativos.

- Este enfoque modular permite:
  - Importar funciones (`add_metrics`, `check_data`) en otros scripts.
  - Probar el procesamiento de todos los CSVs directamente ejecutando `processing.py`.

---
