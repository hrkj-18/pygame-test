import pygame as pg
import time
import random

pg.init()
gameWidth = 500
gameHeight = 500

black = (0,0,0)
white = (255,255,255)


gameDisplay = pg.display.set_mode((gameWidth,gameHeight))
gameCaption = pg.display.set_caption('Save Harsh')

harshImg = pg.image.load('shades.jpeg')

harshWidth = 74
harshHeight = 114

clock = pg.time.Clock()

def harsh(x,y):
    gameDisplay.blit(harshImg,(x,y))


def dodged_things(count):
    font = pg.font.SysFont(None,20)
    text = font.render("Dodged : "+str(count),True,black)
    gameDisplay.blit(text,(0,0))
    
def things(thingx,thingy,thingw,thingh,color):
    pg.draw.rect(gameDisplay,color,(thingx,thingy,thingw,thingh))

def message_display(text):
    crashFont = pg.font.Font('freesansbold.ttf',60)
    textSurface = crashFont.render(text,True,black)
    textRectangle = textSurface.get_rect()
    textRectangle.center = ((gameWidth/2),(gameHeight/2))
    gameDisplay.blit(textSurface,textRectangle)

    pg.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('Harsh got Rekt')

def game_loop():
    x = gameWidth*0.45
    y = gameHeight*0.76

    color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
    x_change = 0

    gameExit = False
    
    
    thing_startx = random.randrange(0,gameWidth - 115)
    thing_starty = -300
    thing_width = 100
    thing_height = 100
    thing_speed = 4

    dodged = 0
    
    while not gameExit:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    quit()
                    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -8

                elif event.key == pg.K_RIGHT:
                    x_change = 8

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0

        x+=x_change
            
        gameDisplay.fill(white)
        harsh(x,y)
        dodged_things(dodged)
        things(thing_startx,thing_starty,thing_width,thing_height,color)
        thing_starty += thing_speed

        if thing_starty > gameHeight:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,gameWidth - 74)
            color = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
            dodged += 1
            thing_speed+=1
        
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + harshWidth > thing_startx and x + harshWidth < thing_startx + thing_width:
                crash()
               
        if x < 0 or x+74 > gameWidth:
            crash()

        pg.display.update()
        clock.tick(60)

game_loop()
pg.quit()
quit()
        
