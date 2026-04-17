import os,yaml

with open("C:/Screensavers/globalconfig.yaml","r") as f:
    filename = yaml.safe_load(f)["screensaver"]
try:
    os.startfile("C:/Screensavers/" + filename + "/scrnsave.exe")
except:
    pass