def saisie(subject):
    while True:
        try:
            entry=input(f"entrer le moyenne correspondant à la matiere suivante : {subject} : ").replace(",",".")
            mean=float(entry)
            if mean< 0 or mean>20 :
                print("La moyenne doit être comprise entre 0 et 20 inclus.")
            else:
                return mean
        except ValueError:
            print("Saisie invalide , veuillez entrer un nombre valide (ex: 12.5 ou 15)")
math_mean=saisie("Mathematiques")*4
pc_mean=saisie("Physique")*3
fr_mean=saisie("Francais")*2
ch_mean=saisie("Chinois")*3
ru_mean=saisie("Russe")*5

#bilans
sc_bilan_mean=(math_mean+pc_mean)/7
sc_bilan_mean=round(sc_bilan_mean,2)
lit_bilan_mean=(fr_mean+ch_mean+ru_mean)/10
lit_bilan_mean=round(lit_bilan_mean,2)
print(f"la moyenne du bilan scientifique est : {sc_bilan_mean}\nla moyenne du bilan litteraire est : {lit_bilan_mean}")
#moyenne generale
total_points = math_mean + pc_mean + fr_mean + ch_mean + ru_mean
MG = round(total_points / 17 , 2)
print(f"la moyenne general est : {MG}")
#interpretation
if MG<10:
    print("cet etudiant est ne peut etre classé")
elif sc_bilan_mean>lit_bilan_mean:
    print("cet etudiant est plus scientifique que litteaire")
elif sc_bilan_mean<lit_bilan_mean:
    print("cet etudiant est plus litteaire que scientifique ")
elif sc_bilan_mean==lit_bilan_mean:
    print("cet etudiant est polyvalent")

