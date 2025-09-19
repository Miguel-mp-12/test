import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# -------------------------------
# Configuración estética de gráficos
# -------------------------------
sns.set_theme(style="whitegrid")  # fondo blanco con grid
sns.set_context("talk")           # tamaño de fuentes para presentación

# -------------------------------
# Carpetas
# -------------------------------
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/processed")
PLOTS_DIR = os.path.join(os.path.dirname(__file__), "../plots")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "../results")
os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# -------------------------------
# Colores corporativos
# -------------------------------
COLORS = {
    "line": "#1f77b4",
    "volatility": "#ff7f0e",
    "drawdown": "#d62728",
    "cumulative": "#2ca02c"
}

# -------------------------------
# Función para cargar todos los CSVs procesados
# -------------------------------
def load_all_csvs():
    dataframes = {}
    for file in os.listdir(PROCESSED_DATA_DIR):
        if file.endswith(".csv"):
            ticker = file.replace(".csv", "")
            path = os.path.join(PROCESSED_DATA_DIR, file)
            df = pd.read_csv(path, parse_dates=['Date'])
            dataframes[ticker] = df
    return dataframes

# -------------------------------
# Funciones para graficar
# -------------------------------
def plot_price_and_cumulative(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close'], color=COLORS['line'], label='Close')
    plt.plot(df['Date'], df['Cumulative_Return'], color=COLORS['cumulative'], label='Cumulative Return')
    plt.title(f"{ticker} - Precio y Retorno Acumulado")
    plt.xlabel("Fecha")
    plt.ylabel("Valor")
    plt.legend()
    plt.tight_layout()
    out_file = os.path.join(PLOTS_DIR, f"{ticker}_price_cumulative.png")
    plt.savefig(out_file)
    plt.close()

def plot_drawdown(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Drawdown'], color=COLORS['drawdown'], label='Drawdown')
    plt.title(f"{ticker} - Drawdown")
    plt.xlabel("Fecha")
    plt.ylabel("Drawdown")
    plt.tight_layout()
    out_file = os.path.join(PLOTS_DIR, f"{ticker}_drawdown.png")
    plt.savefig(out_file)
    plt.close()

def plot_volatility(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Volatility_Annual'], color=COLORS['volatility'], label='Volatility Annual')
    plt.plot(df['Date'], df['Rolling_30D_Volatility'], color=COLORS['line'], label='Rolling 30D Volatility')
    plt.title(f"{ticker} - Volatilidad")
    plt.xlabel("Fecha")
    plt.ylabel("Volatilidad")
    plt.legend()
    plt.tight_layout()
    out_file = os.path.join(PLOTS_DIR, f"{ticker}_volatility.png")
    plt.savefig(out_file)
    plt.close()

# -------------------------------
# Función para calcular resumen de métricas
# -------------------------------
def summary_metrics(df, ticker):
    summary = {
        "Ticker": ticker,
        "Mean_Daily_Return": df['Daily_Return'].mean(),
        "Final_Cumulative_Return": df['Cumulative_Return'].iloc[-1],
        "Max_Drawdown": df['Drawdown'].min(),
        "Annual_Volatility": df['Volatility_Annual'].mean(),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # para tracking
    }
    return summary

# -------------------------------
# Función principal
# -------------------------------
def run_analysis():
    data = load_all_csvs()
    summaries = []

    for ticker, df in data.items():
        # Generar gráficos
        plot_price_and_cumulative(df, ticker)
        plot_drawdown(df, ticker)
        plot_volatility(df, ticker)

        # Guardar métricas resumidas
        summaries.append(summary_metrics(df, ticker))

    # Guardar CSV resumen con timestamp
    summary_df = pd.DataFrame(summaries)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = os.path.join(RESULTS_DIR, f"summary_metrics_{timestamp}.csv")
    summary_df.to_csv(summary_file, index=False)
    print(f"Resumen de métricas guardado: {summary_file}")

# -------------------------------
# Ejecutar análisis si se llama directamente
# -------------------------------
if __name__ == "__main__":
    run_analysis()
