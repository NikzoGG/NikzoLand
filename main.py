import pygame
from sfx_and_music import startbackgroundmusic, stopbackgroundmusic
from console import gamestarted
from movement import left_movement, right_movement, dibeliq_movement
from game_rules import boundaries, boundaries2

#To do
#da se naprai enemitata da se dvijat(feature) - utre
#start coding a platformer game where there are some enemies,different levels,use classes,and the player has to escape traps
#and spikes and go through all the levels.Also add multiplayer(goal)
#or make a multiplayer fighting game something like brawlhalla


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('nik')
clock = pygame.time.Clock()
#defining player
player = pygame.image.load('assets/graphics/player.png')
player_rect = player.get_rect(midbottom=(30, 640))
#defining ground
ground = pygame.image.load('assets/graphics/ground.jpg')
ground_rect = ground.get_rect(midbottom=(640, 1350))
#defining dibeliq
dibeliq = pygame.image.load('assets/graphics/dibeliq.png')
dibeliq_rect = dibeliq.get_rect(midbottom=(-10, 300))
#defining sky
sky = pygame.image.load('assets/graphics/sky.jpg')
sky_rect = sky.get_rect(midbottom=(640, 650))
#variables
score = 0
hidecoin1 = False
hidecoin2 = False
hidecoin3 = False
hidecoin4 = False
hidecoin5 = False
player_gravity = 0
on_platform = False
showbutton1 = False
magic_ability = False
player_health = 100
enemy1_health = 100
enemy2_health = 100
deadenemy1 = False
deadenemy2 = False
deadplayer = False
holdingpotion = False
showkilltext = False
showenoughtext = False
showhavetext = False
timer = 0
timer12 = 0
timer2 = 0
timer3 = 0
startbackgroundmusic()
gamestarted()


#defining magic ability
magicpotion = pygame.image.load('assets/graphics/magicpotion.png')
magicpotion_rect = magicpotion.get_rect(midbottom=(10000,10000))


#defining enough coins image text
enoughcoins = pygame.image.load('assets/graphics/enoughcoins.png')
enoughcoins_rect = enoughcoins.get_rect(midbottom=(500,700))


#defining haveability image text
haveability = pygame.image.load('assets/graphics/haveability.png')
haveability_rect = haveability.get_rect(midbottom=(100,500))


#defining kill image text
killtext = pygame.image.load('assets/graphics/killtext.png')
killtext_rect = killtext.get_rect(midbottom=(700,200))


#defining enemies
enemy1 = pygame.image.load('assets/graphics/enemies/enemy1.png')
enemy1_rect = enemy1.get_rect(midbottom=(1200,640))
enemy2 = pygame.image.load('assets/graphics/enemies/enemy2.png')
enemy2_rect = enemy1.get_rect(midbottom=(900,640))

#rendering text and choosing font
text_font = pygame.font.Font('assets/fonts/Soultimate.otf',60)
text_font2 = pygame.font.Font('assets/fonts/font2.otf',50)
text_font3 = pygame.font.Font('assets/fonts/font3.ttf',40)
text_font4 = pygame.font.Font('assets/fonts/font4.ttf',100)
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_platform == True:
                player_gravity = -23
            #ako e natisnato q i ima magic ability i dokosva enemy to enemy gubi 18health
            if event.key == pygame.K_q and magic_ability == True and player_rect.colliderect(enemy1_rect) and holdingpotion == True:
                enemy1_health -= 18
            #ako e natisnato q i ima magic ability i dokosva enemy to enemy2 gubi 18health
            if event.key == pygame.K_q and magic_ability == True and player_rect.colliderect(enemy2_rect) and holdingpotion == True:
                enemy2_health -= 18
    #main loop (tuk pishem pochti vsichkiq kod)
    keys = pygame.key.get_pressed()
    left_movement(player_rect)
    right_movement(player_rect)
    dibeliq_movement(dibeliq_rect)
    boundaries(player_rect)
    boundaries2(player_rect)


    #defining traps
    trap1 = pygame.image.load('assets/graphics/trap1.png')
    trap1_rect = trap1.get_rect(midbottom=(430,640))


    

    #maintaince the kill image text
    if showkilltext == False:
        killtext_rect.x = 10000
        killtext_rect.y = 10000
    if showkilltext == True:
        killtext_rect.x = 500               #timer1 i timer12 sa po doly na koda zashtoto tam doly kogato enemy e dead showkill text vinagi e true i za da moje da stava na false koga za timera e dolu
        killtext_rect.y = 300               #i pri drugite moje da e dolu no e tuk zashtoto sa v if statement tiq det stavat na true i te stavat samo 1 put

    #maintence the enoughcoins image text
    if showenoughtext == False:
        enoughcoins_rect.x = 10000
        enoughcoins_rect.y = 10000
    if showenoughtext == True:
        enoughcoins_rect.x = 350
        enoughcoins_rect.y = 300
        timer2 += 1
        if timer2 > 150:
            showenoughtext = False
            timer2 = 0
    
    #maintence the already have image text
    if showhavetext == False:
        haveability_rect.x = 10000
        haveability_rect.y = 10000
    if showhavetext == True:
        haveability_rect.x = 200
        haveability_rect.y = 200
        timer3 += 1
        if timer3 > 150:             #dobavih da e i s timer3 = 0 zashtoto inache timera produljava da se uvelichava kato zadurja butona                                                   
            showhavetext = False                    #za tova v tozi sluchai trqbva da go resetna do 0 i kato go natisna toi pak pochva ot nachalo i kato izteche pak se skriva normalno i se resetva
            timer3 = 0                  #hubavo e kat ima nekvi problemi da se pravi backup za da moje da se eksperimentira i da se misli s mozuka
        
            
        


    #defining platforms
    ground1 = pygame.image.load('assets/graphics/ground1.png')
    ground1_rect = ground1.get_rect(midbottom=(500,500))
    ground2 = pygame.image.load('assets/graphics/ground2.png')
    ground2_rect = ground2.get_rect(midbottom=(200,100))

    
    #gravity shit and if statements so players doesnt fall from objects
    player_gravity += 1
    player_rect.y += player_gravity
    
    #checks if the player y position is not in sync with the ground and if its like that it makes his position to fit with the ground
    if player_rect.bottom >= 640:
        player_rect.bottom = 640
        player_gravity = 0

    if player_rect.colliderect(dibeliq_rect):
        player_rect.bottom = dibeliq_rect.top
        on_platform = True
        player_gravity = 0
    elif player_rect.colliderect(ground1_rect):
        player_rect.bottom = 470
        on_platform = True
        player_gravity = 0
    elif player_rect.colliderect(ground2_rect):
        player_rect.bottom = 72
        on_platform = True
        player_gravity = 0
    elif player_rect.colliderect(ground_rect):
        player_rect.bottom = 640
        on_platform = True
        player_gravity = 0
    else:
        on_platform = False
    
    #checks if player touches the traps
    if player_rect.colliderect(trap1_rect):
        player_health -= 1.3
     


    #defining coins
    coin1 = pygame.image.load('assets/graphics/collectibles/coin1.png')
    coin1_rect = coin1.get_rect(midbottom=(535,460))
    coin2 = pygame.image.load('assets/graphics/collectibles/coin2.png')
    coin2_rect = coin2.get_rect(midbottom=(100,72))
    coin3 = pygame.image.load('assets/graphics/collectibles/coin3.png')
    coin3_rect = coin3.get_rect(midbottom=(600,630))
    coin4 = pygame.image.load('assets/graphics/collectibles/coin4.png')
    coin4_rect = coin4.get_rect(midbottom=(750,630))
    coin5 = pygame.image.load('assets/graphics/collectibles/coin5.png')
    coin5_rect = coin5.get_rect(midbottom=(900,300))




    #defining finish screen
    finish = pygame.image.load('assets/graphics/finishscreen.jpg')
    finish_rect = finish.get_rect(midbottom=(300,300))
    

    #defining sound effects
    coin_collect = pygame.mixer.Sound('assets/audio/sfx/coincollect.mp3')


    #shop defining
    shop1 = pygame.image.load('assets/graphics/shop1.png') 
    shop1_rect = shop1.get_rect(midbottom=(1000,645))


    #getting mouse position
    mouse_position = pygame.mouse.get_pos()

    #defining buttons
    buybutton1 = pygame.image.load('assets/graphics/button1.png')
    buybutton1_rect = buybutton1.get_rect(midbottom=(0,0))
    


    #collide checking between player and shop1
    if player_rect.colliderect(shop1_rect):
        showbutton1 = True
    else:
        showbutton1 = False


    #if statements
    if player_rect.colliderect(coin1_rect) and hidecoin1 == False:
        coin_collect.play()
        score = score + 1
        hidecoin1 = True
    if hidecoin1 == True:
        coin1_rect.x = 10000
        coin1_rect.y = 10000
    if player_rect.colliderect(coin2_rect) and hidecoin2 == False:
        coin_collect.play()
        score = score + 1
        hidecoin2 = True
    if hidecoin2 == True:
        coin2_rect.x = 10000
        coin2_rect.y = 10000
    if player_rect.colliderect(coin3_rect) and hidecoin3 == False:
        coin_collect.play()
        score = score + 1
        hidecoin3 = True
    if hidecoin3 == True:
        coin3_rect.x = 10000
        coin3_rect.y = 10000
    if player_rect.colliderect(coin4_rect) and hidecoin4 == False:
        coin_collect.play()
        score = score + 1
        hidecoin4 = True
    if hidecoin4 == True:
        coin4_rect.x = 10000
        coin4_rect.y = 10000
    if player_rect.colliderect(coin5_rect) and hidecoin5 == False:
        coin_collect.play()
        score = score + 1
        hidecoin5 = True
    if hidecoin5 == True:
        coin5_rect.x = 10000
        coin5_rect.y = 10000
    if showbutton1 == True:
        buybutton1_rect.x = 500
        buybutton1_rect.y = 260
    else:
        buybutton1_rect.x = 10000
        buybutton1_rect.y = 10000

    #proverqva dali mishkata e vurhy butona i dali butona e natisnat i ako score = na 2 ili poveche ot dve i choveka nqma abilitito to shte se kupi a ako ima abilitito ili nqma dostatuchno score idva else statement
    if buybutton1_rect.collidepoint(mouse_position):
        if pygame.mouse.get_pressed()[0] == 1:
            if score >= 2 and magic_ability == False:
                score = score - 2
                showenoughtext = True
                magic_ability = True
            else:
                showhavetext = True

    #abilitito otiva v rukata na playera
    if keys[pygame.K_1]:
        holdingpotion = True               
                                                #slagam + 15 za da moje da ne e navrqna pred tqloto na choveka a da e malko pred nego i v rukata
    if holdingpotion == True and magic_ability == True:
        magicpotion_rect.x = player_rect.x + 22
        magicpotion_rect.y = player_rect.y + 18    
   

    #capping enemy health
    if 0 > enemy1_health:
        enemy1_health = 0
    if 0 > enemy2_health:
        enemy2_health = 0

    #kiling enemy
    if enemy1_health == 0:
        deadenemy1 = True
        showkilltext = True
        timer += 1                                                                                       
        if timer > 150:
            showkilltext = False
    
    if enemy2_health == 0:
        deadenemy2 = True
        showkilltext = True
        timer12 += 1
        if timer12 > 150:
            showkilltext = False


        



    #checks if player touched the enemy
    if player_rect.colliderect(enemy1_rect):
            player_health -= 1.5
    if player_rect.colliderect(enemy2_rect):
        player_health -= 1.5


    #defining you died screen
    deadscreen = pygame.image.load('assets/graphics/youdied.png')    
    deadscreen_rect = deadscreen.get_rect(midbottom=(10000,10000))


    enemytexty = 10000
    enemytextx = 10000


    if deadenemy1 == True:
        enemy1_rect.x = 10000
        enemy1_rect.y = 10000
    if deadenemy2 == True:
        enemy2_rect.x = 10000
        enemy2_rect.y = 10000
    if 0 > player_health:
        deadplayer = True
        deadscreen_rect.x = 0
        deadscreen_rect.y = 0
        enemytextx = 60
        enemytexty = 15
        stopbackgroundmusic()
            
     
    #boravi s finish screena
    if deadenemy1 and deadenemy2 == True:
        finish_rect.x = 0
        finish_rect.y = 0
        lefthealthx = 30
        lefthealthy = 250
        stopbackgroundmusic()
    else:
        finish_rect.x = 10000
        finish_rect.y = 10000
        lefthealthx = 10000
        lefthealthy = 10000
    

    #drawing 
    screen.blit(sky, sky_rect)
    screen.blit(enemy2,enemy2_rect)
    screen.blit(haveability,haveability_rect)
    screen.blit(enoughcoins,enoughcoins_rect)
    screen.blit(killtext,killtext_rect)
    screen.blit(trap1,trap1_rect)
    screen.blit(enemy1,enemy1_rect)
    screen.blit(buybutton1,buybutton1_rect)
    screen.blit(shop1,shop1_rect)
    screen.blit(ground2,ground2_rect)                       #vinagi slagai nov object pod screen.blit(sky,sky_rect)
    screen.blit(ground1,ground1_rect)                       #zashtoto inache shte sa zakriti ot nebeto!!!!!!!!!!!:D
    draw_text(str(score),text_font,(0,0,0),600,60)          #za da moje purvo da se loadne golqmoto i posle pred nego malkoto
    fps = int(clock.get_fps())
    draw_text("FPS: " + str(fps),text_font2,(0,0,0),1050,0)  
    draw_text("HEALTH: " + str(player_health),text_font3,(0,0,0),1050,80)                                                                                        
    screen.blit(coin5,coin5_rect)
    screen.blit(coin4,coin4_rect)
    screen.blit(coin3,coin3_rect)
    screen.blit(coin2,coin2_rect)
    screen.blit(coin1,coin1_rect)
    screen.blit(dibeliq, dibeliq_rect)
    screen.blit(ground, ground_rect)
    screen.blit(player, player_rect)
    screen.blit(magicpotion,magicpotion_rect)
    screen.blit(finish,finish_rect)
    draw_text("You finished " + " with "+ str(player_health) + " health",text_font4,(0,0,0),lefthealthx,lefthealthy)
    screen.blit(deadscreen,deadscreen_rect)
    draw_text("The enemy had " + str(enemy1_health) + " Health left",text_font4,(0,0,0),enemytextx,enemytexty)
    pygame.display.flip()
    clock.tick(60)
    screen.blit(dibeliq, dibeliq_rect)
    
    
    
    