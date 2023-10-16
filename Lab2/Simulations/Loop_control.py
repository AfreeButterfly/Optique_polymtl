import sympy
import numpy as np
from sympy import Matrix
from matrix import *

f_list=[25,35,50,100,150] #mm
d_list=[50/1000 ,75/1000 ,100/1000 ,150/1000 ]   #mm
# d=75/1000                      #mm

variables_list=["d","f","L"]
phi1 = 25.4  # (mm)
phi2 = 25.4  # (mm)

for vari in variables_list:
    print(vari)
    if vari=="d":
        plt.close()
        f_list=[25,35,50,100,150] #mm
        d_list=np.linspace(0,150,200)#micrometre
        for f in f_list:
            print(f)
            L=f
            y_plot=[]
            for d in d_list:
                y_plot.append(solveSystem(f, f, L, d/1000, phi1, phi2))
            plt.plot(d_list,y_plot,label=f"f={f} mm")
        plt.legend()
        plt.xlabel("d $\\mu m$")
        plt.ylabel("$\\delta_z$ (mm)")
        plt.savefig("Fig_d")
    elif vari=="f":
        plt.close()
        f_list=np.linspace(10,150,200)   #mm
        d_list=[50 ,75 ,100 ,150]  #micrometre
        for d in d_list:
            print(d)
            y_plot=[]
            for f in f_list:
                L=f
                y_plot.append(solveSystem(f, f, L, d/1000, phi1, phi2))
            plt.plot(f_list,y_plot,label=f"d={d} $\\mu m$ ")
        plt.legend()
        plt.xlabel("$f_1=f_2=f$ (mm)")
        plt.ylabel("$\\delta_z$ (mm)")
        plt.savefig("Fig_f")
    elif vari=="L":
        plt.close()
        d=75
        f_list=[25,35,50,100,150]
        L_list=np.linspace(0,1000,200)
        for f in f_list:
            print(f)
            y_plot=[]
            for L in L_list:
                y_plot.append(solveSystem(f, f, L, d/1000, phi1, phi2))
            plt.plot(L_list,y_plot,label=f"f={f} mm")
        plt.legend()
        plt.xlabel("L (mm) ")
        plt.ylabel("$\\delta_z$  (mm)")
        plt.savefig("Fig_L")



