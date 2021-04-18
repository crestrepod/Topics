# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:42:09 2021

@author: Camilo
"""
import numpy as np
import matplotlib.pyplot as plt

def table(Cph, Cpc, Th, Tc, ddT):
    Th = np.array(Th)
    Tc = np.array(Tc)
    Cpc = np.array(Cpc)
    
    #Corrección Cpc
    Cpc = -Cpc
    
    #Correción de las temperaturas {Th - dT/2}  y  {Tc + dT/2}
    Thw = Th - int(ddT/2)
    Tcw = Tc + int(ddT/2)
    
    #Matriz de Temperaturas globales
    T = []
    T = np.append(T,(Thw,Tcw))
    T = np.sort(list(set(T)))
   
    #Matriz de Cp globales
    Cp = []
    Cp = np.append(Cp, (Cph,Cpc))

    #Matriz Temperaturas locales
    Ti = Thw
    Ti = np.append(Ti, Tcw,axis=0)  
    
    #Diferencia de Temperaturas
    dT = []
    for i in range(len(T)-1):
        dT = np.append(dT, T[i+1]-T[i])
    dT = np.delete(dT,np.where(dT == 0))
    
    #Cps Acumulados
    Cp_acu = np.array([])

    result = np.where(Ti == T[0])
    if len(result[0]) == 1:   
        Cp_acu = np.append(Cp_acu, Cp[int(result[0])])   
        h = 1
    else:
        h = 0
    alpha = 0
    for i in range(h, len(T)):
        Cpi = 0
        for n in range(len(Ti)):
            if T[i] == Ti[n][0] or (T[i] > Ti[n][0] and T[i] < Ti[n][1]): 
                Cpi = Cpi + Cp[n]
        
        if Cpi != 0 and alpha != Cpi: 
            Cp_acu = np.append(Cp_acu,Cpi)
            alpha = Cpi
    
    #Calores
    Q = []
    for i in range(len(dT)):
        Q = np.append(Q, Cp_acu[i]*dT[i])
    
    #Invertir orden Q
    Qi = Q[::-1]        
    print(Qi)
        
    #Cascada
    Cas = 0
    Cass = [0]
    for i in Qi:
        Cas = i + Cas
        Cass = np.append(Cass,Cas)
    
    aju = []
    min = np.min(Cass)
    for i in Cass:
        aju = np.append(aju,i - min)
    aju = aju[::-1]
    
    leyenda = ['Cp 1 = 20','Cp 2 = 40','Cp 3 = 80','Cp 4 = 36']
    problem_table = plt.figure()
    for i in range(len(Thw)):
        plt.plot([i+1,i+1],Thw[i],'r',label=leyenda[i])
        a = i+1
    for i in range(len(Tcw)):
        plt.plot([a+i+1,a+i+1],Tcw[i],'b',label=leyenda[i+a])
    for i in range(len(Ti)):
        for j in range(2):
           plt.plot([0,len(Ti)+1],[Ti[i][j],Ti[i][j]],':k')
    plt.title('Gráfica Temperatura Corregidas')
    plt.xticks(range(0,6,1))
    plt.xlim(0,5)
    plt.legend()
    plt.show()   
    
    fig = plt.figure()
    plt.plot(aju,T)
    plt.title("Grand Composite Curve \n")
    plt.xlabel('Duty [kW]')
    plt.ylabel('Temperature [°C]')
    plt.xlim(0)
    plt.plot()


    
    


    
    

    
    
