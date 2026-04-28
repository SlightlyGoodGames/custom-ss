import pygame,sys,os,yaml

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

init = False
fps = pygame.time.Clock()
frame = 0

with open(localfile("image/config.yaml"),"r") as f:
    loadyaml = yaml.safe_load(f)
    try:
        image = pygame.image.load(loadyaml["imgpath"])
    except:
        image = pygame.image.load(localfile("image/assets/placeholder.png"))
screen.blit(image,(0,0))
pygame.display.flip()
while True:
    for e in pygame.event.get():
        if e.type in (pygame.MOUSEMOTION,pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN,pygame.QUIT) and init:
            pygame.quit()
            sys.exit()
    if frame == 180:
        frame = 0
        pygame.display.update(pygame.Rect(0,0,1,1))
    frame += 1
    fps.tick(60)
    init = True