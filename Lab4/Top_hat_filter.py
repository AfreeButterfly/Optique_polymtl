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

    # Calculer la taille du noyau en fonction de la fréquence de coupure
    kernel_size = int(1 / (cutoff_frequency * (1 / min(image.shape))))

    # Assurez-vous que la taille du noyau est impaire (requis pour le noyau morphologique)
    if kernel_size % 2 == 0:
        kernel_size += 1

    # Créer le noyau
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Opérations de filtrage
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    top_hat = cv2.subtract(image, opening)

    # Afficher l'image originale et l'image filtrée
    cv2.imshow('Image originale', image)
    cv2.imshow('Résultat du filtre passe-haut top-hat', top_hat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Enregistrer l'image filtrée
    output_path = r'Images\Top_Hat_filtered_marvin.png'
    cv2.imwrite(output_path, top_hat)
    print(f"L'image filtrée a été enregistrée sous {output_path}")
