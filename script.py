import os
import sys
import json
import requests
import time
import random


def download_image(url, code):
    """Télécharge une image depuis une URL et la nomme avec le code donné."""

    # Vérifie si le dossier existe déjà
    directory = os.path.join("./cards", code.split("/")[0])
    if not os.path.exists(directory):
        # Crée le dossier si nécessaire
        os.mkdir(directory)

    # Nomme l'image avec le code
    image_file = os.path.join("./cards", f"{code}.jpg")

    # Télécharge l'image
    if os.path.isfile(image_file):
        print('file_exist:', image_file)
        return True

    response = requests.get(url)
    with open(image_file, "wb") as f:
        f.write(response.content)

    # Ajoute un délai aléatoire
    time.sleep(random.randint(1, 3))

def main():
    """Programme principal."""

    # Vérifie si le dossier `cards` existe
    if not os.path.exists("./cards"):
        # Crée le dossier `cards`
        os.mkdir("./cards")

    # Liste les fichiers JSON du dossier donné
    dir_path = "./DB"
    files = os.listdir(dir_path)

    # Parcours les fichiers JSON
    for file in files:
        if file.endswith(".json"):
            # Ouvre le fichier JSON
            with open(os.path.join(dir_path, file), "r", encoding="utf-8") as f:
                # Charge le contenu du fichier JSON
                try:
                    data = json.load(f)
                except Exception as e:
                    print('load_error:', os.path.join(dir_path, file))
                    print(e)
                    sys.exit(0)

            # Parcours les éléments du dictionnaire
            for item in data:
                # Télécharge l'image
                print(' *', item["code"], item["image"])
                download_image(item["image"], item["code"])

if __name__ == "__main__":
    main()
