import pygame
import random
import sys

ancho = 600
alto = 400

class jugador(pygame.sprite.Sprite):
    '''Constructor Jugador'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,25])#surface recibe una dimensiones, ancho y largo
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
          self.image = pygame.Surface([20,20])#surface recibe una dimensiones, ancho y largo
          self.image.fill([255,255,255])
          self.rect = self.image.get_rect()
          self.rect.x=100
          self.rect.y=200
          self.velx=5
          self.vely=0
          self.disparar=False
          self.temp=random.randrange(100)

    def pos(self):
        p = [self.rect.x,self.rect.y]
        return p

    def update(self):
        self.rect.x += self.velx
        if self.rect.x > (ancho - self.rect.width):
            self.velx += -10

        if self.rect.x < 0:
            self.velx += 10
        self.temp -= 1


class bala(pygame.sprite.Sprite):
    def __init__(self,pos,cl = [255,0,255]):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface([5,7])#surface recibe una dimensiones, ancho y largo
          self.image.fill(cl)
          self.rect = self.image.get_rect()
          self.rect.x=pos[0]
          self.rect.y=pos[1]
          self.vely = -7

    def update(self):
        self.rect.y += self.vely


def imprimir(pos,color, texto):
    fuente = pygame.font.Font(None,32)
    tx = fuente.render(texto,0,color)
    pantalla.blit(tx,pos)
    pygame.display.flip()

def perder(vidas):
    if (vidas == 0):
        print("4")
        sys.exit()
    else:
        print("5")
        pass

if __name__ == '__main__':

#SECCION DE VARIABLES
    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla


    jugadores = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balasR = pygame.sprite.Group()
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
    finJuego=False
    vidas = 3
    tx = ""
    index = 20
    while (not fin) and (not finJuego):
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
                    b = bala(pos)
                    balas.add(b)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j.velx = 0
                    j.vely = 0
                if event.key == pygame.K_LEFT:
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
        for b in balas:
            ls = pygame.sprite.spritecollide(b,rivales,True)#con el ultimo parametro en True, se eliminan los objetos con los que cocha j, en falso no
            for e in ls:
                balas.remove(b)
            if b.rect.y < -10:
                balas.remove(b)
        #BALAS DEL rival
        for r in rivales:
            if r.temp == 0:
                r.disparar = True

            if r.disparar:
                b = bala(r.pos(),[0,255,0])
                b.vely = 7
                balasR.add(b)
                r.disparar = False
                r.temp = random.randrange(100)

        for b in balasR:
            if (vidas == 1):
                print("0")
                ls = pygame.sprite.spritecollide(b,jugadores,True)
                index = 0
            else:
                print("1")
                ls = pygame.sprite.spritecollide(b,jugadores,False)
                index = 1
            if b.rect.y > alto:
                balasR.remove(b)

        if index == 0:
            print("2")
            vidas = 0
        if index == 1:
            print("3")
            vidas = vidas - 1
#GESTION DE PANTALLA
        pantalla.fill([0,0,0])
        balas.update()
        balasR.update()
        rivales.update()
        jugadores.update()
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        balasR.draw(pantalla)
        tx = "Vidas: " +str(vidas)
        imprimir([50,10],[255,255,0],tx)
        perder(vidas)
        pygame.display.flip() #flip, refresca la pantalla
        reloj.tick(60)
