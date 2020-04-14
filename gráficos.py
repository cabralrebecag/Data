#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:40:52 2020

@author: rebecacabral
"""

def perfil_velocidade(path_lda, path_pd):
    
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    
    #plot = (path_lda.frame + path_lda.R1 + path_lda.R2)
    
    plot = ([frame[1],frame[2],R1,R2])
    plot = pd.concat(plot, axis=1, ignore_index=True)

    plot = np.array(round(plot,3))

    li=[]
    for i in range(len(plot)):
        if plot[i][0] == 1.50e-01:
            li.append(plot[i][:])
            x = []          
            for i in li:
                x.append(i[1])
                x = np.divide(x,-14.3)
    
    y1 = []
    for i in li:
        y1.append(i[2])
    
    y2 = []
    for i in li:
        y2.append(i[3])
    
    y3 = []
    for i in li:
        y3.append(i[4])

    y4 = []
    for i in li:
        y4.append(i[5])
    
    y5 = []
    for i in li:
        y5.append(i[6])
    
    y6 = []
    for i in li:
        y6.append(i[7])
    
    y7 = []
    for i in li:
        y7.append(i[8])

    y8 = []
    for i in li:
        y8.append(i[9])
    
    y9 = []
    for i in li:
        y9.append(i[10])
    
    y10 = []
    for i in li:
        y10.append(i[11])
            
    fig, (ax1,ax2)=plt.subplots(1,2, figsize=(12,7))
    ax1.plot(x, np.divide(y1,path_pd.W), 'ro', label = 'Teste 1')
    ax1.plot(x, np.divide(y2,path_pd.W), 'bo', label = 'Teste 2')
    ax1.plot(x, np.divide(y3,path_pd.W), 'go', label = 'Teste 3')
    ax1.plot(x, np.divide(y4,path_pd.W), 'mo', label = 'Teste 4')
    ax1.plot(x, np.divide(y5,path_pd.W), 'yo', label = 'Teste 5')
    ax1.legend()
    ax1.set_ylabel('$u/w$')
    ax1.set_ylim(-0.1, 0.2)
    ax1.set_xlabel('$x/passo$')
    ax1.set_title('Perfil da velocidade $u$ no subcanal X' )
    ax2.plot(x, np.divide(y6,path_pd.W), 'ro', label = 'Teste 1')
    ax2.plot(x, np.divide(y7,path_pd.W), 'bo', label = 'Teste 2')
    ax2.plot(x, np.divide(y8,path_pd.W), 'go', label = 'Teste 3')
    ax2.plot(x, np.divide(y9,path_pd.W), 'mo', label = 'Teste 4')
    ax2.plot(x, np.divide(y10,path_pd.W), 'yo', label = 'Teste 5')
    ax2.legend()
    ax2.set_ylabel('$v/w$')
    ax2.set_ylim(-0.1, 0.2)
    ax2.set_xlabel('$x/passo$')
    ax2.set_title('Perfil da velocidade $v$ no subcanal X' )
    plt.savefig('/Users/rebecacabral/Documents/CDTN/INCERTEZA_EXT/Perfil_de_velocidade_U_e_V.png', format='png')
    plt.show()    
    return plt    
        


        



        