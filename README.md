# Python_Exo

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Calculatrice à 3 boutons en utilisant Tkinter](#calculatrice_3boutons)

## Introduction <a name="introduction"></a>
Ce répertoire est conçu durant ma formation POEI Développeur Applicatif Python, afin d'intégrer l'entreprise Pharma Pilot à Cournond'Auvergne.<br>
Accompagné par Human Booster et de nombreux intervenants, j'aurai à la suite de cette formation mon premier CDI de reconversion professionnelle Concepteur Développeur d'Applications.

## Installation <a name="installation"></a>
Ce répertoire à été installé durant la formation sur mon compte github personnel et a une visibilité public à des fins de collaborations optimales avec les collaborateurs, intervenants et collègues.

## Utilisation <a name="utilisation"></a>
Ce répertoire se dote d'un fichier "README.md" dans le but de proposer une explication de chaque exercice réaliser durant la formation.<br>
On aura donc dans le sommaire l'ajout permanent des liens vers les exercices avec les consignes et les mise en application des programmes.

## Contribuer <a name="contribuer"></a>
Toutes personnes à une visibilité sur l'entièreté du répertoire. En revanche, aucune modification n'est possible.<br>
Les véritables contributions se font lors de nos échanges en direct ou en visio, durant tout l'apprentissage de cet emploi.<br>
De nombreux cours théoriques et pratiques sont réalisés pour consolider notre culture et employabilité.

## Licence <a name="licence"></a>
Tout droit réservé à moi même, Monsieur Reviron Jérôme.

# Calculatrice à 3 boutons en utilisant Tkinter <a name="calculatrice_3boutons"></a>
Ce programme Python nommé "calculatrice_3boutons.py" présente une calculatrice simple avec une interface graphique construite à l'aide de la bibliothèque Tkinter.<br>
La calculatrice est conçue pour fonctionner avec trois boutons principaux et permet à l'utilisateur de naviguer à travers une liste de caractères à l'aide de boutons de défilement.

### Fonctionnalités
- Interface Graphique Intuitive: La calculatrice dispose d'une interface utilisateur simple et intuitive construite avec Tkinter.
- Boutons de Défilement: Utilisez les boutons "↑" et "↓" pour faire défiler une liste de caractères.
- Validation des Choix: Appuyez sur le bouton "Valider" pour confirmer votre choix. La calculatrice réagit en conséquence au caractère sélectionné.
- Fonction de Redémarrage: Si le caractère "R" est sélectionné, l'application peut être redémarrée pour un nouvel ensemble d'opérations.
-Prévention de la Division par Zéro: Lorsque le caractère "=" est sélectionné, la calculatrice vérifie la possibilité de division par zéro et affiche un message d'erreur le cas échéant.

### Utilisation
1. Exécutez dans un IDE, avec une installation Python, le run du programme.
2. Une fenêtre de calculatrice graphique s'ouvrira.
3. Utilisez les boutons "↑" et "↓" pour faire défiler les caractères.
4. Appuyez sur le bouton "Valider" pour confirmer chaque choix de caractère.
5. Explorez les fonctionnalités de la calculatrice et redémarrez l'application au besoin.

### Ensemble de calculs possible
- Addition simple avec des Int
- Addition avec des Float
- Soustraction simple(Int & Float)
- Multiplication (Int & Float)
- Division (Int & Float)
- Division Euclidienne (Int & Float)
- Puissance (Int & Float)
- Modulo (Int & Float)
- Calcul complex (Int, Float & Nombreux opérateurs)

### Particularités
La calculatrice à 3 boutons présente plusieurs particularités pour améliorer l'expérience utilisateur :

#### Redémarrage de l'Application

À tout moment, l'utilisateur peut choisir de redémarrer l'application en appuyant sur le caractère "R" puis en appuyant sur "valider".<br>
Cela permet de commencer une nouvelle séquence d'opérations sans quitter l'application.

#### Gestion de la Division par Zéro

La calculatrice intègre une protection contre la division par zéro. Si une division par zéro est détectée lors de l'évaluation de l'expression, un message d'erreur est affiché à l'utilisateur.<br>
La calculatrice doit ensuite etre réinitialisée avec le "redémarrer l'application" pour éviter toute incohérence.

#### Désactivation du Clavier

Pour promouvoir une expérience utilisateur centrée sur la souris, l'utilisation du clavier est désactivée pendant l'exécution du programme.<br> 
Cela garantit que l'utilisateur interagit exclusivement avec l'interface graphique de la calculatrice à l'aide de la souris.
