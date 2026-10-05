from pathlib import Path
import json

def charger_taches(chemin):
    if not Path(chemin).exists():
        return []
    else:
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                donnees = json.load(f)
        except json.JSONDecodeError:
            print("Le fichier de tâches est invalide")
            raise SystemExit
        else:
            if isinstance(donnees, list):
                return donnees
            else:
                print("Le fichier doit contenir uneliste")
                raise SystemExit
            
            
def sauvegarder_taches(taches, chemin):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(taches, f, ensure_ascii=False, indent=4)


charger_taches("taches.json")  # Charger les tâches existantes au démarrage

while True:
    print("\n=== Menu de gestion des tâches ====\n")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")
    choix = input("Choisissez une option : ")
    
    if choix == "1":
        print("\n++++ Ajouter une tâche ++++\n")
        nombre_taches = int(input("Combien de tâches voulez-vous ajouter ? "))
        for i in range(nombre_taches):
            titre = input(f"Entrez le titre de la tâche {i+1} : ")
            taches = charger_taches("taches.json")
            taches.append(titre)
            sauvegarder_taches(taches, "taches.json")
        print(f"Tâche \"{titre}\" ajoutée avec succès.")
    
    elif choix == "2":
        print("\n++++ Liste des tâches ++++\n")
        taches = charger_taches("taches.json")
        for i, tache in enumerate(taches):
            print(f"{i+1}. {tache}")   
    elif choix == "3":
        print("\n++++ Supprimer une tâche ++++\n")
        
        numero = int(input("Entrez le numéro de la tâche à supprimer : "))
        if numero in range(len(charger_taches("taches.json"))):
            taches = charger_taches("taches.json")
            taches.pop(numero)
            sauvegarder_taches(taches, "taches.json")
            print(f"Tâche \"{taches[numero - 1]}\" supprimée avec succès.")
        else:
            print("Numéro de tâche invalide.")    
            
    elif choix == "4":
        break
    else:
        print("Option invalide. Veuillez réessayer.\n")
        
        
#si au lancement suivant on ajoute une tache a la liste python et oublie d'appeler la fonction sauvegarde 
# la tache ne sera pas sauvegardée dans le fichier json. 
#et sera perdu si on quitte le programme.