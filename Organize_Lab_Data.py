import os
from pathlib import Path
import shutil

#replace with local path name for folder 'Sept_30th_2023_v2'
folder = '/Users/ethangramowski/Documents/MATLAB/Lab/Sept_30th_2023_v2'

#https://stackoverflow.com/questions/14176166/list-only-files-in-a-directory
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

file_names = list(files(folder))
files2remove = []

#Creates new folders
for n in range(199, 513):
    os.makedirs(os.path.join(folder, 'M_' + str(n)), exist_ok=True)

#Copies files from main path, sorts into corresponding folder
for n in range(199, 513):
    for file in file_names:
        if "M_" + str(n) in file:
            shutil.copy(os.path.join(folder, file), os.path.join(folder, 'M_' + str(n)))
            files2remove.append(os.path.join(folder, file))

#Removes files from main path
files2remove = list(set(files2remove))
for file in files2remove:
    os.remove(file)
