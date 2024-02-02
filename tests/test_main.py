from visualgo.main import np, somme_elements 

def test_somme_elements():
    # Testons avec un tableau simple
    tableau = np.array([1, 2, 3, 4, 5])
    resultat_attendu = np.sum(tableau)
    resultat_obtenu = somme_elements(tableau)
    assert resultat_obtenu == resultat_attendu

def test_somme_elements_vide():
    # Testons avec un tableau vide
    tableau = np.array([])
    resultat_attendu = 0  # La somme d'un tableau vide est 0
    resultat_obtenu = somme_elements(tableau)
    assert resultat_obtenu == resultat_attendu

def test_somme_elements_negatifs():
    # Testons avec des nombres négatifs
    tableau = np.array([-1, -2, -3, -4, -5])
    resultat_attendu = np.sum(tableau)
    resultat_obtenu = somme_elements(tableau)
    assert resultat_obtenu == resultat_attendu
