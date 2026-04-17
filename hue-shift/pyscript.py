import pygame,sys

if len(sys.argv) > 1:
    if sys.argv[1].lower().startswith("/c"):
        sys.exit()

pygame.init()
screen = pygame.display.set_mode((1920,1100))

colours = [[(255,120,120),(255,129,96),(255,138,72),(255,147,48),(255,156,24)],
[(255,165,0),(255,183,20),(255,201,40),(255,219,60),(255,237,80)],
[(255,255,100),(204,244,80),(153,233,60),(102,222,40),(51,211,20)],
[(0,200,0),(10,211,30),(20,222,60),(30,233,90),(40,244,120)],
[(50,255,150),(40,224,160),(30,193,170),(40,162,180),(50,131,190)],
[(0,100,200),(20,80,200),(40,60,200),(60,40,200),(80,20,200)],
[(100,0,200),(131,24,184),(162,48,168),(193,72,152),(224,96,136)]]
currentColour = 6
frame = 0

fps = pygame.time.Clock()
init = False

pygame.display.set_caption("Screensaver")
pygame.mouse.set_visible(False)

while True:
    if frame == 0:
        screen.fill(colours[currentColour][1])
        pygame.display.flip()
    elif frame == 4:
        screen.fill(colours[currentColour][2])
        pygame.display.flip()
    elif frame == 8:
        screen.fill(colours[currentColour][3])
        pygame.display.flip()
    elif frame == 12:
        screen.fill(colours[currentColour][4])
        pygame.display.flip()
    elif frame == 16:
        currentColour += 1
        if currentColour == len(colours):
            currentColour = 0
        screen.fill(colours[currentColour][0])
        pygame.display.flip()
    for e in pygame.event.get():
        if e.type in (pygame.KEYDOWN,pygame.MOUSEBUTTONDOWN,pygame.MOUSEMOTION) and init:
            pygame.quit()
            sys.exit()
    fps.tick(60)
    frame += 1
    if frame == 60:
        frame = 0
    init = True