---
title: "Análisis Financiero - Apuntes"
author: "Miguel"
date: "`r Sys.Date()`"
output: html_document
---

# Objetivo del Análisis

Usando los CSVs procesados en `data/processed/` con todas las métricas, podemos:

1. **Visualizar la evolución de cada inversión**
   - Gráficos de línea de `Close` y `Cumulative_Return` para ver el crecimiento histórico.

2. **Analizar el riesgo**
   - Volatilidad anual (`Volatility_Annual`) para medir cuánto varía la inversión.
   - Volatilidad móvil de 30 días (`Rolling_30D_Volatility`) para ver cambios recientes.
   - Drawdown para conocer la caída máxima desde un pico histórico.

3. **Comparar inversiones**
   - Retornos acumulados de varios ETFs/fondos en un mismo gráfico.
   - Heatmap de correlación de retornos diarios para entender diversificación.

4. **Identificar tendencias recientes**
   - Retornos móviles de 30 días (`Rolling_30D_Return`) para ver periodos de subida/bajada rápida.

5. **Preparar reportes y PDF corporativos**
   - Tablas resumen con métricas clave: media de retornos, volatilidad, máximo drawdown.
   - Gráficos limpios listos para presentación a directivos o para GitHub.

# Tip Extra

- Los **NaN** en métricas de ventana son normales y reflejan que no hay suficientes datos aún.
- Se puede combinar con métricas avanzadas (Sharpe Ratio, Beta, correlación con índice de referencia) para análisis profesional.
