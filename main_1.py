import pygame
import pygame.mixer
from tkinter import *
from tkinter import messagebox as mb
pygame.init()
count = 0
lives = 3
flag = True
winner_flag = False 
#Class
class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img 
        self.rect = self.image.get_rect()       
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

#hide tkinter window
Tk().wm_withdraw()

#Main window
width = 800
height = 600
window = pygame.display.set_mode( (width, height) )
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
#spawn point
start_x = 8
start_y = 14


#Title
pygame.display.set_caption("Strenger")
#import photo

bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (width, height))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (32, 32))
wall_v = pygame.transform.scale(pygame.image.load("images/wall_v.png"), (8, 112))
wall_h = pygame.transform.scale(pygame.image.load("images/wall_h.png"), (112, 8))
enemy_img = pygame.transform.scale(pygame.image.load("images/enemy1.png"), (36, 36))
coin1_img = pygame.transform.scale(pygame.image.load("images/coin1.png"), (16, 16))
coin2_img = pygame.transform.scale(pygame.image.load("images/coin2.png"), (16, 16))
#creat Group object
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group() 
coins = pygame.sprite.Group() 

#creat object
player = Object(player_img, start_x, start_y, 3)
all_sprites.add(player)
#creat coins
coin1 = Object(coin1_img, 616, 200, 0)
coin2 = Object(coin1_img, 755, 200, 0)
coin3 = Object(coin1_img, 666, 500, 0)
coin4 = Object(coin1_img, 510, 32, 0)
coin5 = Object(coin1_img, 700, 72, 0)
coin6 = Object(coin1_img, 633, 334, 0)
coin7 = Object(coin1_img, 780, 678, 0)
coin8 = Object(coin1_img, 633, 734, 0)
coin9 = Object(coin1_img, 655, 566, 0)
coin10 = Object(coin1_img, 765, 632, 0)
coin11 = Object(coin1_img, 600, 555, 0)
#add to sprites
coins.add(coin1)
all_sprites.add(coin1)
coins.add(coin2)
all_sprites.add(coin2)
coins.add(coin3)
all_sprites.add(coin3)
coins.add(coin4)
all_sprites.add(coin4)
coins.add(coin5)
all_sprites.add(coin5)
coins.add(coin6)
all_sprites.add(coin6)
coins.add(coin7)
all_sprites.add(coin7)
coins.add(coin8)
all_sprites.add(coin8)
coins.add(coin9)
all_sprites.add(coin9)
coins.add(coin10)
all_sprites.add(coin10)
coins.add(coin11)
all_sprites.add(coin11)
#creat enemies
enemy1 = Object(enemy_img, 200, 36, 3)
enemy2 = Object(enemy_img, 200, 72, 3)
enemy3 = Object(enemy_img, 200, 236, 3)
enemy4 = Object(enemy_img, 200, 200, 3)
enemy5 = Object(enemy_img, 450, 36, 3)
enemy6 = Object(enemy_img, 450, 72, 3)
enemy7 = Object(enemy_img, 80, 352, 1)
#add to sprites
enemies.add(enemy1)
all_sprites.add(enemy1)
enemies.add(enemy2)
all_sprites.add(enemy2)
enemies.add(enemy3)
all_sprites.add(enemy3)
enemies.add(enemy4)
all_sprites.add(enemy4)
enemies.add(enemy5)
all_sprites.add(enemy5)
enemies.add(enemy6)
all_sprites.add(enemy6)
enemies.add(enemy7)
all_sprites.add(enemy7)
#create wall.
wall1 = Object(pygame.transform.scale(wall_h, (800, 8)), 0, 0, 0)
wall2 = Object(pygame.transform.scale(wall_v, (8, 600)),  0, 8, 0)
wall3 = Object(pygame.transform.scale(wall_h, (800, 8)), 0, 592, 0)
wall4 = Object(pygame.transform.scale(wall_v, (8, 600)),  792, 8, 0)
wall5 = Object(wall_v, 600, 532, 0)
wall6 = Object(pygame.transform.scale(wall_v, (8, 532)),  600, 8, 0)
# wall7 = Object(wall_h, 56, 96, 0)
# wall8 = Object(wall_h, 0, 144, 0)
# wall9 = Object(wall_h, 56, 196, 0)
# wall10 = Object(wall_h, 0, 244, 0)
# wall11 = Object(wall_h, 56, 292, 0)
# wall12 = Object(wall_h, 0, 340, 0)
# wall13 = Object(wall_h, 0, 388, 0)
# wall14 = Object(wall_h, 56, 436, 0)
# wall15 = Object(wall_h, 0, 484, 0)
# wall16 = Object(wall_h, 56, 532, 0)
#wall17 = Object(pygame.transform.scale(wall_h, (284, 8)), 164, 196, 0)
# wall18 = Object(pygame.transform.scale(wall_h, (300, 8)),  500, 196, 0)
# wall19 = Object(wall_h, 164, 292, 0)
#add to sprites
walls.add(wall1)
all_sprites.add(wall1)
walls.add(wall2)
all_sprites.add(wall2)
walls.add(wall3)
all_sprites.add(wall3)
walls.add(wall4)
all_sprites.add(wall4)
walls.add(wall5)
all_sprites.add(wall5)
walls.add(wall6)
all_sprites.add(wall6)
#walls.add(wall7)
#all_sprites.add(wall7)
# walls.add(wall8)
# all_sprites.add(wall8)
#walls.add(wall9)
#all_sprites.add(wall9)
# walls.add(wall10)
# all_sprites.add(wall10)
# walls.add(wall11)
# all_sprites.add(wall11)
# walls.add(wall12)
# all_sprites.add(wall12)
# walls.add(wall13)
# all_sprites.add(wall13)
# walls.add(wall14)
# all_sprites.add(wall14)
# walls.add(wall15)
# all_sprites.add(wall15)
# walls.add(wall16)
# all_sprites.add(wall16)
# walls.add(wall17)
#all_sprites.add(wall17)
# walls.add(wall18)
# all_sprites.add(wall18)
# walls.add(wall19)
# all_sprites.add(wall19)
run_game = True
danger_flag = False
mb.showinfo("Stranger", "Вы прошли 1-й уровень.Пройдите еще маленькое испытание и получите доступ в сокровищницу!")
while run_game:
    if lives != 0:
        window.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        counter_font = pygame.font.Font(None, 36)
        counter = counter_font.render("Count: " + str(count), True,
                    (180, 0, 0))
        #lives            
        lives_font = pygame.font.Font(None, 36)
        lives_count = lives_font.render("Lives: " + str(lives), True,
                    (180, 39, 0))
        keys = pygame.key.get_pressed()
        if flag:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    player.rect.y -= player.speed
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    player.rect.y += player.speed
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    player.rect.x += player.speed
                    player.image = pygame.transform.flip(player_img, True, False)
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    player.image = pygame.transform.flip(player_img, False, False)
                    player.rect.x -= player.speed
        enemy1.rect.x += enemy1.speed
        enemy2.rect.x += enemy2.speed
        enemy3.rect.x += enemy3.speed
        enemy4.rect.x += enemy4.speed
        enemy5.rect.x += enemy5.speed
        enemy6.rect.x += enemy6.speed
        enemy7.rect.x += enemy7.speed

        if len(pygame.sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = start_x
            player.rect.y = start_y
            lives -= 1
        if len(pygame.sprite.spritecollide(enemy1, walls, False)) > 0:
            enemy1.speed *= -1
        if len(pygame.sprite.spritecollide(enemy2, walls, False)) > 0:
            enemy2.speed *= -1
        if len(pygame.sprite.spritecollide(enemy3, walls, False)) > 0:
            enemy3.speed *= -1
        if len(pygame.sprite.spritecollide(enemy4, walls, False)) > 0:
            enemy4.speed *= -1
        if len(pygame.sprite.spritecollide(enemy5, walls, False)) > 0:
            enemy5.speed *= -1
        if len(pygame.sprite.spritecollide(enemy6, walls, False)) > 0:
            enemy6.speed *= -1
        if len(pygame.sprite.spritecollide(enemy7, walls, False)) > 0:
            enemy7.speed *= -1

        if len(pygame.sprite.spritecollide(player, enemies, False)) > 0:
            player.rect.x = start_x
            player.rect.y = start_y
            lives -= 1
        if len(pygame.sprite.spritecollide(player, coins, True)) > 0:
            count += 1
            print(count)
        all_sprites.draw(window)
        all_sprites.update()

        window.blit(counter, (10, 570))
        window.blit(lives_count, (600, 570))
        pygame.display.update()
    else:
        
        mb.showerror("Message", "YOU LOOOOOOOOOOOOOOOOOOOOOOOOOSE!!!")
        break
    if lives == 1 and not(danger_flag):
        mb.showwarning("Message", "You have 1 live, danger!")
        danger_flag = True
    if count == 1:
        walls.remove(wall5)
        all_sprites.remove(wall5)
    if count == 2 and not(winner_flag):
        mb.showinfo("Message", "YOU WIIIIIIIIIIIIIIIIIIIIIIIIN!!!")
        winner_flag = True
    if count == 8:
        break
