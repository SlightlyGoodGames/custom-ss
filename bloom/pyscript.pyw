import pygame,sys,random

if len(sys.argv) > 1:
    if sys.argv[1].lower().startswith("/c"):
        sys.exit()

pygame.init()
screen = pygame.display.set_mode((1920,1100))
pygame.display.set_caption("Screensaver")
pygame.mouse.set_visible(False)

init = False

allblocks = []
amount = 15

bellcurve = [1,4,9,16,21,24,25]

fps = pygame.time.Clock()
frame = 0

def generateblocks():
    allblocks = []
    allpos = []
    for _ in range(amount):
        size = 15
        pos = [random.randint(1,192-size),random.randint(1,108-size)]
        if pos not in allpos:
            allblocks.append(pygame.Rect(pos[0]*10,pos[1]*10,size*10,size*10))
    return allblocks

while True:
    if frame == 0:
        screen.fill((0,0,0))
        collisions = []
        realblocks = []

        allblocks = generateblocks()
        c = 0
        for i in allblocks:
            realblock = pygame.Rect(i.x,i.y,int(i.w/bellcurve[frame]),int(i.h/bellcurve[frame]))
            realblocks.append(realblock)
            pygame.draw.rect(screen,(255,255,255),realblock)
            for i2 in allblocks[c+1:]:
                posscoll = i.clip(i2)
                if posscoll.height > 0:
                    collisions.append(posscoll)
            c += 1
        for i in collisions:
            pygame.draw.rect(screen,(255,0,0),i)
        pygame.display.update()
    elif 0 < frame < 7:
        collisions = []

        allblocks = generateblocks()
        realblocks = []
        c = 0
        for i in allblocks:
            realblock = pygame.Rect(i.x,i.y,int(i.w/bellcurve[frame]),int(i.h/bellcurve[frame]))
            realblocks.append(realblock)
            pygame.draw.rect(screen,(255,255,255),realblock)
            for i2 in allblocks[c+1:]:
                posscoll = i.clip(i2)
                if posscoll.height > 0:
                    collisions.append(posscoll)
            c += 1
        for i in collisions:
            pygame.draw.rect(screen,(255,0,0),i)
        pygame.display.update()
    for e in pygame.event.get():
        if e.type in (pygame.KEYDOWN,pygame.MOUSEMOTION,pygame.MOUSEBUTTONDOWN) and init:
            pygame.quit()
            sys.exit()
    init = True
    fps.tick(60)
    frame += 1
    if frame == 60:
        frame = 0