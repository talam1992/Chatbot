__author__ = 'Timothy Lam'

import os
import ctypes
import hashlib
import datetime

def selector(message):
    if message == 'windows sort download folder':
        sort_downloads()
        return {'display': 'download files have been sorted', 'say': 'download files have been sorted'}
    elif message == 'windows check duplicates':
        check_duplicates()
        return {'display': 'windows has checked duplicates', 'say': 'find below the ducplicated'}
    elif message == 'windows lock screen': #Lock Screen
        ctypes.windll.user32.LockWorkStation()
    elif message == 'windows sign out': #Logoff
        ctypes.windll.user32.ExitWindowsEx(0)
    elif message ==  'windows shutdown': #Shutdown
        os.system("shutdown /s /t 1")
    elif message == "windows restart": #Restart
        os.system("shutdown /r /t 1")
    else:
        return 'windows is currently offline'


def sort_downloads():
    path = r'C:\Users\Timothy Lam\Downloads'
    # folders = [i for i in os.listdir('.') if os.path.isdir(i)]
    folders = []
    files = []
    os.chdir(path)
    for i in os.listdir('.'):
        if os.path.isdir(i):
            folders.append(i)
        else:
            files.append(i)
    dirs = ['PDF', 'EXE', 'WordFiles', 'FILES', 'PowerPoint', 'Excel', 'Pictures', 'Videos']
    try:
        for i in dirs:
            if i not in folders:
                os.mkdir(path+fr'\{i}')
    except OSError as e:
        print(e)

    for file in files:
        name, ext = os.path.splitext(file)
        ext = ext[1:]
        if name[-1] == ')':
            os.remove(file)
        else:
            if ext == 'exe':
                os.rename(rf'{path}\{file}', rf'{path}\EXE\{file}')
            elif ext == 'pdf':
                os.rename(rf'{path}\{file}', rf'{path}\PDF\{file}')
            elif (ext == 'doc') or (ext == 'docx'):
                os.rename(rf'{path}\{file}', rf'{path}\WordFiles\{file}')
            elif (ext == 'ppt') or (ext == 'pptx'):
                os.rename(rf'{path}\{file}', rf'{path}\PowerPoint\{file}')
            elif (ext == 'csv') or (ext == 'xlsx'):
                os.rename(rf'{path}\{file}', rf'{path}\Excel\{file}')
            elif (ext == 'png') or (ext == 'jpg'):
                os.rename(rf'{path}\{file}', rf'{path}\Pictures\{file}')
            elif (ext == 'avi') or (ext == 'mp4'):
                os.rename(rf'{path}\{file}', rf'{path}\Videos\{file}')
            else:
                os.rename(rf'{path}\{file}', rf'{path}\FILES\{file}')

def get_hash(file):
    ha = hashlib.md5(file)
    hash_no = ha.hexdigest()
    return hash_no


def ft(time_):
    return datetime.datetime.fromtimestamp(time_)


def format_print(dup_dict):
    header = 'file' + ' ' * (36 - len('file')) + '| Duplicates'
    print('-' * (len(header) + 35))
    print(header)
    print('-' * (len(header) + 35))
    for i in dup_dict:
        print(f'{i}' + ' ' * (36 - len(i)) + f'| {", ".join(dup_dict[i])}')
        print('-' * (len(header) + 35))


def check_duplicates():
    path = r'C:\Users\Timothy Lam\Downloads'
    files = {}
    dup_dict = {}
    os.chdir(path)
    for i in os.listdir('.')[::-1]:
        if os.path.isfile(i):
            file = open(i, "rb")
            hash_ = get_hash(file.read())
            if hash_ in files:
                if files[hash_] in dup_dict:
                    dup_dict[files[hash_]].append(i)
                else:
                    dup_dict[files[hash_]] = [i]
                #print(f"'{i}' is duplicated in this directory. Same content with '{files[hash_]}'")
                # created time | modified time
                #print(f"{ft(os.path.getctime(i))}|{ft(os.path.getmtime(i))} vs {ft(os.path.getctime(files[hash_]))}|{ft(os.path.getmtime(files[hash_]))}")
            else:
                files[hash_] = i
    format_print(dup_dict)
