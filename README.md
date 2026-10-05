# Commandes pour executer les 3 scripts
python3 ex1_journal.py

python3 ex2_csv.py

python3 ex3_persistance.py

# Tests effectues

## Exercice 1
1. Commencez sans journal.txt, puis lancez le script et saisissez les trois tâches. Le fichier doit
contenir trois lignes.
2. Fermez le programme et relancez-le. Saisissez « Préparer la révision ». Le fichier doit maintenant
contenir quatre lignes.
3. Vérifiez que les trois premières lignes sont toujours présentes et que les accents s’affichent correcte-
ment.

## Exercice2
Appelez exporter_csv(taches, "taches.csv"), puis affectez le résultat de importer_csv("taches.csv")
à une nouvelle variable. Affichez la liste relue. Vérifiez que le troisième titre garde sa virgule et que
type(taches_relues[0]["faite"]) affiche <class ’bool’>.

## Exercice3
1. Sans fichier : commencez sans taches.json. Le programme doit démarrer avec une liste vide.
2. Après un ajout : ajoutez « Réviser Python », puis quittez. Relancez le script et affichez les tâches
: ce titre doit réapparaître.
3. Après une suppression : supprimez ce titre, quittez et relancez. Il ne doit plus apparaître.
4. Avec un fichier invalide : gardez une copie du JSON valide. Retirez un crochet dans le fichier de
test, puis relancez. Le programme doit signaler l’erreur et s’arrêter sans écraser le fichier.
