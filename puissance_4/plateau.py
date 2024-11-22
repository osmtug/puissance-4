import pygame
import os
pygame.init()
from typing import List

class Plateau(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.place_total: List[List[int]] = [[],[],[],[],[],[]]
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "plateau.xcf"))
        self.image = pygame.transform.scale(self.image, (screen.get_width()*6 / 8 -200,screen.get_height()*4 / 5))
        
        for i in range(6):
            self.place_total[i] = [0,0,0,0,0,0,0]
            
    def dessine(self, screen):
        screen.blit(self.image, (screen.get_width() // 8+100, screen.get_height() // 5))
                
    def ajout_pion(self, l,color):
        i=0
        cpt=0
        ls = l
        gagner = False
        while i<=5 and self.place_total[i][l] == 0:
            i+=1
        cs = i-1
        if color == "rouge":
            c = 1
        else :
            c=2
        self.place_total[cs][l] = c

        while ls != 7 and self.place_total[cs][ls] == c:
            cpt+=1
            ls+=1
        ls = l
        while ls != -1 and self.place_total[cs][ls] == c:
            cpt+=1
            ls-=1
        cpt-=1
        ls=l
        if cpt>=4:
            gagner = True
        cpt=0
        
        while cs!=6 and self.place_total[cs][ls] == c:
            cpt+=1
            cs+=1
        cs = i-1
        
        while cs != -1 and self.place_total[cs][ls] == c:
            cpt+=1
            cs-=1
        cpt-=1
        
        cs=i-1
        if cpt>=4:
            gagner = True
        cpt=0
        
        
        while ls != 7 and cs != -1 and self.place_total[cs][ls] == c:
            cpt+=1
            ls+=1
            cs-=1
        
        ls = l
        cs=i-1
        while ls!=-1 and cs != 6 and self.place_total[cs][ls] == c:
            cpt+=1
            ls-=1
            cs+=1
        cpt-=1
        
        ls=l
        cs=i-1
        if cpt>=4:
            gagner = True
        cpt = 0
        
        
        
        while ls!=7 and cs != 6 and self.place_total[cs][ls] == c:
            cpt+=1
            ls+=1
            cs+=1
        ls = l
        cs=i-1
        
        while ls!=-1 and cs!=-1 and self.place_total[cs][ls] == c:
            cpt+=1
            ls-=1
            cs-=1
        cpt-=1
        
        ls=l
        cs=i-1
        if cpt>=4:
            gagner = True
        cpt = 0
        
        return gagner
        
        
        
        
            
        
        
            
            
        
        