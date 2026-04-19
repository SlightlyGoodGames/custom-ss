import yaml,os,sys

if sys.executable.split("\\")[-1] != "python.exe":
    parentpath = os.path.dirname(sys.executable)
else:
    parentpath = os.path.dirname(__file__)

def localfile(path1,path2=None):
    if path2 == None:
        return os.path.join(parentpath,path1)
    else:
        return os.path.join(parentpath,path1,path2)

print("Welcome to the Custom SS configuration.\nRetrieving screensaver data and config...")
allfolders = [f for f in os.listdir(parentpath) if not os.path.isfile(localfile(f)) and f != ".git"]

alldata = {}
allconf = {}
allids = {}
globalconf = {}
globaldata = {}


for i in allfolders:
    if os.path.exists(localfile(i,"info.yaml")):
        with open(localfile(i,"info.yaml"),"r") as f:
            thisdata = yaml.safe_load(f)
            allids.update({thisdata["id"]:i})
            alldata.update({i:thisdata})
    else:
        alldata.update({i:{"id":-1,"name":i,"codename":i,"desc":"Description not given.","added":"Unknown version","complete":False,"hasconfig":False,"config":{}}})
    if os.path.exists(localfile(i,"config.yaml")):
        with open(localfile(i,"config.yaml"),"r") as f:
            thisdata = yaml.safe_load(f)
            allconf.update({i:thisdata})
    else:
        allconf.update({i:{}})

with open(localfile("globalconfig.yaml"),"r") as f:
    globalconf = yaml.safe_load(f)

with open(localfile("globalinfo.yaml"),"r") as f:
    globaldata = yaml.safe_load(f)

def printscrlist():
    workingscrnsave = len(allids)
    print("\nFound " + str(workingscrnsave) + " screensavers:\n")
    for i in dict(sorted(allids.items())):
        if i != "ph":
            this = alldata[allids[i]]
            if this["id"] != -1:
                print("ID: " + str(this["id"]) + "\nName: " + this["name"] + " [" + allids[i] + "]\nDescription: " + this["desc"] + "\nAdded: " + this["added"] + "\nComplete: " + str(this["complete"]) + "\n")
            else:
                print("Codename: " + this["name"] + "\nNo information has been added for this entry.\n")

while True:
    option = int(input("1) Edit / view configuration\n2) Set default screensaver\n3) View info\nWhat would you like to do? "))
    if option == 1:
        printscrlist()
        view = int(input("Enter the ID of what you would like to edit/view: "))
        try:
            viewdata = alldata[allids[view]]
            viewconf = allconf[allids[view]]
        except KeyError:
            print("Invalid ID.")
        else:
            reallydo = input("View/edit " + viewdata["name"] + " (Y/N)? ").lower()
            if reallydo == "y":
                for i in viewconf:
                    tochange = input(viewdata["config"][i] + " [" + i + "]: " + str(viewconf[i]) + " ")
                    if tochange != "":
                        if isinstance(viewconf[i],int):
                            viewconf[i] = int(tochange)
                        elif isinstance(viewconf[i],bool):
                            viewconf[i] = tochange.lower() == "true"
                setasscrn = input("Set as current screensaver (Y/N)? ")
                reallydo2 = input("Save changes (Y/N)? ").lower()
                if reallydo2 == "y":
                    if viewdata["hasconfig"]:
                        with open(localfile(viewdata["codename"],"config.yaml"),"w") as f:
                            yaml.dump(viewconf,f)
                        print("Successfully written to file!\n")
                    if setasscrn == "y":
                        with open(localfile("globalconfig.yaml"),"w") as f:
                            yaml.dump({"cycle":[viewdata["codename"]],"screensaver":0},f)
                        print("Successfully set as screensaver!\n")
    elif option == 2:
        cycleqm = input("Would you like cycling screensavers? ").lower()
        printscrlist()
        if len(globalconf["cycle"]) > 1:
            scrarray = globalconf["cycle"]
            scrnames = []
            for scr in scrarray:
                scrnames.append(alldata[scr]["name"])
            print("Current screensavers: " + ", ".join(scrnames) + "\nPress ENTER to keep current screensavers.")
        else:
            print("Current screensaver: " + alldata[globalconf["cycle"][0]]["name"] + "\nPress ENTER to keep current screensaver.")
        if cycleqm == "y":
            newscr = input("What are the new screensaver's IDs (separated by commas)? ")
            if newscr != "":
                newscrlist = newscr.split(",")
                newscrcodes = []
                newscrnames = []
                c = 0
                for scr in newscrlist:
                    newscrlist[c] = scr = int(scr)
                    newscrname = sort[scr-1]
                    newscrcodes.append(newscrname)
                    newscrnames.append(alldata[newscrname]["name"])
                    c += 1
                reallydo = input("Change your screensavers to " + ", ".join(newscrnames) + " (Y/N)? ").lower()
                if reallydo == "y":
                    globalconf = {"cycle":newscrcodes,"screensaver":0}
                    with open(localfile("globalconfig.yaml"),"w") as f:
                        yaml.dump(globalconf,f)
                    print("Successfully set a cycling screensaver!\n")
        else:
            newscr = input("What is the new screensaver's ID? ")
            if newscr != "":
                newscrname = sort[int(newscr)-1]
                reallydo = input("Change your screensaver to " + alldata[newscrname]["name"] + " (Y/N)? ").lower()
                if reallydo == "y":
                    globalconf = {"cycle":[newscrname],"screensaver":0}
                    with open(localfile("globalconfig.yaml"),"w") as f:
                        yaml.dump(globalconf,f)
                    print("Successfully set as screensaver!\n")
    elif option == 3:
        print("\nCustom SS Information\n\nPath Installed In: " + parentpath + "\n\nCurrent Version: " + globaldata["version"] + "\nTitle: " + globaldata["vertitle"] + "\nDescription: " + globaldata["verdesc"] + "\nDate updated: " + globaldata["date"] + "\n")