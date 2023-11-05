import matplotlib.pyplot as plt
import numpy as np

# Exemple de données pour x et y
angle = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115]
puissance = [0.295,0.292,0.284,0.272,0.257,0.238,0.217,0.193,0.170,0.144,0.119,0.093,0.071,0.050,0.032,0.018,0.008,0.002,0.001,0.004,0.011,0.022,0.037,0.056]


## Coordonnées du point que vous voulez ajouter
#nouveau_x = 2.5
#nouveau_y = 60.0
#
## Calcul de la fonction y(x) - dans cet exemple, on élève chaque élément de x au carré
#y_calculé = [4.186 * y[i] / x[i] for i in range(12, len(x))]
#x_square = [x[i] ** 2 for i in range(12, len(x))]

# Tracer les points
plt.errorbar(angle, puissance, xerr = 0.5, yerr=0.0005, ecolor='blue' , label='Puissance mesurée et erreur sur les mesures', color='red', markersize=5, capsize=2)

## Tracer le nouveau point
#plt.scatter(nouveau_x ** 2, nouveau_y, label='Nouveau Point', color='green', marker='s')

##cRégression linéaire pour obtenir une approximation linéaire avec NumPy
#A = np.vstack([angle, np.ones(len(angle))]).T
#m, c = np.linalg.lstsq(A, puissance, rcond=None)[0]
#
### Créer l'approximation linéaire
#y_approx_linéaire = m * np.array(angle) + c
##
## Tracer la fonction y(x)
#plt.plot(angle, y_approx_linéaire, label=f'Approximation linéaire: y = {m:.4f} * x^2 + {c:.2f}', color='blue')

## Ajouter des titres et une légende
plt.xlabel('Angle (degrés)')
plt.ylabel('Puissance (mW)')
plt.legend()

# Afficher le graphique
plt.show()
