# Calculatrice Web - Équipe 21

## Objectif

Application web de calculatrice avec Flask pour effectuer des opérations arithmétiques de base.

## Description du projet

Ce projet vise à développer une calculatrice web interactive. L'application permet aux utilisateur d'effectuer des calculs arithmétique simple via une interface graphique accessible depuis n'importe quel navigateur web. Il sera en mesure d'effectuer des calcul d'expression simple, c'est-à-dire avec un seul opérateur, et d'afficher les résultats en temps réel. Il supportera les opérateurs d'addition, de soustraction, de multiplication et de division sur des nombres entiers.

## Prérequis

- Python 3.x ou supérieur
- pip (gestionnaire de paquets Python)
- git

## Guide d'installation

### 1. Cloner le dépôt

```bash
git clone <url-du-depot>
cd LOG3000-TP3
```

### 2. Installer les dépendances

Installer Flask :
```bash
pip install flask
```

Installer pytest (pour les tests) :
```bash
pip install pytest
```

## Guide d'utilisation

### 1. Lancer l'application

Dans le terminal, exécutez la commande suivante depuis le répertoire du projet :
```bash
python app.py
```

Vous devriez voir un message similaire à :
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

Ouvrez ensuite votre navigateur web et accédez à l'adresse : **http://127.0.0.1:5000/**

### 2. Utiliser la calculatrice

1. Cliquez sur les boutons numériques pour saisir le premier nombre
2. Cliquez sur un bouton d'opérateur (+, -, *, /)
3. Cliquez sur les boutons numériques pour saisir le second nombre
4. Cliquez sur le bouton "=" pour obtenir le résultat
5. Pour effectuer un nouveau calcul, cliquez sur "C" pour effacer l'écran

### 3. Arrêter l'application

Pour arrêter l'application, retournez dans le terminal et appuyez sur :
`Ctrl + C`

## Exécution des tests

Pour exécuter les tests, utilisez la commande suivante depuis le répertoire du projet :
```bash
python -m pytest -v
```

## Flux de contribution

### Branches

- **main** : Branche principale contenant le code stable
- Pour toute modification, créer une branche depuis `main` :
  - `feature/nom-fonctionnalite` pour une nouvelle fonctionnalité
  - `fix/nom-bug` pour corriger un bug
  - `docs/nom-documentation` pour des modifications de documentation

### Processus de contribution

1. Créer une issue décrivant le problème ou la fonctionnalité
2. Créer une branche appropriée pour l'issue (`feature/`, `fix/`, ou `docs/`)
3. Faire les modifications nécessaires sur cette branche
4. Écrire et exécuter les tests (si applicable)
5. Réexécuter les tests qui échouaient pour vérifier la correction
6. Commit avec un message clair expliquant comment la modification résout le problème
7. Pousser la branche sur GitHub
8. Créer une Pull Request vers `main` en liant l'issue
9. Attendre la révision d'un membre de l'équipe
10. Merger après approbation
11. Documenter que les tests passent maintenant
12. Fermer l'issue en la marquant comme complétée

### Pull Requests

- Décrire clairement les changements effectués dans la description
- Lier l'issue correspondante (si applicable)
- Une révision par un pair est requise avant le merge
- Ne jamais merger sa propre Pull Request

### Issues

- Créer une issue pour chaque bug ou fonctionnalité à développer
- Assigner l'issue au membre responsable de la tâche
- Référencer l'issue dans les commits