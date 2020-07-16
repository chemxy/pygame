import pygame
import random
import time

# initializing data
pygame.init()

# set up clock
clock = pygame.time.Clock()



pygame.display.set_caption("my first game")

# character animation, canvas dimensions and background picture
canvas_width = 920
canvas_height = 768
win = pygame.display.set_mode((canvas_width, canvas_height))
runLeft = [pygame.image.load('runleft1.png'), pygame.image.load('runleft2.png'), pygame.image.load(
    'runleft3.png'), pygame.image.load('runleft4.png'), pygame.image.load('runleft5.png'), pygame.image.load('runleft6.png')]
runRight = [pygame.image.load('runright1.png'), pygame.image.load('runright2.png'), pygame.image.load(
    'runright3.png'), pygame.image.load('runright4.png'), pygame.image.load('runright5.png'), pygame.image.load('runright6.png')]
idle = [pygame.image.load('idle1.png'), pygame.image.load('idle1.png'), pygame.image.load(
    'idle1.png'), pygame.image.load('idle2.png'), pygame.image.load('idle2.png'), pygame.image.load('idle2.png')]
bg = pygame.image.load('bg.png')


class Character:
    def __init__(self):
        self.life = 3


class Game:
    def __init__(self):

        # character's width and height
        self.char_width = 20
        self.char_height = 20
        # iniitial x-y coordinates
        self.x = canvas_width / 2
        self.y = canvas_height - self.char_height - 41
        # movement value
        self.mov_value = 5
        # jump
        self.isJump = False
        self.jumpCount = 10
        # run
        self.runCount = 0
        self.left = False
        self.right = False
        # idle
        self.idleCount = 0


    def draw(self, win):

        win.blit(bg, (0, 0))

        # draw the character as a rectangle
        #pygame.draw.rect(win,(255,0,0), (x,y, char_width,char_height))

        # check all the count vraiables
        if self.runCount + 1 > 6:  # if runCount + 1 >= 18 --> each step is wider and slower
            self.runCount = 0
        if self.idleCount + 1 > 18:  # if idleCount + 1 >= 6 --> each nod is faster
            self.idleCount = 0

        # draw the character according to the images
        if self.left:
            # win.blit( runLeft[runCount//3], (x,y)) # each step is slower and wider
            win.blit(runLeft[self.runCount], (self.x, self.y))
            self.runCount += 1
        elif self.right:
            # win.blit( runLeft[runCount//3], (x,y)) # each step is slower and wider
            win.blit(runRight[self.runCount], (self.x, self.y))
            self.runCount += 1
        else:
            # win.blit(idle[idleCount], (x,y)) # not good - frames refresh very quickly
            win.blit(idle[self.idleCount//3], (self.x, self.y))
            self.idleCount += 1

        # update display
        pygame.display.update()

    def run(self):
        self.run = True
        # main loop
        while self.run:
            # set frame rate
            #pygame.time.delay(6)
            clock.tick(18)
            # detect quit input
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

            # detect user input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and (self.x > self.mov_value):
                self.x -= self.mov_value
                self.left = True
                self.right = False
            elif keys[pygame.K_RIGHT] and (self.x < canvas_width - self.char_width - self.mov_value):
                self.x += self.mov_value
                self.left = False
                self.right = True
            else:
                self.left = False
                self.right = False
                self.runCount = 0

            if not(self.isJump):
                # if keys[pygame.K_UP] and (y > mov_value):
                #    y -= mov_value
                # if keys[pygame.K_DOWN] and (y < canvas_height - char_height - mov_value):
                #    y += mov_value
                if keys[pygame.K_SPACE]:
                    self.isJump = True
                    self.left = False
                    self.right = False
                    self.runCount = 0
                    self.idleCount = 0
            else:
                if self.jumpCount >= -10:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2)*0.12*neg
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 10

            # fill the background for every movement
            win.fill((0, 0, 0))

            self.draw(win)


def main():
    theGame = Game()
    theGame.run()

# main
if __name__ == "__main__":
    main()
