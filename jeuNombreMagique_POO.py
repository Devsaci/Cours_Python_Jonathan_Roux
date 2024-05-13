## Code Python en programmation orientée objet pour trouver le nombre magique
"""
Voici un exemple de code Python en programmation orientée objet pour trouver 
le nombre magique :
"""
# jeuNombreMagique_POO.python
import random

class JeuDevinerNombre:
  """
  Classe pour implémenter le jeu de deviner un nombre magique.

  Attributs:
    nombre_magique: Entier, le nombre à deviner.
    essais_max: Entier, le nombre maximum d'essais autorisés.
    nombre_essais: Entier, le nombre d'essais utilisés jusqu'à présent.

  Méthodes:
    __init__(self, nombre_magique, essais_max): Initialise le jeu.
    jouer(self): Lance le jeu.
    verifier_nombre(self, nombre_propose): Vérifie si le nombre proposé est 
    le nombre magique.
    afficher_resultat(self): Affiche le résultat du jeu.
  """

  def __init__(self, nombre_magique, essais_max):
    """
    Initialise le jeu.

    Args:
      nombre_magique: Entier, le nombre à deviner.
      essais_max: Entier, le nombre maximum d'essais autorisés.
    """
    self.nombre_magique = nombre_magique
    self.essais_max = essais_max
    self.nombre_essais = 0

  def jouer(self):
    """
    Lance le jeu.
    """
    while self.nombre_essais < self.essais_max:
      nombre_propose = int(input("Entrez un nombre : "))
      resultat = self.verifier_nombre(nombre_propose)
      if resultat == 0:
        self.afficher_resultat(True)
        break
      else:
        self.nombre_essais += 1
        print(resultat)
    if self.nombre_essais == self.essais_max:
      self.afficher_resultat(False)

  def verifier_nombre(self, nombre_propose):
    """
    Vérifie si le nombre proposé est le nombre magique.

    Args:
      nombre_propose: Entier, le nombre proposé par le joueur.

    Returns:
      0 si le nombre proposé est le nombre magique,
      -1 si le nombre proposé est inférieur au nombre magique,
      1 si le nombre proposé est supérieur au nombre magique.
    """
    if nombre_propose == self.nombre_magique:
      return 0
    elif nombre_propose < self.nombre_magique:
      return -1
    else:
      return 1

  def afficher_resultat(self, victoire):
    """
    Affiche le résultat du jeu.

    Args:
      victoire: Booléen, indique si le joueur a gagné ou perdu.
    """
    if victoire:
      print("Félicitations, vous avez trouvé le nombre magique !")
    else:
      print(f"Vous avez perdu. Le nombre magique était {self.nombre_magique}.")

# Exemple d'utilisation
jeu = JeuDevinerNombre(random.randint(1, 100), 5)
jeu.jouer()

"""
Ce code définit une classe `JeuDevinerNombre` qui implémente le jeu de deviner 
un nombre magique. La classe a les attributs suivants :

* `nombre_magique`: Le nombre à deviner.
* `essais_max`: Le nombre maximum d'essais autorisés.
* `nombre_essais`: Le nombre d'essais utilisés jusqu'à présent.

La classe a les méthodes suivantes :

* `__init__`: Initialise le jeu.
* `jouer`: Lance le jeu.
* `verifier_nombre`: Vérifie si le nombre proposé est le nombre magique.
* `afficher_resultat`: Affiche le résultat du jeu.

L'exemple d'utilisation crée une instance de la classe `JeuDevinerNombre`, 
définit le nombre magique et le nombre maximum d'essais, puis lance le jeu.

## Remarque

Ce code est un exemple simple et peut être étendu de différentes manières. 
Par exemple, vous pouvez ajouter des fonctionnalités pour :

* Afficher l'historique des essais du joueur.
* Permettre au joueur de choisir le niveau de difficulté (en changeant 
le nombre magique et/ou le nombre maximum d'essais).
* Gérer les erreurs (par exemple, si le joueur entre un nombre non valide).


## Algorithme pédagogique pour le jeu de deviner le nombre magique en Python

**Objectif:**

Apprendre les concepts de base de la programmation orientée objet en Python 
en implémentant un jeu de deviner le nombre magique.

**Niveau:**

Débutant

**Prérequis:**

* Connaissances de base en Python (variables, types de données, opérateurs, 
instructions conditionnelles, boucles)
* Concepts de base de la programmation orientée objet 
(classes, objets, méthodes, attributs)

**Déroulement:**

1. **Définir la classe `JeuDevinerNombre`:**
    * Attributs:
        * `nombre_magique`: Entier, le nombre à deviner.
        * `essais_max`: Entier, le nombre maximum d'essais autorisés.
        * `nombre_essais`: Entier, le nombre d'essais utilisés jusqu'à présent.
    * Méthodes:
        * `__init__(self, nombre_magique, essais_max)`: Initialise le jeu avec 
        le nombre magique et le nombre maximum d'essais.
        * `jouer(self)`: Lance le jeu et gère les interactions avec le joueur.
        * `verifier_nombre(self, nombre_propose)`: Vérifie si le nombre proposé 
        par le joueur est le nombre magique.
            * Retourne 0 si le nombre est correct, -1 s'il est inférieur, 
            1 s'il est supérieur.
        * `afficher_resultat(self, victoire)`: Affiche le résultat
          du jeu (victoire ou défaite) et le nombre magique si le joueur a perdu.

2. **Implémenter les méthodes de la classe:**
    * Dans la méthode `__init__`, initialiser les attributs 
    `nombre_magique`, `essais_max` et `nombre_essais`.
    * Dans la méthode `jouer`, utiliser une boucle `while` pour tant que 
    le nombre d'essais n'est pas dépassé:
        * Demander au joueur de saisir un nombre.
        * Appeler la méthode `verifier_nombre` pour vérifier le nombre proposé.
        * En fonction du résultat, afficher un message approprié et incrémenter 
        le nombre d'essais si nécessaire.
        * Si le joueur trouve le nombre magique, arrêter la boucle et afficher 
        un message de félicitations.
    * Dans la méthode `verifier_nombre`, comparer le nombre proposé avec le nombre 
    magique et retourner 0, -1 ou 1 selon le résultat.
    * Dans la méthode `afficher_resultat`, afficher un message de victoire ou de 
    défaite et le nombre magique si le joueur a perdu.

3. **Créer une instance de la classe et lancer le jeu:**
    * Générer un nombre magique aléatoire.
    * Créer une instance de la classe `JeuDevinerNombre` en passant 
    le nombre magique 
    et le nombre maximum d'essais comme arguments.
    * Appeler la méthode `jouer` de l'instance pour lancer le jeu.

**Explication pédagogique:**

* Cet algorithme met en pratique les concepts de la programmation orientée objet en 
créant une classe pour représenter le jeu de deviner le nombre magique.
* La classe encapsule les données (attributs) et le comportement (méthodes) 
liés au jeu.
* Les méthodes permettent de gérer les différentes étapes du jeu, de l'initialisation
 à l'interaction avec le joueur et à l'affichage du résultat.
* L'utilisation d'une boucle `while` permet de répéter les actions tant que le joueur 
n'a pas trouvé le nombre magique ou atteint le nombre maximum d'essais.
* Les instructions conditionnelles permettent de prendre des décisions en fonction du 
résultat de la vérification du nombre proposé.
* Les messages affichés au joueur permettent de l'informer et de le guider tout au 
long du jeu.

**Avantages pédagogiques:**

* Cet algorithme est simple à comprendre et à suivre pour les débutants en programmation 
orientée objet.
* Il met en évidence les concepts clés de la POO tels que les classes, les objets, 
les méthodes et les attributs.
* Il permet de pratiquer la création de classes, l'utilisation de méthodes et 
la gestion des interactions avec l'utilisateur.
* Le jeu est un contexte motivant pour apprendre les concepts de base de la POO 
de manière ludique.

**Variantes:**

* On peut enrichir l'algorithme en ajoutant des fonctionnalités, comme l'affichage 
de l'historique des essais du joueur, la possibilité de choisir le niveau de difficulté 
ou la gestion des erreurs de saisie.
* On peut également adapter l'algorithme à d'autres types de jeux basés sur 
la devinette, comme deviner un mot
"""