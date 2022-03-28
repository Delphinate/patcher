import os
from colorama import Fore, Back

source = input('Enter the path to the folder you want to patch: ')
a = input(
    'If you want to see the entire contents of the folder, click ENTER\nIf you want to select the files you want to '
    'search for, enter '
    'key letters: ')
found_flag = False
if source:
    for adress, dirs, files in os.walk(source):
        for file in files:
            full = os.path.join(adress, file)
            if a in full:
                print(adress, file)
                found_flag = True
if not found_flag:
    print(Fore.BLACK)
    print(Back.RED)
    print('Please check your name and try again')
input()
