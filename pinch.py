# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_pinch(Cp,T):
  dT = []
  for i in range(len(T)):
    dT.append(T[i][1]-T[i][0])
  Q = []
  for i in range(len(T)):
    Q.append(Cp[i]*dT[i])
  Q_acc = [0]
  for i in range(len(T)):
    Q_acc.append(Q_acc[i]+Q[i])

  plt.figure()
  plt.title("Hot Steam")
  plt.xlabel("Q [kW]")
  plt.ylabel("T [°C]")
  for i in range(2):
    plt.plot([Q_acc[i],Q_acc[i+1]],T[i], 'r')
    plt.plot([0,Q_acc[2]],[T[i],T[i]],'--k')
  plt.show()

  plt.figure()
  plt.title("Cold Steam Single")
  plt.xlabel("Q [kW]")
  plt.ylabel("T [°C]")
  for i in range(2,4):
    plt.plot([Q_acc[i],Q_acc[i+1]],T[i], 'b')
    plt.plot([Q_acc[2],Q_acc[4]],[T[i],T[i]],'--k')
  plt.show()

  Th =[
      [T[0][0],T[1][0]],
      [T[1][0],T[0][1]],
      [T[0][1],T[1][1]]]
  Qhc = [
      Cp[0] * (Th[0][1]-Th[0][0]),
      (Cp[0] + Cp[1]) * (Th[1][1]-Th[1][0]),
      Cp[1] * (Th[2][1]-Th[2][0])]

  Qhc_acc = [0]
  for i in range(3):
    Qhc_acc.append(Qhc_acc[i]+Qhc[i])

  plt.figure()
  plt.title("Hot Steam Comp")
  plt.xlabel("Q [kW]")
  plt.ylabel("T [°C]")
  for i in range(3):
    plt.plot([Qhc_acc[i],Qhc_acc[i+1]],Th[i], 'r')
  plt.show()

  Tc = [
      [T[2][0],T[3][0]],
      [T[3][0],T[2][1]],
      [T[2][1],T[3][1]]]
  Qcc = [
      Cp[2] * (Tc[0][1]-Tc[0][0]),
      (Cp[2] + Cp[3]) * (Tc[1][1]-Tc[1][0]),
      Cp[3] * (Tc[2][1]-Tc[2][0])]
  Qcc_acc = [0]
  for i in range(3):
    Qcc_acc.append(Qcc_acc[i]+Qcc[i])
  plt.figure()
  plt.title("Cold Steam Comp")
  plt.xlabel("Q [kW]")
  plt.ylabel("T [°C]")
  for i in range(3):
    plt.plot([Qcc_acc[i],Qcc_acc[i+1]],Tc[i], 'b')
  plt.show()

  plt.figure()
  plt.title("Steam Comp")
  plt.xlabel("Q [kW]")
  plt.ylabel("T [°C]")
  for i in range(3):
    plt.plot([Qcc_acc[i],Qcc_acc[i+1]],Tc[i], 'b')
    plt.plot([Qhc_acc[i],Qhc_acc[i+1]],Th[i], 'r')
  plt.show()
