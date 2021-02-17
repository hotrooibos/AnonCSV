#coding:utf-8
import io
import os
import sys
import pandas
import random
import conf
import shutil

ORIGINAL_EXT        = ".orig.csv"
CURRENT_DIR         = os.path.join(sys.path[0])


'''
Functions
'''
def anonymizer(file_to_anon: str):
    '''
    Anonymize the file in argument
    '''
    file_url = os.path.join(f'{CURRENT_DIR}\\{file_to_anon}')
    csv_file = pandas.read_csv(file_url,
                                sep=conf.CSV_DELIMITER,
                                quotechar=conf.CSV_QUOTE_CHAR).copy()

    for colname in conf.COLUMN_TO_ANONYMIZE:
        try:
            data = csv_file[colname].copy()

            # Replace int data
            if data.dtype == 'int64':
                for index, value in data.items():
                    ran_start = 10**    (len(str(data[index]))    -1)   # Nbr random de départ de même longueur que l'occurence (data[index]) -> Ex : 10**(6-1) = 100000
                    ran_end   = (10**   len(str(data[index])))    -1    # Ex : (10** 6) -1  = 999999
                    data[index] = random.randint(ran_start,ran_end)     # Remplacement de l'occurence par une valeur randomized

            # Replace other (string) data
            elif data.dtype == 'object':
                for index, value in data.items():
                    ran_max_index = len(conf.NAMES) -1                          # Récup la taille du du confionnaire de noms
                    data[index] = conf.NAMES[random.randint(0, ran_max_index)]  # Remplace les noms aléatoirement à partir du conf
        
            csv_file[colname] = data    # Write changes to DataFrame

            # Write changes to csv file
            csv_file.to_csv(file_url,
                            index=False,
                            sep=conf.CSV_DELIMITER,
                            quotechar=conf.CSV_QUOTE_CHAR)

        except KeyError:
            continue


'''
Testonly
'''
for file in os.listdir(CURRENT_DIR):
    if file[-9:] == ORIGINAL_EXT or file[-4:] != ".csv":
        continue

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
        if userinput == "y":
            anonymizer(filename)
            break

        elif userinput == "all":
            for filename in file_list:
                anonymizer(filename)
            quit()

        elif userinput == "n" or userinput == "":
            break
        else:
            pass