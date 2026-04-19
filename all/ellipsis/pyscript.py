import pygame,sys,yaml,os

if sys.executable.split("\\")[-1] != "python.exe":
    parentpath = os.path.dirname(os.path.dirname(sys.executable))
else:
    parentpath = os.path.dirname(os.path.dirname(__file__))

def localfile(path1,path2=None):
    if path2 == None:
        return os.path.join(parentpath,path1)
    else:
        return os.path.join(parentpath,path1,path2)

pygame.init()
screen = pygame.display.set_mode((1920,1100))
pygame.display.set_caption("Screensaver")
pygame.mouse.set_visible(False)

coords = [pygame.Rect(710,490,100,100),pygame.Rect(910,490,100,100),pygame.Rect(1110,490,100,100)]
colours = [[[(0,0,0),(51,51,51),(102,102,102),(153,153,153),(204,204,204),(255,255,255)],
[(0,0,0),(51,24,24),(102,48,48),(153,72,72),(204,96,96),(255,120,120)],
[(0,0,0),(51,33,0),(102,66,0),(153,99,0),(204,132,0),(255,165,0)],
[(0,0,0),(51,51,20),(102,102,40),(153,153,60),(204,204,80),(255,255,100)],
[(0,0,0),(0,40,0),(0,80,0),(0,120,0),(0,160,0),(0,200,0)],
[(0,0,0),(10,51,30),(20,102,60),(30,153,90),(40,204,120),(50,255,150)],
[(0,0,0),(0,20,40),(0,40,80),(0,60,120),(0,80,160),(0,100,200)],
[(0,0,0),(20,0,40),(40,0,80),(60,0,120),(80,0,160),(100,0,200)]],
[[(0,0,0),(17,17,17),(34,34,34),(51,51,51),(68,68,68),(85,85,85)],
[(0,0,0),(17,8,8),(34,16,16),(51,24,24),(68,32,32),(85,40,40)],
[(0,0,0),(17,11,0),(34,22,0),(51,33,0),(68,44,0),(85,55,0)],
[(0,0,0),(17,17,7),(34,34,14),(51,51,20),(68,68,27),(85,85,34)],
[(0,0,0),(0,14,0),(0,27,0),(0,40,0),(0,54,0),(0,67,0)],
[(0,0,0),(4,17,10),(7,34,20),(10,51,30),(14,68,40),(17,85,50)],
[(0,0,0),(0,7,14),(0,14,27),(0,20,40),(0,27,54),(0,34,67)],
[(0,0,0),(7,0,14),(14,0,27),(20,0,40),(27,0,54),(34,0,67)]]]

fps = pygame.time.Clock()
frame = 0
init = False
currentDot = 2
dotColour = [0,0,0]
dotDimming = [0,0,0]
setDimmed = 0
rainbow = False
dimFrames = 0

try:
    with open(localfile("ellipsis","config.yaml"),"r") as f:
        loadyaml = yaml.safe_load(f)
        readColour,readRainbow,readDimmed = loadyaml["colour"],loadyaml["rainbow"],loadyaml["dimmed"]
        dotColour[0] = dotColour[1] = dotColour[2] = int(readColour)
        rainbow = bool(int(readRainbow))
        if rainbow:
            dotColour[0] = dotColour[1] = dotColour[2] = 1
        setDimmed = dotDimming[0] = dotDimming[1] = dotDimming[2] = int(readDimmed)
except:
    pass


while True:
    if frame == 0:
        currentDot += 1
        if currentDot == 3:
            currentDot = 0
        if rainbow:
            dotColour[currentDot] = dotColour[currentDot-1]+1
            if dotColour[currentDot] == len(colours[0]):
                dotColour[currentDot] = 1
    if frame == 0:
        pygame.draw.rect(screen,colours[dotDimming[currentDot]][dotColour[currentDot]][1],coords[currentDot])
        pygame.draw.rect(screen,colours[dotDimming[currentDot-1]][dotColour[currentDot-1]][4],coords[currentDot-1])
        pygame.display.update([coords[currentDot],coords[currentDot-1]])
    elif frame == 1:
        pygame.draw.rect(screen,colours[dotDimming[currentDot]][dotColour[currentDot]][2],coords[currentDot])
        pygame.draw.rect(screen,colours[dotDimming[currentDot-1]][dotColour[currentDot-1]][3],coords[currentDot-1])
        pygame.display.update([coords[currentDot],coords[currentDot-1]])
    elif frame == 2:
        pygame.draw.rect(screen,colours[dotDimming[currentDot]][dotColour[currentDot]][3],coords[currentDot])
        pygame.draw.rect(screen,colours[dotDimming[currentDot-1]][dotColour[currentDot-1]][2],coords[currentDot-1])
        pygame.display.update([coords[currentDot],coords[currentDot-1]])
    elif frame == 3:
        pygame.draw.rect(screen,colours[dotDimming[currentDot]][dotColour[currentDot]][4],coords[currentDot])
        pygame.draw.rect(screen,colours[dotDimming[currentDot-1]][dotColour[currentDot-1]][1],coords[currentDot-1])
        pygame.display.update([coords[currentDot],coords[currentDot-1]])
    elif frame == 4:
        pygame.draw.rect(screen,colours[dotDimming[currentDot]][dotColour[currentDot]][5],coords[currentDot])
        pygame.draw.rect(screen,colours[dotDimming[currentDot-1]][dotColour[currentDot-1]][0],coords[currentDot-1])
        if not rainbow:
            dotColour[0] = dotColour[1] = dotColour[2] = dotColour[currentDot]
        dotDimming[0] = dotDimming[1] = dotDimming[2] = dotDimming[currentDot]
        pygame.display.update([coords[currentDot],coords[currentDot-1]])

    dotToAppend = currentDot+1
    if dotToAppend == 3:
        dotToAppend = 0

    for e in pygame.event.get():
        if e.type in (pygame.KEYDOWN,pygame.MOUSEMOTION) and init:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 2:
                dotDimming[dotToAppend] = setDimmed = int(not bool(dotDimming[currentDot]))
                dimFrames = 0
            elif e.button == 4:
                if rainbow:
                    rainbow = False
                    dotColour[dotToAppend] = len(colours[0])-1
                else:
                    dotColour[dotToAppend] -= 1
                    if dotColour[dotToAppend] == -1:
                        dotColour[dotToAppend] = 1
                        rainbow = True
            elif e.button == 5:
                if rainbow:
                    rainbow = False
                    dotColour[dotToAppend] = 0
                else:
                    dotColour[dotToAppend] += 1
                    if dotColour[dotToAppend] == len(colours[0]):
                        dotColour[dotToAppend] = 1
                        rainbow = True
            else:
                pygame.quit()
                sys.exit()
            with open(localfile("ellipsis","config.yaml"),"w+") as f:
                yaml.dump({"colour":dotColour[dotToAppend],"rainbow":rainbow,"dimmed":dotDimming[dotToAppend]},f)
    fps.tick(60)
    frame += 1
    dimFrames += 1
    if dimFrames == 108000:
        dotDimming[dotToAppend] = 1
    if frame == 60:
        frame = 0
    init = True