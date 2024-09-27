# Définition d'une fonction qui ajoute deux nombres et renvoie la somme
def add(a, b):
    return a + b

# Si le fichier addition.py n'est pas exécuté comme fichier principal
# Ce code ne sera pas exécuté
if __name__ == '__main__':
    nombre1 = int(input('Saisir un premier nombre: '))
    nombre2 = int(input('Saisir un second nombre: '))
    resultat = add(nombre1, nombre2)
    print(resultat)