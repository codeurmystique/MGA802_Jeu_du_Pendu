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

def normaliser_mot(mot):
    """
    Transforme un mot en une version sans accents.

    Exemple :
        "éléphant" devient "elephant"
        "château" devient "chateau"

    Paramètre :
        mot : le mot original à transformer

    Retour :
        Le même mot, en minuscules et sans accents
    """

    # Mettre le mot en minuscules pour éviter les différences entre majuscules et minuscules.
    mot = mot.lower()

    # Décomposer les lettres accentuées.
    # Par exemple, "é" devient "e" + accent séparé.
    mot_decompose = unicodedata.normalize("NFD", mot)

    # Créer une chaîne vide pour reconstruire le mot sans accents.
    mot_sans_accents = ""

    # Parcourir chaque caractère du mot décomposé.
    for caractere in mot_decompose:

        # La catégorie "Mn" correspond aux marques d'accent.
        # On garde seulement les caractères qui ne sont pas des accents.
        if unicodedata.category(caractere) != "Mn":
            mot_sans_accents += caractere

    # Retourner le mot nettoyé.
    return mot_sans_accents


def afficher_mot_cache(mot, lettres_trouvees):
    """
    Affiche l'état actuel du mot à deviner.

    Les lettres déjà trouvées sont affichées.
    Les lettres non trouvées sont remplacées par un tiret bas _.

    Paramètres :
        mot : le mot secret normalisé, sans accents
        lettres_trouvees : liste des lettres déjà devinées correctement

    Retour :
        Une chaîne de caractères représentant le mot partiellement découvert
    """

    # Créer une chaîne vide pour construire l'affichage du mot.
    affichage = ""

    # Parcourir chaque lettre du mot secret.
    for lettre in mot:

        # Si la lettre a déjà été trouvée, on l'affiche.
        if lettre in lettres_trouvees:
            affichage += lettre + " "

        # Sinon, on affiche un tiret bas.
        else:
            affichage += "_ "

    # Enlever l'espace inutile à la fin et retourner l'affichage.
    return affichage.strip()

def demander_lettre():
    """
    Demande à l'utilisateur d'entrer une lettre valide.

    Conditions :
    - Une seule lettre
    - Pas de chiffre
    - Pas de symbole

    Retour :
        Une lettre valide en minuscule
    """

    while True:
        lettre = input("Entrez une lettre : ").lower()

        # Vérifier que l'entrée contient exactement un caractère
        if len(lettre) != 1:
            print("Veuillez entrer une seule lettre.")
            continue

        # Vérifier que c'est bien une lettre alphabétique
        if not lettre.isalpha():
            print("Veuillez entrer une lettre valide (a-z).")
            continue

        return lettre

def jouer_partie(liste_mots):
    """
    Lance une partie complète du jeu du pendu.

    Paramètre :
        liste_mots : liste des mots disponibles pour le jeu

    Fonctionnement :
        - Choisit un mot au hasard
        - Donne 6 chances au joueur
        - Demande des lettres
        - Affiche l'état du mot
        - Met à jour les chances
        - Vérifie la victoire ou la défaite
    """

    # Choisir un mot au hasard dans la liste.
    mot_secret = choisir_mot(liste_mots)

    # Normaliser le mot pour gérer les accents.
    mot_secret_normalise = normaliser_mot(mot_secret)

    # Initialiser le nombre de chances.
    chances = 6

    # Liste des lettres correctement trouvées.
    lettres_trouvees = []

    # Liste de toutes les lettres déjà essayées.
    lettres_essayees = []

    # Message d'introduction pour une nouvelle partie.
    print("\nNouvelle partie !")
    print("Vous avez 6 chances pour deviner le mot.")

    # La boucle continue tant qu'il reste des chances.
    while chances > 0:

        # Afficher l'état actuel du mot.
        print("\nMot à deviner :", afficher_mot_cache(mot_secret_normalise, lettres_trouvees))

        # Afficher les chances restantes.
        print("Chances restantes :", chances)

        # Afficher les lettres déjà essayées si la liste n'est pas vide.
        if lettres_essayees:
            print("Lettres déjà essayées :", ", ".join(lettres_essayees))

        # Demander une lettre valide à l'utilisateur.
        lettre = demander_lettre()

        # Normaliser la lettre entrée pour gérer les accents éventuels.
        lettre = normaliser_mot(lettre)

        # Vérifier si la lettre a déjà été essayée.
        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue

        # Ajouter la lettre à la liste des lettres essayées.
        lettres_essayees.append(lettre)

        # Vérifier si la lettre est dans le mot secret.
        if lettre in mot_secret_normalise:

            # Ajouter la lettre aux lettres trouvées.
            lettres_trouvees.append(lettre)

            # Informer l'utilisateur.
            print("Bonne réponse !")

        else:
            # Retirer une chance si la lettre n'est pas dans le mot.
            chances -= 1

            # Informer l'utilisateur.
            print("Mauvaise réponse.")

        # Vérifier si toutes les lettres du mot ont été trouvées.
        mot_actuel = afficher_mot_cache(mot_secret_normalise, lettres_trouvees)

        # Si le mot affiché ne contient plus de _, le joueur a gagné.
        if "_" not in mot_actuel:
            print("\nMot complété :", mot_actuel)
            print("Bravo ! Vous avez gagné.")
            print("Le mot était :", mot_secret)
            return

    # Si la boucle se termine parce que chances vaut 0, le joueur a perdu.
    print("\nDommage ! Vous avez perdu.")
    print("Le mot était :", mot_secret)


def demander_rejouer():
    """
    Demande à l'utilisateur s'il souhaite rejouer.

    Retour :
        True si oui, False si non
    """

    while True:
        reponse = input("\nVoulez-vous rejouer ? (o/n) : ").lower()

        if reponse == "o":
            return True
        elif reponse == "n":
            return False
        else:
            print("Veuillez entrer 'o' pour oui ou 'n' pour non.")


# ------------------------------------------------------------
# Programme principal
# ------------------------------------------------------------

def main():
    mots = charger_mots()

    # Boucle principale du jeu
    while True:
        jouer_partie(mots)

        # Demander si l'utilisateur veut rejouer
        if not demander_rejouer():
            print("Merci d'avoir joué !")
            break


# Lancer le programme
if __name__ == "__main__":
    main()
