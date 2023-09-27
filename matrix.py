######################### Code pour les matrices ############################
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

f1 = 35 #(mm)
f2 = 32 #(mm)
phi1 = 25.4 #(mm) 
phi2 = 25.4 #(mm)
L = 0
d = 75 #(mm)


def calculateInverse(f1, f2, L):
    M1 = sp.Matrix([[1, f1],[0, 1]])
    M2 = sp.Matrix([[1, 0],[-1/f1, 1]])
    M3 = sp.Matrix([[1, 0],[L, 1]])
    M4 = sp.Matrix([[1, 0],[-1/f2, 1]])
    M5 = sp.Matrix([[1, 0],[f2, 1]])
    M_tot=sp.MatMul(M5,M4,M3,M2,M1)
    M_tot_inverse = M_tot.inv()
    return M_tot_inverse



