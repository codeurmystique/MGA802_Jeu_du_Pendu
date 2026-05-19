# Jeu du Pendu - MGA802 Module 3

## Description

Ce projet est une implémentation du jeu du pendu en Python.

Le programme choisit un mot aléatoire à partir d’un fichier texte et demande à l’utilisateur de deviner le mot lettre par lettre.

Le projet utilise :
- les fonctions Python
- la gestion des fichiers
- les boucles
- les conditions
- Git et GitHub

---

## Contenu du dépôt

Le dépôt contient les fichiers suivants :

- `jeu_du_pendu.py` : script principal du jeu
- `mots_pendu.txt` : fichier contenant les mots par défaut
- `README.md` : documentation du projet

---

## Fonctionnalités

Le programme permet :

- de choisir un mot aléatoire
- d’afficher le mot caché avec des `_`
- de gérer les lettres accentuées
- de limiter le nombre de chances à 6
- d’afficher les lettres déjà essayées
- de rejouer après une victoire ou une défaite
- d’utiliser un fichier personnalisé de mots

---

## Utilisation

### Lancer le programme

Exécuter le fichier :

```text
jeu_du_pendu.py
```

### Utiliser le fichier par défaut

Lorsque le programme demande :

```text
Voulez-vous utiliser votre propre fichier de mots ? (o/n)
```

répondre :

```text
n
```

---

### Utiliser un fichier personnalisé

Créer un fichier texte contenant un mot par ligne.

Exemple :

```text
python
canada
montreal
avion
```

Ensuite :
- répondre `o`
- entrer le nom du fichier

Exemple :

```text
mes_mots.txt
```

---

## Pseudo-code

```text
Charger les mots depuis un fichier texte

Demander à l’utilisateur s’il souhaite utiliser un fichier personnalisé

Si aucun fichier personnalisé n’est fourni :
    utiliser le fichier par défaut

Tant que l’utilisateur veut jouer :

    choisir un mot aléatoire

    normaliser les accents du mot

    initialiser :
        - les chances à 6
        - les lettres trouvées
        - les lettres essayées

    Tant qu’il reste des chances :

        afficher le mot caché

        demander une lettre valide

        vérifier si la lettre a déjà été essayée

        si la lettre est correcte :
            ajouter la lettre aux lettres trouvées

        sinon :
            retirer une chance

        vérifier si toutes les lettres ont été trouvées

        si le mot est complété :
            afficher un message de victoire
            terminer la partie

    si les chances atteignent 0 :
        afficher un message de défaite

    demander à l’utilisateur s’il souhaite rejouer
```

---

## Auteur

Projet réalisé dans le cadre du module 3 du cours MGA802.