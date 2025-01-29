import math

def pb1():
    def test_survie(m, s):
        SEUIL_FATAL = s  # Seuil de mortalité
        return m <= SEUIL_FATAL  # True si survit, False sinon

    def recherche_dichotomique(n):
        gauche, droite = 1, n
        repas_manges = 0
        eleves_morts = 0

        while gauche <= droite:
            milieu = (gauche + droite) // 2
            repas_manges += 1

            if test_survie(milieu, s):
                gauche = milieu + 1  # L'étudiant survit, on cherche plus haut
            else:
                droite = milieu - 1  # L'étudiant ne survit pas, on cherche plus bas
                eleves_morts += 1

        return gauche, repas_manges, eleves_morts  # Le premier nombre d'assiettes qui cause la mort

    n = 20  # Nombre max d'assiettes possibles
    k = 25  # Nombre d'étudiants disponibles
    s = 14  # Seuil fatal d'assiettes

    if k >= math.log2(n):
        seuil_mortel, nb_repas, morts = recherche_dichotomique(n)
        print(
            f"Le seuil mortel est atteint à {seuil_mortel} assiettes. Nombre de repas manges {nb_repas}. Nombre de mort {morts}.")
    else:
        print("Le nombre d'étudiants est insuffisant pour utiliser la recherche dichotomique.")

def pb2():
    def test_survie(m, s):
        SEUIL_FATAL = s  # Seuil de mortalité
        return m <= SEUIL_FATAL  # True si survit, False sinon

    def recherche_multi_etapes(n, k):
        a = max(1, n // (2 * k - 1))  # Taille des sauts
        last_safe = 0
        repas_manges = 0
        eleves_morts = 0

        # Recherche par sauts
        for i in range(1, k + 1):
            test_value = i * a
            repas_manges += 1

            if test_value > n:
                break  # Éviter de dépasser n

            if not test_survie(test_value, s):  # Si l'étudiant échoue
                eleves_morts += 1
                break
            last_safe = test_value

        # Recherche linéaire
        for j in range(last_safe + 1, last_safe + a):
            repas_manges += 1
            if not test_survie(j, s):  # On trouve le seuil mortel
                eleves_morts += 1
                return j, repas_manges, eleves_morts

        return n + 1, repas_manges, eleves_morts  # Si on survit après n assiettes

    n = 40  # Nombre max d'assiettes possibles
    k = 5  # Nombre d'étudiants disponibles
    s = 14  # Seuil fatal d'assiettes

    seuil_mortel, nombre_de_repas, nombre_de_morts = recherche_multi_etapes(n, k)
    print(
        f"Le seuil mortel est atteint à {seuil_mortel} assiettes. Nombre de repas mangés {nombre_de_repas}. Nombre de morts {nombre_de_morts}.")


def pb3():
    def test_survie(m, s):
        SEUIL_FATAL = s
        return m <= SEUIL_FATAL  # True si survit, False sinon

    def recherche_racine_n(n):
        step = int(n ** 0.5)
        last_safe = 0  # Dernière valeur survivable
        repas_manges = 0  # Nombre de repas testés
        eleves_morts = 0  # Nombre d'élèves morts

        # Recherche par paliers de sqrt(n)
        for i in range(step, n + 1, step):
            repas_manges += 1
            if not test_survie(i, s):  # Si l'étudiant échoue
                eleves_morts += 1
                break
            last_safe = i  # Mettre à jour la dernière valeur survivable

        # Recherche linéaire dans la dernière plage testée
        for j in range(last_safe + 1, min(last_safe + step, n + 1)):
            repas_manges += 1
            if not test_survie(j, s):  # On trouve le seuil mortel
                eleves_morts += 1
                return j, repas_manges, eleves_morts

        return n + 1, repas_manges, eleves_morts  # Si on survit après n assiettes

    n = 100  # Nombre max d'assiettes possibles
    s = 64  # Seuil fatal d'assiettes

    seuil_mortel, nombre_de_repas, nombre_de_morts = recherche_racine_n(n)
    print(
        f"Le seuil mortel est atteint à {seuil_mortel} assiettes. Nombre de repas mangés {nombre_de_repas}. Nombre de morts {nombre_de_morts}.")

pb1()
pb2()
pb3()