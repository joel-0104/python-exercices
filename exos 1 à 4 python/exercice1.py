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


   
     
    
        
          

