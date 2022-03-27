import pygame

class jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.direccion=2
        self.con=0
        self.image=self.m[self.direccion][self.con]
        self.rect=self.image.get_rect()
        self.velx = 0
        self.vely = 0

    def update(self):
        self.image=self.m[self.direccion][self.con]
        if self.con < 2:
            self.con +=1
        else:
            self.con = 0
        self.rect.x += self.velx
        self.rect.y += self.vely



def obtenerMatriz(img):
    m=[]
    j=0
    while(j < 8):
        ls=[]
        i=0
        n=0
        posActual=32
        while(i < 12):
            cuadro = img.subsurface(i*32,j*32,32,32)
            ls.append(cuadro)
            i= i+1
        m.append(ls)
        j=j+1
    return(m)


def recortar(imagen,pos):
    ls = []
    cuadro = imagen.subsurface(pos[0]*32,pos[1]*32,32,32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)
    ls.append(cuadro)#agregamos la imagen a la lista

    return cuadro


if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    imagen = pygame.image.load('animals.png')
    jugadores= pygame.sprite.Group()
    imagen = obtenerMatriz(imagen)
    j = jugador(imagen)
    jugadores.add(j)

    pygame.display.flip() #flip, refresca la pantalla




    reloj = pygame.time.Clock()
    fin = False

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.direccion = 2
                    j.velx = 5
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.direccion = 1
                    j.velx = -5
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.direccion = 3
                    j.vely = -5
                    j.velx = 0
                if event.key == pygame.K_DOWN:
                    j.direccion = 0
                    j.vely = 5
                    j.velx = 0
                if event.key == pygame.K_SPACE:
                    j.vely = 0
                    j.velx = 0
        jugadores.update()
        pantalla.fill([0,0,0])
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
