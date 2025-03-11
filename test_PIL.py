def disposable_camera_filter(chemin_image, intensite):
    """Applique un filtre type caméra jetable avec une intensité 1-10."""
    intensite = max(1, min(10, intensite))  # Verifier que ca ne depasse pas 10
    facteur_intensite = intensite / 10  # Convertir en facteur 0.1-1.0 pour faciliter le calcul
    image = Image.open(chemin_image).convert("RGB")
    filtre_jaune = Image.new("RGB", image.size, (255, 230, 150)) #Teinte jaunatre
    image = Image.blend(image, filtre_jaune, facteur_intensite * 0.3) #On melange les deux images pour appliquer sur l'image de depart
    px = image.load()
    width, height = image.size
    for _ in range(int(width * height * facteur_intensite * 0.05)):  # On cree un bruit en modifiant la couleur de facon aleatoire
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        r, g, b = px[x, y]
        bruit = random.randint(-30, 30)  # On varie la couleur de facon aleatoire
        px[x, y] = (max(0, min(255, r + bruit)),
                        max(0, min(255, g + bruit)),
                        max(0, min(255, b + bruit)))
    return image

filtered = disposable_camera_filter("chien.jpg", 10)
filtered.show()
