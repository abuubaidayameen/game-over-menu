


import pygame
import button

pygame.init()


#recreate the width
SCREEN_WIDTH = 800
SCREEN_HEIGHT=600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("main menu")

#define varialble
game_paused=False
menu_state="main"
# define font
font= pygame.font.sysfont("arialblack",40)

#define colour
TEXT_COL =(255,255,255)


#load button image:
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
option_img =  pygame.image.load("images/button_option.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
audio_img = pygame.image.load("images/button_audio.png").convert_alpha()
key_img = pygame.image.load("images/button_key.png").convert_alpha()
back_img = pygame.image.load("images/button_back.png").convert_alpha()

#create the button instances:
resume_button = button.Button(304,125,resume_img,1)
option_button = button.Button(297,250,option_img,1)
quit_button = button.Button(336,375,quit_img,1)
quit_button = button.Button(336,375,quit_img,1)
audio_button = button.Button(225,200,audio_img,1)
key_button = button.Button(246,325,key_img,1)
back_button = button.Button(336,450,back_img,1)

def draw_text(text,font,text_col,x,y):
    img= font.render(text,True,text_col)
    screen.blit(img,(x,y))
    
    #game loop
    run=True
    while run :
        screen.fill((52, 78,91))
        
#check if game is paused
if game_paused == True:
    #chechk menu state
    if menu_state == "main":
#draw pause screen buttons
     if resume_button.draw(screen):
       game_paused = False
if option_button.draw(screen):
     pass
if quit_button.draw(screen):
    run  = False
#check if the option menu is open
 #if menu_state == "options":
#draw the different option buttons
if audio_button.draw(screen):
    print("audio settings")
if key_button.draw(screen):
    print("key settings")
if back_button.draw(screen):
    print("back")
else:
   draw_text("press space to pause",font,TEXT_COL,160,250)  
 #event handler:
for event in pygame.event.get():
 if event.type== pygame.KEYDOWN:
     if event.key == pygame.K_SPACE:
         print("pause")      
 if event.type== pygame.QUIT:
                run=False
                
pygame.display.update()

pygame.quit()