import pygame
import os
pygame.init()
import random

from pygame.sprite import Group
from pion import Pion
from plateau import Plateau

class Game(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        couleur = random.randint(1,2)
        if couleur == 1:
            self.current_pion = Pion(screen,"rouge")
        else:
            self.current_pion = Pion(screen,"jaune")
        self.plateau = Plateau(screen)
        self.pion_tombe = False
        self.pion_lache = self.current_pion
        self.all_pion: Group = pygame.sprite.Group()
        
    def change_pion(self,screen,couleur):
        self.current_pion = Pion(screen,couleur)
        
    def win(self,screen,color):
        victoryScreenPath = os.path.join(os.path.dirname(__file__), f"{color}_victory.PNG")
        bg = pygame.image.load(victoryScreenPath)
        screen.blit(bg, (0,0))
        
        
    def lacher(self,screen):
        gagner = False
        if self.current_pion.pos_x>765:
            self.current_pion.pos_x = 807
            if self.plateau.place_total[0][6]==0:
                gagner = self.plateau.ajout_pion(6,self.current_pion.color)
                possible = True
            else:
                possible = False
                        
        elif self.current_pion.pos_x>680:
            self.current_pion.pos_x = 722
            if self.plateau.place_total[0][5]==0:
                gagner = self.plateau.ajout_pion(5,self.current_pion.color)
                possible = True
            else:
                possible = False
                                
        elif self.current_pion.pos_x>590:
            self.current_pion.pos_x = 637
            if self.plateau.place_total[0][4]==0:
                gagner = self.plateau.ajout_pion(4,self.current_pion.color)
                possible = True
            else:
                possible = False
                                
        elif self.current_pion.pos_x>508:
            self.current_pion.pos_x = 551
            if self.plateau.place_total[0][3]==0:
                gagner = self.plateau.ajout_pion(3,self.current_pion.color)
                possible = True
            else:
                possible = False
                                
        elif self.current_pion.pos_x>424:
            self.current_pion.pos_x = 467
            if self.plateau.place_total[0][2]==0:
                gagner = self.plateau.ajout_pion(2,self.current_pion.color)
                possible = True
            else:
                possible = False
                                
        elif self.current_pion.pos_x>336:
            self.current_pion.pos_x = 380
            if self.plateau.place_total[0][1]==0:
                gagner = self.plateau.ajout_pion(1,self.current_pion.color)
                possible = True
            else:
                possible = False
                                
        else :
            self.current_pion.pos_x = 295
            if self.plateau.place_total[0][0]==0:
                gagner = self.plateau.ajout_pion(0,self.current_pion.color)
                possible = True
            else:
                possible = False
                                
        if possible: 
            self.pion_lache = self.current_pion
            if self.current_pion.color == "rouge":
                self.change_pion(screen,"jaune")
            else :
                self.change_pion(screen,"rouge")
            self.pion_tombe = True
            buttonSoundPath = os.path.join(os.path.dirname(__file__), "button.mp3")
            pygame.mixer.Sound(buttonSoundPath).play()
        else:
            errorSoundPath = os.path.join(os.path.dirname(__file__), "error.mp3")
            pygame.mixer.Sound(errorSoundPath).play()
        return gagner
    
    
    
    def joue(self,screen):
        l = self.meilleur_coup()
        print("jouer")
        gagner = False
        if l == 0:
            self.current_pion.pos_x = 295
        elif l == 1:
            self.current_pion.pos_x = 380
        elif l == 2:
            self.current_pion.pos_x = 467
        elif l == 3:
            self.current_pion.pos_x = 551
        elif l == 4:
            self.current_pion.pos_x = 637
        elif l == 5:
            self.current_pion.pos_x = 722
        elif l == 6:
            self.current_pion.pos_x = 807
        gagner = self.lacher(screen)
        
        return gagner
    
    
    def meilleur_coup(self):
        place = self.plateau.place_total
        cptmax = 0
        ptsmax = 0
        jmax = 2
        
        
        for j in range (0,7):
            x=0
            
            pts = -1
            while x<5 and place[x][j] == 0:
                x+=1
            c = 2
            place[x-1][j] = 2
            
            csj = x-1
            lsj = j
            
            cpt = 0
            while lsj != 7 and place[csj][lsj] == c:
                cpt+=1
                lsj+=1
            lsj = j
            while lsj != -1 and place[csj][lsj] == c:
                cpt+=1
                lsj-=1
            cpt-=1
            lsj=j
            if cpt>=4:
                pts+=7
            elif cpt == 3:
                pts += 3
            cpt=0
            
            while csj!=6 and place[csj][lsj] == c:
                cpt+=1
                csj+=1
            csj = x-1
            
            while csj != -1 and place[csj][lsj] == c:
                cpt+=1
                csj-=1
            cpt-=1
            
            csj=x-1
            if cpt>=4:
                pts+=7
            elif cpt == 3:
                pts += 3
            cpt=0
            
            
            while lsj != 7 and csj != -1 and place[csj][lsj] == c:
                cpt+=1
                lsj+=1
                csj-=1
            
            lsj = j
            csj=x-1
            while lsj!=-1 and csj != 6 and place[csj][lsj] == c:
                cpt+=1
                lsj-=1
                csj+=1
            cpt-=1
            
            lsj=j
            csj=x-1
            if cpt>=4:
                pts+=7
            elif cpt == 3:
                pts += 3
            cpt = 0
            
            
            
            while lsj!=7 and csj != 6 and place[csj][lsj] == c:
                cpt+=1
                lsj+=1
                csj+=1
            lsj = j
            csj=x-1
            
            while lsj!=-1 and csj!=-1 and place[csj][lsj] == c:
                cpt+=1
                lsj-=1
                csj-=1
            cpt-=1
            
            lsj=j
            csj=x-1
            if cpt>=4:
                pts+=7
            elif cpt == 3:
                pts += 3
            cpt = 0
            
            for l in range (0,7):
                
                i=0
                cpt=0
                
                ls = l
                while i<5 and place[i][l] == 0:
                    i+=1
                i = i-1
                cs = i
                
                
                c=1
                place[cs][l] = 1
                
                
                while ls != 7 and place[cs][ls] == c:
                    cpt+=1
                    ls+=1
                ls = l
                while ls != -1 and place[cs][ls] == c:
                    cpt+=1
                    ls-=1
                cpt-=1
                ls=l
                if cpt>=4:
                    pts -= 4
                elif cpt == 3:
                    pts -= 2
                elif cpt> cptmax:
                    cptmax = cpt
                    
                    
                cpt=0
                
                while cs!=6 and place[cs][ls] == c:
                    cpt+=1
                    cs+=1
                cs = i
                
                while cs != -1 and place[cs][ls] == c:
                    cpt+=1
                    cs-=1
                cpt-=1
                
                cs=i
                if cpt>=4:
                    pts -= 4
                elif cpt == 3:
                    pts -= 2
                elif cpt> cptmax:
                    cptmax = cpt
                    
                cpt=0
                
                
                while ls != 7 and cs != -1 and place[cs][ls] == c:
                    cpt+=1
                    ls+=1
                    cs-=1
                
                ls = l
                cs=i
                while ls!=-1 and cs != 6 and place[cs][ls] == c:
                    cpt+=1
                    ls-=1
                    cs+=1
                cpt-=1
                
                ls=l
                cs=i
                if cpt>=4:
                    pts -= 4
                elif cpt == 3:
                    pts -= 2
                elif cpt> cptmax:
                    cptmax = cpt
                cpt = 0
                
                
                
                while ls!=7 and cs != 6 and place[cs][ls] == c:
                    cpt+=1
                    ls+=1
                    cs+=1
                ls = l
                cs=i
                
                while ls!=-1 and cs!=-1 and place[cs][ls] == c:
                    cpt+=1
                    ls-=1
                    cs-=1
                cpt-=1
                
                ls=l
                cs=i
                if cpt>=4:
                    pts -= 4
                elif cpt == 3:
                    pts -= 2
                elif cpt> cptmax:
                    cptmax = cpt
                place[cs][l] = 0
                
                
            place[x-1][j] = 0
            
            print (pts)
            if pts > ptsmax:
                ptsmax = pts
                jmax = j
                
        return jmax
        
            
            
        
        
        
        
    
            
        
