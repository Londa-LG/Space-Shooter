import pygame

class Chaser:
    speed = 7

    def __init__(self,screen,target):
        self.target = target
        self.screen = screen
        self.surface = pygame.Surface((30,30))
        self.surface.fill("red")
        self.rect = self.surface.get_rect()

    def chase(self):
        # chase after self.target
        pass

    def display(self):
        self.screen.blit(self.surface, self.rect)

    def update(self):
        self.chase()
        self.display()

class Player:
    speed = 10

    def __init__(self,screen):
        self.screen = screen
        self.surface = pygame.Surface((60,60))
        self.surface.fill("orange")
        self.rect = self.surface.get_rect(midbottom =(300,300))

    def update(self):
        # Detect keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_s]:
            self.move_down()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_d]:
            self.move_right()

        self.display()

    def display(self):
        self.screen.blit(self.surface,self.rect)

    def move_left(self):
        self.rect.centerx -= self.speed
        
    def move_right(self):
        self.rect.centerx += self.speed

    def move_up(self):
        self.rect.centery -= self.speed
        
    def move_down(self):
        self.rect.centery += self.speed
        
