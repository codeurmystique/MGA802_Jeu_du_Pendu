# ------------------------------------------------------------
# Jeu du Pendu - MGA802 Module 3
# Ce script permet de jouer au jeu du pendu.
# Le programme choisit un mot au hasard dans un fichier texte.
# ------------------------------------------------------------

# Le module random servira plus tard à choisir un mot au hasard.
import random

# Le module unicodedata servira plus tard à enlever les accents.
import unicodedata


def charger_mots(nom_fichier="mots_pendu.txt"):
    """
    Charge les mots contenus dans un fichier texte.

    Paramètre :
        nom_fichier : nom du fichier texte contenant les mots.
                      Par défaut, le programme utilise 'mots_pendu.txt'.

    Retour :
        Une liste de mots nettoyés.
    """

    # Création d'une liste vide qui contiendra les mots du fichier.
    liste_mots = []

    # On essaie d'ouvrir le fichier demandé.
    # encoding="utf-8" permet de lire correctement les accents.
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:

            # On parcourt chaque ligne du fichier texte.
            for ligne in fichier:

                # strip() enlève les espaces inutiles et le saut de ligne \n.
                mot = ligne.strip()

                # On vérifie que la ligne n'est pas vide.
                if mot != "":

                    # On met le mot en minuscules pour simplifier les comparaisons.
                    mot = mot.lower()

                    # On ajoute le mot nettoyé à la liste.
                    liste_mots.append(mot)

    # Si le fichier n'existe pas, on affiche un message clair.
    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' est introuvable.")
        print("Vérifiez que le fichier est bien dans le même dossier que le script.")

    # On retourne la liste des mots trouvés.
    return liste_mots



def choisir_mot(liste_mots):
    """
    Choisit un mot aléatoire dans la liste de mots.

    Paramètre :
        liste_mots : liste contenant tous les mots disponibles

    Retour :
        Un mot choisi aléatoirement
    """

    # Vérification de sécurité : si la liste est vide
    if not liste_mots:
        print("Erreur : la liste de mots est vide.")
        return None

    # random.choice permet de choisir un élément au hasard dans une liste
    mot_choisi = random.choice(liste_mots)

    # Retourner le mot sélectionné
    return mot_choisi

# ------------------------------------------------------------
# Test temporaire de la fonction choisir_mot
# Cette partie sert seulement à vérifier que la lecture du fichier fonctionne.
# Elle sera retirée ou modifiée plus tard.
# ------------------------------------------------------------

mots = charger_mots()
mots_secret = choisir_mot(mots)

print("Mot choisi :", mots_secret)

