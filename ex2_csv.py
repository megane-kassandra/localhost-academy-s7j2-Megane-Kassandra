import csv

taches = [
{ " titre " : " Reviser Python " , " faite " : False } ,
{ " titre " : " Lire le cours " , " faite " : True } ,
{ " titre " : " Acheter du pain , du lait " , " faite " : False }
]

def exporter_csv(taches, chemin="taches.csv"):
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[" titre ", " faite "])
        writer.writeheader()
        for tache in taches:
            writer.writerow(tache)


def importer_csv(chemin="taches.csv"):
    taches_importees = []
    with open(chemin, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[" faite "] == "True":
                row[" faite "] = True
            else:
                row[" faite "] = False
            taches_importees.append(row)
    return taches_importees

exporter_csv(taches)
taches_relues = importer_csv("taches.csv")
print(taches_relues)
print(type(taches_relues[0][" faite "]))  # Affiche le titre de la première tâche
    