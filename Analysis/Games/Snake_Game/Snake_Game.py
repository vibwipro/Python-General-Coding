import pygame, sys

pygame.init()

win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Pygame")

x = 50
y = 50
width = 40
hight = 60
velocity = 10

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x == 0:
                print('GameOver')
                pygame.QUIT()
                sys.exit()
            x -= velocity

        if keys[pygame.K_RIGHT]:
            if x == 360:
                print('GameOver')
                pygame.QUIT()
                sys.exit()
            x += velocity

        if keys[pygame.K_UP]:
            if y == 0:
                print('GameOver')
                pygame.QUIT()
                sys.exit()
            y -= velocity

        if keys[pygame.K_DOWN]:
            if y == 340:
                print('GameOver')
                pygame.QUIT()
                sys.exit()
            y += velocity

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0, 255, 0), (x, y, width, hight))
        pygame.display.update()

pygame.quit()