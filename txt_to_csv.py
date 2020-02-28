#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:32:01 2020

@author: cfx
"""

import pandas as pd
import numpy as np
#df = pd.read_fwf('15mm_campo_topo_t05.txt')
#df.to_csv('15mm_campo_topo_t05.csv')
import glob
path = r'/home/cfx/Rebeca' # use your path
all_files = glob.glob('15mm_campo_topo_t0*.csv')
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
frame = pd.concat(li, axis=1, ignore_index=True)
frame=frame.drop(df.index[0:5])
frame=frame.iloc[:,[0,1,2,8,9,28,29,48,49,68,69,88,89]]
frame = frame.convert_objects(convert_dates='coerce',convert_numeric=True)
R1=frame.filter([8,28,48,68,88], axis=1)
R2=frame.filter([9,29,49,69,89], axis=1)
df1 = pd.DataFrame(R1) 
df2 = pd.DataFrame(R2)
Mean1=df1.mean(axis=1)
Mean2=df2.mean(axis=1)
DLDA1=0.03902   #Em metros
DLDA2=0.03878   #Em metros
LâmbidaLDA1=0.000000561   #Em metros
LâmbidaLDA2=0.000000532   #Em metros
Dfocal=0.1596   #Em metros
Incerteza_D=0.00002   #Em metros
Incerteza_f=0.00002   #Em metros
Hz=852190.7893
TB1=0.007557497351   #Em radianos
gama1=np.arctan((DLDA1/2)/Dfocal)
gama2=np.arctan((DLDA2/2)/Dfocal)
CTE1=(LâmbidaLDA1/(2*np.sin(gama1)))  #aproximação diferente
CTE2=(LâmbidaLDA2/(2*np.sin(gama2)))  #aproximação diferente
Mean1F=(Mean1/CTE1)
Mean2F=(Mean2/CTE2)
STD1=((R1.std(axis=1))/np.sqrt(2))
STD2=((R2.std(axis=1))/np.sqrt(2))
STD1F=STD1/CTE1
STD2F=STD2/CTE2
Incerteza_ângulo1=np.sqrt(((Dfocal*2*Incerteza_D)/((4*(Dfocal)**2)+((DLDA1)**2)))**2+((-2*DLDA1*Incerteza_f)/((4*(Dfocal)**2)+(DLDA1**2)))**2)
Incerteza_ângulo2=np.sqrt(((Dfocal*2*Incerteza_D)/((4*(Dfocal)**2)+((DLDA2)**2)))**2+((-2*DLDA2*Incerteza_f)/((4*(Dfocal)**2)+(DLDA2**2)))**2)
Componente_ângulo1=(-np.cos(gama1)*Mean1*Incerteza_ângulo1/(2*np.sin(gama1)))
Componente_ângulo2=(-np.cos(gama2)*Mean2*Incerteza_ângulo2/(2*np.sin(gama2)))
Tait_Bryan1=(((np.cos(TB1)**2)-((np.sin(TB1)**3)))-1)*Mean1F-(np.cos(TB1)*np.sin(TB1))*Mean2F+((np.cos(TB1)*np.sin(TB1))+(np.cos(TB1)*np.sin(TB1)**2))*Hz
Tait_Bryan2=((np.cos(TB1)*np.sin(TB1))+(np.cos(TB1)*np.sin(TB1)**2))*Mean1F+((np.cos(TB1)**2)-1)*Mean2F+((np.sin(TB1)**2)-((np.cos(TB1)**2)*(np.sin(TB1))))*Hz
Incerteza_Freq1=np.sqrt((STD1F)**2+(Tait_Bryan1)**2)
Incerteza_Freq2=np.sqrt((STD2F)**2+(Tait_Bryan2)**2)
Componente_Freq1=((LâmbidaLDA1)*Incerteza_Freq1)/(2*np.sin(gama1))
Componente_Freq2=((LâmbidaLDA2)*Incerteza_Freq2)/(2*np.sin(gama2))
Incerteza_Extendida1=2*(np.sqrt((Componente_ângulo1)**2+(Componente_Freq1)**2))
Incerteza_Extendida2=2*(np.sqrt((Componente_ângulo2)**2+(Componente_Freq2)**2))
Result = ([frame.iloc[:,[1]], frame.iloc[:,[2]], Mean1, Mean2, Incerteza_Extendida1, Incerteza_Extendida2])
Result_con= pd.concat(Result, axis=1, ignore_index=True)
#Result_df=pd.DataFrame(['X[mm]','Y[mm]','MédiaLda1','MédiaLda2','IncertezaExtendidaLda1','IncertezaExtendidaLda2'])
#for i in range(781):
 #   df.loc[i]=Result_con
#Final=Result_df.append(Result_con)
#result = [Result_df, Result_con]
#result = pd.concat(result)
#Result_df=({"X[mm]":[Result_con[0]],"Y[mm]":[Result_con[1]],"Média Lda1":[Result_con[2]], "Média Lda2":[Result_con[3]], "Incerteza Extendida Lda1":[Result_con[4]], "Incerteza Extendida Lda2":[Result_con[5]]})
#Final=pd.DataFrame(Result_df)
#print(Result_df)
result = pd.DataFrame(Result_con.values, columns = ['X[mm]','Y[mm]','MédiaLda1','MédiaLda2','IncertezaExtendidaLda1','IncertezaExtendidaLda2'] )
result.to_csv("/home/cfx/Rebeca/Final")