import seance2
a=int(input("entrer la valeur 1 pour l'addition"))
b=int(input("entrer la valeur 2 pour l'addition"))
print(f"la somme de {a} et {b} est{seance2.somme(a,b)}")
c=int(input("entrer la valeur 1 pour la division"))
while True:
    d=int(input("entrer la valeur 2 pour la division"))
    if d==0:
       print("entrer une valeur differente de zero")
    else:
         break
print(f"le quotient de {c} et {d}  est {seance2.division(c,d)}")
while True:
    e=int(input("entrer la valeur 1 pour l'inverse"))
    if e==0:
       print("entrer une valeur differente de zero")
    else:
         break
print(f"l'inverse de {e} est {seance2.inv(e)}")
f=int(input("entrer la valeur 1 pour la soustraction"))
g=int(input("entrer la valeur 2 pour la soustraction"))
print(f"la difference entre {f} et {g} est {seance2.soustraction(f,g)}")