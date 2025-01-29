import random

cpt=0
cache_uses = 0

def memoise(f): # fonction qui permet de mémoriser les résultats des appels à la fonction f
    cache = {}
    def wrapper(cible, nombres):
        global cache_uses
        key = (cible, tuple(sorted(nombres)))
        if key in cache:
            cache_uses += 1
            return cache[key]
        result = f(cible, nombres)
        cache[key] = result
        return result
    return wrapper

@memoise
def trouveEnbrpr(cible, nombres) :
    global cpt
    cpt+=1  # compteur d'appels à la fonction
    if len(nombres) == 1 : # si la liste des nombres ne contient qu'un seul élément
        if (cible == nombres[0]) : 
            return (True,str(cible))
        else : 
            return (False, "")
    else :
        if cible in nombres : # si la cible est dans la liste des nombres
            return (True, str(cible))
        else :
            for nbr in nombres :
                nombres_temp = nombres[:] # copie de la liste des nombres
                nombres_temp.remove(nbr) # on enlève nbr de la liste des nombres
                
                (t, ch) = trouveEnbrpr(cible+nbr, nombres_temp)
                if t: return (t, ch + " - " + str(nbr))
                
                if (cible >= nbr) and cible%nbr == 0: 
                    (t, ch) = trouveEnbrpr(cible//nbr, nombres_temp)
                    if t : return (t, "("+ch+") * "+str(nbr))

                if (cible <= nbr) and nbr%cible == 0: 
                    (t, ch) = trouveEnbrpr(nbr//cible, nombres_temp)
                    if t : return (t, str(nbr)+" / ("+ch+") ")

                if (cible >= nbr) : 
                    (t, ch) = trouveEnbrpr(cible-nbr, nombres_temp)
                    if t : return (t, str(nbr)+" + (" + ch+") ")

                (t, ch) = trouveEnbrpr(cible*nbr, nombres_temp)
                if t : return  (t, "("+ch+") / "+str(nbr))

            return(False,"")

NBNOMBRES = 6
nombres=[]
operateurs = ['+', '-', '*', '/']
#operandes=list(range(1,11))+list(range(1,11))+[25,50,75,100] # 1 à 10 en double, 25,50,75,100
cible=799 
nombres = [4, 8, 5, 6, 6, 2]
#for i in range(NBNOMBRES) :
    #nombres.append(operandes[random.randint(0,len(operandes)-1)]) # on tire un nombre au hasard parmit ceunbr possibles
#cible = random.randint(100,999) # détermine la cible

res = trouveEnbrpr (cible, nombres)
print("Nombre cible: ",cible, "\nListe des nombres piochés: ", nombres, "\nSolution trouvé: ", res, "\nNombre d'appel à la fonction: ", cpt, "\nUtilisation du cache: ", cache_uses)
if (res[0]==False) :
    for i in range(cible) :
        print("écart",i)
        res = trouveEnbrpr (cible+i, nombres)
        if (res[0]==True) : 
            print(cible, cible+i, nombres, res, cpt)
            break
        res = trouveEnbrpr (cible-i, nombres)
        if (res[0]==True) : 
            print(cible, cible-i, nombres, res, cpt)
            break

