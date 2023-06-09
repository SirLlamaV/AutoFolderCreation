import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory


try:
    inputDirectory = askdirectory(title='Select Your Input Directory')+"/"
    outputDirectory = askdirectory(title='Select Your Input Directory')+"/."
        
except:
    print("Error")
    
inputDirectoryFiles = os.listdir(inputDirectory)
for file in inputDirectoryFiles:
    if file.endswith('.zip') or file.endswith('.7z') or file.endswith('.rar'):
        shutil.move(os.path.join(inputDirectory,file), os.path.join(outputDirectory,file))
        
outputDirectoryFiles = os.listdir(outputDirectory)
for file in outputDirectoryFiles:
    