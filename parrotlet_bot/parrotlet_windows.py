__author__ = 'Timothy Lam'

import os
import ctypes

def selector(message):
    if message == 'windows sort download folder':
        sort_downloads()
        return {'display': 'download files have been sorted', 'say': 'download files have been sorted'}
    elif message == 'windows lock screen': #Lock Screen
        ctypes.windll.user32.LockWorkStation()
    elif message == 'windows sign out': #Logoff
        ctypes.windll.user32.ExitWindowsEx(0)
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