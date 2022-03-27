import pygame
import random


ancho = 600
alto = 400

class jugador(pygame.sprite.Sprite):
    '''Constructor Jugador'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,50])#surface recibe una dimensiones, ancho y largo
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y=400
        self.velx=0
        self.vely=0
        'Retorna la Posicion del jugador'
    def pos(self):
        p = [self.rect.x,self.rect.y]
        return p

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class rival(pygame.sprite.Sprite):
    def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface([40,50])#surface recibe una dimensiones, ancho y largo
          self.image.fill([255,255,255])
          self.rect = self.image.get_rect()
          self.rect.x=100
          self.rect.y=200
          self.velx=5
          self.vely=0
          self.disparar=False

    def pos(self):
        p = [self.rect.x,self.rect.y]
        return p

    def update(self):
        self.rect.x += self.velx
        if self.rect.x > (ancho - self.rect.width):
            self.velx += -10

        if self.rect.x < 0:
            self.velx += 10

if __name__ == '__main__':

#SECCION DE VARIABLES
    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla

    jugadores = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    j = jugador()
    jugadores.add(j)

    n= 10
    for i in range(n):
        r = rival()
        r.rect.x = random.randrange(ancho)
        r.rect.y = random.randrange(alto - 300)
        rivales.add(r)

    pygame.display.flip() #flip, refresca la pantalla


    reloj = pygame.time.Clock()
    fin = False

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
#GESTION DE EVENTOS
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
                if event.key == pygame.K_SPACE:
                    pos = j.pos()
                    print pos

            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0
#GESTION DE CONTROL
        if j.rect.x > (ancho - j.rect.width):
            j.rect.x = ancho - j.rect.width
            j.velx = 0
        if j.rect.x < 0:
            j.rect.x = 0
            j.velx = 0
        if j.rect.y > (alto - j.rect.height):
            j.rect.y = alto - j.rect.height
            j.vely = 0
        if j.rect.y < 0:
            j.rect.y = 0
            j.vely = 0
#BALAS DEL JUGADOR
        ls = pygame.sprite.spritecollide(j,rivales,True)#con el ultimo parametro en True, se eliminan los objetos con los que cocha j, en falso no
        for e in ls:
            print("colision")

#GESTION DE PANTALLA
        rivales.update()
        jugadores.update()
        pantalla.fill([0,0,0])
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        pygame.display.flip() #flip, refresca la pantalla
        reloj.tick(30)
