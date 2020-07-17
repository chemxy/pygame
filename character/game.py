"""
@Author: Xingyun Chen
@Github: github.com/chemxy
@All Copyright Reserved.

"""
import pygame
import random
import time

# some global variables

# initializing pygame
pygame.init()

# set up game clock
clock = pygame.time.Clock()

# set game tittle
pygame.display.set_caption("Avoid This!")

# set pictures and animations' sources and canvas dimensions
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
bomb = pygame.image.load('bomb.png')


class Projectile:
    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction

    def draw(self):
        win.blit(bomb, (self.x, self.y))
        # update display
        pygame.display.update()


class Background:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        win.blit(bg, (self.x, self.y))


class Character:
    def __init__(self):
        # character's width and height in pixels
        self.char_width = 20
        self.char_height = 20
        # iniitial character x-y coordinates in pixels
        self.x = 400
        self.y = canvas_height - self.char_height - 41
        # each movement value of the cahracter in pixels
        self.mov_value = 10 # the bigger the number, faster the character runs
        # charatcer's jump height in pixels
        self.isJump = False
        self.jumpCount = 10
        # character's facing and runnig animation count
        self.runCount = 0
        self.left = False
        self.right = False
        # character's idle animation count
        self.idleCount = 0

    def draw(self):
        # draw the character according to the movements:
        # runleft / runright / idle and jump
        if self.left:
            # win.blit( runLeft[runCount//3], (x,y)) # each step is slower and wider
            win.blit(runLeft[int(self.runCount)], (int(self.x), int(self.y)))
            self.runCount += 1
        elif self.right:
            # win.blit( runLeft[runCount//3], (x,y)) # each step is slower and wider
            win.blit(runRight[int(self.runCount)], (int(self.x), int(self.y)))
            self.runCount += 1
        else:
            # win.blit(idle[idleCount], (x,y)) # not good - frames refresh (every nod) very quickly
            win.blit(idle[int(self.idleCount//3)], (int(self.x), int(self.y)))
            self.idleCount += 1
        # check all the count vraiables to loop properly
        if self.runCount + 1 > 6:  # if runCount + 1 >= 18 --> each step is wider and slower
            self.runCount = 0
        if self.idleCount + 1 > 18:  # if idleCount + 1 >= 6 --> each nod is faster
            self.idleCount = 0

    def makeMovement(self, keys):
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
            # if keys[pygame.K_UP] and (self.y > self.mov_value):
            #    self.y -= self.mov_value
            # if keys[pygame.K_DOWN] and (self.y < canvas_height - char_height - mov_value):
            #    self.y += self.mov_value
            if keys[pygame.K_UP]:
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

class Game:
    def __init__(self, level):
        # flag: is the game runnig
        self.isRun = True
        # load background picture
        self.background = Background(0, 0)
        # load character
        self.character = Character()
        # load bombs
        self.bombs = []
        self.bombRange = 13
        # load the number of bombs (level)
        self.level = level
        self.levelScore = 0
        # load score
        self.score = 0

    def draw(self):
        # draw background
        self.background.draw()
        # draw character
        self.character.draw()
        # draw bombs
        for abomb in self.bombs:
            abomb.draw()
        # update display
        pygame.display.update()

    def detectUserInput(self):
        # detect user input
        keys = pygame.key.get_pressed()
        return keys

    def isHit(self):
        for abomb in self.bombs:
            if abomb.x in range(int(self.character.x) - self.bombRange, int(self.character.x) + self.bombRange) and abomb.y in range(int(self.character.y) - self.bombRange, int(self.character.y) + self.bombRange):
                print("character hit a bomb! game over!") 
                return True

    def randomBombs(self):
        bombx = random.randint(50,850)
        bomby = random.randint(0,300)
        speed = self.level + 5
        self.bombs.append(Projectile(bombx, bomby, speed, "DOWN"))

    def addLevel(self):
        if self.levelScore == 100:
            self.level += 1
            self.levelScore = 0

    def run(self):
        # main loop
        while self.isRun:
            # set game frame rate
            #pygame.time.delay(30) # the smaller the number, the faster the frame refreshes
            clock.tick(18) # the bigger the number, the faster the frame refreshes
            self.score += 1
            self.levelScore += 1
            #print("score: " + str(self.score) + " level: " + str(self.level) + " levelScore: " + str(self.levelScore))
            # detect QUIT input
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    self.isRun = False
                    pygame.quit()
            # detect game level
            self.addLevel()

            # detect user input
            keys = self.detectUserInput()
            #print(keys)
            self.character.makeMovement(keys)

            #check if the character hit any bomb
            if self.isHit():
                self.isRun = False

            # add bombs according to the level
            if len(self.bombs) < self.level:
                self.randomBombs()
            #bomb falling down
            for abomb in self.bombs:
                if abomb.y < canvas_height:
                    #print("bomb x: " + str(abomb.x) + " bomb y: " + str(abomb.y))
                    if abomb.direction == "DOWN":
                        abomb.y += self.level + 5
                else:
                    self.bombs.pop(self.bombs.index(abomb))

            # draw animations
            self.draw()
        return self.score

def main():
    theGame = Game(1)
    print("game begin! avoid bombs!")
    theGame.run()
    print("game end. Score: " + str(theGame.score))


# main
if __name__ == "__main__":
    main()

"""
@Author: Xingyun Chen
@Github: github.com/chemxy
@All Copyright Reserved.

"""