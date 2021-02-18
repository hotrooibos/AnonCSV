# AnonCSV
Ce programme écrit en python permet d'anonymiser les données d'un fichier de données CSV.
Le programme est composé de deux fichiers :
- anoncsv.py : programme
- config.yaml : fichier de configuration/paramétrage 

## Installation, exécution
- Copier anoncsv.py et config.yaml dans un dossier.
- Paramétrer config.yaml (voir plus bas).
- Par défaut, placer les CSV à anonymiser dans un dossier "csv" créé à côté du programme. Ce répertoire peut être modifié dans la configuré.
- Exécuter anoncsv.py

## Configuration (config.yaml)
Les paramètres du programmes sont stockés dans le fichier **config.yaml** : dossier contenant les fichiers CSV, séparateur CSV, caractère de quote, caractère d'échappement.

Des **listes** de données de substitution (anonymes) peuvent être définies. Dans la partie suivantes, on pourra indiquer au programme de choisir aléatoirement des valeurs dans ces listes, en remplacement des données d'origine.

Par exemple, des noms de famille figurant sur un fichier CSV à anonymiser pourront être remplacés par un nom issu de la liste `LASTNAME`, choisi aléatoirement par AnonCSV.

```yaml
LASTNAME : &LASTNAME [Martin,Bernard,Thomas, ...]
```

Trois listes sont fournies par défaut : une liste de noms de famille, de prénoms, et de commentaires.

#### Colonnes à anonymiser
`COLUMN_TO_ANONYMIZE` est une liste de type dictionnaire (une liste de clés associés à une valeur). Cette liste doit être paramétrée selon le contenu des CSV à anonymiser.

---

## Exemple
Fichier CSV avant anonymisation :

|id|NOMPERS|PRENOMPERS|observation|salaire|
|--|-------|----------|-----------|-------|
|0000081|chirac|patrick|"D'un naturel ""jovial"", Patrick Chirac est un excellent élément."|1450|
|0000082|norris|chuck|"A su compter jusqu'à l'infini deux fois."|9050|
```csv
id,NOMPERS,PRENOMPERS,observation,salaire
0000081,chirac,patrick,"D'un naturel ""jovial"", Patrick Chirac est un excellent élément.",1450
0000082,norris,chuck,"A su compter jusqu'à l'infini deux fois.",9050
```

config.yaml :
```yaml
COLUMN_TO_ANONYMIZE:
#   Clé: nom de colonne   Valeur de remplacement
    NOMPERS:              *LASTNAME
    PRENOMPERS:           *FIRSTNAME
    observation:          *COMMENT
    salaire:              int4
```
<small>Par exemple, on indique ici que pour tous les fichiers CSV trouvés, si l'on trouve une (ou plusieurs) colonne nommée `NOMPERS`, le programme remplacera ses valeurs par l'une des valeurs de la liste `LASTNAME` définie plus haut.</small>

Fichier CSV après exécution AnonCSV :
|id|NOMPERS|PRENOMPERS|observation|salaire|
|--|-------|----------|-----------|-------|
|81|Bernard|Léo|"Un terminator."|4842|
|82|Thomas|Gabriel|"Qui est cette personne ?"|1254|
```csv
id,NOMPERS,PRENOMPERS,observation,salaire
81,Bernard,Léo,"Un terminator.",4842
82,Thomas,Gabriel,"Qui est cette personne ?",1254
```