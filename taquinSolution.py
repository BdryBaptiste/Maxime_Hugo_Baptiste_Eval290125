import os
from collections import deque

TROU  =  '0'
nbcomb=0
dim = 0

def afficheJeu(jeu) :
	for l in jeu :
		for c in l :
			print(c, end=' ')
		print()
	print()

def initTaquin(nf) :
	f = open(nf,"r")
	lignes = f.readlines()
	jeu, ref = [], []
	global dim 
	dim = len(lignes)//2
	print(dim)
	for l in lignes[:dim] :
		c = l.split()
		jeu.append(c[:])
	for l in lignes[dim:] :
		c = l.split()
		ref.append(c[:])
	return jeu, ref

def chercher(val, ref) :
	for i in range(len(ref)) :
		if val in ref[i] : return i, ref[i].index(val)		

def valJeu( jeu,  ref) :
	sommedist=0
	for i in range(len(jeu)) :
		for j in range(len(jeu[i])) :
			if (jeu[i][j] != ref[i][j]) :
				y, x  = chercher(jeu[i][j], ref)
				sommedist += abs(y-i) + abs(x-j)
	return sommedist

def meilleureConfig(lstJeu, ref) : 
	return lstJeu[0]

def pasDansListe(jeu, lstJeu) :
	for j in lstJeu :
		if valJeu(j[0], jeu) == 0 : return 0
	return 1

def copie_jeu(j) :
	jeu=[]
	for i in range(len(j)) :
		jeu.append(j[i][:])
	return jeu

def jouer(ref, jeu):
    mouvements = [(-1, 0, "Haut"), (1, 0, "Bas"), (0, -1, "Gauche"), (0, 1, "Droite")]
    mouvements_effectues = []

    queue = deque([(jeu, mouvements_effectues)])  # File avec (état du jeu (initialement, premier état), liste des mouvements)
    etats_explores = set()  # États déjà explorés
    
    while queue:
        etat_actuel, chemin = queue.popleft()

        if etat_actuel == ref:
            print(f"Trouvé en {len(chemin)} mouvements ! La solution :")
            for i, direction in enumerate(chemin, 1):
                print(f"{i}. {direction}")
            return

        etats_explores.add(str(etat_actuel))

        y, x = chercher(TROU, etat_actuel)

        for dy, dx, direction in mouvements:
			# Nouvelle coordonnées du trou
            ny, nx = y + dy, x + dx
			# Vérification coordonnées plausibles
            if 0 <= ny < dim and 0 <= nx < dim:
                nouveau_jeu = copie_jeu(etat_actuel)
                nouveau_jeu[y][x], nouveau_jeu[ny][nx] = nouveau_jeu[ny][nx], nouveau_jeu[y][x]

				# Si nouvel état, rajout dans la queue
                if str(nouveau_jeu) not in etats_explores:
                    queue.append((nouveau_jeu, chemin + [direction]))

# jeu, ref = initTaquin("taquin4.txt")
jeu, ref = initTaquin("c:\\Users\\htreg\\Downloads\\taquin4.txt")
afficheJeu(jeu)
afficheJeu(ref)

jouer(ref, jeu)





