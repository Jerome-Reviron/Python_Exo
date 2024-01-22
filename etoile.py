import turtle

def dessiner_branche(longueur, angle):
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
