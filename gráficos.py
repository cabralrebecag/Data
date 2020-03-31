#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:40:52 2020

@author: rebecacabral
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from txt_to_csv import frame
from txt_to_csv import R1
from txt_to_csv import R2

plot = ([frame[1],frame[2],R1,R2])
plot = pd.concat(plot, axis=1, ignore_index=True)

plot = np.array(round(plot,2))

li=[]
for i in range(len(plot)):
        if plot[i][0] == 1.50e-01:
            li.append(plot[i][:])
            
ax1=plt.subplot(1,1,1)
q1=ax1.quiver(li[:][0], li[:][1], li[:[2]], li[:][3], li[:][4], li[:[5]])
      
        
        


        



        