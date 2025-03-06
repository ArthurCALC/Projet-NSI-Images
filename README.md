
# Fonctions de modification d'images avec la bibliotheque PILLOW

Objectifs :
Appliquer les bases de programmation Python
Appliquer plusieurs algorithmes pour transformer des images numériques
Utiliser une bibliothèque et sa documentation

1/ Introduction et installation :
Une image est constituée de points appelés pixels. Chaque pixel a une couleur représentée par un triplet (r, v, b) correspondant aux composantes rouge, verte et bleue. Chaque composante est un nombre codé sur 1 octet (entre 0 et 255 donc).
Pour manipuler les images numériques, vous allez utiliser la bibliothèque Python de traitement d’images PIL.

Pour cela,ouvrir un terminal et entrez la commande :
pip3 install PILLOW (ou pip install PILLOW)

Vous pourrez maintenant, en utilisant les images données dans le dossier partagé, exécuter le fichier test_PIL.py qui vous aidera à utiliser la bibliothèque PIL.
Vous pouvez utiliser les images disponibles dans le dossier partagé ou d’autres images de votre choix.

2/ Votre mission
Dans un nouveau fichier que vous nommerez  projet_images.py, vous écrirez les fonctions demandées ci-dessous :

assombrissement(image)
noir_et_blanc(image, seuil)
flou(image)
effet_jeu_video(image, nb_valeurs)
et une fonction libre (soyez créatifs !).

Une fois les fonctions écrites, vous écrirez une fonction main() dans laquelle vous proposerez à l’utilisateur l’une ou l’autre des 5 transformations et afficherez dans la même image l’image initiale et l’image transformée.

Description des fonctions :

la fonction assombrissement prend en argument une image couleur et renvoie l’image assombrie obtenue en divisant par 2 la valeur des 3 composantes des pixels.

la fonction noir_et_blanc prend en argument une image couleur et un seuil (entier). Pour chaque pixel, elle calcule la moyenne des 3 composantes rouge, verte et bleue et si la valeur est supérieure au seuil donné, affecte la couleur blanche au pixel de l’image résultat, la couleur noire sinon. L’image en noir et blanc est ensuite renvoyée.

la fonction flou prend en argument une image et renvoie l’image floutée obtenue en réalisant pour chaque pixel la moyenne de la valeur du pixel et de celles des 8 pixels voisins.

la fonction effet_jeu_video limite à n le nombre de valeurs pour chaque canal de couleur, de façon à donner un effet “vieux jeu vidéo”. Par exemple, pour n = 8, si la valeur de la composante rouge d’un pixel est entre 0 et 31, on la remplace par 0, entre 32 et 63, on la remplace par 32 etc.


## Authors

- [Arthur Cantat](https://github.com/ArthurCALC)
- [Mickael Naouri](https://github.com/MickaelNaouri)
- [Solal Chasques](https://github.com/)
