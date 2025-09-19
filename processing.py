import pandas as pd
import os

# Carpetas
RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(__file__), "../data/processed")
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# -------------------------------
# Función para leer CSV de forma segura
# -------------------------------
def read_csv_safe(file_path):
    """
    Lee el CSV ignorando la fila extra de ticker repetido y parsea la fecha.
    """
    # La fila 0 tiene 'Date, Close, High...' -> usamos header=0
    # La fila 1 es la fila con 'IEV, IEV, ...' que ignoramos
    df = pd.read_csv(file_path, header=0, skiprows=[1])

    # Convertimos 'Date' a datetime
    df['Date'] = pd.to_datetime(df['Date'])

    return df


# -------------------------------
# Función para revisar los datos
# -------------------------------
def check_data(df, file_path):
    """
    Revisa que los datos estén correctos.
    - Muestra primeras filas y estadísticas.
    """
    print(f"\nArchivo: {file_path}")
    print("Primeras filas:")
    print(df.head())
    print("\nResumen estadístico:")
    print(df.describe())
    print("\nTipos de columnas:")
    print(df.dtypes)

# -------------------------------
# Función para añadir métricas financieras
# -------------------------------
def add_metrics(df):
    """
    Añade métricas financieras usando la columna 'Close'.

    Columnas nuevas:
    - Daily_Return: retorno diario
    - Cumulative_Return: retorno acumulado
    - Volatility_Annual: volatilidad anualizada
    - Rolling_30D_Volatility: volatilidad móvil 30 días
    - Drawdown: caída máxima desde un pico histórico
    - Rolling_30D_Return: retorno acumulado móvil 30 días
    """
    df = df.sort_values('Date')

    price_col = 'Close'  # Usamos 'Close' ya que no hay 'Adj Close'

    # Retorno diario
    df['Daily_Return'] = df[price_col].pct_change()

    # Retorno acumulado
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1

    # Volatilidad anualizada (252 días de trading)
    df['Volatility_Annual'] = df['Daily_Return'].rolling(window=252).std() * (252**0.5)

    # Volatilidad móvil 30 días
    df['Rolling_30D_Volatility'] = df['Daily_Return'].rolling(window=30).std() * (252**0.5)

    # Drawdown
    df['Cumulative_Max'] = df[price_col].cummax()
    df['Drawdown'] = (df[price_col] - df['Cumulative_Max']) / df['Cumulative_Max']
    df.drop(columns=['Cumulative_Max'], inplace=True)

    # Retorno acumulado móvil 30 días
    df['Rolling_30D_Return'] = df['Daily_Return'].rolling(window=30).sum()

    return df

# -------------------------------
# Función para procesar todos los CSVs
# -------------------------------
def process_all():
    """
    Procesa todos los CSV en la carpeta data/
    - Revisa los datos
    - Añade métricas financieras
    - Guarda el CSV procesado en data/processed/
    """
    for file in os.listdir(RAW_DATA_DIR):
        if file.endswith(".csv"):
            path = os.path.join(RAW_DATA_DIR, file)

            # Leer CSV seguro
            df = read_csv_safe(path)

            # Revisar datos
            check_data(df, path)

            # Añadir métricas
            df = add_metrics(df)

            # Guardar CSV procesado
            out_path = os.path.join(PROCESSED_DATA_DIR, file)
            df.to_csv(out_path, index=False)
            print(f"Procesado y guardado: {out_path}")

# -------------------------------
# Test rápido si se ejecuta directamente
# -------------------------------
if __name__ == "__main__":
    process_all()
