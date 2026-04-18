import os,yaml

with open("C:/Screensavers/globalconfig.yaml","r") as f:
    loadyaml = yaml.safe_load(f)
filename = loadyaml["cycle"][loadyaml["screensaver"]]
loadyaml["screensaver"] += 1
if loadyaml["screensaver"] == len(loadyaml["cycle"]):
    loadyaml["screensaver"] = 0
with open("C:/Screensavers/globalconfig.yaml","w") as f:
    yaml.dump(loadyaml,f)
try:
    os.startfile("C:/Screensavers/" + filename + "/scrnsave.exe")
except:
    pass