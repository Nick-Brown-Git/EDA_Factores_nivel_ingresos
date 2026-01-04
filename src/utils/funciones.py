import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# function to show the coefficient of variation
def variabilidad(df):
    df_var = df.describe().loc[["std","mean"]].T
    df_var["CV"] = df_var["std"]/df_var["mean"]
    return df_var

# function to show the contigency table
def tabla_contingencia(df,col1,col2):
    tabla_contingencia = pd.crosstab(df[col1], df[col2])
    return tabla_contingencia

