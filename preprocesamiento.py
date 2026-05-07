import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def limpiar_datos(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def normalizar(df):
    return (df - df.min()) / (df.max() - df.min())

def codificar(df):
    return pd.get_dummies(df)