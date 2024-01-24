import csv
import os
import pandas as pd

def add_and_log(numbers, csv_filename='history.csv'):
    """
    Addition calculée et stockée dans le fichier "history.csv".

    Args:
        numbers (list): Liste de nombres fournie par l'utilisateur.

    Returns:
        float: Résultat calculé et stocké dans le fichier CSV.
    """
    result = sum(numbers)

    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['Numbers', 'Result']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Numbers': ' + '.join(map(str, numbers)) + ' = ', 'Result': result})

    return result

# Liste pour stocker les résultats de chaque opération
results_list = []

# Effectuez les opérations et enregistrez-les dans le fichier CSV
while True:
    input_str = input('Entrez les nombres séparés par des virgules (ex: 10+20+30) : ')

    # Validation des entrées
    try:
        numbers = [float(num) for num in input_str.split('+')]
    except ValueError:
        print('Erreur : Veuillez entrer des nombres valides.')
        continue

    resultat = add_and_log(numbers)
    print(f'Résultat : {resultat}')

    # Ajoutez le résultat actuel à la liste
    results_list.append({'Numbers': ', '.join(map(str, numbers)), 'Result': resultat})

    continuer = input('Voulez-vous effectuer une autre opération ? (O/N) : ')
    if continuer.lower() != 'o':
        break

# Créer un DataFrame à partir de la liste des résultats
df = pd.DataFrame(results_list)

# Afficher le DataFrame
print(df)

# #---------Correction Johlan
# def addition(x=0, y=0):
#     """ Additionne les deux nombres
#     Args:
#         x (int): nombre a additionner
#         y (int): nombre a additionner
#     Returns:
#         str: Message d'erreur
#         int: resultat de l'addition
#     """
#     if type(x) not in [int,float] or type(y) not in [int,float]:
#         return "Entrez seulement des nombres" 
#     else:
#         data = pd.DataFrame({'Numero X': [x] ,'Numero Y': [y] ,'Resultat': [(x+y)]})
#         data.to_csv('addition.csv',mode='a',index='Numero X',header=False)
#         return x + y
