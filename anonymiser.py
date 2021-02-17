#coding:utf-8
import io
import os
import sys
import pandas
import random
import dict
import shutil


CSV_DELIMITER       = ';'
CSV_QUOTE_CHAR      = '"'
COLUMN_TO_ANONYMIZE = ("NACHN", "VORNA", "YYID1", "YYPN2")
FILES_TO_SKIP       = ('pa0002.orig.csv', 'pa9533.orig.csv', '.gitignore', '.git', '__pycache__', os.path.basename(__file__))
CURRENT_DIR         = os.path.join(sys.path[0])


'''
Functions
'''
def anonymize(files_to_anonymize):
    fta = files_to_anonymize

    if type(fta) == list:
        for filename in fta:
            file_url = os.path.join(f'{CURRENT_DIR}\\{filename}')
            csv_file = pandas.read_csv(file_url,
                                       sep=CSV_DELIMITER,
                                       quotechar=CSV_QUOTE_CHAR).copy()

            for colname in COLUMN_TO_ANONYMIZE:
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
                            ran_max_index = len(dict.NAMES) -1
                            data[index] = dict.NAMES[random.randint(0, ran_max_index)]
                
                    csv_file[colname] = data    # Write changes to DataFrame
                    print(f'{csv_file}\n')

                    # Write changes to csv file
                    csv_file.to_csv(file_url,
                                    index=False,
                                    sep=CSV_DELIMITER,
                                    quotechar=CSV_QUOTE_CHAR)

                except KeyError:
                    continue
            



    elif type(fta) == io.TextIOWrapper:
        print ("ELSE :", fta)
    else:
        print("Error, quitting")
        quit()

    
def anonymizer(file_to_anon: str):
    '''
    Anonymize the file in argument
    '''



'''
Testonly
'''
os.remove(CURRENT_DIR + '\\pa0002.csv')
src= CURRENT_DIR + '\\pa0002.orig.csv'
dst = CURRENT_DIR + '\\pa0002.csv'
shutil.copyfile(src, dst)

'''
Main
'''
file_list = []

for filename in sorted(os.listdir(CURRENT_DIR), reverse=True):
    if filename in FILES_TO_SKIP:
        continue
    file_list.append(filename)


for filename in file_list:
    while True:
        userinput = input(f"Traiter {filename} ? [y/N/all]")
        if userinput == "y":
            with open(os.path.join(f'{CURRENT_DIR}\\{filename}')) as file:
                anonymize(file) # Call anonymize avec le fichier complet en argument
            break

        elif userinput == "all":
            anonymize(file_list) # Call anonymize avec une liste de str (noms fichiers) en argument
            quit()

        elif userinput == "n" or userinput == "":
            break
        else:
            pass