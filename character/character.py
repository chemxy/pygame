import pygame, random, time

#initializing data
pygame.init()
#canvas's width and height
canvas_width = 920 
canvas_height = 768
#character's width and height 
char_width = 20
char_height = 20
# iniitial x-y coordinates
x = canvas_width / 2 
y = canvas_height - char_height - 41

#movement value
mov_value = 5
#jump
isJump = False
jumpCount = 10
#run
runCount = 0
left = False
right = False
#idle
idleCount = 0

#set up clock
clock = pygame.time.Clock()

win = pygame.display.set_mode((canvas_width,canvas_height))
runLeft = [pygame.image.load('runleft1.png'), pygame.image.load('runleft2.png'), pygame.image.load('runleft3.png'), pygame.image.load('runleft4.png'), pygame.image.load('runleft5.png'), pygame.image.load('runleft6.png') ]
runRight = [pygame.image.load('runright1.png'), pygame.image.load('runright2.png'), pygame.image.load('runright3.png'), pygame.image.load('runright4.png'), pygame.image.load('runright5.png'), pygame.image.load('runright6.png') ]
idle = [pygame.image.load('idle1.png'), pygame.image.load('idle1.png'),pygame.image.load('idle1.png'), pygame.image.load('idle2.png'), pygame.image.load('idle2.png'), pygame.image.load('idle2.png')]
bg = pygame.image.load('bg.png')

pygame.display.set_caption("my first game")

def draw():
    global runCount
    global idleCount
    win.blit(bg, (0,0))
    
    #draw the character as a rectangle
    #pygame.draw.rect(win,(255,0,0), (x,y, char_width,char_height))
    
    #check all the count vraiables
    if runCount + 1 > 6: #if runCount + 1 >= 18 --> each step is wider and slower
        runCount = 0
    if idleCount + 1 > 18: #if idleCount + 1 >= 6 --> each nod is faster
        idleCount = 0
    
    #draw the character according to the images
    if left:
        #win.blit( runLeft[runCount//3], (x,y)) # each step is slower and wider
        win.blit( runLeft[runCount], (x,y))
        runCount += 1
    elif right:
        #win.blit( runLeft[runCount//3], (x,y)) # each step is slower and wider
        win.blit( runRight[runCount], (x,y))
        runCount += 1
    else:
        #win.blit(idle[idleCount], (x,y)) # not good - frames refresh very quickly
        win.blit(idle[idleCount//3], (x,y))
        idleCount += 1
        
    #update display
    pygame.display.update()

#main loop
run= True
while run:
    #set frame rate
    #pygame.time.delay(6)
    clock.tick(18)

    #detect quit input
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    #detect user input    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (x > mov_value):
        x -= mov_value
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and (x < canvas_width - char_width - mov_value):
        x += mov_value
        left = False
        right = True
    else:
        left = False
        right = False
        runCount = 0
        

    if not(isJump):
        #if keys[pygame.K_UP] and (y > mov_value):
        #    y -= mov_value
        #if keys[pygame.K_DOWN] and (y < canvas_height - char_height - mov_value):
        #    y += mov_value    
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            runCount = 0
            idleCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2)*0.12*neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
     
            
    # fill the background for every movement
    win.fill((0,0,0))

    draw()
            