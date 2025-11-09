# Module de Tests

## Raison d'être

Ce module contient l'ensemble des tests unitaires du projet. Il assure la qualité du code en validant le bon fonctionnement des opérations arithmétiques et de la logique métier de l'application.

## Principaux fichiers

### `__init__.py`
Fichier d'initialisation du package Python permettant d'importer le module tests. Dans notre cas, il est vide intentionnellement car aucun import n'est nécessaire.

### `operators_test.py`
**Responsabilité :** Teste toutes les fonctions d'opérations arithmétiques du module `operators.py`

Contenu :
- Tests des opérations de base : addition, soustraction, multiplication, division
- Tests des cas limites et erreurs (division par zéro, etc.)
- Validation des types de retour et des résultats

### `app_test.py`
**Responsabilité :** Teste la logique métier de l'application Flask et la fonction `calculate()`

Contenu :
- Tests de la fonction `calculate()` avec diverses expressions
- Tests des cas d'erreur (expressions invalides, multiples opérateurs, etc.)
- Tests de l'interface Flask et des routes

## Dépendances

### Bibliothèques requises
- **pytest** : Framework de tests utilisé pour exécuter et organiser les tests
- **flask** : Nécessaire pour tester les routes et l'application web

### Hypothèses
- Les modules `app.py` et `operators.py` doivent être présents à la racine du projet
- Les tests supposent que les opérations arithmétiques suivent les règles mathématiques standard
- Les expressions testées suivent le format : `nombre opérateur nombre` (un seul opérateur par expression)

## Exécution

Pour exécuter les tests depuis la racine du projet :
```bash
python -m pytest -v
```

Pour exécuter uniquement les tests d'un fichier spécifique :
```bash
python -m pytest tests/operators_test.py -v
python -m pytest tests/app_test.py -v
```

