#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:55:38 2020

@author: cfx
"""
import pandas as pd
import numpy as np
H=76.2  #em mm
D=10.75  #em mm
At=H**2-25*((np.pi*D**2)/4)
P=(4*H)+(25*np.pi*D)
Dh=(4*At)/P
Incerteza_Dh=np.sqrt((((((((4*H)+(25*np.pi*D))*8*H)-((4*(H**2))-25*np.pi*(D**2))*4)/(((4*H)+(25*np.pi*D))**2))*H)**2)+((((((4*H)+25*np.pi*D)*50*np.pi*D)-(((4*(H**2))-(25*np.pi*(D**2)))*25*np.pi))/(((4*H)+(25*np.pi*D))**2))*D)**2)
df = pd.read_fwf('HTP07.23.3')
df.to_csv('HTP07.23.3.csv')
df = pd.read_fwf('HTP07.24.4')
df.to_csv('HTP07.24.4.csv')
df = pd.read_fwf('HTP07.25.5')
df.to_csv('HTP07.25.5.csv')
df = pd.read_fwf('HTP07.26.7')
df.to_csv('HTP07.26.7.csv')
df = pd.read_fwf('HTP07.27.8')
df.to_csv('HTP07.27.8.csv')
df = pd.read_fwf('HTP07.28.9')
df.to_csv('HTP07.28.9.csv')
df0 = pd.read_fwf('HTP07.29.0')
df0.to_csv('HTP07.29.0.csv')
import glob
path = r'/home/cfx/Rebeca/W_COMBINADA' # use your path
all_files = glob.glob('HTP07.2*.csv')
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
frame = pd.concat(li, axis=1, ignore_index=True)

a0= 0.244257733
a1=0.00974634476
a2=-0.00373234996
a3=0.000268678472
a4=0.0015892057
a5=0.00245934259
a6=0.90070492
a7=-0.0166626219
lambIR=5.432937
lambUV=0.229202
T=273.15
RO=1000
LAMB=589
LAMB1=532

MédiaT=frame.iloc[:,[8,34,60,86,112,138,164]]
MédiaT=MédiaT.mean(axis=0)
MédiaT=MédiaT.mean()
MédiaT=MédiaT+273.15

MédiaROST=frame.iloc[:,[10,36,62,88,114,140,172]]
médiaROST=MédiaROST.mean(axis=0)
MmédiaROST=médiaROST.mean()
stdROST=((MédiaROST.std(axis=1))/np.sqrt(2))

Ta=MédiaT/T
ROa=MédiaROST/RO
LAMBa=LAMB1/LAMB
C=a0+a1*ROa+a2*Ta+(a3*(LAMBa**2)*Ta)+(a4/LAMBa**2)+(a5/(LAMBa**2-lambUV**2))+(a6/(LAMBa**2-lambIR**2))+a7*ROa
nH20=np.sqrt(((2*ROa*C)+1)/(1-(ROa*C)))

MédiaRE=frame.iloc[:,[20,46,72,98,124,150,176]]
médiaRE=MédiaRE.mean(axis=0)
VetorRE=[médiaRE[20],médiaRE[46],médiaRE[72],médiaRE[98],médiaRE[124],médiaRE[150],médiaRE[176]]
MmédiaRE=sum(VetorRE) / len(VetorRE) 
stdRE=((médiaRE.std(axis=0))/np.sqrt(2))

MédiaROPO=frame.iloc[:,[16,42,68,94,120,146,172]]
médiaROPO=MédiaROPO.mean(axis=0)
VetorROPO=[médiaROPO[16],médiaROPO[42],médiaROPO[68],médiaROPO[94],médiaROPO[120],médiaROPO[146],médiaROPO[172]]
MmédiaROPO=sum(VetorROPO)/len(VetorROPO)
stdROPO=((MédiaROPO.std(axis=1))/np.sqrt(2))

Visc=frame.iloc[:,[18,44,70,96,122,148,174]]
visc=Visc.mean(axis=0)
visc=visc*0.10
Vetorvisc=[visc[18],visc[44],visc[70],visc[96],visc[122],visc[148],visc[174]]
Mvisc=sum(Vetorvisc) / len(Vetorvisc) 
stdVisc=((visc.std(axis=0))/np.sqrt(2))

w=np.divide(np.multiply(médiaRE,visc), np.multiply(médiaROPO,Dh))
W=w.mean()
stdW=((w.std(axis=0))/np.sqrt(2))
stdDERI=((((Mvisc*stdRE)/(MmédiaROPO*Dh))**2)+(((MmédiaRE*stdVisc)/(MmédiaROPO*Dh))**2)+(((MmédiaRE*Mvisc*stdROPO)/(Dh*(MmédiaROPO)**2))**2)+(((MmédiaRE*Mvisc*Incerteza_Dh)/(Dh*(MmédiaROPO)**2))**2))
stdDERI=stdDERI.mean()
stdCOMB=np.sqrt((0**2)+(stdDERI**2))
stdEXP=2*np.sqrt((stdW**2)+(stdDERI**2))
result = pd.DataFrame([W,stdCOMB,stdEXP], index = ['W','Incerteza Combinada', 'Incerteza Expandida'])
print(result)