# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:03:10 2021

@author: Camilo
"""

import matplotlib.pyplot as plt
import numpy as np

def data(Cph,Cpc,Th,Tc):
    #Calculo T, dT, Q
    T  = np.array([])
    for i in range(len(Th)):
        T = np.append(T, Th[i,:]) 
    for i in range(len(Tc)):
        T = np.append(T, Tc[i,:]) 
    dTh = np.array([])
    for i in range(len(Th)):
        dTh = np.append(dTh, Th[i,1]-Th[i,0])
    dTc = np.array([])
    for i in range(len(Tc)):
        dTc = np.append(dTc, Tc[i,1]-Tc[i,0])

    Qh = np.array([])
    for i in range(len(Th)):
        Qh = np.append(Qh, Cph[i]*dTh[i])
    Qc = np.array([])
    for i in range(len(Tc)):
        Qc = np.append(Qc, Cpc[i]*dTc[i])

    Qh_acc = np.array([0])
    for i in range(len(Qh)):
        Qh_acc = np.append(Qh_acc, Qh_acc[i]+Qh[i])

    Qc_acc = np.array([0])
    for i in range(len(Qc)):
        Qc_acc = np.append(Qc_acc, Qc_acc[i]+Qc[i])
    
#Cálculo Corrientes Compuestas 
    #Caliente
    hot = []
    hot = np.append(hot, (Th[:]))
    hot.sort()

    Cph_acu = np.array([])
    result = np.where(Th == hot[0])
    Cph_acu = np.append(Cph_acu, Cph[int(result[0])])

    for i in range(1, len(hot)):
        Cpi = 0
        for n in range(len(Th)):
            if hot[i] in Th[n] or (hot[i] > Th[n][0] and hot[i] < Th[n][1]): 
                Cpi = Cpi + Cph[n]
        if Cpi != 0 : 
            Cph_acu = np.append(Cph_acu,Cpi)

    #Código raro para eliminar Cps repetidos consecutivos
    n = np.array([Cph_acu[0]])
    for i in range(1,len(Cph_acu)):
       if Cph_acu[i] != Cph_acu[i-1]:
           n = np.append(n,Cph_acu[i])
    Cph_acu = n       


    #Código Calcular Q Compuesto
    Qh_comp = np.array([0])       

    for i in range(len(Cph_acu)):
        Qh_comp = np.append(Qh_comp, Qh_comp[i] + (Cph_acu[i]*(hot[i+1]-hot[i])))
        
    #Fria
    cold = []
    cold = np.append(cold, (Tc[:]))
    cold.sort()

    Cpc_acu = np.array([])
    result = np.where(Tc == cold[0])
    Cpc_acu = np.append(Cpc_acu, Cpc[int(result[0])])
    for i in range(1, len(cold)):
        Cpi = 0
        for n in range(len(Tc)):
            if cold[i] in Tc[n] or (cold[i] > Tc[n][0] and cold[i] < Tc[n][1]): 
                Cpi = Cpi + Cpc[n]
        if Cpi != 0 : 
            Cpc_acu = np.append(Cpc_acu,Cpi)

#Código raro para eliminar Cps repetidos consecutivos
    n = np.array([Cpc_acu[0]])
    for i in range(1,len(Cpc_acu)):
        if Cpc_acu[i] != Cpc_acu[i-1]:
            n = np.append(n,Cpc_acu[i])
    Cpc_acu = n       


#Código Calcular Q Compuesto
    Qc_comp = np.array([0])       
    for i in range(len(Cpc_acu)):
        Qc_comp = np.append(Qc_comp, Qc_comp[i] + (Cpc_acu[i]*(cold[i+1]-cold[i])))

    return(Qh,Qc,Qh_acc,Qc_acc,hot,cold,Qh_comp,Qc_comp)

	
def plot(Tc):
    fig, ax = plt.subplots(1,2,figsize=(15,5))
    ax[0].set_title("Hot Steam")
    ax[1].set_title("Cold Steam")
    for i in range(len(Tc)):
        ax[0].plot([Qh_acc[i],Qh_acc[i+1]],Th[i], 'r')
        ax[0].plot([0,Qh_acc[-1]],[Th[i],Th[i]],':k')
    for i in range(len(Tc)):
        ax[1].plot([Qc_acc[i],Qc_acc[i+1]],Tc[i], 'b')
        ax[1].plot([0,Qc_acc[-1]],[Tc[i],Tc[i]],'--k')
    for i in range(len(ax)):
        ax[i].set(xlabel='Q', ylabel='T')
