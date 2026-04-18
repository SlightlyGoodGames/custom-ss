import pygame,sys,random,yaml,os

pygame.init()
screen = pygame.display.set_mode((1920,1100))
pygame.display.set_caption("Screensaver")
pygame.mouse.set_visible(False)

frame = 0
init = False
fps = pygame.time.Clock()

dimmed = False
currentcolour = 0
rainbow = False

todim = False
tocolour = 0

if os.path.exists("C:/Screensavers/col-squares/config.yaml"):
    with open("C:/Screensavers/col-squares/config.yaml","r") as f:
        loadyaml = yaml.safe_load(f)
        dimmed,currentcolour,rainbow = loadyaml["dimmed"],loadyaml["colour"],loadyaml["rainbow"]
        todim,tocolour = dimmed,currentcolour

def dividecol(col,num):
    return (int(col[0]*num),int(col[1]*num),int(col[2]*num))

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
currentcoords = pygame.Rect(random.randint(10,1610),random.randint(10,770),300,300)

while True:
    for e in pygame.event.get():
        if e.type in (pygame.KEYDOWN,pygame.MOUSEMOTION) and init:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 2:
                todim = not todim
            elif e.button == 4:
                if rainbow:
                    tocolour = len(colours[0])-1
                    rainbow = False
                else:
                    tocolour -= 1
                    if tocolour == -1:
                        tocolour = 1
                        rainbow = True
            elif e.button == 5:
                if rainbow:
                    tocolour = 0
                    rainbow = False
                else:
                    tocolour += 1
                    if tocolour == len(colours[0]):
                        tocolour = 1
                        rainbow = True
            with open("C:/Screensavers/col-squares/config.yaml","w+") as f:
                yaml.dump({"colour":tocolour,"dimmed":todim,"rainbow":rainbow},f)
    if frame > -1 and frame < 41:
        pygame.draw.rect(screen,dividecol(colours[dimmed][currentcolour][5],frame/40),currentcoords)
        pygame.display.update(currentcoords)
    elif frame > 149 and frame < 191:
        pygame.draw.rect(screen,dividecol(colours[dimmed][currentcolour][5],(-frame+190)/40),currentcoords)
        pygame.display.update(currentcoords)
    elif frame == 257:
        currentcoords = pygame.Rect(random.randint(10,1610),random.randint(10,770),300,300)
        dimmed = todim
        if not rainbow:
            currentcolour = tocolour
        if rainbow:
            currentcolour += 1
            if currentcolour == len(colours[0]):
                currentcolour = 1
    fps.tick(60)
    frame += 1
    if frame == 300:
        frame = 0
    init = True