# TODO NOTES
# 1. create a title screen
# 2. put all walls into game
# 3. make it so you win when you beat all monsters


import pygame, sys, time
import random
import os
from pygame.locals import *
pygame.init()
pygame.font.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Welcome to G\'s game')
clock = pygame.time.Clock()

#def text_objects(text, font):
 #   textSurface = font.render(text, True, (0, 0, 0))
  #  return textSurface, textSurface.get_rect()

#def message_display(text):
 #   largeText = pygame.font.Font('freesansbold.ttf', 25)
  #  TextSurf, TextRect = text_objects(text, largeText)
   # TextRect.center = ((display_width-600),(display_height-200))
    #gameDisplay.blit(TextSurf, TextRect)

#myfont = pygame.font.SysFont('ariel', 50)
#textsurface = myfont.render('Welcome to \n G\'s game', False, (0, 0, 0))



# TODO NOTES
# 1. create a title screen
# 2. put all walls into game
# 3. make it so you win when you beat all monsters


import pygame, sys, time
import random
import os
from pygame.locals import *
pygame.init()
pygame.font.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Welcome to G\'s game')
clock = pygame.time.Clock()

#def text_objects(text, font):
 #   textSurface = font.render(text, True, (0, 0, 0))
  #  return textSurface, textSurface.get_rect()

#def message_display(text):
 #   largeText = pygame.font.Font('freesansbold.ttf', 25)
  #  TextSurf, TextRect = text_objects(text, largeText)
   # TextRect.center = ((display_width-600),(display_height-200))
    #gameDisplay.blit(TextSurf, TextRect)

#myfont = pygame.font.SysFont('ariel', 50)
#textsurface = myfont.render('Welcome to \n G\'s game', False, (0, 0, 0))



    #Initial Values
len_sprt_x = 21
len_sprt_y = 32 #sprite size
sprt_rect_x = 5
sprt_rect_y = 160 #where to find first sprite on sheet

SPRT_RECT_X=0
SPRT_RECT_Y=0
#This is where the sprite is found on the sheet

LEN_SPRT_X=100
LEN_SPRT_Y=100
#This is the length of the sprite

screen = pygame.display.set_mode((20, 30)) #Create the screen
sheet = pygame.image.load('/home/diegogomez/Descargas/PYTHON/3KvKpwY.png') #Load the sheet
sheet_chests = pygame.image.load("/home/diegogomez/Descargas/PYTHON/154057568119963649.png")

monsters = pygame.image.load("/home/diegogomez/Descargas/PYTHON/Typhon_Monster-Sire_Sprite.png")
draw_monsters = pygame.transform.scale(monsters, (55, 45))

sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y)) #Locate the sprite you want
sheet_chests.set_clip(pygame.Rect(32, 8, 34, 33))
draw_me2 = sheet_chests.subsurface(sheet_chests.get_clip())
draw_me = sheet.subsurface(sheet.get_clip()) #Extract the sprite you want
direction = "none"

def text_objects(text, font):   #dont need this anymore
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def game_intro():       #dont need this anymore
    intro = True

    while intro:
        gameDisplay.fill(WHITE)
        largeText = pygame.font.SysFont('ariel', 50)
        TextSurf, TextRect = text_objects("Welcome to Grant\'s game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(5)
        intro = False

class EasyChest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load("/home/diegogomez/Descargas/PYTHON/154057568119963649.png")
        self.rect = self.image.get_rect()
        self.rect.x = x  # 425
        self.rect.y = y  # 327
        self.rect.topleft = self.rect.x, self.rect.y


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("/home/diegogomez/Descargas/PYTHON/Typhon_Monster-Sire_Sprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = x #175
        self.rect.y = y #520
        self.rect.topleft = self.rect.x, self.rect.y


class Monster2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("/home/diegogomez/Descargas/PYTHON/Typhon_Monster-Sire_Sprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = x #330
        self.rect.y = y #400
        self.rect.topleft = self.rect.x, self.rect.y


class Monster3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("/home/diegogomez/Descargas/PYTHON/Typhon_Monster-Sire_Sprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = x #285
        self.rect.y = y #190
        self.rect.topleft = self.rect.x, self.rect.y


inventory = []
inventory.append("sword")
class Player(pygame.sprite.Sprite):
    """Spawn a player."""

    def __init__(self):
        self.image = draw_me  # Assign the player image.
        # Assign the topleft coords of the rect.
        self.rect = self.image.get_rect(topleft=(450, 685))
        # The direction should be an instance attribute not a global variable.
        self.direction = None
        self.rect.topleft = self.rect.x, self.rect.y

    def keys(self, event):
        """Control player movement."""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.direction = "left"
                self.rect.x += -steps
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.direction = "right"
                self.rect.x += steps
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.direction = "up"
                self.rect.y += -steps
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.direction = "down"
                self.rect.y += steps
            elif event.key == pygame.K_i:
                print(inventory)
            print(self.direction)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up stop')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('down stop')

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color1):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color1)

        # Make the top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


mapwidth = 20
mapheight= 30
tilesize = 25


#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TROPICBLUE = (152,245,255)
GREY = (142,142,142)
WOOD = (156,102,31)
PATH = (139,115,85)
GINGER = (255,127,0)
FACE = (238,213,183)
FACESHADE = (205,183,158)
RED1 = (165,42,42)

HAIR = 0
SKIN = 1
NOSE = 2
GRASS = 3
WATER = 4
DEEPWATER = 5
MOUTH = 6
DIRT = 7
PATH = 8

colours = {
    HAIR: GINGER,
    SKIN:FACE,
    NOSE: FACESHADE,
    GRASS: GREEN,
    WATER: TROPICBLUE,
    DEEPWATER: BLUE,
    MOUTH: RED1,
    DIRT: WOOD,
    PATH: PATH
}

tilemap = [
    [DEEPWATER, WATER, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, WATER, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, DIRT],
    [DEEPWATER, WATER, WATER, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, DIRT, DIRT, DIRT, DIRT, DIRT],
    [DEEPWATER, DEEPWATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH],
    [DEEPWATER, DEEPWATER, WATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH],
    [DEEPWATER, DEEPWATER, WATER, WATER, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
]

#walls = []
#for i in range(0, 35):
#    boxes.append(Boxes())

# LETS MAKE SOME WALLS!
# "IM GOING TO BUILD A WALL!" -Pdaddy trump
#21 walls to go

wall_list = pygame.sprite.Group()

wall1 = Wall(96, 0, 5, 100, BLUE)
wall_list.add(wall1)
wall2 = Wall(96, 100, 29, 5, BLUE)
wall_list.add(wall2)
wall3 = Wall(120, 100, 5, 350, BLUE)
wall_list.add(wall3)
wall4 = Wall(120, 450, 55, 5, BLUE)
wall_list.add(wall4)
wall4 = Wall(175, 450, 5, 50, BLUE)
wall_list.add(wall4)
wall5 = Wall(150, 495, 29, 5, BLUE)
wall_list.add(wall5)
wall6 = Wall(145, 495, 5, 85, BLUE)
wall_list.add(wall6)
wall7 = Wall(145, 575, 55, 5, BLUE)
wall_list.add(wall7)
wall8 = Wall(195, 575, 5, 75, BLUE)
wall_list.add(wall8)
wall9 = Wall(195, 650, 105, 5, BLUE)
wall_list.add(wall9)
wall10 = Wall(295, 650, 5, 75, BLUE)
wall_list.add(wall10)
wall11 = Wall(295, 725, 205, 5, BLUE)
wall_list.add(wall11)
wall12 = Wall(495, 675, 5, 50, BLACK)
wall_list.add(wall12)
wall13 = Wall(374, 675, 165, 5, BLUE)
wall_list.add(wall13)
wall14 = Wall(374, 450, 5, 228, BLUE)
wall_list.add(wall14)
wall13 = Wall(374, 450, 103, 5, BLUE)
wall_list.add(wall13)


steps = 5
done = False

monster_list = pygame.sprite.Group()
chest_list = pygame.sprite.Group()

c1 = EasyChest(425, 327)
c1Open = False
chest_list.add(c1)
m1 = Monster(175, 520)
monster_list.add(m1)
m2 = Monster2(330, 400)
monster_list.add(m2)
m3 = Monster3(285, 190)
monster_list.add(m3)
p1 = Player()

offset_x = p1.rect[0] - p1.rect[0]
offset_y = p1.rect[1] - p1.rect[1]

m1Alive = True
m2Alive = True
m3Alive = True

clock = pygame.time.Clock()  # A clock to limit the frame rate.
main = True
main1 = True

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        # Pass the previous event to the player in the event loop
        # (once per event not per frame).
        p1.keys(event)

    if pygame.sprite.spritecollide(p1, wall_list, False):
        print("sprites have collided!")
        # Move the player back one step if a collision occurred.
        if p1.direction == "left":
            p1.rect.x += steps
        elif p1.direction == "right":
            p1.rect.x -= steps
        elif p1.direction == "up":
            p1.rect.y += steps
        elif p1.direction == "down":
            p1.rect.y -= steps
    if pygame.sprite.spritecollide(p1, chest_list, False):
        if c1Open == False:
            x = 1
            while x < 10:
                print("You opened a chest")
                x=x+1
            inventory.append("sword")
            inventory.append("key")
            c1Open = True

    if pygame.sprite.collide_rect(p1, m1):
        print("You are now fighting a monster!")
        if inventory.count("sword") > 0:
            monster_list.remove(m1)
            m1Alive = False
            inventory.remove("sword")
        else:
            print("you died")
            main = False
    if pygame.sprite.collide_rect(p1, m2):
        print("You are now fighting a monster!")
        if inventory.count("sword") > 0:
            monster_list.remove(m2)
            m2Alive = False
            inventory.remove("sword")
        else:
            print("you died")
            main = False
    if pygame.sprite.collide_rect(p1, m3):
        print("You are now fighting a monster!")
        if inventory.count("sword") > 0:
            monster_list.remove(m3)
            m3Alive = False
            inventory.remove("sword")
        else:
            print("you died")
            main = False


    screen = pygame.display.set_mode((mapwidth * tilesize, mapheight * tilesize))
    for row in range(mapheight):
        for column in range(mapwidth):
            backdrop1 = pygame.draw.rect(screen, colours[tilemap[row][column]],
                                         (column * tilesize, row * tilesize, tilesize, tilesize))

    backdrop = backdrop1
    screen.blit(draw_me2, c1.rect)
    if m1Alive == True:
        screen.blit(draw_monsters, m1.rect)
    if m2Alive == True:
        screen.blit(draw_monsters, m2.rect)
    if m3Alive == True:
        screen.blit(draw_monsters, m3.rect)
    wall_list.draw(screen)
    # Blit the player image at the player rect.
    screen.blit(p1.image, p1.rect)
    # Test if the player rect moves correctly.
    pygame.draw.rect(screen, (0, 0, 0), p1.rect, 1)
    pygame.display.update()  # Call `display.update` only once per frame.
    clock.tick(60)  # Limit the frame rate to 60 FPS.
