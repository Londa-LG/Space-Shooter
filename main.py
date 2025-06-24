import pygame
from characters import *
        

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Galactic wars")
clock = pygame.time.Clock()
running = True
dt = 0

p1 = Player(screen)
e2 = Shooter(screen,p1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    p1.update()
    e2.update()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


