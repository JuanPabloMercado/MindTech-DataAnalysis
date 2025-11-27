import pandas as pd

def cargar_dataset(path):
    """Carga un CSV y devuelve un DataFrame."""
    return pd.read_csv(path, skipinitialspace=True)
