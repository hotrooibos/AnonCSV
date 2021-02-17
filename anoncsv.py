#coding:utf-8
import conf
import os
import pandas
import random
import shutil
import sys
import time

ORIGINAL_EXT        = ".orig.csv"                   # Testing purpose only...
CURRENT_DIR         = os.path.join(sys.path[0])


'''
FONCTION ANONYMIZE
Cette fonction prend un nom de fichier csv en argument, et le lis avec Pandas.
Pour chaque colonne définie dans dans les clés du dictionnaire COLUMN_TO_ANONYMIZE (conf.py), remplace l'ensemble
des données de la colonne selon un traitement appelé par la valeur correspondant à la clé (LASTNAME, "intXX", etc.).
Une fois les données anonymisées, le fichier CSV est réécrit/écrasé avec les nouvelles valeurs.
'''
def anonymize(file_to_anon: str):
    '''
    Anonymize the file in argument
    '''
    
    file_url    = os.path.join(f'{CURRENT_DIR}\\{file_to_anon}')
    csv_file    = pandas.read_csv(file_url,
                                  sep       =conf.CSV_DELIMITER,
                                  quotechar =conf.CSV_QUOTE_CHAR,
                                  escapechar=conf.CSV_ESCAPE_CHAR).copy()

    for key in conf.COLUMN_TO_ANONYMIZE:
        vcta = conf.COLUMN_TO_ANONYMIZE[key] # Valeur de remplacement, si spécifiée en constante dans conf.py
        try:
            data = csv_file[key].copy()

            # Si les data de la colonnes (objet pandas.Series) sont de type entier
            # On randomize un entier dans une fourchette d'entiers de la même longueur
            # data          -> objet pandas.Series de la colonne
            # data.items()  -> tuple de toutes les (index, data) de la colonne
            if data.dtype == 'int64':
                for index, value in data.items():
                    ran_start = 10**    (len(str(value))    -1)         # ** = puissance, équivalent à pow()
                    ran_end   = (10**   len(str(value)))    -1          # Ex : 10**(6-1) = 100000
                    data[index] = random.randint(ran_start, ran_end)

            # Si de type "object" (strings, mixed..)
            # Selon la valeur (vcta) correspondant à la clé (nom colonne) spécifiée dans COLUMN_TO_ANONYMIZE,
            # Si vcta est une string "intXX", génère un entier de longueur XX
            # Sinon (vcta pointe vers un tuple (LASTNAME...)), y sélectionne une donnée aléatoire
            elif data.dtype == 'object':
                for index, value in data.items():

                    if vcta[:3] == "int":
                        ran_start = 10** (int(vcta[3:]) -1)
                        ran_end   = (10** int(vcta[3:])) -1
                        data[index] = random.randint(ran_start, ran_end)

                    else:
                        ran_max_index = len(vcta) -1                          # Récup la taille du dictionnaire de string
                        data[index] = vcta[random.randint(0, ran_max_index)]  # Remplace les string aléatoirement à partir du dict

            else:
                # TODO autres datatypes : datetime64, float64, bool...
                pass

            csv_file[key] = data    # Write changes to DataFrame

            # Write changes to csv file
            csv_file.to_csv(file_url,
                            index     =False,
                            sep       =conf.CSV_DELIMITER,
                            quotechar =conf.CSV_QUOTE_CHAR,
                            escapechar=conf.CSV_ESCAPE_CHAR)

            print(f"\tAnonymize {data.name}")
        except KeyError:
            continue




'''''''''''''''''''''''''''''''''''''''''''''

Testing purpose only... (restaure les fichiers originaux à chaque lancement du script)

'''''''''''''''''''''''''''''''''''''''''''''
for file in os.listdir(CURRENT_DIR):
    if file[-4:] != ".csv":
        continue
    elif file[-9:] == ORIGINAL_EXT:
        src= file
        dst= f'{CURRENT_DIR}\\{file[:-9]}.csv'
    else:
        os.remove(f'{CURRENT_DIR}\\{file}')
        src= f'{CURRENT_DIR}\\{file[0:-4]}.orig.csv'
        dst= f'{CURRENT_DIR}\\{file}'

    shutil.copyfile(src, dst)


'''
MAIN
-> PROGRAM STARTS HERE <-
'''
file_list = []

for filename in os.listdir(CURRENT_DIR):
    if filename[-9:] == ORIGINAL_EXT or filename[-4:] != ".csv":
        continue

    file_list.append(filename)


for filename in file_list:
    print(f"{filename} -------------")

    timer_start = time.time()
    anonymize(filename)
    timer_end = time.time() - timer_start

    print(f"\t{format(timer_end, '.3f')}s")