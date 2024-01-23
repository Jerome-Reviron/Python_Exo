"""Module fournissant une fonction pour afficher la version de Python."""
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

# Exemple d'utilisation
while True:
    lettre_utilisateur = input("Entrez une lettre : ").strip()

    # Vérifiez si l'utilisateur a entré une seule lettre alphabétique
    if len(lettre_utilisateur) == 1 and lettre_utilisateur.isalpha():
        est_une_voyelle(lettre_utilisateur)
        break
    else:
        print("Veuillez entrer une seule lettre alphabétique.")
