import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
df = pd.read_csv("https://pycourse.s3.amazonaws.com/movies.csv")


#Analise exploratoria dos dados com report em HTML
#profile = ProfileReport(df=df, title="Movies dataset")
#profile.to_file('Analise_df_movies.html')

#Limpeza de dados faltantes e n�o numericos

#  Inicie sempre removendo as colunas com poucas entradas v�lidas
df.drop(['belongs_to_collection',
         'homepage',
         'tagline'],
         axis='columns',
         inplace=True)
# limpeza: remo��o de colunas com pouca variabilidade ou irrelevante para a an�lise

df.drop(['adult', 'overview'],
        axis='columns',
        inplace=True)
# limpeza: remo��o de linhas com dados faltantes
df.dropna(axis='index', inplace=True) #removendo todas as linhas que tenham dados faltantes







