import pygame
import random
import sys
# el codigo trabaja con imganes de 32x32
ancho = 1300
alto = 1000
def crearMatriz(imagen):
    mt = []
    ls = []
    info = imagen.get_rect()
    i = 0
    while (i < info[3]/32):
        ls = obtenerFila(imagen,i)
        mt.append(ls)
        i += 1

    return mt


def obtenerFila(imagen,fila):
    ls = []
    info = imagen.get_rect()
    a = info[2]
    x = 0
    while ( x < a):
        cuadro = recortar(imagen,[x,fila*32])
        ls.append(cuadro)
        x += 32
    return ls

def recortar(imagen,pos):
    ls = []
    cuadro = imagen.subsurface(pos[0],pos[1],32,32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)
    ls.append(cuadro)#agregamos la imagen a la lista

    return cuadro


if __name__ == '__main__':

#SECCION DE VARIABLES
    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    imagen = pygame.image.load('animals.png')#cargamos la imagen en la variable imagen
    #pantalla.blit(imagen,[0,0])#ponemos la imagen en la pocision 0,0
    info = imagen.get_rect()#informacion de la imagen, pos 2 es ancho, pos 3 es alto
    ls = obtenerFila(imagen,6)



    pygame.display.flip()
    fin = False

    while (not fin):
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pantalla.blit(ls[10],[0,0])
                    pantalla.blit(ls[11],[32,0])
                    pantalla.blit(ls[9],[64,0])
                    pantalla.blit(ls[10],[96,0])
                    pantalla.blit(ls[11],[128,0])
        pygame.display.flip()
