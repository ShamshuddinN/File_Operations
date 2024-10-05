import os
import shutil

def choose_folder(num: int, folders: list):
    assert isinstance(num, int) and isinstance(folders, list), "Given arguments are Incorrect"

    if num > len(folders) or num <= 0:
        return "That Folder Dosen't Exist"
    
    return folders[num - 1]

# 1. Prefix Sequential (1_file_name.ext) given seperator choice
def op1(files: list, folder_name: str, sep: str):

    for i, file in enumerate(files):
        ext_indx = file[-10:][::-1].index('.') + 1
        # taking Extension of file seperately
        ext = file[-ext_indx:]
        fnm = file.replace(ext, '')

        old_file = os.path.join(folder_name, file)
        new_file = os.path.join(folder_name, f'{i+1}{sep}{fnm}{ext}')
        
        os.rename(old_file, new_file)


# 2. text + sequential (text_1.ext) given seperator choice
# 3. sequential + text (1_text.ext) given seperator choice
def op2n3(files: list, folder_name: str, sep: str, cmn: str, nature: str):

    for i, file in enumerate(files):
        ext_indx = file[-10:][::-1].index('.') + 1
        # taking Extension of file seperately
        ext = file[-ext_indx:]

        old_file = os.path.join(folder_name, file)
        
        if nature == 't+s':
            new_file = os.path.join(folder_name, f'{cmn}{sep}{i+1}{ext}')
        elif nature == 's+t':
            new_file = os.path.join(folder_name, f'{i+1}{sep}{cmn}{ext}')
        
        os.rename(old_file, new_file)

def move_or_copy(nature: str, folder: str, files_list: list, dest_fol: str, file_type: str):    
    
    if not os.path.isdir(dest_fol):
        os.mkdir(dest_fol)
    
    for f in files_list:
        ext_indx = f[-10:][::-1].index('.') + 1
        ext = f[-ext_indx:]
    
        if ext == file_type:
            source = folder + '/' + f
            destination = dest_fol + '/' + f

            if nature == 'm':
                shutil.move(source, destination)
            elif nature == 'c':
                shutil.copy(source, destination)