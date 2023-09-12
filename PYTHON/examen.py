
def echange (liste,x,y):
    liste[x],liste[y]=liste[y],liste[x]
    return echange
def ajouter(liste, nom, i):
    if i >= 0 and i <= len(liste):
        liste.insert(i, nom)
    else:
        print("L'indice i n'est pas valide pour cette liste.")


ma_liste = ["Alice", "Bob", "Charlie"]
ma2_liste =["eliezer","mununga","kayinda"]
liste_3= ma_liste+ma2_liste

ajouter(liste_3, "David", 1)
echange (liste_3, 1,3)
print(liste_3)


