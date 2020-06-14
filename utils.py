
import shutil
import os, glob

def retrieve_content_list(path):
    os.chdir('.\\static\\content\\' + path)
    matches = [file for file in glob.glob('*.txt')]
    os.chdir('..\\..\\..\\')

    matches = [x[:-4] for x in matches]

    return matches
