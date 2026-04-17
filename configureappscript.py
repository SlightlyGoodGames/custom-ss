import yaml,os

print("Welcome to the Custom SS configuration.\nRetrieving information...")
allfolders = [f for f in os.listdir("C:/Screensavers") if not os.path.isfile("C:/Screensavers/"+f) and f != ".git"]

alldata = {}
allconf = {}
allids = {}
sort = []

for i in range(len(allfolders)):
    sort.append("ph")

for i in allfolders:
    if os.path.exists("C:/Screensavers/"+i+"/info.yaml"):
        with open("C:/Screensavers/"+i+"/info.yaml") as f:
            thisdata = yaml.safe_load(f)
            sort[thisdata["id"]-1] = i
            allids.update({thisdata["id"]:i})
            alldata.update({i:thisdata})
    else:
        alldata.update({i:{"id":-1,"name":i,"codename":i,"desc":"Description not given.","added":"Unknown version","complete":False,"hasconfig":False,"config":{}}})
    if os.path.exists("C:/Screensavers/"+i+"/config.yaml"):
        with open("C:/Screensavers/"+i+"/config.yaml") as f:
            thisdata = yaml.safe_load(f)
            allconf.update({i:thisdata})
    else:
        allconf.update({i:{}})

workingscrnsave = 0

for i in sort:
    if i != "ph":
        workingscrnsave += 1

print("\nFound " + str(workingscrnsave) + " screensavers:\n")
for i in sort:
    if i != "ph":
        this = alldata[i]
        if this["id"] != -1:
            print("ID: " + str(this["id"]) + "\nName: " + this["name"] + " [" + i + "]\nDescription: " + this["desc"] + "\nAdded: " + this["added"] + "\nComplete: " + str(this["complete"]) + "\n")
        else:
            print("Codename: " + this["name"] + "\nNo information has been added for this entry.\n")

while True:
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
                    with open("C:/Screensavers/" + viewdata["codename"] + "/config.yaml","w") as f:
                        yaml.dump(viewconf,f)
                    print("Successfully written to file!")
                if setasscrn == "y":
                    with open("C:/Screensavers/globalconfig.yaml","w") as f:
                        yaml.dump({"screensaver":viewdata["codename"]},f)
                    print("Successfully set as screensaver!")