import pandas as pd

def rename_columns(df, names):
    df1 = df.copy()
    df1.columns = list(names)
    return df1

