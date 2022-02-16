# Your header should go here, each comment should be initialed -DK
import pygame, sys

# pygame.init()
FPS = 60

# Useful Variables
size = height, width = 900, 500
white = 255, 255, 255
zonhw = zheight, zwidth = 70, 70
VEL = 5
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zonic bootleg")
lscale = lheight, lwidth = 80, 80
# beamsz = 60, 40

# graphics
zonic = pygame.image.load("zonic.gif")
zonic = pygame.transform.scale(zonic, zonhw)
bg = pygame.image.load("sonic-back.jpg")
bg = pygame.transform.scale(bg, size)
lazerz = pygame.image.load("Lazerz.gif")
lazerz = pygame.transform.scale(lazerz, lscale)
# beam = pygame.image.load("laserbeam.jpg").convert_alpha()
# beam = pygame.transform.scale(beam, beamsz)


# def bullet(x,y):


# draw
def drawingfunc(zonicrect, lazerect):
    # screen.fill(white)
    screen.blit(bg, (0, 0))
    screen.blit(zonic, (zonicrect.x, zonicrect.y))
    # screen.blit(beam, (lazerect.x - 2, lazerect.y - 2))
    screen.blit(lazerz, (lazerect.x, lazerect.y))
    pygame.display.update()


# zonic movement
def KWS(keyvar, zonicrect):
    if keyvar[pygame.K_RIGHT]:  # right
        zonicrect.x += VEL

    if keyvar[pygame.K_LEFT] and zonicrect.x + VEL > 0:  # left
        zonicrect.x -= VEL

    # mainloop and refresh rate (also includes gravity jump)


def main():
    jump = False
    jumpCount = 0
    jumpMax = 15
    zonicrect = pygame.Rect(10, 250, zheight, zwidth)
    lazerect = pygame.Rect(500, 250, lheight, lwidth)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if not jump and event.key == pygame.K_SPACE:
                    jump = True
                    jumpCount = jumpMax
        drawingfunc(zonicrect, lazerect)
        keyspressed = pygame.key.get_pressed()
        KWS(keyspressed, zonicrect)
        if jump:
            zonicrect.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False
    pygame.quit()


# calling function NOTE: needs to always be at the end of file
if __name__ == "__main__":
    main()