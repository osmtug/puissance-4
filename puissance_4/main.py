import pygame
import os


pygame.init()

from game import Game



current_dir = os.path.dirname(__file__)
pygame.display.set_caption("puissance 4")
screen = pygame.display.set_mode((1080, 620))
clock = pygame.time.Clock()
running = True
dt = 0.0
gagner = False
joue_ia = False
equal = False
fondPath = os.path.join(current_dir, "fond.jpg")
logo = pygame.image.load(fondPath)
logo = pygame.transform.scale(logo, (1080,620))

game = Game(screen)  
velocite = 0.0



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    if gagner and not game.pion_tombe:
        pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = Game(screen)
                    gagner = False
                    equal = False
        if equal:
            game.win(screen,"equal")
        elif game.current_pion.color == "rouge":
            game.win(screen,"yellow")
        else :
            game.win(screen,"red")
    else : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type==pygame.KEYDOWN:
                if not game.pion_tombe:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_DOWN:
                        velocite = 0.0
                        gagner = game.lacher(screen)
                        
                        
        screen.fill(pygame.Color(255,244,113))
        screen.blit(logo,(0,0))


        game.current_pion.dessine(screen)
        for pion in game.all_pion:
            pion.dessine(screen)
            
            
        
        
        
            
        if game.pion_tombe:
            game.pion_lache.dessine(screen)
            game.pion_lache.pos_y+=velocite
            velocite+=0.6
            #pygame.time.delay(10)
            game.pion_lache.update_rect()
            if game.pion_lache.pos_y>screen.get_height()-40 or pygame.sprite.spritecollideany(game.pion_lache, game.all_pion):
                if velocite>0:
                    velocite = -velocite/3 +0.5
                    if velocite < -3:
                        fallSoundPath = os.path.join(current_dir, "pion.mp3")
                        pygame.mixer.Sound(fallSoundPath).play()
                    elif velocite < -0.5:
                        fallSoundPath = os.path.join(current_dir, "pion_petit.mp3")
                        pygame.mixer.Sound(fallSoundPath).play()
                
                if velocite < 0.5 and velocite >0:
                    game.pion_tombe = False
                    game.all_pion.add(game.pion_lache)
                
                
            
        game.plateau.dessine(screen)
        
        if not game.pion_tombe and not gagner:
            if not joue_ia or game.current_pion.color == "rouge":
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q] or keys[pygame.K_LEFT]:
                    game.current_pion.move_left(dt)
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    game.current_pion.move_right(dt,screen)
                if keys[pygame.K_o] and keys[pygame.K_s] and keys[pygame.K_m] and keys[pygame.K_a] and keys[pygame.K_n]:
                    velocite = 0.0
                    game.lacher(screen)
                    gagner = True
                if keys[pygame.K_p] :
                    if game.current_pion.color == "rouge":
                        game.change_pion(screen, "jaune")
                    else:
                        game.change_pion(screen, "rouge")
            else:
                gagner = game.joue(screen)
        if not gagner and not (0 in game.plateau.place_total[0] or 0 in game.plateau.place_total[1] or 0 in game.plateau.place_total[2] or 0 in game.plateau.place_total[3] or 0 in game.plateau.place_total[4] or 0 in game.plateau.place_total[5] ):
            gagner = True
            equal = True
            
        
    

    # flip() the display to put your work on screen
    pygame.display.flip()
    
    #limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()