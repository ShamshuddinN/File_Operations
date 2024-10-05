import os
from functions import choose_folder, op1, op2n3


files = os.listdir()

folders = []

for i in files:
    if os.path.isdir(i):
        folders.append(i)

if folders:
    print('Select Folder to rename files inside it: ')
    fcount = 1
    for folder in folders:
        print(f"{fcount}. {folder}")
        fcount += 1
else:
    print('No Folders Found in the "Renanme_Files" Directory')

chosen_folder_num = input('Enter Folder Number to choose a Folder: ')



# Checking if input is an Number
isnum = 0
try:
    int(chosen_folder_num)
    isnum = 1
except:
    print('Only Number input is allowed!')

# checking if input is less than 0
go_ahead = 0
folder_got = ''
rename_option = ''
seperator_choice = ''
if isnum and int(chosen_folder_num) >= 1:
    folder_got = choose_folder(num = int(chosen_folder_num), folders = folders)
    if folder_got != "That Folder Dosen't Exist":
        print(f"\nPreview of first 5 files inside {folder_got}: \n {os.listdir(folder_got)[:5]}")
        files_got = os.listdir(folder_got)
        rename_option = input('Choose Renaming Option:\n 1. Prefix Sequential \n 2. text + sequential \n 3. sequential + text\n: ')
        seperator_choice = input('Choose a seperator (-, _, . | etc.): ')

        try:
            int(rename_option)
            go_ahead = 1
        except:
            go_ahead = 0
            print('Rename Option should be a number')

        if go_ahead:
            if int(rename_option) >= 1 and  int(rename_option) <= 3:
                pass
            else:
                go_ahead = 0

    else:
        print(folder_got)
else:
    print('Enter correct folder number')


if go_ahead:
    print('Everything is okay')
    files_got = os.listdir(folder_got)

    if int(rename_option) == 1:
        print('Renaming files with option 1..')
        op1(files= files_got, folder_name = folder_got, sep = seperator_choice)
    elif int(rename_option) == 2:
        common_f_name = input('Enter a common file name: ')
        print('Renaming files with option 2..')
        op2n3(files= files_got, folder_name = folder_got, sep = seperator_choice, cmn = common_f_name, nature='t+s')
        print('Done')
    elif int(rename_option) == 3:
        common_f_name = input('Enter a common file name: ')
        print('Renaming files with option 3..')
        op2n3(files= files_got, folder_name = folder_got, sep = seperator_choice, cmn = common_f_name, nature='s+t')
        print('Done')


# Options:
# 1. Prefix Sequential (1_file_name.ext) given seperator choice
# 2. text + sequential (text_1.ext) given seperator choice
# 3. sequential + text (1_text.ext) given seperator choice




# python3 rename.py