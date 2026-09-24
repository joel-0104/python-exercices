import math
#fonction de saisie 
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
            print("Saisie invalide , veuillez entrer un nombre valide (ex: 17.5 ou 12)")
            

            
#verification    
while True:
    side_one = saisir_cote_positif(1)
    side_two = saisir_cote_positif(2)
    side_three = saisir_cote_positif(3)
    if side_one + side_two <= side_three or side_one + side_three <= side_two or side_two + side_three <= side_one:
        print("Ces longueurs ne peuvent pas former un triangle valide")
        print("Veuillez ressaisir les 3 côtés.\n")
    else:
        break
#type du triangle comme j'ai la flemme d'ecrire dans les fonction 
def triangle_type(a,b,c):
    rectangle=a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2
    iso=a==b or b==c or c==a
    if a==b and b==c and c==a:
        return "equilateral"
    elif rectangle and iso:
        return "rectangle isocele"
    elif iso:
        return "isocele"
    elif rectangle:
        return "rectangle"
    else:
        return "quelconque"
print(f"le triangle est : {triangle_type(side_one,side_two,side_three)}")
def perimetre(a,b,c):
    return a+b+c
def aire(a,b,c):
    if triangle_type(a,b,c)=="equilateral":
        return round(((math.sqrt(3))/4)*math.pow(a,2),2)
    elif triangle_type(a,b,c)=="isocele":
        if a == b:
            base, cote = c, a
        elif a == c:
            base, cote = b, a
        else:
            base, cote = a, b
        return round((base / 4) * math.sqrt(4 * (cote**2) - (base**2)),2)
    elif triangle_type(a,b,c)=="rectangle":
        if a ** 2 + b ** 2 == c ** 2:
            return (a*b)/2
        elif b ** 2 + c ** 2 == a ** 2:
            return (b*c)/2
        elif c ** 2 + a ** 2 == b ** 2:
            return (a*c)/2

    else:
        #formule de heron
        aire_tri = 0.25 * math.sqrt((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c))
        return round(aire_tri,2) 
print(f"le perimetre du triangle est est: {perimetre(side_one,side_two,side_three)} cm")
print(f"l'aire du triangle est: {aire(side_two,side_two,side_three)} cm²")

   
     
    
        
          

