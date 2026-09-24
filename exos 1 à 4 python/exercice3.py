print("entrez le prix des articles\n")
#montant valid?
def montant_valid(num):
    while True:
        try:
            entry=input(f"entrez le prix de l'article {num}: ").replace(',','.')
            m=float(entry)
            if m<= 0 :
                print("entrez un motant superieur a zéro \n")
            else:
                return m
        except ValueError:
            print("mauvaise saisie entrez des chiffres \n")
#saisie 
articles=[]
for i in range(1,6):
    article=montant_valid(i)
    print()
    articles.append(article)
print(f"voici les montant entrés : {articles} \n")
#calcules
def montant_ht(montant):
    return round((montant/1.18),2)

tab_ht=[montant_ht(i) for i in articles ]
total_ht=sum(tab_ht)
total_ttc=sum(articles)

print(f"le montant total hors taxes est : {total_ht} Fcfa\n")
print(f"le montant total toute taxes compris est : {total_ttc} Fcfa\n")

if total_ttc>25000:
    print("le total étant superieur a 25000Fcfa vous avez un remise de 20%\n")
    print(f"la somme final à payer est : {total_ttc*0.8} Fcfa")
else :
    print(f"la somme à payer est : {total_ttc} Fcfa")
