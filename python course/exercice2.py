def saisir_cote_positif(numero_cote):
    while True:
        try:
            entry=input(f"Entrez une valeur positive non nulle pour le côté {numero_cote} : ").replace(',','.')
            valeur = float(entry)
            if valeur <=0:
                print("La valeur doit être strictement supérieure à 0")  
            else:
                return valeur
        except ValueError:
            print("Saisie invalide , veuillez entrer un nombre valide (ex: 4 ou 15)")

while True:
    try:
        quadri=int(input("entre 1 pour un carré, 2 pour un rectangle "))
        if quadri != 2 or quadri !=1:
            print("il y a uniquement deux choix possible 1 et 2")
        else :
            break
    except ValueError:
        print("saisie invalide , veuillez entrer 1 ou 2")


if quadri==1:
    # carré
    print("un carré est sensé avoir les 4 cotés positifs\n en entrez la valuer du premier coté uniquement ")
    cotes = saisir_cote_positif(1)


    def aire_carre(c):
        return c * c


    def perimetre_carre(c):
        return 4 * c


    print(f"l'aire du carré entré est {aire_carre(cotes)}")
    print(f"le perimetre du carré entré est : ;{perimetre_carre(cotes)}")
    print()
elif quadri==2:
    # rectangle

    print("entrer la longueur et la largeur du rectangle")
    cote_un = saisir_cote_positif(1)
    cote_deux = saisir_cote_positif(2)


    def peri_rec(l, la):
        return 2 * (l + la)


    def aire_rec(l, la):
        return l * la


    print(f"l'aire du rectangle est : {aire_rec(cote_un, cote_deux)}")
    print(f"le périmetre du rectangle est {peri_rec(cote_un, cote_deux)}")

#losange

