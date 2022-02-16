import pygame
import os

res = height, width = 1280, 720
WIN = pygame.display.set_mode(res)
pygame.display.set_caption("First Game!")
FPS = 60
spcres = spheight, spwidth = 55, 45
white = 255, 255, 255
black = 0, 0, 0
border = pygame.Rect(width-75, 0, 10, height)
VEL = 5

yellowspc = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
yellowspc = pygame.transform.rotate(pygame.transform.scale(yellowspc, (spcres)), 90)

redspc = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
redspc = pygame.transform.rotate(pygame.transform.scale(redspc, (spcres)), 270)

def drawin(red, yellow):
    WIN.fill(white)
    pygame.draw.rect(WIN, black, border)
    WIN.blit(yellowspc, (yellow.x, yellow.y))
    WIN.blit(redspc, (red.x, red.y))
    pygame.display.update()


def KWS(keyspressed, yellow, red):
    if keyspressed[pygame.K_RIGHT]: #right
        red.x += VEL
    if keyspressed[pygame.K_LEFT]: #left
        red.x -= VEL
    if keyspressed[pygame.K_UP]: #up
        red.y -= VEL
    if keyspressed[pygame.K_DOWN]: #down
        red.y += VEL
    if keyspressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if keyspressed[pygame.K_d] and yellow.x + VEL + yellow.width < border.x: #right
        yellow.x += VEL
    if keyspressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keyspressed[pygame.K_s] and yellow.y + VEL + yellow.height < height: #down
        yellow.y += VEL 


def main():
    yellow = pygame.Rect(350, 200, spheight, spwidth)
    red = pygame.Rect(1000, 200, spheight, spwidth)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keyspressed = pygame.key.get_pressed()
        KWS(keyspressed, yellow, red)


        drawin(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
