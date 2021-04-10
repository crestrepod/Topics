import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def fun(Cph,Cpc,Th,Tc):
    Cph = np.array(Cph)
    Cpc = np.array(Cpc)
    Th  = np.array(Th)
    Tc  = np.array(Tc)
	
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

    Qc = np.array([0])
    for i in range(len(Tc)):
        Qc = np.append(Qc, Cpc[i]*dTc[i])

    Qh_acc = np.array([0])
    for i in range(len(Qh)):
        Qh_acc = np.append(Qh_acc, Qh_acc[i]+Qh[i])

    Qc_acc = np.array([])
    for i in range(len(Qc)):
        Qc_acc = np.append(Qc_acc, Qc_acc[i]+Qc[i])
		
		
    hot = pd.DataFrame({'T in': Th[:,1],
                    'T out':Th[:,0],
                    'Cp':   Cph,
                    'Q':Qh,
                    'Q acc':Qh_acc[1:]
                    })
  
    print(hot)
    cold = pd.DataFrame({'T in': Tc[:,1],
                    'T out':Tc[:,0],
                    'Cp':   Cpc,
                    'Q':Qc,
                    'Q acc':Qc_acc[1:]
                    })
    print(cold)
        
		return(Qh, Qc, Qh_acc, Qc_acc)

	
def plot():
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
