import pygame
import random
import sys


class jugador(pygame.sprite.Sprite):
    '''Constructor Jugador'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,25])#surface recibe una dimensiones, ancho y largo
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.velx=0
        self.vely=0
        'Retorna la Posicion del jugador'
    def pos(self):
        p = [self.rect.x,self.rect.y]
        return p

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class comida(pygame.sprite.Sprite):
    '''Constructor Jugador'''
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,25])#surface recibe una dimensiones, ancho y largo
        self.image.fill([0,255,255])
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        'Retorna la Posicion del jugador'
    def pos(self):
        p = [self.rect.x,self.rect.y]
        return p


if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    jugadores = pygame.sprite.Group()
    comidas = pygame.sprite.Group()

    j = jugador()
    jugadores.add(j)

    c = comida([random.randrange(600),random.randrange(400)])
    comidas.add(c)

    temp = 0
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = -5
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.vely = -5
                    j.velx = 0
                if event.key == pygame.K_DOWN:
                    j.vely = 5
                    j.velx = 0
            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0
        ls = pygame.sprite.spritecollide(j,comidas,True)#con el ultimo parametro en True, se eliminan los objetos con los que cocha j, en falso no
        

        pantalla.fill([0,0,0])
        jugadores.update()
        temp += 1
        comidas.draw(pantalla)
        jugadores.draw(pantalla)
        if temp == 60:
            cc = comida([random.randrange(600),random.randrange(400)])
            comidas.add(cc)
            temp = 0
        pygame.display.flip() #flip, refresca la pantalla
        reloj.tick(60)
