import os,sys,shutil,time
from tkinter import Tk
from tkinter import filedialog

win = Tk()
win.iconify()
path = None

def join(file):
    return os.path.join(sys._MEIPASS,file)

def importfile(file):
    shutil.copy(join(file),path)

def importfold(fold):
    shutil.copytree(join(fold),os.path.join(path,fold))

toinstall = input("Welcome to the Custom SS Installer.\nThis will install Custom SS onto your machine.\nWould you like to install (Y/N)? ").lower()
if toinstall == "y":
    print("Please select the file you would like to install in.\nWARNING: Please make sure the directory is empty.\nIf it is not, this installer may fail.\n")
    win.attributes("-topmost",True)
    path = filedialog.askdirectory()
    win.destroy()
    if path != None:
        print("Unpacking files...",end="")
        importfile("configure.exe")
        importfile("Custom Screensaver.scr")
        importfile("globalconfig.yaml")
        importfile("globalinfo.yaml")
        importfile("README.md")
        importfold("ellipsis")
        importfold("cube")
        importfold("col-squares")
        print(" done!")
        print("Setting as screensaver...",end="")
        os.system("reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v SCRNSAVE.EXE /t REG_SZ /d \"" + os.path.join(path,"Custom Screensaver.scr") + "\" /f")
        print(" done!\nCustom SS has been successfully installed on your machine.\nFor configurable options, launch configure.exe.\n\nThis window will close automatically in 10 seconds...")
    else:
        print("There was an error selecting the directory. Please try again. This window will close in 10 seconds...")
    time.sleep(10)