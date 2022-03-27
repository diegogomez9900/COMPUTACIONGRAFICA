import pygame
import random
import sys

ancho = 1300
alto = 1000

def obtenerMatriz(imagen, fila, col):
    ls = []
    info = imagen.get_rect()
    a = info[2]
    b = info[3]
    for i in range(0,)


def obtenerFila(imagen,fila):
    ls = []
    info = imagen.get_rect()
    a = info[2]
    x = 0
    while ( x < a):
        cuadro = imagen.subsurface(x,fila*32,32,(fila*32)+32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)
        ls.append(cuadro)#agregamos la imagen a la lista
        x += 32
    return ls

if __name__ == '__main__':

#SECCION DE VARIABLES
    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    imagen = pygame.image.load('terrenogen.png')#cargamos la imagen en la variable imagen
    #pantalla.blit(imagen,[0,0])#ponemos la imagen en la pocision 0,0
    info = imagen.get_rect()#informacion de la imagen, pos 2 es ancho, pos 3 es alto
    print info

    cuadro = imagen.subsurface(64,0,32,32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)

    pantalla.blit(cuadro,[0,0])
    pygame.display.flip()
    fin = False

    while (not fin):
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin = True
