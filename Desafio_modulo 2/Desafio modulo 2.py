import pandas as pd
import numpy as np

data_fr=pd.read_csv("C:/Users/mattheus.paula/Downloads/bike-sharing.csv")

#tamanho do data frame
#print(data_fr)

#media da coluna windspeed

#media=data_fr['windspeed'].mean()#fazer o slicing e calcular a media

#print(media)


#media da coluna temp
#media_temp=data_fr['temp'].mean()

#print(media_temp)


#registro 2011
#k11=data_fr[data_fr['year']==0]
#ou
#k11_2=data_fr[data_fr['datetime'].str.contains('2011',regex=False)]
#print(k11,k11_2)

#registro 2012
#k12=data_fr[data_fr['year']==1]
#ou
#k12_2=data_fr[data_fr['datetime'].str.contains('2012',regex=False)]

#print(k12,k12_2)


#media de locacao por estacao do ano

#df_medias=data_fr[['season','total_count']].groupby(data_fr['season']).mean()
#print(df_medias)

#maior e menor media de locacao por horario do dia

#data_fr['datetime']=pd.to_datetime(data_fr['datetime'])
#df_hora=data_fr[['hour','total_count']].groupby(data_fr['hour']).mean()
#print(df_hora,"\nO maior valor da media e :\n", max(df_hora['total_count']))
#print("\nO menor valor da menor media e:\n",min(df_hora['total_count']))


#dia da semana com a menor media

#df_day=data_fr[['weekday','total_count']].groupby(data_fr['weekday']).mean()
#print(df_day,"\nO menor valor da menor media e:\n",min(df_day['total_count']))


#Horario com a maior media de locacao as quartas feiras

#quartas=data_fr[data_fr['weekday']==3]
#quartas_horario=quartas[['hour','total_count']].groupby(quartas['hour']).mean()
#print(quartas_horario,"\nO horario com a maior media de locacao as quartas feiras",max(quartas_horario['total_count']))


#Horario com a maior media de locacao as sextas feiras

#sextas=data_fr[data_fr['weekday']==6]
#sextas_horario=sextas[['hour','total_count']].groupby(sextas['hour']).mean()
#print(quartas_horario,"\nO horario com a maior media de locacao as sextas feiras",max(sextas_horario['total_count']))





