def est_une_voyelle(lettre):
    """
    Vérifie si la lettre donnée est une voyelle.

    :param lettre: La lettre à vérifier.
    :type lettre: str
    """
    match lettre.upper():
        case 'A' | 'E' | 'I' | 'O' | 'U' | 'Y':
            print(f'La lettre {lettre} est une voyelle.')
        case _:
            print(f'La lettre {lettre} n\'est pas une voyelle.')

# Exemples d'utilisation
lettre_utilisateur = input("Entrez une lettre : ")
est_une_voyelle(lettre_utilisateur)
