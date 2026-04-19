import os,yaml,sys

if sys.executable.split("\\")[-1] != "python.exe":
    parentpath = os.path.dirname(sys.executable)
else:
    parentpath = os.path.dirname(__file__)

with open(os.path.join(parentpath,"globalconfig.yaml"),"r") as f:
    loadyaml = yaml.safe_load(f)
filename = loadyaml["cycle"][loadyaml["screensaver"]]
loadyaml["screensaver"] += 1
if loadyaml["screensaver"] == len(loadyaml["cycle"]):
    loadyaml["screensaver"] = 0
with open(os.path.join(parentpath,"globalconfig.yaml"),"w") as f:
    yaml.dump(loadyaml,f)
try:
    os.startfile(os.path.join(parentpath,filename,"scrnsave.exe"))
except:
    pass