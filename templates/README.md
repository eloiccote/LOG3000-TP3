# Module Templates

## Raison d'être

Ce module contient les templates HTML utilisés par Flask pour générer l'interface utilisateur de la calculatrice web.

## Principaux fichiers

### `index.html`
**Responsabilité :** Template principal de l'application qui affiche l'interface de la calculatrice

Contenu :
- Structure HTML de la calculatrice
- Formulaire HTML pour soumettre les expressions au serveur Flask
- Zone d'affichage des résultats et des messages d'erreur
- Boutons interactifs (0-9, opérateurs +, -, *, /, égal, effacer)

Fonctionnalités :
- Affichage dynamique de l'expression
- Soumission du formulaire lors du clic sur le bouton "="
- Affichage du résultat retourné par le serveur Flask
- Bouton "C" pour effacer l'écran et recommencer un nouveau calcul

## Dépendances

### Fichiers liés
- **static/style.css** : Feuille de style CSS pour l'apparence de l'interface
- **app.py** : Application Flask qui rend ce template via `render_template('index.html')`

### Hypothèses
- Les variables passées depuis Flask sont :
  - `result` : Le résultat du calcul ou un message d'erreur
- Le formulaire utilise la méthode POST pour soumettre l'expression à la route `/`
- Les fichiers statiques (CSS) se trouve dans le dossier `/static/`

