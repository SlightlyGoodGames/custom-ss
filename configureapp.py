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
            sort[thisdata["id"]] = i
            allids.update({thisdata["id"]:i})
            alldata.update({i:thisdata})
    else:
        alldata.update({i:{"id":-1,"name":i,"desc":"Description not given.","added":"Unknown version","config":{}}})
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

print("\nFound " + str(workingscrnsave) + " finished screensavers:\n")
for i in sort:
    if i != "ph":
        this = alldata[i]
        if this["id"] != -1:
            print("ID: " + str(this["id"]) + "\nName: " + this["name"] + " [" + i + "]\nDescription: " + this["desc"] + "\nAdded: " + this["added"] + "\n")
        else:
            print("Codename: " + this["name"] + "\nNo information has been added for this entry.\n")

while True:
    view = int(input("Enter the ID of what you would like to edit/view: "))
    try:
        viewdata = alldata[allids[view]]
    except KeyError:
        print("Invalid ID.")
    else:
        reallydo = input("View/edit " + viewdata["name"] + " (Y/N)? ").lower()
        if reallydo == "y":
            pass#do it