# Module Static

## Raison d'être

Ce module contient le fichier statique (CSS) utilisé pour styliser l'interface utilisateur de l'application web. Il sépare la présentation visuelle de la logique métier et de la structure HTML.

## Principaux fichiers

### `style.css`
**Responsabilité :** Définit l'apparence visuelle de la calculatrice web

Contenu :
- Positionnement de la calculatrice sur la page
- Style de l'écran d'affichage
- Style des boutons
- Effets visuels et interactions
- Couleurs et thème général de l'interface

Éléments stylisés :
- `.calculator` : Conteneur principal de la calculatrice
- `.display` : Écran d'affichage des expressions et résultats
- `.buttons` : Conteneur de la grille de boutons
- `button` : Style des boutons individuels
- Classes spéciales pour différents types de boutons

## Dépendances

### Fichiers liés
- **templates/index.html** : Template HTML qui référence ce fichier CSS

### Hypothèses
- Le fichier CSS est lié dans le template via :
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```
- Les classes CSS correspondent aux éléments HTML définis dans `index.html`

