def explorar_dataset(df):
    """Imprime información general del dataset."""
    print("\n Primeras filas:")
    print(df.head())

    print("\n Información del DataFrame:")
    print(df.info())

    print("\n Valores nulos:")
    print(df.isnull().sum())

    print("\n Resumen estadístico:")
    print(df.describe().round(2))
