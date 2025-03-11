from PIL import Image, ImageEnhance
from random import randint

def assombrissement(chemin_image):
    """fontion assombrissement qui prend en argument une
    image couleur et renvoie l’image assombrie obtenue en
    divisant par 2 la valeur des 3 composantes des pixels.
    """
    image = Image.open(chemin_image)
    image = image.convert("RGB")
    pixel = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixel[i, j]
            pixel[i, j] = (r // 2, g // 2, b // 2) # On divise par deux la valeur de la couleur de chaque pixel

    return(image)

def noir_et_blanc(chemin_image, seuil):
    image = Image.open(chemin_image).convert("RGB")
    largeur, hauteur = image.size
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            moyenne = (r + g + b) // 3
            couleur = 255 if moyenne > seuil else 0
            image.putpixel((x, y), (couleur, couleur, couleur))

    return image

def jeu_video(chemin_image, n):
    image = Image.open(chemin_image).convert("RGB")
    pixels = image.load()
    step = 256 // n
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r // step * step, g // step * step, b // step * step)

    return image

def vintage(chemin_image, intensite):
    """Applique un filtre type caméra jetable avec une intensité 1-10."""
    intensite = max(1, min(10, intensite))  # Verifier que ca ne depasse pas 10
    facteur_intensite = intensite / 10  # Convertir en facteur 0.1-1.0 pour faciliter le calcul
    image = Image.open(chemin_image).convert("RGB")
    filtre_jaune = Image.new("RGB", image.size, (255, 230, 150)) #Teinte jaunatre
    image = Image.blend(image, filtre_jaune, facteur_intensite * 0.3) #On melange les deux images pour appliquer sur l'image de depart
    px = image.load()
    width, height = image.size
    for i in range(int(width * height * facteur_intensite * 0.05)):  # On cree un bruit en modifiant la couleur de facon aleatoire
        x, y = randint(0, width - 1), randint(0, height - 1)
        r, g, b = px[x, y]
        bruit = randint(-30, 30)  # On varie la couleur de facon aleatoire
        px[x, y] = (max(0, min(255, r + bruit)),
                        max(0, min(255, g + bruit)),
                        max(0, min(255, b + bruit)))

    return image

i=0
if __name__ == "__main__":
     while True:
        print("Choisissez un effet :")
        print("1 - Noir et blanc")
        print("2 - Effet jeu vidéo")
        print("3 - Effet Vintage")
        print("4 - Sortir")
        choix = input("Entrez le chiffre : ")

        if choix == "4":
            break
        chemin_image = input("Entrez le chemin de l'image : ")
        if choix == "1":
            seuil = int(input("Entrez le seuil (0-255) : "))
            image_modifiee = noir_et_blanc(chemin_image, seuil)
        elif choix == "2":
            n = int(input("Entrez le nombre de niveaux (1-10) : "))
            if n > 10:
                n = int(input("Nombre trop grand veuillez reselectionner (1-10):"))
                image_modifiee = jeu_video(chemin_image, n)
            else:
                image_modifiee = jeu_video(chemin_image, n)
        elif choix == "3":
            n = int(input("Entrez le nombre de niveaux (1-10) : "))
            image_modifiee = vintage(chemin_image, n)
        else:
            print("Choix invalide.")
        image_modifiee.show()
        if "image_modifiee" +str(i) +".jpg": # Si l'image avec ce nom existe deja on rajoute un chiffre au nom
            i += 1
            image_modifiee.save("image_modifiee" + str(i) + ".jpg")
        else:
            image_modifiee.save("image_modifiee.jpg")
