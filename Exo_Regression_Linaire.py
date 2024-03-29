### Moyenne de T
# Série de nombres
t = [0, 2, 4, 6, 8, 10, 12, 14]

# Calcul de la moyenne
moyenne_t = sum(t) / len(t)

# Affichage du résultat
print(f"La moyenne de la série t est :{moyenne_t}")



### Moyenne de T des l'éléments au carré -7
# Série de nombres
t = [0, 2, 4, 6, 8, 10, 12, 14]

# Calcul de la moyenne des carrés des éléments de la série t moins le carré de 7.
moyenne_variance = (sum(x**2 for x in t) / len(t)) - moyenne_t**2

# Affichage du résultat
print(f"""La moyenne des carrés des éléments t - le carré de la moyenne :
        {moyenne_variance}""")



### Moyenne de ln(N)
# Série de nombres
t = [0.69, 1.61, 2.77, 2.99, 3.69, 4.60, 5.30, 5.77]

# Calcul de la moyenne
moyenne_t = sum(t) / len(t)

# Affichage du résultat
print(f"La moyenne de la série t est : {round(moyenne_t, 2)}")



### Moyenne de ln(N)
# Série de nombres
t = [0.69, 1.61, 2.77, 2.99, 3.69, 4.60, 5.30, 5.77]

# Calcul de la moyenne des carrés des éléments de la série t moins le carré de 7.
moyenne_variance = (sum(x**2 for x in t) / len(t)) - moyenne_t**2

# Affichage du résultat
print(f"""La moyenne des carrés des éléments t - le carré de moyenne_variance, arrondi est :
        {round(moyenne_variance, 2)}""")
