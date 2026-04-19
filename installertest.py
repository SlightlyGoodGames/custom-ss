import os,sys,shutil,time

def join(file):
    return os.path.join(sys._MEIPASS,file)

def importfile(file):
    shutil.copy(join(file),"C:/Screensaver")

def importfold(fold):
    shutil.copytree(join(fold),os.path.join("C:/Screensaver",fold))

toinstall = input("Welcome to the Custom SS Installer.\nThis will install Custom SS onto your machine.\nWould you like to install (Y/N)? ").lower()
if toinstall == "y":
    print("Unpacking files...",end="")
    os.makedirs("C:/Screensaver",exist_ok=True)
    importfile("configure.exe")
    importfile("Custom Screensaver.scr")
    importfile("globalconfig.yaml")
    importfile("globalinfo.yaml")
    importfold("ellipsis")
    importfold("cube")
    importfold("col-squares")
    print(" done!")
    print("Setting as screensaver...",end="")
    os.system("reg add \"HKEY_CURRENT_USER\Control Panel\Desktop\" /v SCRNSAVE.EXE /t REG_SZ /d \"C:/Screensaver/Custom Screensaver.scr\" /f")
    print(" done!\nCustom SS has been successfully installed on your machine.\nFor configurable options, launch configure.exe.\n\nThis window will close automatically in 10 seconds...")
    time.sleep(10)