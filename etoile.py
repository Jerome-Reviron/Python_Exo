"""Module fournissant une bibliothèque graphique turtle."""
import turtle


def dessiner_branche(longueur, angle):
    """Dessine les branches d'une étoile.

    Args:
        longueur (int): Longueur de chaque branche.
        angle (int): Angle de rotation entre les branches.

    Returns:
        Dessin dans une nouvelle fenètre
    """
    for _ in range(5):
        my_art.forward(longueur)
        my_art.right(angle)
        my_art.forward(longueur)
        my_art.left(2 * angle)

# Initialiser la fenêtre et la tortue
wn = turtle.Screen()
my_art = turtle.Turtle()

# Définir la longueur et l'angle pour une branche
longueur_branche = 100
angle_branche = 144

# Dessiner une seule étoile
dessiner_branche(longueur_branche, angle_branche)

# Fermer la fenêtre en cliquant
wn.exitonclick()


#----------------------------------------------------------------------------------------------branche 5 étoiles sans fond
# import turtle

# vm = turtle.Screen()
# my_art = turtle.Turtle()

# # Dessiner le contour de l'étoile à cinq branches
# for i in range(5):
#     my_art.forward(50)
#     my_art.left(72)
#     my_art.forward(50)
#     my_art.right(144)
#     my_art.forward(50)
#     my_art.left(72)
#     my_art.forward(50)
#     my_art.right(144)
#     # Tourner pour dessiner la prochaine branche

# turtle.exitonclick()


#----------------------------------------------------------------------------------------------branche 5 étoiles sans fond

# import turtle

# WN = turtle.Screen()
# My_art = turtle.Turtle()

# for i in range(10):
#     My_art.forward(50)
#     if i % 2 == 0:
#         my_art.left(72)
#     else :
#         My_art.right(144)
# turtle.exitonclick()
