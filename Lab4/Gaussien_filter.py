import cv2
import numpy as np

# Charger l'image
image_path = r'Images\marvin_clean.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Vérifier si l'image est chargée avec succès
if image is None:
    print("Erreur : Impossible de charger l'image.")
else:
    # Définir la fréquence de coupure en pixels^-1
    cutoff_frequency = 50

    # Calculer l'écart type pour le filtre gaussien
    sigma = 1 / (2 * np.pi * cutoff_frequency)

    # Appliquer le filtre gaussien
    gaussian_filtered = cv2.GaussianBlur(image, (0, 0), sigma)

    # Afficher l'image originale et l'image filtrée
    cv2.imshow('Image originale', image)
    cv2.imshow('Résultat du filtre gaussien', gaussian_filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Enregistrer l'image filtrée
    output_path = r'Images\Gaussian_filtered_marvin.png'
    cv2.imwrite(output_path, gaussian_filtered)
    print(f"L'image filtrée a été enregistrée sous {output_path}")
