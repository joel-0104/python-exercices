import seance2
cont=True
while cont:
    while True:
	    try:
	          choix=input("faite un choix entre les operation suivantes: \n\n1 somme\n\n2 différence\n\n3 produit\n\n 4 division\n\n5 inverse")
	       if choix not in list(range(1,6)):
	  	        print("enrez une valeur comprise entre 1 et 5(ex:1 ou 2)")
	       else :
    	      	break
    	 except ValueError:
	          	print("Error! entre un CHIFFRE compris entre 1 et 5")
    if choix==1:
       	print("vous avez choisis l'addition")
       	a=int(input("entrer la valeur 1 pour l'addition"))
           b=int(input("entrer la valeur 2 pour l'addition"))
           print(f"la somme de {a} et {b} est{seance2.somme(a,b)}")
    elif choix==4:
    		c=int(input("entrer la valeur 1 pour la division"))
            while True:
               d=int(input("entrer la valeur 2 pour la division"))
               if d==0:
                  print("entrer une valeur differente de zero")
               else:
                    break 
               print(f"le quotient de {c} et {d}  est {seance2.division(c,d)}")     	
    elif choix==5:
    	    while True:
                   e=int(input("entrer la valeur 1 pour l'inverse"))
                   if e==0:
                          print("entrer une valeur differente de zero")
                   else:
                          break
print(f"l'inverse de {e} est {seance2.inv(e)}" )
    elif choix==2:
    	    f=int(input("entrer la valeur 1 pour la soustraction"))
            g=int(input("entrer la valeur 2 pour la soustraction"))
            print(f"la difference entre {f} et {g} est {seance2.soustraction(f,g)}")
    while True:
        choix=input("voulez-vous faire un nouvel essai ? (Entrez oui ou non ): ")
        

        yes=r"^(oui|o)"

        no=r"^(non|n)"

        if re.match(yes,choix,re.I):
            print("vous avez choisis de continuer ")

            break

        elif re.match(no,choix,re.I):

            cont=False

        else:

            print("Erreur ! Entrez oui ou non")