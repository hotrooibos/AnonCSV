# AnonCSV
Ce programme écrit en python permet d'anonymiser les données d'un fichier de données CSV.
Le programme est composé de deux fichiers :
- anoncsv.py : programme principal0
- conf.py : fichier de configuration/paramétrage 

## Installation, exécution
- Copier anoncsv.py et conf.py dans un dossier,
- Placer les CSV à anonymiser à la racine du même dossier,
- Paramétrer conf.py (voir plus bas)
- Exécuter anoncsv.py

## Configuration (conf.py)
Les paramètres du programmes sont stockés sous forme de constantes dans le fichier **conf.py**.
Les premières constantes permettent de définir le format du csv (séparateur, caractère de quote, caractère d'échappement) et les listes de données (nom, prénom, commentaires) dans lesquels le programme choisira aléatoirement les données de substitution (anonymes).

Par exemple, des noms de famille figurant sur un fichier CSV à anonymiser peuvent être remplacés par un nom issu de la liste "LASTNAME", choisi aléatoirement par AnonCSV.

```python
LASTNAME  = ("Martin","Bernard","Thomas", ...)
```

#### Colonnes à anonymiser
La constante "COLUMN_TO_ANONYMIZE" est une liste de type dictionnaire (une liste de "clé:valeur") à paramétrer selon le contenu des CSV à anonymiser.

#### Exemple

Fichier CSV avant anonymisation :
```csv
id,nompers,prenompers,observation
0000081,chirac,patrick,"D'un naturel ""jovial"", Patrick Chirac est un excellent élément.",1450
0000082,norris,chuck,"A su compter jusqu'à l'infini deux fois.",9050
```

conf.py :
```python
                        #   Clé: nom de colonne     Valeur remplacement
COLUMN_TO_ANONYMIZE =   {   "NOMPERS":              LASTNAME,
                            "PRENOMPERS":           FIRSTNAME,
                            "OBSERVATION":          COMMENT,
                            "SALAIRE":              "int4"
                        }
```

Fichier CSV après exécution AnonCSV :
```csv
id,nompers,prenompers,observation
81,Bernard,Léo,"Un terminator.",4842
82,Thomas,Gabriel,"Qui est cette personne ?",1254
```