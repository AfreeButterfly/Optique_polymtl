import matplotlib.pyplot as plt
import numpy as np

# Exemple de données pour x et y
angles = [[0,0],[5,10],[10,20],[15,30],[20,40],[25,50],[30,60],[40,80],[50,100],[60,120],[65,130],[70,140],[75,150],[80,160],[85,170],[90,180],[95,190],[100,200],[105,210],[110,220],[115,230]]
puissance = [0.191,0.187,0.177,0.163,0.145,0.125,0.103,0.062,0.037,0.011,0.006,0.003,0.0012,0.0007,0.0006,0.0006,0.0006,0.0008,0.0016,0.0037,0.0075]
x = [(angle[1]-angle[0]) for angle in angles]
incertitude_y = [0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.00005,0.00005,0.00005,0.00005,0.00005,0.00005,0.00005]

## Coordonnées du point que vous voulez ajouter
#nouveau_x = 2.5
#nouveau_y = 60.0
#
## Calcul de la fonction y(x) - dans cet exemple, on élève chaque élément de x au carré
#y_calculé = [4.186 * y[i] / x[i] for i in range(12, len(x))]
#x_square = [x[i] ** 2 for i in range(12, len(x))]

# Tracer les points
plt.errorbar( x, puissance, xerr = 1, yerr=incertitude_y, ecolor='blue' , label='Puissance mesurée et erreur sur les mesures', color='red', markersize=5, capsize=2)



### Tracer le nouveau point
##plt.scatter(nouveau_x ** 2, nouveau_y, label='Nouveau Point', color='green', marker='s')
#
###cRégression linéaire pour obtenir une approximation linéaire avec NumPy
##A = np.vstack([angle, np.ones(len(angle))]).T
##m, c = np.linalg.lstsq(A, puissance, rcond=None)[0]
##
#### Créer l'approximation linéaire
##y_approx_linéaire = m * np.array(angle) + c
###
### Tracer la fonction y(x)
##plt.plot(angle, y_approx_linéaire, label=f'Approximation linéaire: y = {m:.4f} * x^2 + {c:.2f}', color='blue')

## Ajouter des titres et une légende
plt.xlabel('Écart entre le polarisateur 1, 2 et 3 (degrés)')
plt.ylabel('Puissance (mW)')
plt.legend()

# Afficher le graphique
plt.show()
