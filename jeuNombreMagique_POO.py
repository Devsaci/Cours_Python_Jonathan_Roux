## Code Python en programmation orientée objet pour trouver le nombre magique
"""
Voici un exemple de code Python en programmation orientée objet pour trouver le nombre magique :
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
    verifier_nombre(self, nombre_propose): Vérifie si le nombre proposé est le nombre magique.
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
Ce code définit une classe `JeuDevinerNombre` qui implémente le jeu de deviner un nombre magique. La classe a les attributs suivants :

* `nombre_magique`: Le nombre à deviner.
* `essais_max`: Le nombre maximum d'essais autorisés.
* `nombre_essais`: Le nombre d'essais utilisés jusqu'à présent.

La classe a les méthodes suivantes :

* `__init__`: Initialise le jeu.
* `jouer`: Lance le jeu.
* `verifier_nombre`: Vérifie si le nombre proposé est le nombre magique.
* `afficher_resultat`: Affiche le résultat du jeu.

L'exemple d'utilisation crée une instance de la classe `JeuDevinerNombre`, définit le nombre magique et le nombre maximum d'essais, puis lance le jeu.

## Remarque

Ce code est un exemple simple et peut être étendu de différentes manières. Par exemple, vous pouvez ajouter des fonctionnalités pour :

* Afficher l'historique des essais du joueur.
* Permettre au joueur de choisir le niveau de difficulté (en changeant le nombre magique et/ou le nombre maximum d'essais).
* Gérer les erreurs (par exemple, si le joueur entre un nombre non valide).
"""