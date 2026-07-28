import os 
from os.path import isfile, join

def clean_filename(filename : str):
     return filename.split('.')[0].replace('-', ' ').replace('_', '. ')

def choosing_theme():
    files = sorted([f for f in os.listdir('Themes') if isfile(join('Themes', f))])
    print("Choisissez parmis ces thèmes : ")
    for file in files:
        print(clean_filename(file))
    choice = int(input())
    choosen_file = files[choice]
    return join('Themes', choosen_file)

