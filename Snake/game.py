import pygame, sys, random, time
from pygame.locals import *

#initializing data
pygame.init()
#canvas's width and height
canvas_width = 640
canvas_height = 480

# set up game window size
DISPLAY = pygame.display.set_mode((canvas_width,canvas_height))
# set up game clock
clock = pygame.time.Clock()
# set yp game tittle
pygame.display.set_caption("Snake")
# set up game font
defaultFont = pygame.font.SysFont("SIMYOU.TTF", 80)

# set up default colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)
    
class Game:
    def __init__(self, level):
        self.level = level # default: 7
        self.checkFood = True # False:food is eaten, True: food is still there
        self.isRun = True
        self.score = 0
        self.foodLocation = [300,300] # initialize food location
        self.head = [80, 100] # initialize snake's location [x, y]
        self.body = [[80,100], [60,100], [40,100]] # initialize snake's length (Note: default block is 20*20 pixels)
        self.direction = "RIGHT" # initialize snake's facing

    # generate food
    def generateFood(self):
        # generate x-y coordinates randomly
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        self.foodLocation = [int(x*20),int(y*20)]
        self.checkFood = True

    # draw snake
    def drawSnake(self):
        for x in self.body:
            pygame.draw.rect(DISPLAY, WHITE, Rect(x[0], x[1], 20, 20))

    # draw food
    def drawFood(self):
        pygame.draw.rect(DISPLAY, RED, Rect(self.foodLocation[0], self.foodLocation[1], 20, 20))

    # show scores
    def drawScore(self, score):
        # score color
        Score_Surf = defaultFont.render('%s' %(score), True, GREY)
        # score location
        score_Rect = Score_Surf.get_rect()
        score_Rect.midtop = (320, 40)
        # draw score
        DISPLAY.blit(Score_Surf, score_Rect)

    def GameOver(self):
        # color
        GameOver_Surf = defaultFont.render('Game Over!', True, GREY)
        # location
        GameOver_Rect = GameOver_Surf.get_rect()
        GameOver_Rect.midtop = (320, 10)
        # draw
        DISPLAY.blit(GameOver_Surf, GameOver_Rect)

        pygame.display.flip()
        # wait 1s
        time.sleep(1)
        run = False
        # quit
        pygame.quit()
        sys.exit()

    def addLevel(self):
        len(self.body) - 3

    def run(self):
        while self.isRun:
            # set game clock
            #pygame.time.delay(100) # the smaller the number, the faster the frame refreshes
            clock.tick(self.level)
        
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()        
                #detect user input
                elif event.type == KEYDOWN:
                    if (event.key == K_UP ) and self.direction != 'DOWN':
                        self.direction = 'UP'
                    if (event.key == K_DOWN ) and self.direction != 'UP':
                        self.direction = 'DOWN'
                    if (event.key == pygame.K_LEFT ) and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    if (event.key == K_RIGHT ) and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            # change snake's head direction
            if self.direction == 'LEFT':
                self.head[0] -= 20
            if self.direction == 'RIGHT':
                self.head[0] += 20
            if self.direction == 'UP':
                self.head[1] -= 20
            if self.direction == 'DOWN':
                self.head[1] += 20
            
            # draw
            DISPLAY.fill(BLACK)
            self.drawSnake()
            self.drawFood()
            self.drawScore(len(self.body) - 3)
            pygame.display.update()

            # check if the food is eaten
            if self.head[0] == self.foodLocation[0] and self.head[1] == self.foodLocation[1]:
                self.checkFood = False
            else:
                self.body.pop()

            if self.checkFood == False:
                self.generateFood()

            # add snake's self.head
            self.body.insert(0, list(self.head))
            
            # chech if snake hits the wall
            if self.head[0] < 0 or self.head[0]>canvas_width:
                self.GameOver()
            if self.head[1] < 0 or self.head[1]>canvas_height:
                self.GameOver()
            # check if snake hits itself
            for i in self.body[1:]:
                if self.head[0]==i[0] and self.head[1]==i[1]:
                    self.GameOver()


def main():
    theGame = Game(10)
    print("game begin!!")
    theGame.run()
    print("game end.")


# main
if __name__ == "__main__":
    main()