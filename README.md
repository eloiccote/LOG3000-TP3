# Calculatrice Web - Équipe 104

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

Pour executer les tests, il faut executer la commande pytest -v dans le terminal. 
La commande peut etre executee a la racine du projet ou dans le dossier \tests.

## Fluc de contribution

//TODO : À faire