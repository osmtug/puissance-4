import pygame
pygame.init()

class Pion(pygame.sprite.Sprite):
    def __init__(self, screen,color):
        super().__init__()
        self.pos_x = screen.get_width() / 2
        self.pos_y = 70.0
        self.color = color
        self.rect = pygame.Rect(self.pos_x-40, self.pos_y-40, 40, 40)
        self.image = pygame.image.load(f"pion_{color}.xcf")
        self.image = pygame.transform.scale(self.image, (80,80))
        #self.score = {
         #   "horizontale" : 0,
          #  "vertical" : 0,
           # "diagonal_h" : 0,
            #"diagonal_b" : 0}
        
    def move_right(self,dt,screen):
        if self.pos_x<screen.get_width()-250:
            self.pos_x += 400 * dt
        
    def move_left(self,dt):
        if self.pos_x>250:
            self.pos_x -= 400 * dt
            
    def update_rect(self):
        self.rect = pygame.Rect(self.pos_x-40, self.pos_y-40, 15, 82)
        
    def dessine(self,screen):
        #pygame.draw.circle(screen, "red", (self.pos_x, self.pos_y), 30)
        screen.blit(self.image, (self.pos_x-50,self.pos_y-50))
        