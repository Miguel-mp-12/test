# Métricas financieras: guía para entenderlas y aplicarlas

Cuando hablamos de ETF, fondos o carteras, estas son las métricas clave
que un Data Analyst financiero suele calcular:

## Retornos

- Daily Return (Daily_Return)

Retorno diario = (Precio hoy / Precio ayer) - 1

Muestra cómo cambia el valor cada día.

- Cumulative Return (Cumulative_Return)

Retorno acumulado = producto(1 + Daily Return) - 1

Muestra cuánto habría crecido o caído la inversión desde el inicio.

- Monthly / Yearly Return

Se agrupa por mes o año y se calcula la misma fórmula.

Útil para comparar rendimiento en periodos largos.

## Riesgo

- Volatilidad

Desviación estándar de los retornos diarios.

Mayor volatilidad → inversión más arriesgada.

Fórmula simplificada: vol = std(Daily_Return) * sqrt(252) (para anualizar).

- Drawdown

Mide la caída máxima desde un pico hasta un valle.

Indica el peor escenario histórico para la inversión.

## Relación riesgo/rendimiento

Sharpe Ratio

Sharpe = (Rendimiento medio - Tasa libre de riesgo) / Volatilidad

Permite comparar inversiones teniendo en cuenta su riesgo.

Más alto = mejor rendimiento ajustado al riesgo.

## Correlación y diversificación

Correlación entre ETFs o fondos:

1 → se mueven juntos

0 → movimientos independientes

-1 → se mueven en sentidos opuestos

Muy útil para armar una cartera diversificada.

## Visualizaciones recomendadas

- Líneas de precios / retornos acumulados → evolución histórica.

- Barras de retorno mensual/anual → comparar periodos.

- Heatmap de correlaciones → entender diversificación.

- Drawdown plot → ver máximas caídas históricas.

En conjunto, estas métricas te permiten entender el comportamiento
de un fondo o ETF desde diferentes perspectivas:

- Rentabilidad → cuánto ganas

- Riesgo → cuánto puedes perder

- Sharpe / correlaciones → cómo se ajusta al riesgo y diversifica la cartera