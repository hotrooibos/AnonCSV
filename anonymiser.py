#coding:utf-8
import csv
import io
import os
import sys

CSV_DELIMITER   = ';'
CSV_QUOTE_CHAR  = '"'
COLUMN_TO_ANONYMIZE = ("VORNA")
CURRENT_DIR     = os.path.join(sys.path[0])


'''
Functions
'''
def anonymize(files_to_anonymize):
    fta = files_to_anonymize

    if type(fta) == list:
        for filename in fta:
            with open(os.path.join(f'{CURRENT_DIR}\\{filename}')) as file:
                reader = csv.reader(file,
                                    delimiter=CSV_DELIMITER,
                                    quotechar=CSV_QUOTE_CHAR)

                for row in reader:
                    # content = list(row[i] for i in COLUMN_TO_ANONYMIZE)
                    print(row)


    elif type(fta) == io.TextIOWrapper:
        print ("ELSE :", fta)
    else:
        print("Error, quitting")
        quit()

    


    # for file in to_anonymize:
    #     # reader = csv.reader()
    #     if type(file) == "tuple":
    #         pass
    #     print(type(file))

'''
Main
'''
file_list = []

for filename in sorted(os.listdir(CURRENT_DIR), reverse=True):
    if filename == os.path.basename(__file__):
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