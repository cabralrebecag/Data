#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:01:25 2020

@author: rebecacabral
"""

import csv
import pandas as pd
import numpy as np
 
save_path = r'/Users/rebecacabral/Documents/CDTN/TENSORES_DE_REYNOLDS'
st = '30mm_sub2_topo_t01.000001.txt'


lista=[]
linha=[]
aux1=[]


for aux in range (1,9):
    st2 = st[:-5]
    aux2 = str(aux)
    st3 = st2 + aux2 + '.txt'
    '    df = pd.read_fwf(st3)'
    
    

    with open(st3, newline='') as csvfile:
    
        spamreader = csv.reader(csvfile, delimiter=' ') 
    
        for linha in spamreader:
            aux1=str(linha[0]).split('\t')
            lista.append(aux1)
            

 
        
for aux in range (10,73):  #mudar o ultimo indice para o número de testes feitos pelo programa
    st2 = st[:-6]
    aux2 = str(aux)
    st3 = st2 + aux2 + '.txt'
    
    with open(st3, newline='') as csvfile:
    
        spamreader = csv.reader(csvfile, delimiter=' ') 
    
        for linha in spamreader:
            aux1=str(linha[0]).split('\t')
            lista.append(aux1)
            
            
#for aux in range (100,999):  #mudar o ultimo indice para o número de testes feitos pelo programa
#    st2 = st[:-6]
#    aux2 = str(aux)
#    st3 = st2 + aux2 + '.txt'
#    
#    with open(st3, newline='') as csvfile:
#    
#        spamreader = csv.reader(csvfile, delimiter=' ') 
#    
#        for linha in spamreader:
#            aux1=str(linha[0]).split('\t')
#            lista.append(aux1)

u=[]
v=[]
Vx=[]
Vy=[]
VxVx=[]
VyVy=[]
VxVy=[]
VxVxrms=[]
VyVyrms=[]
VxVyrms=[]

for i in lista:
    u.append(i[3])
    v.append(i[4])   
    
u=np.array(u,dtype=float)
v=np.array(v,dtype=float)
    
#umean=sum(u)/len(u)

u_prime = (u - (sum(u)/len(u)))
v_prime = (v - (sum(v)/len(v)))
umod_prime = np.absolute(u - u.mean())
vmod_prime = np.absolute(v - v.mean())
uv = (u_prime) * (v_prime)
uu = (u_prime) * (u_prime)
vv = (v_prime) * (v_prime)
    
uvmod = umod_prime*vmod_prime
    
    
Vx.append(u_prime.mean())
Vy.append(v_prime.mean())
VxVy.append(uv.mean())
VxVx.append((u_prime*u_prime).mean())
VyVy.append((v_prime*v_prime).mean())
VxVxrms.append(uu.mean()**0.5)
VyVyrms.append(vv.mean()**0.5)
VxVyrms.append(uvmod.mean()**0.5)
    
das = {'u':Vx,'v':Vy,'uu':VxVx, 'vv':VyVy,'uv':VxVy,'uu_rms':VxVxrms, 'vv_rms':VyVyrms,'uv_rms':VxVyrms}
resultado = pd.DataFrame(data=das)
pd.DataFrame(resultado).to_csv("30mm_sub2_topo_t01TR.csv", sep='\t')