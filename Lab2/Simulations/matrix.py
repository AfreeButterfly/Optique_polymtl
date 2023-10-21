import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

f3 = sp.symbols('f3')
L2 = sp.symbols('L2')
t2 = sp.symbols('t2')
t3 = sp.symbols('t3')
f2 = sp.symbols('f2')
f1 = sp.symbols('f1')

# I define a function for the translation matrix
def Mt(d):
    '''
        Translation ray transfer matrix
    '''
    M = np.array([[1, d],
                  [0, 1]])
    return M

# I define a function for the thin lens matrix
def Ml(f):
    '''
        Thin lens ray transfer matrix
    '''
    M = np.array([[1, 0],
                  [-1/f, 1]])
    return M

# I create a function for the total system matrix M
def M_system(t2, t3, L):
    '''
        Computes the total system transfer matrix
    '''
    M = Ml(f=75)@Mt(d=t2)@Ml(f=-75)@Mt(d=t3)@Ml(f=150)@Mt(d=L-t3-t2)
    return M

L = 200
print(M_system(t2,t3, L))

#x = sp.symbols('x') # symbolize x
t2range = np.linspace(25, 75) # range of values for s
t3_solutions = [] # empty array for solutions

# Iteratively solve the problem
for t2 in t2range:
    Mtot = M_system(t2, t3, L) # compute the system's matrix
    B = Mtot[0, 1] # get B(x) from system's matrix
    t3_sol = sp.solve(B) # Solve B(x) = 0 Carefull, there may be many solutions...
    t3_solutions.append(sp.solve(B)) # add solution to list
    
    
# plot results
plt.figure(dpi=96)
plt.plot(t2range, t3_solutions, '.-')
plt.xlabel('t2 [mm]')
plt.ylabel('t3 [mm]')
plt.show()