import pygame

ancho = 800
alto = 600

def recortar(imagen,pos):
    cuadro = imagen.subsurface(pos[0]*32,pos[1]*32,32,32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)

    return cuadro

class jugador(pygame.sprite.Sprite):
    '''Constructor Jugador'''
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,50])#surface recibe una dimensiones, ancho y largo
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        'Retorna la Posicion del jugador'
    def pos(self):
        p = [self.rect.x,self.rect.y]
        return p

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Bloque(pygame.sprite.Sprite):

    def __init__(self, imagen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

if __name__ == '__main__':

    pygame.init()

    fondo = pygame.image.load('/home/diegogomez/Descargas/playa.jpg')
    imagen =  pygame.image.load('/home/diegogomez/Descargas/PYTHON/GRAFICAS-PLANOS/terrenogen.png')
    cuadro = recortar(imagen,[0,0])
    pantalla = pygame.display.set_mode([ancho,alto])#cambia resolucion de ventana y define una ventana llamada pantalla
    pygame.display.flip() #flip, refresca la pantalla

    jugadores = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    j = jugador([350,300])
    jugadores.add(j)

    b = Bloque(cuadro,[1000,200])
    bloques.add(b)

    info = fondo.get_rect()
    anf = info[2]
    alf = info[3]

    fx = 0
    fy = 0
    fvelx = 0
    fvely = 0
    limx = 700
    limx2 = 100
    limy = 500
    limy2 = 100


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
                if event.key == pygame.K_RIGHT:
                    j.velx = 0
                    j.vely = 0
                    fvelx = 0
                    for b in bloques:
                        b.velx = fvelx
                if event.key == pygame.K_LEFT:
                    j.velx = 0
                    j.vely = 0
                    fvelx = 0
                    for b in bloques:
                        b.velx = fvelx
                if event.key == pygame.K_UP:
                    j.vely = 0
                    j.velx = 0
                    fvely = 0
                    for b in bloques:
                        b.vely = fvely
                if event.key == pygame.K_DOWN:
                    j.vely = 0
                    j.velx = 0
                    fvely = 0
                    for b in bloques:
                        b.vely = fvely
        if j.velx>0:
            if j.rect.right > limx:
                j.rect.right = limx
                j.velx = 0
                j.vely = 0
                if (ancho - anf)  fx:
                    fvelx = -5
                else:
                    fvelx = 0
                for b in bloques:
                    b.velx = fvelx
        elif j.velx < 0:
            if j.rect.left < limx2:
                j.rect.left = limx2
                j.velx = 0
                j.vely = 0
                if 0 > fx:
                    fvelx = 5
                else:
                    fvelx = 0
                for b in bloques:
                    b.velx = fvelx
        elif j.vely > 0:
            if j.rect.top > limy:
                j.rect.top = limy
                j.velx = 0
                j.vely = 0
                if (alto - alf):
                    fvely = -5
                else:
                    fvely = 0
                for b in bloques:
                    b.vely = fvely
        elif j.vely < 0:
            if j.rect.bottom < limy2:
                j.rect.bottom = limy2
                j.velx = 0
                j.vely = 0
                if (alto - alf):
                    fvely = 5
                else:
                    fvely = 0
                for b in bloques:
                    b.vely = fvely

        pantalla.fill([0,0,0])
        pantalla.blit(fondo,[fx,fy])
        jugadores.update()
        bloques.update()
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)
