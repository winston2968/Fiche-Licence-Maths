# Fiche Licence Maths

Toutes mes fiches de ma Licence de Mathématiques en LaTeX avec un environnement de compilation python. 

## Table des matières

1. [À propos](#à-propos)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
4. [Contact](#contact)

## À propos

Mon projet est composé de différents répertoires permettant l'édition de fiches, la gestion générale du projet et sa compilation. La compilation se fait à l'aide de ```pdflatex``` (pour compiler les fichiers .tex) et la génération des fichiers de build se fait avec ```python3``` (voir ```pybuild.py```). 

Le projet doit respecter une certaine architecture pour permettre le bon fonctionnement de la compilation du document. Ainsi, il doit se présenter sous la forme :

```
.
│
├── build/
├── subjects
│   ├── blabla
│   │   ├── chapitres
│   │   │   ├── chapitre1_*.tex
│   │   │   └── chapitre..._*.tex     
│   │   ├── main_*.tex
│   │   └── title_*.tex
│   └── bloublou
│       ├── chapitres
│       │   ├── chapitre1_*.tex
│       │   └── chapitre..._*.tex     
│       ├── main_*.tex
│       └── title_*.tex
└─ fichiers_de_compilation
```

Où chaque subject (blabla, bloublou) est un projet LaTeX $ part entière avec un fichier main qui contient le préambule et les ```\include{}``` pour les chapitres ```chapitre..._*.tex ```. 

## Installation

### Prérequis

Il est nécessaire de disposer des logiciels suivants :

- [Python3](https://www.python.org/downloads/)
- [LaTeX](https://www.latex-project.org/get/)
- [Make](https://www.gnu.org/software/make/)

### Étapes d'installation

1. Clone le projet depuis GitHub :
   ```bash
   git clone https://github.com/winston2968/Fiche-Licence-Maths.git
2. Exécute le fichier python pour pré-compiler le projet :
    ```bash 
        make pre_compile 
3. Lance le build via pdflatex :
    ```bash 
        make build 
4. Tu peux supprimer les fichiers issus de la compilation (conseillé) : 
    ```bash 
        make clean


## Utilisation 

Pour ce qui est de l'utilisation du projet, les fichiers sont édités dans leur répertoire (chapitres) et sont sous-compilés directement via ```pdflatex```depuis l'éditeur utilisé (pas pris en charge ici). 

Le fichier principal (dans le répertoire racine) doit OBLIGATOIREMENT être nommé ```main.tex```. La page de titre pour le fichier général n'est encore pas prise en charge. 


## Contact

- E-mail : winston2968@gmail.com
- Discord : winston01123