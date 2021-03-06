#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:04:21 2020

@author: rebecacabral
"""

import pandas as pd
import numpy as np
H=76.2  #em mm
D=10.75  #em mm
At=H**2-25*((np.pi*D**2)/4)
P=(4*H)+(25*np.pi*D)
Dh=(4*At)/P
Incerteza_Dh=np.sqrt((((((((4*H)+(25*np.pi*D))*8*H)-((4*(H**2))-25*np.pi*(D**2))*4)/(((4*H)+(25*np.pi*D))**2))*H)**2)+((((((4*H)+25*np.pi*D)*50*np.pi*D)-(((4*(H**2))-(25*np.pi*(D**2)))*25*np.pi))/(((4*H)+(25*np.pi*D))**2))*D)**2)
# df = pd.read_fwf('HTP07.23.3')
# df.to_csv('HTP07.23.3.csv')
# df = pd.read_fwf('HTP07.24.4')
# df.to_csv('HTP07.24.4.csv')
# df = pd.read_fwf('HTP07.25.5')
# df.to_csv('HTP07.25.5.csv')
# df = pd.read_fwf('HTP07.26.7')
# df.to_csv('HTP07.26.7.csv')
# df = pd.read_fwf('HTP07.27.8')
# df.to_csv('HTP07.27.8.csv')
# df = pd.read_fwf('HTP07.28.9')
# df.to_csv('HTP07.28.9.csv')
# df0 = pd.read_fwf('HTP07.29.0')
# df0.to_csv('HTP07.29.0.csv')
import glob

def path_pd(path3):
    save_path = path3
#path = r'/Users/rebecacabral/Documents/CDTN/W_COMBINADA' # use your path
    
    all_files = glob.glob(save_path + '/HTP07.2*.csv')
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        frame = pd.concat(li, axis=1, ignore_index=True)

    a0=0.244257733
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
    LAMB=589.0
    LAMB1=532.0

    MediaT=frame.iloc[:,[8,34,60,86,112,138,164]]
    MediaT=MediaT.mean(axis=0)
    MediaT=MediaT.mean()
    MediaT=MediaT+273.15

    MediaROST=frame.iloc[:,[10,36,62,88,114,140,172]]
    mediaROST=MediaROST.mean(axis=0)
    MmediaROST=mediaROST.mean()
    stdROST=((MediaROST.std(axis=1))/np.sqrt(2))

    Ta=MediaT/T
    ROa=MmediaROST/RO
    LAMBa=LAMB1/LAMB
    C=a0+a1*ROa+a2*Ta+(a3*(LAMBa**2)*Ta)+(a4/LAMBa**2)+(a5/(LAMBa**2-lambUV**2))+(a6/(LAMBa**2-lambIR**2))+a7*ROa
    nH20=np.sqrt(((2*ROa*C)+1)/(1-(ROa*C)))

    MediaRE=frame.iloc[:,[20,46,72,98,124,150,176]]
    mediaRE=MediaRE.mean(axis=0)
    VetorRE=[mediaRE[20],mediaRE[46],mediaRE[72],mediaRE[98],mediaRE[124],mediaRE[150],mediaRE[176]]
    MmediaRE=sum(VetorRE) / len(VetorRE) 
    stdRE=((mediaRE.std(axis=0))/np.sqrt(2))

    MediaROPO=frame.iloc[:,[16,42,68,94,120,146,172]]
    mediaROPO=MediaROPO.mean(axis=0)
    VetorROPO=[mediaROPO[16],mediaROPO[42],mediaROPO[68],mediaROPO[94],mediaROPO[120],mediaROPO[146],mediaROPO[172]]
    MmediaROPO=sum(VetorROPO)/len(VetorROPO)
    stdROPO=((MediaROPO.std(axis=1))/np.sqrt(2))

    Visc=frame.iloc[:,[18,44,70,96,122,148,174]]
    visc=Visc.mean(axis=0)
    visc=visc*0.10
    Vetorvisc=[visc[18],visc[44],visc[70],visc[96],visc[122],visc[148],visc[174]]
    Mvisc=sum(Vetorvisc) / len(Vetorvisc) 
    stdVisc=((visc.std(axis=0))/np.sqrt(2))

    w=np.divide(np.multiply(VetorRE,Vetorvisc), np.multiply(mediaROPO,Dh))
    W=w.mean()
    stdW=((w.std(axis=0))/np.sqrt(2))
    stdDERI=((((Mvisc*stdRE)/(MmediaROPO*Dh))**2)+(((MmediaRE*stdVisc)/(MmediaROPO*Dh))**2)+(((MmediaRE*Mvisc*stdROPO)/(Dh*(MmediaROPO)**2))**2)+(((MmediaRE*Mvisc*Incerteza_Dh)/(Dh*(MmediaROPO)**2))**2))
    stdDERI=stdDERI.mean()
    stdCOMB=np.sqrt((0**2)+(stdDERI**2))
    stdEXP=2*np.sqrt((stdW**2)+(stdDERI**2))
    resultad = pd.DataFrame([W,stdCOMB,stdEXP], index = ['W','Incerteza Combinada', 'Incerteza Expandida'])
    return(resultad)