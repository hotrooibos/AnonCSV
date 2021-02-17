#coding:utf-8
import conf
import os
import pandas
import random
import shutil
import sys
import time

ORIGINAL_EXT        = ".orig.csv"
CURRENT_DIR         = os.path.join(sys.path[0])


'''
Functions
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
        val = conf.COLUMN_TO_ANONYMIZE[key] # Valeur de remplacement, si spécifiée en constante dans conf.py

        try:
            data = csv_file[key].copy()

            # Replace int data
            if data.dtype == 'int64':
                for index, value in data.items():
                    ran_start = 10**    (len(str(value))    -1)         # Nb random de départ de même longueur que l'occurence (data[index]) -> Ex : 10**(6-1) = 100000
                    ran_end   = (10**   len(str(value)))    -1          # Ex : (10** 6) -1  = 999999
                    data[index] = random.randint(ran_start, ran_end)    # Remplacement de l'occurence par une valeur randomized

            # Replace other (string) data
            elif data.dtype == 'object':
                for index, value in data.items():
                    # print("Anonymize->",str(value)[0:50])

                    # Si la valeur à anon est taggée en "intXX"
                    if val[:3] == "int":
                        ran_start = 10** (int(val[3:]) -1)  # Nbr random de départ de même longueur que l'occurence (data[index]) -> Ex : 10**(6-1) = 100000
                        ran_end   = (10** int(val[3:])) -1  # Ex : (10** 6) -1  = 999999
                        data[index] = random.randint(ran_start, ran_end)

                    else:
                        ran_max_index = len(val) -1                          # Récup la taille du dictionnaire de string
                        data[index] = val[random.randint(0, ran_max_index)]  # Remplace les string aléatoirement à partir du dict

            csv_file[key] = data    # Write changes to DataFrame

            # Write changes to csv file
            csv_file.to_csv(file_url,
                            index     =False,
                            sep       =conf.CSV_DELIMITER,
                            quotechar =conf.CSV_QUOTE_CHAR,
                            escapechar=conf.CSV_ESCAPE_CHAR)
            
        except KeyError:
            continue


'''
Pour test (restaure les fichiers originaux à chaque lancement du script)
'''
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
Main
'''
file_list = []

for filename in os.listdir(CURRENT_DIR):
    if filename[-9:] == ORIGINAL_EXT or filename[-4:] != ".csv":
        print(filename[-9:])
        continue

    file_list.append(filename)


for filename in file_list:
    while True:
        userinput = input(f"Traiter {filename} ? [y/N/all]")

        timer_start = time.time()
        if userinput == "y":
            anonymize(filename)
            timer_end = time.time() - timer_start
            print(f"{filename} anonymized in {format(time.time() - timer_start, '.3f')}s")
            break

        elif userinput == "all":
            for filename in file_list:
                anonymize(filename)
                timer_end = time.time() - timer_start
                print(f"{filename} anonymized in {format(timer_end, '.3f')}s")
            quit()

        elif userinput == "n" or userinput == "":
            break
        else:
            print("Wrong input. Type \"y\", \"n\" or \"all\"")