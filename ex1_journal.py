from pathlib import Path

FICHIER = Path("journal.txt")

def charger():
    if not FICHIER.exists():
        taches = []
        for i in range(3):
            title = input(f"Entrez le titre de la {i+1}ème tache : ")
            taches.append(title)
        with FICHIER.open("w", encoding="utf-8") as f: # permet d'ouvrir le fichier en mode écriture
            for tache in taches:
                f.write(tache + "\n")
        with FICHIER.open("r", encoding="utf-8") as f: # permet d'ouvrir le fichier en mode lecture
            contenu = f.read()
            for ligne in contenu.splitlines():
                print(ligne, end="" "\n")
    else:
        title = input("Entrez le titre de la tache à ajouter : ")
        with FICHIER.open("a", encoding="utf-8") as f: # permet d'ouvrir le fichier en mode ajout
            f.write(title + "\n")

charger()