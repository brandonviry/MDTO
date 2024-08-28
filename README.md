# MDTO

## Description

**MDTO** est un projet de traitement de texte qui fournit des outils pour extraire et formater des informations à partir de fichiers texte. Le But c'est de faire la mise ne forme du post LinkedIn et le sauvegarde dans un fichier text.


> Ce projet risque de changer c'est a dire que il  peut être modifié à tout moment.Nouvelle fonctionnalité et amélioration de code 

## Structure du Projet

Le projet est organisé comme suit :

```
MDTO/
│   README.md          # Ce fichier
│         
├───exemple            # Exemples de fichiers Markdown
│       Lapin.md       # Exemple de fichier Markdown
│       
└───src                # Scripts Python
      extract.py     # Script pour extraire des motifs à partir de texte
      file.py        # Utilitaires pour la gestion des fichiers
      formatUnicode.py # Fonctionnalités pour le formatage Unicode
      main.py        # Script principal d'exécution
       
    
```

## Installation

1. Clonez le dépôt :

    ```bash
    git clone <URL-du-repository>
    cd MDTO
    ```

2. Créez un environnement virtuel (optionnel mais recommandé) :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```


## Utilisation

1. **Exécuter le Script Principal :**

    Le fichier principal `main.py` est utilisé pour lancer le traitement principal. Vous pouvez l'exécuter en utilisant la commande suivante :

    ```bash
    py src/main.py  <file_name>
    ```

2. **Scripts Individuels :**

    - `extract.py` : Contient des fonctions pour extraire des motifs à partir de texte en utilisant des expressions régulières.
    - `file.py` : Fournit des utilitaires pour la gestion des fichiers.
    - `formatUnicode.py` : Inclut des fonctions pour le formatage Unicode des chaînes de texte.

3. **Exemples :**

    Le répertoire `exemple/` contient des fichiers Markdown d'exemple pour vous aider à comprendre comment utiliser les fonctionnalités du projet.



## Auteur

- **VIRY Brandon** - Créateur et mainteneur du projet.

## Licence

Ce projet est sous Aucune Licence.

