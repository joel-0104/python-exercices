import exercice1
import exercice2
import re
_continue=True
while _continue:

    while True :
        print("veuillez choisir la figure dont vous voullez calculer l'aire et le périmetre parmis les suivantes:\n1 pour triangle\n2 pour un carré\n3 pour un rectanglen\4 pour un losange ")
        try:
           figure=int(input("entrez le numéro correspondant à votre choix entre 1 et 4 (ex: 1 ou 2):"))
           if  figure not in range(1,5) :
               print("\nentrez un chiffre positif unique entre 1 et 4(ex:1 ou 2)")
           else:
                break
        except ValueError:
            print("Erreur! entrer une CHIFFRE positif compris entre 1 et 4(ex:1 ou 2)\n")
#triangle

    if figure==1:
        print("vous avez choisis un triangle")
        while True:
            side_one = exercice1.saisir_cote_positif(1)
            side_two = exercice1.saisir_cote_positif(2)
            side_three = exercice1.saisir_cote_positif(3)
            if side_one + side_two <= side_three or side_one + side_three <= side_two or side_two + side_three <= side_one:
                print("Ces longueurs ne peuvent pas former un triangle valide")
                print("Veuillez ressaisir les 3 côtés.\n")
            else:
                break
        print(f"le triangle est : {exercice1.triangle_type(side_one,side_two,side_three)}")
        print(f"le perimetre du triangle est est: {exercice1.perimetre(side_one,side_two,side_three)} cm")
        print(f"l'aire du triangle est: {exercice1.aire(side_two,side_two,side_three)} cm²")
    elif figure==2:
        print("vous avez choisis un carré")
        print("un carré est sensé avoir les 4 cotés positifs\nentrez la valuer du premier coté uniquement ")
        cotes = exercice1.saisir_cote_positif(1)
        print(f"l'aire du carré entré est {exercice2.aire_carre(cotes)}")
        print(f"le perimetre du carré entré est : ;{exercice2.perimetre_carre(cotes)}")
        print()
    elif figure==3:
        print("vous avez choisis un rectangle")
        print("entrer la longueur et la largeur du rectangle")
        cote_un = exercice1.saisir_cote_positif(1)
        cote_deux = exercice1.saisir_cote_positif(2)
        print(f"l'aire du rectangle est : {exercice2.aire_rec(cote_un, cote_deux)}")
        print(f"le périmetre du rectangle est {exercice2.peri_rec(cote_un, cote_deux)}")
    elif figure==4:
        print("vous avez choisis un losange")
    while True:
        choix=input("voulez-vous faire un nouvel essai ? (Entrez oui ou non ): ")
        
        yes=r"^(oui|o)"
        no=r"^(non|n)"
        if re.match(yes,choix,re.I):
            print("vous avez choisis de continuer ")
            break
        elif re.match(no,choix,re.I):
            _continue=False
        else:
            print("Erreur ! Entrez oui ou non")

    
        


    
        
       



