import pygame
import ConfigParser
import random
import sys

def recortar(imagen,pos):
    cuadro = imagen.subsurface(pos[0]*32,pos[1]*32,32,32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)

    return cuadro

def recortar2(imagen,pos,anC,alC):
    cuadro = imagen.subsurface(pos[0]*anC,pos[1]*alC,anC,alC)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)
    return cuadro


def listadir(imagen,posiciones):
    ls = []
    cuadro = None
    for pos in posiciones:
        cuadro = recortar(imagen,pos)
        ls.append(cuadro)

    return ls

def listadir2(imagen,posiciones,anC,alC):
    ls = []
    cuadro = None
    for pos in posiciones:
        cuadro = recortar2(imagen,pos,anC,alC)
        ls.append(cuadro)

    return ls

def matrizimagen(imagen,filas,columnas,anC,alC):
    mt = []
    for i in range(0,filas):
        ls = []
        for j in range(0,columnas):
            cuadro = recortar2(imagen,[j,i],anC,alC)
            ls.append(cuadro)
        mt.append(ls)

    return mt

def printmapa(imagen,mp):
    i = 0
    fl = 0
    cl = 0
    j = 0
    jj = 0
    tp = ''
    for fila in mp:
        jj = j*32
        for e in fila:
            tp = mapa.get(e,'tipo')
            if tp == 'vacio':
                i += 32
            else:
                fl = int( mapa.get(e,'fil'))
                cl = int( mapa.get(e,'col'))
                pantalla.blit(recortar(imagen,[cl,fl]),[i,jj])
                i += 32
        i = 0
        j += 1

def printsprites(imagen,mp,mapa):
    bloques = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    i = 0
    fl = 0
    cl = 0
    j = 0
    jj = 0
    tp = ''
    for fila in mp:
        jj = j*32
        for e in fila:
            tp = mapa.get(e,'tipo')
            if tp == 'vacio':
                i += 32
            elif tp == 'muro':
                fl = int( mapa.get(e,'fil'))
                cl = int( mapa.get(e,'col'))
                b = Bloque(recortar(imagen,[cl,fl]),[i,jj])
                muros.add(b)
                #pantalla.blit(recortar(imagen,[cl,fl]),[i,jj])
                i += 32
            elif tp == 'bloque':
                fl = int( mapa.get(e,'fil'))
                cl = int( mapa.get(e,'col'))
                b = Muro(recortar(imagen,[cl,fl]),[i,jj])
                bloques.add(b)
                i += 32
        i = 0
        j += 1
    return [muros,bloques]


def printrayo(imagen,mp,pos):
    rayos = pygame.sprite.Group()
    rayospar = pygame.sprite.Group()#rayos punta de arriba
    rayospab = pygame.sprite.Group()#rayos punta de abajo
    rayospi = pygame.sprite.Group()#rayos punta de la izquierda
    rayospd = pygame.sprite.Group()#rayos punta de la derecha
    rayosar = pygame.sprite.Group()#rayos de arriba
    rayosab = pygame.sprite.Group()#rayos de abajo
    rayosi = pygame.sprite.Group()#rayos de la izquierda
    rayosd = pygame.sprite.Group()#rayos de la derecha

    i = 0
    fl = 0
    cl = 0
    j = 0
    jj = 0
    tp = ''
    for fila in mp:
        jj = j*32
        for e in fila:
            tp = raio.get(e,'tipo')
            if tp == 'vacio':
                i += 32
            else:
                fl = int( raio.get(e,'fil'))
                cl = int( raio.get(e,'col'))
                b = rayo(recortar(imagen,[cl,fl]),[i + pos[0],jj + pos[1]])
                if tp == 'puntaar':
                    rayospar.add(b)
                if tp == 'puntaab':
                    rayospab.add(b)
                if tp == 'puntai':
                    rayospi.add(b)
                if tp == 'puntad':
                    rayospd.add(b)
                if tp == 'rayoar':
                    rayosar.add(b)
                if tp == 'rayoab':
                    rayosab.add(b)
                if tp == 'rayoi':
                    rayosi.add(b)
                if tp == 'rayod':
                    rayosd.add(b)
                rayos.add(b)
                #pantalla.blit(recortar(imagen,[cl,fl]),[i,jj])
                i += 32
        i = 0
        j += 1
    return [rayos,rayospar,rayospab,rayospi,rayospd,rayosar,rayosab,rayosi,rayosd]
