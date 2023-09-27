######################### Code pour les matrices ############################
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

f1 = 35 #(mm)
f2 = 35 #(mm)
phi1 = 25.4 #(mm) 
phi2 = 25.4 #(mm)
L = 0
d = 0.075 #(mm)


def solveSystem(f1, f2, L, d, phi1, phi2):
    M1 = sp.Matrix([[1, f1],[0, 1]])
    M2 = sp.Matrix([[1, 0],[-1/f1, 1]])
    M3 = sp.Matrix([[1, 0],[L, 1]])
    M4 = sp.Matrix([[1, 0],[-1/f2, 1]])
    M5 = sp.Matrix([[1, 0],[f2, 1]])
    r2_f_angle = -np.arctan((phi2-d/2)/f2)
    r2_f_y = d/2
    M_tot=sp.MatMul(M5,M4,M3,M2,M1)
    print(M_tot)
    alpha, y = sp.symbols('alpha y')    
    r2_f = sp.Matrix([r2_f_angle, r2_f_y])
    r2_i = sp.Matrix([alpha, y])
    eq = sp.Eq(M_tot*r2_i,r2_f)
    solution = sp.solve(eq, (alpha, y))
    # M_tot_inverse = M_tot.inv()
    # solution = sp.MatMul(M_tot_inverse, r2_f)
    return solution

print(solveSystem(f1, f2, L, d, phi1, phi2))



