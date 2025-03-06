from PIL import Image, ImageEnhance

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

def effet_jeu_video(chemin_image, n):
    image = Image.open(chemin_image).convert("RGB")
    pixels = image.load()
    step = 256 // n
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r // step * step, g // step * step, b // step * step)

    return image

def apply_vintage_effect(image):

    image = Image.open(chemin_image)
    image = image.convert("RGB")

    couleur = ImageEnhance.Color(image)
    image = couleur.enhance(0.5)
    lumiere = ImageEnhance.Brightness(image)
    image = lumiere.enhance(0.9)
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
            n = int(input("Entrez le nombre de niveaux (ex: 8) : "))
            image_modifiee = effet_jeu_video(chemin_image, n)
        elif choix == "3":
            image_modifiee = apply_vintage_effect(chemin_image)
        else:
            print("Choix invalide.")
        image_modifiee.show()
        if "image_modifiee" +str(i) +".jpg":
            i += 1
            image_modifiee.save("image_modifiee" + str(i) + ".jpg")
        else:
            image_modifiee.save("image_modifiee.jpg")
