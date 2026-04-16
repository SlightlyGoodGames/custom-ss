import pygame,sys

if len(sys.argv) > 1:
    if sys.argv[1].lower().startswith("/c"):
        sys.exit()

pygame.init()
screen = pygame.display.set_mode((1920,1100))
pygame.display.set_caption("Screensaver")
pygame.mouse.set_visible(False)

init = False
frame = 0
dimframes = 0
colours = [[(255,120,120),(255,165,0),(255,255,100),(0,200,0),(50,255,150),(0,100,200),(100,0,200)],
[(85,40,40),(85,55,0),(85,85,33),(0,67,0),(17,85,50),(0,33,67),(33,0,67)]]
currentColour = 0
direction = 0

sizex = 200
sizey = 200

dimmed = 0
todim = 0
wasdimmed = 0

try:
    with open("C:/Screensavers/cube/.config","r") as f:
        readsizex,readsizey,readdimmed = f.read().split(",")
        sizex,sizey,dimmed,todim = int(readsizex),int(readsizey),int(readdimmed),int(readdimmed)
except:
    pass

fps = pygame.time.Clock()

screen.fill((0,0,0))
pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540-(sizey/2),sizex,sizey))
pygame.display.update(pygame.Rect(960-(sizex/2),540-(sizey/2),sizex,sizey))

while True:
    if direction == 0:
        if frame == 0:
            dimmed = todim
            currentColour += 1
            if currentColour == len(colours[0]):
                currentColour = 0

            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-5/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-5/10),sizex,sizey/10))
        elif frame == 1:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-4/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-4/10),sizex,sizey/10))
        elif frame == 2:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-3/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-3/10),sizex,sizey/10))
        elif frame == 3:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-2/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-2/10),sizex,sizey/10))
        elif frame == 4:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-1/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-1/10),sizex,sizey/10))
        elif frame == 5:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*0/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*0/10),sizex,sizey/10))
        elif frame == 6:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*1/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*1/10),sizex,sizey/10))
        elif frame == 7:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*2/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*2/10),sizex,sizey/10))
        elif frame == 8:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*3/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*3/10),sizex,sizey/10))
        elif frame == 9:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*4/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*4/10),sizex,sizey/10))
            direction = 1
    elif direction == 1:
        if frame == 0:
            dimmed = todim
            currentColour += 1
            if currentColour == len(colours[0]):
                currentColour = 0

            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*4/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*4/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 1:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*3/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*3/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 2:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*2/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*2/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 3:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*1/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*1/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 4:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*0/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*0/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 5:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-1/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-1/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 6:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-2/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-2/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 7:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-3/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-3/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 8:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-4/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-4/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 9:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-5/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-5/10),540-(sizey/2),sizex/10,sizey))
            direction = 2
    elif direction == 2:
        if frame == 0:
            dimmed = todim
            currentColour += 1
            if currentColour == len(colours[0]):
                currentColour = 0

            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*4/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*4/10),sizex,sizey/10))
        elif frame == 1:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*3/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*3/10),sizex,sizey/10))
        elif frame == 2:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*2/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*2/10),sizex,sizey/10))
        elif frame == 3:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*1/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*1/10),sizex,sizey/10))
        elif frame == 4:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*0/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*0/10),sizex,sizey/10))
        elif frame == 5:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-1/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-1/10),sizex,sizey/10))
        elif frame == 6:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-2/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-2/10),sizex,sizey/10))
        elif frame == 7:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-3/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-3/10),sizex,sizey/10))
        elif frame == 8:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-4/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-4/10),sizex,sizey/10))
        elif frame == 9:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960-(sizex/2),540+(sizey*-5/10),sizex,sizey/10))
            pygame.display.update(pygame.Rect(960-(sizex/2),540+(sizey*-5/10),sizex,sizey/10))
            direction = 3
    elif direction == 3:
        if frame == 0:
            dimmed = todim
            currentColour += 1
            if currentColour == len(colours[0]):
                currentColour = 0

            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-5/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-5/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 1:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-4/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-4/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 2:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-3/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-3/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 3:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-2/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-2/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 4:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*-1/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*-1/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 5:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*0/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*0/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 6:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*1/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*1/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 7:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*2/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*2/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 8:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*3/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*3/10),540-(sizey/2),sizex/10,sizey))
        elif frame == 9:
            pygame.draw.rect(screen,colours[dimmed][currentColour],pygame.Rect(960+(sizex*4/10),540-(sizey/2),sizex/10,sizey))
            pygame.display.update(pygame.Rect(960+(sizex*4/10),540-(sizey/2),sizex/10,sizey))
            direction = 0
    for e in pygame.event.get():
        if e.type in (pygame.KEYDOWN,pygame.MOUSEMOTION) and init:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 2:
                wasdimmed = todim = int(not bool(todim))
                dimframes = 0
            elif e.button == 4:
                nsizex = sizex-10
                nsizey = sizey-10
                if not bool(wasdimmed):
                    todim = 0
                    dimframes = 0
            elif e.button == 5:
                nsizex = sizex+10
                nsizey = sizey+10
                if not bool(wasdimmed):
                    todim = 0
                    dimframes = 0
            else:
                pygame.quit()
                sys.exit()
            try:
                toprint = pygame.transform.scale(screen.subsurface(pygame.Rect(960-(sizex/2),540-(sizey/2),sizex,sizey)),(nsizex,nsizey))
            except:
                if e.button == 4:
                    sizex -= 10
                    sizey -= 10
                    toprint = pygame.transform.scale(screen.subsurface(pygame.Rect(960-(sizex/2),540-(sizey/2),sizex,sizey)),(1070,1070))
                    screen.fill((0,0,0))
                    screen.blit(toprint,(960-(sizex/2),540-(sizey/2)))
                    pygame.display.update(pygame.Rect(960-(sizex/2),540-(sizey/2),1070,1070))
            else:
                sizex,sizey = nsizex,nsizey
                screen.fill((0,0,0))
                screen.blit(toprint,(960-(sizex/2),540-(sizey/2)))
                pygame.display.update(pygame.Rect(960-(sizex/2),540-(sizey/2),sizex,sizey))
            with open("C:/Screensavers/cube/.config","w+") as f:
                f.write(str(sizex)+","+str(sizey)+","+str(wasdimmed))
    init = True
    frame += 1
    if frame == 60:
        frame = 0
    dimframes += 1
    if dimframes == 108000:
        wasdimmed = todim
        todim = 1
    fps.tick(60)