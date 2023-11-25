import os
from PIL import Image


def rename_files(path):
    """
    Renommer tous les fichiers JPG dans le chemin spécifié et ses sous-dossiers
    au format correct (JPG, PNG ou GIF).

    Args:
        path: Le chemin vers le répertoire contenant les fichiers JPG.
    """
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".jpg"):
                # Extrait le nom de fichier et l'extension
                filename, extension = os.path.splitext(file)

                # Ouvre le fichier image et détermine son format réel
                image = Image.open(os.path.join(root, file))
                true_format = image.format

                # Remplace "JPEG" par "JPG" et convertit en minuscules
                true_format = true_format.replace("JPEG", "JPG").lower()

                # Construit le nouveau nom de fichier avec le format correct
                new_filename = filename + "." + true_format

                # Renommer le fichier
                print(
                    os.path.join(root, file),
                    os.path.join(root, new_filename))
                os.rename(
                    os.path.join(root, file),
                    os.path.join(root, new_filename))


if __name__ == "__main__":
    path = "./cards"
    rename_files(path)
