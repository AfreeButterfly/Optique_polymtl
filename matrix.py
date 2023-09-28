# ######################### Code pour les matrices ############################
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp




def solveSystem(f1, f2, L, d, phi1, phi2):
    # Définition des matrices du système
    M1 = sp.Matrix([[1, f1], [0, 1]])
    M2 = sp.Matrix([[1, 0], [-1/f1, 1]])
    M3 = sp.Matrix([[1, L], [0, 1]])
    M4 = sp.Matrix([[1, 0], [-1/f2, 1]])
    M5 = sp.Matrix([[1, f2], [0, 1]])
    M_tot = M5 * M4 * M3 * M2 * M1  # Calcul de la matrice totale
    #Calcul du vecteur du rayon 2 final (au sténopé), cette étape pourrait être mise hors de 
    #la fonction pour accélérer le temps de calcul si d et f2 ne varient pas
    r2_f_angle = -np.arctan((phi2 - d/2) / f2)
    r2_f_y = d/2
    print(M_tot) # Imprime la matrice totale pour vérification
    
    r2_i_alpha, r2_i_y = sp.symbols('r2_i_alpha r2_i_y') #Définition des variables à résoudre
    r2_i = sp.Matrix([r2_i_alpha, r2_i_y])
    
    eq = sp.Eq(M_tot * r2_i, sp.Matrix([r2_f_angle, r2_f_y])) #Définition de l'équation à résoudre
    solution = sp.solve(eq, (r2_i_alpha, r2_i_y)) # Solution de l'angle et hauteur du rayon 2 initial
    r2_i_alpha_value = solution[r2_i_alpha] # Extrait l'angle du vecteur solution
    r2_i_y_value = solution[r2_i_y] #Extrait la hauteur du vecteur solution

    #VÉRIFIER LE CALCUL DE DELTAZ (ca speut que j'ai écrit de la merde, mais normalement ca devrait être bon)
    #*** Le calcul de deltaz suppose une résolution symétrique centrée sur le plan focal
    deltaz = abs(2 * r2_i_y_value / math.tan(r2_i_alpha_value)) #Calcul de la résolution avec l'angle et la heuteur
    return deltaz

f1 = 35  # (mm)
f2 = 35  # (mm)
L = 35 # (mm)
d = 0.075  # (mm)
phi1 = 25.4  # (mm)
phi2 = 25.4  # (mm)

print(solveSystem(f1, f2, L, d, phi1, phi2))




