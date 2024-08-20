# corm => Copy or Move Files using python :)
import os
from functions import move_or_copy

# Cpoy or move specific files filtered with type using extension

files = os.listdir()

folders = []

for i in files:
    if os.path.isdir(i):
        folders.append(i)

if folders:
    print('Select Folder to Move or Copy files inside it: ')
    for i, folder in enumerate(folders):
        print(f"{i+1}. {folder}")

else:
    print('No Folders Found in the "Renanme_Files" Directory')

fdr_num = input('Enter Folder Number to choose a Folder: ')
morc = input('Move or Copy files? Enter - m or c: ')
filter_ext = input('Enter File type (Eg: .pdf/.doc/.docx etc): ')
dest_fol_name = input('Enter Destination folder name: ')


move_or_copy(nature = morc, folder = folders[int(fdr_num) - 1],
             files_list = os.listdir(folders[int(fdr_num) - 1]), dest_fol = dest_fol_name, file_type = filter_ext)

# python3 corm.py