import pygame
import ConfigParser
import random
import sys
import time
import gc

#VERSION ESTABLE, PRESENTADO EN PARCIAL
#DIMENSIONES PANTALLA

ancho = 640
alto = 416
nivelActual = 1

#FUNCIONES QUE UTILIZA EL JUEGO
def list_ima(imag,ancho,largo,an_c,al_c):

    list=[]
    for i in range(0,ancho):
        auxlis=[]
        for j in range (0,largo):
            cuadro=imag.subsurface(i*an_c,j*al_c,an_c,al_c)
            auxlis.append(cuadro)
        list.append(auxlis)
    return list


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

def printrayo(imagen,mp,pos,raio):
    rayos = pygame.sprite.Group()

    rayoarab = listadir(imagen,[[0,4],[1,4],[2,4],[3,4]])#tipo 0
    rayoizde = listadir(imagen,[[1,0],[1,1],[1,2],[1,3]])#tipo 1
    rayocentro = listadir(imagen,[[2,0],[2,1],[2,2],[2,3]])#tipo 2

    puntaiz = listadir(imagen,[[0,0],[0,1],[0,2],[0,3]])#tipo 3
    puntade = listadir(imagen,[[4,0],[4,1],[4,2],[4,3]])#tipo 4
    puntaarr = listadir(imagen,[[4,4],[0,5],[1,5],[2,5]])#tipo 5
    puntaaba = listadir(imagen,[[3,5],[4,5],[0,6],[1,6]])#tipo 6

    rayoj = []
    puntaj = []

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
            elif tp == 'rayoar':
                b = rayo(rayoarab,[i + pos[0],jj + pos[1]],0,7)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoab':
                b = rayo(rayoarab,[i + pos[0],jj + pos[1]],1,8)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoi':
                b = rayo(rayoizde,[i + pos[0],jj + pos[1]],2,5)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayod':
                b = rayo(rayoizde,[i + pos[0],jj + pos[1]],3,6)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'centro':
                b = rayo(rayocentro,[i + pos[0],jj + pos[1]],4,9)
                rayos.add(b)
                i += 32
            elif tp == 'puntai':
                b = rayo(puntaiz,[i + pos[0],jj + pos[1]],5,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
            elif tp == 'puntad':
                b = rayo(puntade,[i + pos[0],jj + pos[1]],6,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
            elif tp == 'puntaar':
                b = rayo(puntaarr,[i + pos[0],jj + pos[1]],7,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
            elif tp == 'puntaab':
                b = rayo(puntaaba,[i + pos[0],jj + pos[1]],8,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
        i = 0
        j += 1
    return [rayos,rayoj,puntaj]

def printrayo2(imagen,mp,pos,raio):
    rayos = pygame.sprite.Group()

    rayoarab = listadir(imagen,[[0,4],[1,4],[2,4],[3,4]])#tipo 0
    rayoizde = listadir(imagen,[[1,0],[1,1],[1,2],[1,3]])#tipo 1
    rayocentro = listadir(imagen,[[2,0],[2,1],[2,2],[2,3]])#tipo 2

    puntaiz = listadir(imagen,[[0,0],[0,1],[0,2],[0,3]])#tipo 3
    puntade = listadir(imagen,[[4,0],[4,1],[4,2],[4,3]])#tipo 4
    puntaarr = listadir(imagen,[[4,4],[0,5],[1,5],[2,5]])#tipo 5
    puntaaba = listadir(imagen,[[3,5],[4,5],[0,6],[1,6]])#tipo 6

    rayoj = []
    puntaj = []

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
            elif tp == 'rayoar':
                b = rayo(rayoarab,[i + pos[0],jj + pos[1]],0,99)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoar1':
                b = rayo(rayoarab,[i + pos[0],jj + pos[1]],99,7)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoab':
                b = rayo(rayoarab,[i + pos[0],jj + pos[1]],1,19)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoab1':
                b = rayo(rayoarab,[i + pos[0],jj + pos[1]],19,8)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoi':
                b = rayo(rayoizde,[i + pos[0],jj + pos[1]],2,29)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayoi1':
                b = rayo(rayoizde,[i + pos[0],jj + pos[1]],29,5)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayod':
                b = rayo(rayoizde,[i + pos[0],jj + pos[1]],3,39)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'rayod1':
                b = rayo(rayoizde,[i + pos[0],jj + pos[1]],39,6)
                rayos.add(b)
                rayoj.append(b)
                i += 32
            elif tp == 'centro':
                b = rayo(rayocentro,[i + pos[0],jj + pos[1]],4,9)
                rayos.add(b)
                i += 32
            elif tp == 'puntai':
                b = rayo(puntaiz,[i + pos[0],jj + pos[1]],5,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
            elif tp == 'puntad':
                b = rayo(puntade,[i + pos[0],jj + pos[1]],6,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
            elif tp == 'puntaar':
                b = rayo(puntaarr,[i + pos[0],jj + pos[1]],7,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
            elif tp == 'puntaab':
                b = rayo(puntaaba,[i + pos[0],jj + pos[1]],8,9)
                rayos.add(b)
                puntaj.append(b)
                i += 32
        i = 0
        j += 1
    return [rayos,rayoj,puntaj]


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
#____
#recortar una imagen y convertir en matriz,anC, es el ancho del cuadro a recortar, y alC es el alto del cuadro a recortar,filas = cantidad de filas que tiene la imagen a recortar al igual que columnas
def recortar2(imagen,pos,anC,alC):
    cuadro = imagen.subsurface(pos[0]*anC,pos[1]*alC,anC,alC)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)
    return cuadro


def matrizimagen(imagen,filas,columnas,anC,alC):
    mt = []
    for i in range(0,filas):
        ls = []
        for j in range(0,columnas):
            cuadro = recortar2(imagen,[j,i],anC,alC)
            ls.append(cuadro)
        mt.append(ls)

    return mt
#_____________________________

def recortar(imagen,pos):
    cuadro = imagen.subsurface(pos[0]*32,pos[1]*32,32,32)#la funcion subsurface() permite tomar una parte de una imagen, recibe (pos x(inicio del recorte), posy(inicio del recorte), recorte en ancho, recorte en alto)

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

def posbomba(x,y):
    ls = lista32()
    ee = 0
    for e in ls:
        if x<e:
            x = ee
            break
        else:
            ee = e
    ee = 0
    for e in ls:
        if y<e:
            y = ee
            break
        else:
            ee = e
    return [x,y]

def posbomba2(x,y):
    ls = lista32()
    ee = 0
    for e in ls:
        if x<e:
            x = ee
            break
        else:
            ee = e
    ee = 0
    for e in ls:
        if y<e:
            y = ee
            break
        else:
            ee = e
    return [x/32,y/32]


def lista32():
    ls = []
    for e in range(0,21):
        n = 32*e
        ls.append(n)
    return ls

def imprimir(pos,color, texto,tamano = 32):
    fuente = pygame.font.Font(None,tamano)
    tx = fuente.render(texto,0,color)
    pantalla.blit(tx,pos)

#MENU DE PAUSA

def pausa():
    imagen = pygame.image.load('flecha2.png')
    im = pygame.image.load('pausa.png')
    im = pygame.transform.scale(im,(ancho, alto + 50))
    select = pygame.mixer.Sound('select2.wav')
    musica = pygame.mixer.music.load('level-song.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    fin = False
    fin2 = False
    paused = False
    i = 0
    ps = [0,0]
    ms = []
    botonsel = 0
    sel = False
    enter = 5
    reloj = pygame.time.Clock()
    while not fin:

        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            ms = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if event.button == 1:
                    if pos[0] > 128 and pos[0] < 224 and pos[1] > 96 and pos[1] < 128:
                        select.play()
                        fin=True
                        paused = True
                    if pos[0] > 128 and pos[0] < 352 and pos[1] > 160 and pos[1] < 192:
                        select.play()
                        fin = True
                        fin2 = True
                    if pos[0] > 128 and pos[0] < 256 and pos[1] > 224 and pos[1] < 256:
                        select.play()
                        fin = True
                        fin2 = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    select.play()
                    botonsel = botonsel - 1
                    if botonsel == -1:
                        botonsel = 2
                if event.key == pygame.K_DOWN:
                    select.play()
                    botonsel = botonsel + 1
                    if botonsel == 3:
                        botonsel = 0
                if event.key == pygame.K_z:
                    sel = True
            if enter == 0 and sel:
                select.play()
                fin=True
                paused = True
            if enter == 1 and sel:
                select.play()
                fin = True
                fin2 = True
            if enter == 2 and sel:
                select.play()
                fin = True
                fin2 = False

            if (ms[0] > 128 and ms[0] < 224 and ms[1] > 96 and ms[1] < 128) or botonsel == 0:
                ps = [352,92]
                botonsel = 0
            if (ms[0] > 128 and ms[0] < 352 and ms[1] > 160 and ms[1] < 192) or botonsel == 1:
                ps = [352,156]
                botonsel = 1
            if (ms[0] > 128 and ms[0] < 256 and ms[1] > 224 and ms[1] < 256) or botonsel == 2:
                ps = [352,220]
                botonsel = 2

        if sel:
            enter = botonsel

        imprimir([128,96],[0,0,0],"VOLVER")
        imprimir([128,160],[0,0,0],"SALIR DEL JUEGO")
        imprimir([128,224],[0,0,0],"INICIO")
        if not (ps == [0,0]):
            cuadro = listadir(imagen,[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[5,0],[4,0],[3,0],[2,0]])
            cuadro = cuadro[i]
            if i < 10:
                i += 1
            else:
                i = 1
            pantalla.blit(cuadro,ps)

        pygame.display.flip()
        pantalla.blit(im,[0,0])
        reloj.tick(10)


    return [fin2,paused]

#MENU DE INICIO

def inicio():

    #CARGA DE IMAGENES
    imagen1 = pygame.image.load('flecha.png')
    imagen = pygame.image.load('bomberman-sprites.png')
    cuadro = imagen.subsurface(4,259,226,138)
    cuadro = pygame.transform.scale(cuadro,(452, 276))

    #CARGA DE SONIDOS Y MUSICA
    select = pygame.mixer.Sound('select2.wav')
    mus = pygame.mixer.music.load('title-screen.mp3')
    pygame.mixer.music.play(-1)

    #VARIABLES NECESARIAS CICLO
    fin = False
    fin2 = False
    sel = False

    y = -138
    i = 0
    ps = [0,0]
    ms = [0,0]
    enter = 5
    botonsel = 0

    reloj = pygame.time.Clock()
    while not fin:

        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            ms = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if event.button == 1:
                    if y == 32:
                        if pos[0] > 288 and pos[0] < 384 and pos[1] > 320 and pos[1] < 352:
                            select.play()
                            fin = True
                            pygame.mixer.music.stop()
                            pygame.mixer.music.rewind()
                        if pos[0] > 298 and pos[0] < 384 and pos[1] > 352 and pos[1] < 384:
                            select.play()
                            fin = True
                            fin2 = True
                            pygame.mixer.music.stop()
                            pygame.mixer.music.rewind()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    select.play()
                    if botonsel == 1:
                        botonsel = 0
                    else:
                        botonsel = 1
                if event.key == pygame.K_DOWN:
                    select.play()
                    if botonsel == 1:
                        botonsel = 0
                    else:
                        botonsel = 1
                if event.key == pygame.K_z:
                    sel = True

        if y == 32:
            pantalla.blit(cuadro,[90,32])
            imprimir([288,320],[255,255,255],"INICIAR")
            imprimir([298,352],[255,255,255],"SALIR")
            if (ms[0] > 288 and ms[0] < 384 and ms[1] > 320 and ms[1] < 352) or botonsel == 0:
                ps = [384,320]
                botonsel = 0
                enter = botonsel
            if (ms[0] > 298 and ms[0] < 384 and ms[1] > 352 and ms[1] < 384) or botonsel == 1:
                ps = [384,352]
                botonsel = 1
                enter = botonsel
            if not (ps == [0,0]):
                cuadro1 = listadir(imagen1,[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[5,0],[4,0],[3,0],[2,0]])
                cuadro1 = cuadro1[i]
                if i < 10:
                    i += 1
                else:
                    i = 1
                pantalla.blit(cuadro1,ps)

        else:
            pantalla.blit(cuadro,[90,y])
            y += 5

        if enter == 0 and sel:
            select.play()
            reloj.tick(2)
            fin = True
            pygame.mixer.music.stop()
            pygame.mixer.music.rewind()
        if enter == 1 and sel:
            select.play()
            reloj.tick(2)
            fin = True
            fin2 = True
            pygame.mixer.music.stop()
            pygame.mixer.music.rewind()
        pygame.display.flip()
        reloj.tick(10)
        pantalla.fill([0,0,0])
        gc.collect()
    return fin2

#PANTALLA DE INICIO DE NIVEL, i ES EL NUMERO DEL NIVEL

def tuto():
    mus = pygame.mixer.music.load('historia.mp3')
    im = pygame.image.load('tutorial.png')
    im = pygame.transform.scale(im,(ancho, alto))
    select = pygame.mixer.Sound('select2.wav')
    pygame.mixer.music.play(-1)
    reloj = pygame.time.Clock()
    fin = False
    fin2 = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                select.play()
                fin = True
            if event.type == pygame.KEYDOWN:
                select.play()
                fin = True
        pantalla.fill([0,0,0])
        pantalla.blit(im,[0,0])
        imprimir([ancho/2,alto+20],[255,255,255],"PRESIONE UNA TECLA PARA CONTINUAR",23)
        pygame.display.flip()
        reloj.tick(15)
        gc.collect()
    return(fin2)

def prologo():
    im = pygame.image.load('prologo.png')
    im = pygame.transform.scale(im,(ancho, alto))
    select = pygame.mixer.Sound('select2.wav')
    reloj = pygame.time.Clock()
    fin = False
    fin2 = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                select.play()
                fin = True
            if event.type == pygame.KEYDOWN:
                select.play()
                fin = True
        pantalla.fill([0,0,0])
        pantalla.blit(im,[0,0])
        imprimir([ancho/2,alto+20],[255,255,255],"PRESIONE UNA TECLA PARA CONTINUAR",23)
        pygame.display.flip()
        reloj.tick(15)
        gc.collect()
    return(fin2)

def completado():
    mus = pygame.mixer.music.load('historia.mp3')
    pygame.mixer.music.play(-1)
    im = pygame.image.load('finalfinal.jpg')
    im = pygame.transform.scale(im,(ancho, alto))
    select = pygame.mixer.Sound('select2.wav')
    reloj = pygame.time.Clock()
    fin = False
    fin2 = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                select.play()
                fin = True
            if event.type == pygame.KEYDOWN:
                select.play()
                fin = True
        pantalla.fill([0,0,0])
        pantalla.blit(im,[0,0])
        imprimir([ancho/2,alto+20],[255,255,255],"PRESIONE UNA TECLA PARA CONTINUAR",23)
        pygame.display.flip()
        reloj.tick(15)
        gc.collect()
    return(fin2)

def interludio():
    mus = pygame.mixer.music.load('historia.mp3')
    pygame.mixer.music.play(-1)
    im = pygame.image.load('interludio.jpg')
    im = pygame.transform.scale(im,(ancho, alto))
    select = pygame.mixer.Sound('select2.wav')
    reloj = pygame.time.Clock()
    fin = False
    fin2 = False

    tasa=60
    seg=0
    lim=180

    while not fin:
        tiempo = ((seg*4)//tasa)
        seg+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tiempo > 4:
                    select.play()
                    fin = True
            if event.type == pygame.KEYDOWN:
                if tiempo > 5:
                    select.play()
                    fin = True
        pantalla.fill([0,0,0])
        pantalla.blit(im,[0,0])


        if tiempo > 1:
            imprimir([100,120],[255,255,255],"Es Hora...",32)
        if tiempo > 2:
            imprimir([100,155],[255,255,255],"De ir...",32)
        if tiempo > 3:
            imprimir([100,190],[255,255,255],"Contra...",32)
        if tiempo > 4:
            imprimir([100,225],[255,255,255],"El Jefe.",32)
        if tiempo > 5:
            imprimir([ancho/2,alto+20],[255,255,255],"PRESIONE UNA TECLA PARA CONTINUAR",23)
        pygame.display.flip()
        reloj.tick(15)
        gc.collect()
    return(fin2)

def postprologo():
    im = pygame.image.load('final-prologo.jpg')
    im = pygame.transform.scale(im,(ancho, alto))
    select = pygame.mixer.Sound('select2.wav')
    reloj = pygame.time.Clock()
    fin = False
    fin2 = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                select.play()
                fin = True
            if event.type == pygame.KEYDOWN:
                select.play()
                fin = True
        pantalla.fill([0,0,0])
        pantalla.blit(im,[0,0])
        imprimir([ancho/2,alto+20],[255,255,255],"PRESIONE UNA TECLA PARA CONTINUAR",23)
        pygame.display.flip()
        reloj.tick(15)
        gc.collect()
    return(fin2)

def level(i):
    mus = pygame.mixer.music.load('level-start.mp3')
    pygame.mixer.music.play(-1)
    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            ms = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                fin=True
                fin2 = True
        pantalla.fill([0,0,0])
        imprimir([288,160],[255,255,255],"NIVEL "+str(i))
        pygame.display.flip()
        reloj.tick(0.3)
        fin = True
        gc.collect()
    pygame.mixer.music.stop()

#PANTALLA DE NIVEL COMPLETADO
def ganar():
    imagen = pygame.image.load('cuadronegro.png')
    imagen1 = pygame.image.load('lineaverde.png')
    mus = pygame.mixer.music.load('level-complete.mp3')
    pygame.mixer.music.play(-1)
    reloj = pygame.time.Clock()
    x = 0
    fin = False
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            ms = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                fin=True
                fin2 = True
        for i in range(0,20):
            pantalla.blit(imagen,[x,135])
            pantalla.blit(imagen1,[x,130])
            pantalla.blit(imagen1,[x,199])
            x += 32
        imprimir([200,160],[255,255,255],"NIVEL COMPLETADO")
        pygame.display.flip()
        reloj.tick(0.3)
        pantalla.fill([0,0,0])
        pygame.display.flip()
        fin = True
        gc.collect()
    pygame.mixer.music.stop()

def ganar2():
    imagen = pygame.image.load('cuadronegro.png')
    imagen1 = pygame.image.load('lineaverde.png')
    mus = pygame.mixer.music.load('level-complete.mp3')
    pygame.mixer.music.play(-1)
    reloj = pygame.time.Clock()
    x = 0
    fin = False
    fin2 = False
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            ms = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                fin = True
            if event.type == pygame.KEYDOWN:
                fin = True
        for i in range(0,20):
            pantalla.blit(imagen,[x,135])
            pantalla.blit(imagen,[x,135+64])
            pantalla.blit(imagen1,[x,130])
            pantalla.blit(imagen1,[x,199+64])
            x += 32
        imprimir([200,160+8],[255,255,255],"NIVEL COMPLETADO")
        imprimir([200,160+56],[255,255,255],"JUEGO TERMINADO")
        pygame.display.flip()
        reloj.tick(0.3)
        pantalla.fill([0,0,0])
        pygame.display.flip()
        fin = True
        gc.collect()
    pygame.mixer.music.stop()
    return fin2


#MENU DEL FIN DEL JUEGO

def finJuego():
    mus = pygame.mixer.music.load('game-over.mp3')
    select = pygame.mixer.Sound('select2.wav')
    pygame.mixer.music.play(-1)
    reloj = pygame.time.Clock()
    fin = False
    fin2 = False
    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select.play()
                fin=True
                fin2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                select.play()
                fin = True
            if event.type == pygame.KEYDOWN:
                select.play()
                fin = True
        pantalla.fill([0,0,0])
        imprimir([200,130],[255,255,255],"JUEGO TERMINADO")
        imprimir([100,380],[255,255,255],"OPRIMA UNA TECLA PARA CONTINUAR")
        reloj.tick(5)
        gc.collect()
        pygame.display.flip()
    pygame.mixer.music.stop()
    return fin2



#DECLARACION DE LAS CLASES

class jugador(pygame.sprite.Sprite):
    def __init__(self,im):
        pygame.sprite.Sprite.__init__(self)
        self.im=im
        self.direccion=0
        self.con=0
        self.limite = 2
        self.vivo = True
        self.mover = False
        self.image=self.im[self.con]
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.velx = 0
        self.vely = 0

    def update(self):
        self.image=self.im[self.con]
        if self.mover:
            if self.con < self.limite:
                self.con +=1
            else:
                self.con = 0
            self.rect.x += self.velx
            self.rect.y += self.vely

class jefe(pygame.sprite.Sprite):
    def __init__(self,im,pos):
        pygame.sprite.Sprite.__init__(self)
        self.im=im
        self.direccion=0
        self.con=0
        self.limite = 2
        self.vivo = True
        self.image=self.im[self.con]
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 4
        self.vely = 0

    def update(self):
        self.image=self.im[self.con]
        if self.con < self.limite:
            self.con +=1
        else:
            self.con = 0
        self.rect.x += self.velx
        self.rect.y += self.vely

class enemigoA(pygame.sprite.Sprite):
    def __init__(self,im,pos):
        pygame.sprite.Sprite.__init__(self)
        self.m=im
        self.direccion=0
        self.con=0
        self.limite = 3
        self.vivo = True
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 4
        self.vely = 0

    def update(self):
        self.image=self.m[self.con]
        if self.con < self.limite:
            self.con +=1
        else:
            self.con = 0
        self.rect.x += self.velx
        self.rect.y += self.vely

class enemigoB(pygame.sprite.Sprite):
    def __init__(self,m,pos):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.direccion=0
        self.con=0
        self.limite = 1
        self.vivo = True
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 4
        self.vely = 0

    def update(self):
        self.image=self.m[self.con]
        if self.con < self.limite:
            self.con +=1
        else:
            self.con = 0
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
        self.xreal = 0

    def update(self):
        self.rect.x += self.velx
        self.xreal += self.velx
        self.rect.y += self.vely

class Muro(pygame.sprite.Sprite):

    def __init__(self, imagen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        mur = pygame.image.load('muros.png')
        murosdes = listadir(mur,[[2,0],[3,0],[4,0],[5,0],[6,0]])
        self.im = murosdes
        self.con = 0
        self.limit = 4
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx = 0
        self.vely = 0
        self.animacion = False

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if self.animacion:
            self.image=self.im[self.con]
            if self.con < self.limit:
                self.con +=1
            else:
                self.con = 0


class spawn(pygame.sprite.Sprite):

    def __init__(self, imagen,pos,tipe):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.tipo = tipe
        self.velx = 0
        self.vely = 0
        self.xreal = 0

    def update(self):
        self.rect.x += self.velx
        self.xreal += self.velx
        self.rect.y += self.vely

class ventaja(pygame.sprite.Sprite):

    def __init__(self, imagen,pos,tipo):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.type = tipo
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class bomba(pygame.sprite.Sprite):

    def __init__(self, ls, pos):
        pygame.sprite.Sprite.__init__(self)
        self.ls = ls
        self.con = 0
        self.time = 0
        self.remover = False
        self.estallada = False
        self.image = self.ls[self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.image = self.ls[self.con]
        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.con < 2:
            self.con += 1
        else:
            self.con = 0

        if self.time == 45:
            self.remover = True
        else:
            self.time += 1

class rayo(pygame.sprite.Sprite):

    def __init__(self, ls, pos,tipo,tiposig):
        pygame.sprite.Sprite.__init__(self)
        self.con = 0
        self.type = tipo
        self.typesig = tiposig
        self.ls = ls
        self.remover = False
        self.image = self.ls[self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.image = self.ls[self.con]
        self.rect.x += self.velx
        self.rect.y += self.vely
        if self.con < 3:
            self.con += 1
        else:
            self.remover = True

class fondo(pygame.sprite.Sprite):

    def __init__(self, imagen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx = 0
        self.xreal = 0
        self.mover = 0

    def update(self):
        self.xreal += self.velx

#FUNCION PRINCIPAL

if __name__ == '__main__':
    #INICIALIZACION DE PYGAME, MIXER, Y PANTALLA
    pygame.init()
    pygame.mixer.init()
    pantalla = pygame.display.set_mode([ancho,alto +50])


    #LECTURA DE MAPAS
    mapa = ConfigParser.ConfigParser()
    mapa2 = ConfigParser.ConfigParser()
    mapa3 = ConfigParser.ConfigParser()
    raio = ConfigParser.ConfigParser()
    raioc = ConfigParser.ConfigParser()
    mapa.read('mapa.map')
    mapa2.read('mapa2.map')
    mapa3.read('mapa3.map')
    raio.read('rayo1.map')
    raioc.read('rayo2.map')

    #DIVISION DE CADA PARTE DEL MAPA EN ELEMENTO DE LISTA
    mp = mapa.get('info','mapa')
    mp = mp.split('\n')

    mp2 = mapa2.get('info','mapa')
    mp2 = mp2.split('\n')

    mp3 = mapa3.get('info','mapa')
    mp3 = mp3.split('\n')

    ry = raio.get('info','mapa')
    ry = ry.split('\n')

    ryc = raioc.get('info','mapa')
    ryc = ryc.split('\n')

    #CARGA DE IMAGENES
    fond = pygame.image.load('fondo.png')
    fondgris = pygame.image.load('fondo-gris.png')
    imagen = pygame.image.load('muros.png')
    personaje = pygame.image.load('bomberman.png')
    personaje2 = pygame.image.load('bomberman2.png')
    muros = pygame.image.load('sprites.png')
    boom = pygame.image.load('bomba2.png')
    rayoimage = pygame.image.load('rayo3.png')
    vB = pygame.image.load('ventajas.png')
    boss = pygame.image.load('boss3.png')

    #DEFINICION DE ANIMACIONES USADAS POR CLASES
    bs = listadir(boom,[[0,0],[1,0],[2,0],[3,0]])

    abajo = listadir2(personaje,[[3,0],[4,0],[5,0]],28,28)
    arriba = listadir2(personaje,[[6,0],[7,0],[0,1]],28,28)
    derecha = listadir2(personaje2,[[5,0],[6,0],[7,0]],28,28)
    izquierda = listadir2(personaje,[[0,0],[1,0],[2,0]],28,28)
    animuerte = listadir2(personaje,[[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]],28,28)

    babajo = listadir(boss,[[0,0],[1,0],[2,0]])
    barriba = listadir(boss,[[0,3],[1,3],[2,3]])
    bizquierda = listadir(boss,[[0,1],[1,1],[2,1]])
    bderecha = listadir(boss,[[0,2],[1,2],[2,2]])
    bmuerto = recortar(boss,[3,0])

    mEA = listadir2(personaje,[[7,6],[4,2],[5,2],[6,2],[7,2]],28,28)
    mEB = listadir2(personaje,[[7,5],[4,2],[5,2],[6,2],[7,2]],28,28)
    IenemigoA = listadir2(personaje,[[4,6],[5,6],[6,6]],28,28)
    IenemigoA.append(recortar2(personaje2,[2,6],28,28))
    enemigoBd = listadir2(personaje,[[4,5],[5,5],[6,5]],28,28)
    enemigoBi = listadir2(personaje2,[[3,5],[2,5],[1,5]],28,28)
    enemigoBaa = listadir2(personaje,[[4,5],[5,5]],28,28)

    ventajaBomba = recortar(vB,[0,0])
    ventajaDetonador = recortar(vB,[3,0])
    ventajaFuego = recortar(vB,[1,0])

    imgSpawn = recortar(vB,[5,0])

    #CARGA DE SONIDOS
    explosionSonido = pygame.mixer.Sound('explosion.wav')
    select = pygame.mixer.Sound('select2.wav')
    ponerBomba = pygame.mixer.Sound('put-bomb.wav')
    muertoJ = pygame.mixer.Sound('lose.wav')
    poder = pygame.mixer.Sound('power.wav')
    musica = pygame.mixer.music.load('stage-theme.mp3')

    #INICIO DE REPRODUCCION DE MUSICA
    pygame.mixer.music.play(-1)

    #CREACION DE GRUPOS DE SPRITES
    bloques = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    bombas = pygame.sprite.Group()
    rayos = pygame.sprite.Group()
    enemigosA = pygame.sprite.Group()
    enemigosB = pygame.sprite.Group()
    murosI = pygame.sprite.Group()
    generadores = pygame.sprite.Group()
    ventajas = pygame.sprite.Group()
    fondos = pygame.sprite.Group()
    jefes = pygame.sprite.Group()

    #INICIALIZADO DE sprite.Group()'s

    f = fondo(fond,[0,0])
    fondos.add(f)

    spp = printsprites(imagen,mp,mapa)
    bloques = spp[0]
    muros = spp[1]
    murosI = spp[1]

    j = jugador(abajo)
    jugadores.add(j)

    pospawner = [608,384]
    pospawner2 = [544,320]
    g = spawn(imgSpawn,pospawner,1)
    gg = spawn(imgSpawn,pospawner2,2)
    generadores.add(g)
    generadores.add(gg)


    cont = random.randrange(0,len(muros) - 1)
    cont2 = random.randrange(0,len(muros) - 1)
    cont3 = random.randrange(0,len(muros) - 1)
    while cont == cont2 or cont2 == cont3 or cont3 == cont:
        if cont == cont2 or cont == cont3:
            cont = random.randrange(0,len(muros) - 1)
        else:
            cont3 = random.randrange(0,len(muros) - 1)

    for mr in muros:
        cont = cont - 1
        cont2 = cont2 - 1
        cont3 = cont3 - 1
        if cont == 0:
            v = ventaja(ventajaBomba,[mr.rect.x,mr.rect.y],0)
            ventajas.add(v)
        if cont2 == 0:
            vv = ventaja(ventajaDetonador,[mr.rect.x,mr.rect.y],1)
            ventajas.add(vv)
        if cont3 == 0:
            vv = ventaja(ventajaFuego,[mr.rect.x,mr.rect.y],2)
            ventajas.add(vv)
    #ACTUALIZACION DE PANTALLA
    pygame.display.flip()
    #VARIABLES DEL CICLO
    fin = False
    reloj = pygame.time.Clock()
    temp = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    temp5 = 0
    rayoj = []
    puntaj = []
    reproducir = True
    controlador = False
    estallar = False
    spawner = True
    tiempo = 0
    cantBomb = 1
    longrayo = 1
    limiteEnemigosA = 4
    limiteEnemigosB = 3
    pause = False
    lsVel = [4,-4]
    xfondo = 0
    vidasJugador = 3
    vidaJefe = 3

#CONTROL DE TIEMPO
    tasa=60
    seg=0
    lim=180
    fuente=pygame.font.Font(None, 24)


    #MOSTRADO DE INICIO DE JUEGO
    pygame.mixer.music.stop()
    fin = inicio()
    if not fin:
        fin = tuto()
        if not fin:
            fin = prologo()
            if not fin:
                fin = postprologo()
                if not fin:
                    level(nivelActual)
    musica = pygame.mixer.music.load('stage-theme.mp3')
    pygame.mixer.music.play(-1)

    #CICLO PRINCIPAL
    while not fin:
    #NIVEL COMPLETADO
        if len(bombas) == 0 and not spawner:
            if nivelActual == 1:
                fin = ganar()
                nivelActual += 1
                level(nivelActual)
                musica = pygame.mixer.music.load('stage-theme.mp3')
                pygame.mixer.music.play(-1)
                enemigosA = pygame.sprite.Group()
                enemigosB = pygame.sprite.Group()
                bombas = pygame.sprite.Group()
                rayos = pygame.sprite.Group()
                jefes = pygame.sprite.Group()
                generadores = pygame.sprite.Group()
                ventajas = pygame.sprite.Group()
                jugadores = pygame.sprite.Group()
                spp = printsprites(imagen,mp2,mapa2)
                bloques = spp[0]
                muros = spp[1]
                pospawner = [576,384]
                pospawner2 = [576,320]
                g = spawn(imgSpawn,pospawner,1)
                gg = spawn(imgSpawn,pospawner2,2)
                generadores.add(g)
                generadores.add(gg)
                temp = 0
                temp2 = 0
                temp3 = 0
                temp4 = 0
                temp5 = 0
                estallar = False
                spawner = True
                tiempo = 0
                limiteEnemigosA = 6
                limiteEnemigosB = 5
                lim=180
                segundo = 0
                seg=0
                f.mover = 0
                cont = random.randrange(0,len(muros) - 1)
                cont2 = random.randrange(0,len(muros) - 1)
                cont3 = random.randrange(0,len(muros) - 1)
                while cont == cont2 or cont2 == cont3 or cont3 == cont:
                    if cont == cont2 or cont == cont3:
                        cont = random.randrange(0,len(muros) - 1)
                    else:
                        cont3 = random.randrange(0,len(muros) - 1)

                for mr in muros:
                    cont = cont - 1
                    cont2 = cont2 - 1
                    cont3 = cont3 - 1
                    if cont == 0:
                        v = ventaja(ventajaBomba,[mr.rect.x,mr.rect.y],0)
                        ventajas.add(v)
                    if cont2 == 0:
                        vv = ventaja(ventajaDetonador,[mr.rect.x,mr.rect.y],1)
                        ventajas.add(vv)
                    if cont3 == 0:
                        vv = ventaja(ventajaFuego,[mr.rect.x,mr.rect.y],2)
                        ventajas.add(vv)
                j = jugador(abajo)
                jugadores.add(j)
            elif nivelActual == 2:
                fin = ganar()
                fin = interludio()
                if not fin:
                    nivelActual += 1
                    musica = pygame.mixer.music.load('BossFight.mp3')
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    enemigosA = pygame.sprite.Group()
                    enemigosB = pygame.sprite.Group()
                    bombas = pygame.sprite.Group()
                    rayos = pygame.sprite.Group()
                    generadores = pygame.sprite.Group()
                    ventajas = pygame.sprite.Group()
                    jugadores = pygame.sprite.Group()
                    jefes = pygame.sprite.Group()
                    bloques = pygame.sprite.Group()
                    muros = pygame.sprite.Group()
                    spp = printsprites(imagen,mp3,mapa3)
                    bloques = spp[0]
                    muros = spp[1]
                    pospawner = [608,384]
                    pospawner2 = [608,0]
                    g = spawn(imgSpawn,pospawner,1)
                    gg = spawn(imgSpawn,pospawner2,2)
                    generadores.add(g)
                    generadores.add(gg)
                    temp = 0
                    temp2 = 0
                    temp3 = 0
                    temp4 = 0
                    temp5 = 0
                    estallar = False
                    spawner = True
                    tiempo = 0
                    limiteEnemigosA = 6
                    limiteEnemigosB = 5
                    lim=180
                    segundo = 0
                    seg=0
                    vidaJefe = 3
                    f.mover = 0
                    j = jugador(abajo)
                    jugadores.add(j)

                    fj = jefe(babajo,[576,224])
                    jefes.add(fj)
            elif nivelActual == 3:
                fin = ganar2()
                fin = completado()
                nivelActual = 1
                if not fin:
                    fin = inicio()
                    if not fin:
                        level(nivelActual)
                        musica = pygame.mixer.music.load('stage-theme.mp3')
                        pygame.mixer.music.play(-1)
                        enemigosA = pygame.sprite.Group()
                        enemigosB = pygame.sprite.Group()
                        bombas = pygame.sprite.Group()
                        rayos = pygame.sprite.Group()
                        generadores = pygame.sprite.Group()
                        ventajas = pygame.sprite.Group()
                        jugadores = pygame.sprite.Group()
                        jefes = pygame.sprite.Group()
                        spp = printsprites(imagen,mp,mapa)
                        bloques = spp[0]
                        muros = spp[1]
                        pospawner = [608,384]
                        pospawner2 = [576,320]
                        g = spawn(imgSpawn,pospawner,1)
                        gg = spawn(imgSpawn,pospawner2,2)
                        generadores.add(g)
                        generadores.add(gg)
                        temp = 0
                        temp2 = 0
                        temp3 = 0
                        temp4 = 0
                        temp5 = 0
                        controlador = False
                        estallar = False
                        spawner = True
                        tiempo = 0
                        cantBomb = 1
                        longrayo = 1
                        limiteEnemigosA = 4
                        limiteEnemigosB = 3
                        lim=180
                        segundo = 0
                        seg=0
                        f.mover = 0
                        cont = random.randrange(0,len(muros) - 1)
                        cont2 = random.randrange(0,len(muros) - 1)
                        cont3 = random.randrange(0,len(muros) - 1)
                        while cont == cont2 or cont2 == cont3 or cont3 == cont:
                            if cont == cont2 or cont == cont3:
                                cont = random.randrange(0,len(muros) - 1)
                            else:
                                cont3 = random.randrange(0,len(muros) - 1)
                        for mr in muros:
                            cont = cont - 1
                            cont2 = cont2 - 1
                            cont3 = cont3 - 1
                            if cont == 0:
                                v = ventaja(ventajaBomba,[mr.rect.x,mr.rect.y],0)
                                ventajas.add(v)
                            if cont2 == 0:
                                vv = ventaja(ventajaDetonador,[mr.rect.x,mr.rect.y],1)
                                ventajas.add(vv)
                            if cont3 == 0:
                                vv = ventaja(ventajaFuego,[mr.rect.x,mr.rect.y],2)
                                ventajas.add(vv)
                        j = jugador(abajo)
                        jugadores.add(j)
        if j.vivo == True:
            for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior

    #GESTION DE EVENTOS

                if event.type == pygame.QUIT:
                    select.play()
                    fin=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        j.limite = 2
                        j.im = derecha
                        j.mover = True
                        j.velx = 4
                        j.vely = 0
                        f.velx = 0

                    if event.key == pygame.K_LEFT:
                        j.limite = 2
                        j.im = izquierda
                        j.mover = True
                        j.velx = -4
                        j.vely = 0
                        f.velx = 0

                    if event.key == pygame.K_UP:
                        j.limite = 2
                        j.im = arriba
                        j.mover = True
                        j.vely = -4
                        j.velx = 0
                    if event.key == pygame.K_DOWN:
                        j.limite = 2
                        j.im = abajo
                        j.mover = True
                        j.vely = 4
                        j.velx = 0
                    if event.key == pygame.K_p:
                        #Mostrado de menu pausa
                        select.play()
                        reloj.tick(3)
                        ls = pausa()
                        pygame.mixer.music.set_volume(1)
                        fin = ls[0]
                        pause = ls[1]
                        if not fin and not pause:
                            jugadores.remove(j)
                            pygame.mixer.music.stop()
                            fin = inicio()
                            nivelActual = 1
                            if not fin:
                                level(nivelActual)
                                musica = pygame.mixer.music.load('stage-theme.mp3')
                                pygame.mixer.music.play(-1)
                                enemigosA = pygame.sprite.Group()
                                enemigosB = pygame.sprite.Group()
                                bombas = pygame.sprite.Group()
                                rayos = pygame.sprite.Group()
                                generadores = pygame.sprite.Group()
                                ventajas = pygame.sprite.Group()
                                jugadores = pygame.sprite.Group()
                                jefes = pygame.sprite.Group()
                                spp = printsprites(imagen,mp,mapa)
                                bloques = spp[0]
                                muros = spp[1]
                                pospawner = [608,384]
                                pospawner2 = [576,320]
                                g = spawn(imgSpawn,pospawner,1)
                                gg = spawn(imgSpawn,pospawner2,2)
                                generadores.add(g)
                                generadores.add(gg)
                                temp = 0
                                temp2 = 0
                                temp3 = 0
                                temp4 = 0
                                temp5 = 0
                                controlador = False
                                estallar = False
                                spawner = True
                                tiempo = 0
                                cantBomb = 1
                                longrayo = 1
                                limiteEnemigosA = 4
                                limiteEnemigosB = 3
                                lim=180
                                segundo = 0
                                seg=0
                                vidasJugador = 3
                                f.mover = 0
                                cont = random.randrange(0,len(muros) - 1)
                                cont2 = random.randrange(0,len(muros) - 1)
                                cont3 = random.randrange(0,len(muros) - 1)
                                while cont == cont2 or cont2 == cont3 or cont3 == cont:
                                    if cont == cont2 or cont == cont3:
                                        cont = random.randrange(0,len(muros) - 1)
                                    else:
                                        cont3 = random.randrange(0,len(muros) - 1)

                                for mr in muros:
                                    cont = cont - 1
                                    cont2 = cont2 - 1
                                    cont3 = cont3 - 1
                                    if cont == 0:
                                        v = ventaja(ventajaBomba,[mr.rect.x,mr.rect.y],0)
                                        ventajas.add(v)
                                    if cont2 == 0:
                                        vv = ventaja(ventajaDetonador,[mr.rect.x,mr.rect.y],1)
                                        ventajas.add(vv)
                                    if cont3 == 0:
                                        vv = ventaja(ventajaFuego,[mr.rect.x,mr.rect.y],2)
                                        ventajas.add(vv)
                                j = jugador(abajo)
                                jugadores.add(j)
                        else:
                            musica = pygame.mixer.music.load('stage-theme.mp3')
                            pygame.mixer.music.play(-1)
                #Creacion de Bombas en posicion del jugador
                    if event.key == pygame.K_z:
                        x = j.rect.x
                        y = j.rect.y
                        if len(bombas) < cantBomb:
                            ponerBomba.play()
                            b = bomba(bs,posbomba(x+15,y+15))
                            bombas.add(b)
                    if event.key == pygame.K_x:
                        if len(bombas) != 0:
                            estallar = True
                        else:
                            estallar = False
                        tiempo = 0
                        if controlador:
                            for b in bombas:
                                if tiempo > b.time:
                                    pass
                                else:
                                    tiempo = b.time
                            for b in bombas:
                                if b.time == tiempo:
                                    b.remover = True
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_RIGHT:
                        j.mover = False
                        f.mover = 0
                        j.velx = 0
                        j.vely = 0
                        for m in muros:
                            m.velx = 0
                            m.vely = 0
                        for bl in bloques:
                            bl.vely = 0
                            bl.velx = 0
                        for gn in generadores:
                            gn.vely = 0
                            gn.velx = 0
                            pospawner = [gn.rect.x,gn.rect.y]
                        for vn in ventajas:
                            vn.vely = 0
                            vn.velx = 0
                        for bm in bombas:
                            bm.vely = 0
                            bm.velx = 0
                        for rr in rayos:
                            rr.vely = 0
                            rr.velx = 0
                    if event.key == pygame.K_LEFT:
                        j.mover = False
                        f.mover = 0
                        j.velx = 0
                        j.vely = 0
                        for m in muros:
                            m.velx = 0
                            m.vely = 0
                        for bl in bloques:
                            bl.vely = 0
                            bl.velx = 0
                        for gn in generadores:
                            gn.vely = 0
                            gn.velx = 0
                            pospawner = [gn.rect.x,gn.rect.y]
                        for vn in ventajas:
                            vn.vely = 0
                            vn.velx = 0
                        for bm in bombas:
                            bm.vely = 0
                            bm.velx = 0
                        for rr in rayos:
                            rr.vely = 0
                            rr.velx = 0
                    if event.key == pygame.K_UP:
                        j.mover = False
                        j.vely = 0
                        j.velx = 0
                    if event.key == pygame.K_DOWN:
                        j.mover= False
                        j.vely = 0
                        j.velx = 0

        #Mostrado de fin del juego
        else:
            j.velx = 0
            j.vely = 0
            j.mover = True
            j.limite = 6
            j.im = animuerte
            if reproducir:
                muertoJ.play()
                vidasJugador -= 1
                reproducir = False
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.rewind()
            if j.con == 6:
                jugadores.remove(j)
                reproducir = True
                if vidasJugador == 0:
                    fin = finJuego()
                    if not fin:
                        pygame.mixer.music.stop()
                        fin = inicio()
                        nivelActual = 1
                        if not fin:
                            level(nivelActual)
                        musica = pygame.mixer.music.load('stage-theme.mp3')
                        pygame.mixer.music.play(-1)
                        enemigosA = pygame.sprite.Group()
                        enemigosB = pygame.sprite.Group()
                        bombas = pygame.sprite.Group()
                        rayos = pygame.sprite.Group()
                        generadores = pygame.sprite.Group()
                        ventajas = pygame.sprite.Group()
                        jefes = pygame.sprite.Group()
                        spp = printsprites(imagen,mp,mapa)
                        bloques = spp[0]
                        muros = spp[1]
                        pospawner = [608,384]
                        pospawner2 = [576,320]
                        g = spawn(imgSpawn,pospawner,1)
                        gg = spawn(imgSpawn,pospawner2,2)
                        generadores.add(g)
                        generadores.add(gg)
                        temp = 0
                        temp2 = 0
                        temp3 = 0
                        temp4 = 0
                        temp5 = 0
                        controlador = False
                        estallar = False
                        spawner = True
                        tiempo = 0
                        cantBomb = 1
                        longrayo = 1
                        f.mover = 0
                        limiteEnemigosA = 4
                        limiteEnemigosB = 3
                        lim=180
                        segundo = 0
                        seg=0
                        vidasJugador = 3
                        vidaJefe = 3
                        cont = random.randrange(0,len(muros) - 1)
                        cont2 = random.randrange(0,len(muros) - 1)
                        cont3 = random.randrange(0,len(muros) - 1)
                        while cont == cont2 or cont2 == cont3 or cont3 == cont:
                            if cont == cont2 or cont == cont3:
                                cont = random.randrange(0,len(muros) - 1)
                            else:
                                cont3 = random.randrange(0,len(muros) - 1)

                        for mr in muros:
                            cont = cont - 1
                            cont2 = cont2 - 1
                            cont3 = cont3 - 1
                            if cont == 0:
                                v = ventaja(ventajaBomba,[mr.rect.x,mr.rect.y],0)
                                ventajas.add(v)
                            if cont2 == 0:
                                vv = ventaja(ventajaDetonador,[mr.rect.x,mr.rect.y],1)
                                ventajas.add(vv)
                            if cont3 == 0:
                                vv = ventaja(ventajaFuego,[mr.rect.x,mr.rect.y],2)
                                ventajas.add(vv)
                        j = jugador(abajo)
                        jugadores.add(j)
                else:
                    reloj.tick(0.8)
                    pantalla.fill([0,0,0])
                    level(nivelActual)

                    enemigosA = pygame.sprite.Group()
                    enemigosB = pygame.sprite.Group()
                    bombas = pygame.sprite.Group()
                    rayos = pygame.sprite.Group()
                    generadores = pygame.sprite.Group()
                    ventajas = pygame.sprite.Group()
                    jefes = pygame.sprite.Group()
                    if nivelActual == 1:
                        spp = printsprites(imagen,mp,mapa)
                        musica = pygame.mixer.music.load('stage-theme.mp3')
                        pygame.mixer.music.play(-1)
                        pospawner = [608,384]
                        pospawner2 = [576,320]
                        limiteEnemigosA = 4
                        limiteEnemigosB = 3
                    if nivelActual == 2:
                        spp = printsprites(imagen,mp2,mapa2)
                        musica = pygame.mixer.music.load('stage-theme.mp3')
                        pygame.mixer.music.play(-1)
                        pospawner = [576,384]
                        pospawner2 = [576,320]
                        limiteEnemigosB = 5
                        limiteEnemigosA = 6

                    if nivelActual == 3:
                        musica = pygame.mixer.music.load('BossFight.mp3')
                        pygame.mixer.music.play(-1)
                        spp = printsprites(imagen,mp3,mapa3)
                        pospawner = [608,384]
                        pospawner2 = [608,0]
                        fj = jefe(babajo,[580,200])
                        jefes.add(fj)
                        vidaJefe = 3
                        limiteEnemigosB = 5
                        limiteEnemigosA = 6
                    bloques = spp[0]
                    muros = spp[1]
                    g = spawn(imgSpawn,pospawner,1)
                    gg = spawn(imgSpawn,pospawner2,2)
                    generadores.add(g)
                    generadores.add(gg)
                    temp = 0
                    temp2 = 0
                    temp3 = 0
                    temp4 = 0
                    temp5 = 0
                    controlador = False
                    estallar = False
                    spawner = True
                    tiempo = 0
                    cantBomb = 1
                    longrayo = 1
                    f.mover = 0
                    lim=180
                    segundo = 0
                    seg=0
                    if nivelActual != 3:
                        cont = random.randrange(0,len(muros) - 1)
                        cont2 = random.randrange(0,len(muros) - 1)
                        cont3 = random.randrange(0,len(muros) - 1)
                        while cont == cont2 or cont2 == cont3 or cont3 == cont:
                            if cont == cont2 or cont == cont3:
                                cont = random.randrange(0,len(muros) - 1)
                            else:
                                cont3 = random.randrange(0,len(muros) - 1)

                        for mr in muros:
                            cont = cont - 1
                            cont2 = cont2 - 1
                            cont3 = cont3 - 1
                            if cont == 0:
                                v = ventaja(ventajaBomba,[mr.rect.x,mr.rect.y],0)
                                ventajas.add(v)
                            if cont2 == 0:
                                vv = ventaja(ventajaDetonador,[mr.rect.x,mr.rect.y],1)
                                ventajas.add(vv)
                            if cont3 == 0:
                                vv = ventaja(ventajaFuego,[mr.rect.x,mr.rect.y],2)
                                ventajas.add(vv)
                    j = jugador(abajo)
                    jugadores.add(j)


#GESTION DE ENEMIGOS

    #GESTION DEL JEFE
        jefes.update()

        #Eliminacion de enemigos luego de mostrar animacion de muerte
        for jf in jefes:
            if vidaJefe == 0:
                hh = [jf.rect.x,jf.rect.y]
                jefes.remove(jf)
                spawner = False

        #Cambio de movimiento cuando el temporizador 2 es igual aun random
        for jf in jefes:
            if temp5 == random.randrange(0,70):
                if jf.velx > 0:
                    jf.velx = 0
                    jf.vely = 4
                    temp5 = 0
                elif jf.velx < 0:
                    jf.velx = 0
                    jf.vely = -4
                    temp5 = 0
                elif jf.vely > 0:
                    jf.velx = 4
                    jf.vely = 0
                    temp5 = 0
                elif jf.vely < 0:
                    jf.velx = -4
                    jf.vely = 0
                    temp5 = 0
            else:
                temp5 += 1

        #Coliciones Jefes contra Bordes pantalla
        for jf in jefes:
            if jf.rect.x > (ancho - jf.rect.width):
                jf.rect.x = ancho - jf.rect.width
                jf.velx = -4
                temp5 = 0
            if jf.rect.x < 0:
                jf.rect.x = 0
                jf.velx = 4
                temp5 = 0
            if jf.rect.y > (alto - jf.rect.height):
                jf.rect.y = alto - jf.rect.height
                jf.vely = -4
                temp5 = 0
            if jf.rect.y < 0:
                jf.rect.y = 0
                jf.vely = 4
                temp5 = 0

        #Coliciones Jefes contra Bloques
        for jf in jefes:
            ls_col = pygame.sprite.spritecollide(jf,bloques, False)
            for b in ls_col:
                if jf.velx > 0:
                    if jf.rect.right > b.rect.left:
                        jf.rect.right = b.rect.left
                        jf.velx = 0
                        jf.vely = 4
                        temp5 = 0
                elif jf.velx < 0:
                    if jf.rect.left < b.rect.right:
                        jf.rect.left = b.rect.right
                        jf.velx = 0
                        jf.vely = -4
                        temp5 = 0
                elif jf.vely > 0:
                    if jf.rect.bottom > b.rect.top:
                        jf.rect.bottom = b.rect.top
                        jf.vely = 0
                        jf.velx = -4
                        temp5 = 0
                elif jf.vely < 0:
                    if jf.rect.top < b.rect.bottom:
                        jf.rect.top = b.rect.bottom
                        jf.vely = 0
                        jf.velx = 4
                        temp5 = 0



        #Coliciones Jefes contra Bombas
        for jf in jefes:
            ls_col = pygame.sprite.spritecollide(jf,bombas, False)
            for b in ls_col:
                if jf.velx > 0:
                    if jf.rect.right > b.rect.left:
                        jf.rect.right = b.rect.left
                        jf.velx = 0
                        jf.vely = 4
                        temp5 = 0
                elif jf.velx < 0:
                    if jf.rect.left < b.rect.right:
                        jf.rect.left = b.rect.right
                        jf.velx = 0
                        jf.vely = -4
                        temp5 = 0
                elif jf.vely > 0:
                    if jf.rect.bottom > b.rect.top:
                        jf.rect.bottom = b.rect.top
                        jf.vely = 0
                        jf.velx = -4
                        temp5 = 0
                elif jf.vely < 0:
                    if jf.rect.top < b.rect.bottom:
                        jf.rect.top = b.rect.bottom
                        jf.vely = 0
                        jf.velx = 4
                        temp5 = 0

        #Colision Rayos contra Jefes
        convida = 0
        tip = []
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,jefes,False)

            for e in ls:
                tip.append(b.typesig)

        for i in tip:
            for e in rayos:
                if e.type == i:
                    tip.append(e.typesig)
                    rayos.remove(e)

        for b in rayos:
            ls = pygame.sprite.spritecollide(b,jefes,False)
            if ls != []:
                rayos.remove(b)
                convida += 1

        if convida > 0:
            vidaJefe -= 1


        #Colision Jefes contra jugador
        for jf in jefes:
            ls = pygame.sprite.spritecollide(jf,jugadores,False)
            for e in ls:
                e.vivo = False


    #GESTION DE ENEMIGOS A
        enemigosA.update()

        #Eliminacion de enemigos luego de mostrar animacion de muerte
        for bm in enemigosA:
            if bm.con == 4:
                enemigosA.remove(bm)

        #Creacion de enemigos automaticamente
        if temp == 70:
            temp = 0
            temp2 = 0
            if len(enemigosA) < limiteEnemigosA and pospawner != [0,0]:
                bmb = enemigoA(IenemigoA,pospawner)
                enemigosA.add(bmb)
        else:
            temp += 1
            temp2 += 1

        #Cambio de movimiento cuando el temporizador 2 es igual aun random
        for bm in enemigosA:
            if temp2 == random.randrange(0,70):
                if bm.velx > 0:
                    bm.velx = 0
                    bm.vely = 4
                    temp2 = 0
                elif bm.velx < 0:
                    bm.velx = 0
                    bm.vely = -4
                    temp2 = 0
                elif bm.vely > 0:
                    bm.velx = 4
                    bm.vely = 0
                    temp2 = 0
                elif bm.vely < 0:
                    bm.velx = -4
                    bm.vely = 0
                    temp2 = 0

        #Coliciones EnemigosA contra Bordes pantalla
        for bm in enemigosA:
            if bm.rect.x > (ancho - bm.rect.width):
                bm.rect.x = ancho - bm.rect.width
                bm.velx = -4
                temp2 = 0
            if bm.rect.x < 0:
                bm.rect.x = 0
                bm.velx = 4
                temp2 = 0
            if bm.rect.y > (alto - bm.rect.height):
                bm.rect.y = alto - bm.rect.height
                bm.vely = -4
                temp2 = 0
            if bm.rect.y < 0:
                bm.rect.y = 0
                bm.vely = 4
                temp2 = 0

        #Coliciones EnemigosA contra Bloques
        for bm in enemigosA:
            ls_col = pygame.sprite.spritecollide(bm,bloques, False)
            for b in ls_col:
                if bm.velx > 0:
                    if bm.rect.right > b.rect.left:
                        bm.rect.right = b.rect.left
                        bm.velx = 0
                        bm.vely = 4
                        temp2 = 0
                elif bm.velx < 0:
                    if bm.rect.left < b.rect.right:
                        bm.rect.left = b.rect.right
                        bm.velx = 0
                        bm.vely = -4
                        temp2 = 0
                elif bm.vely > 0:
                    if bm.rect.bottom > b.rect.top:
                        bm.rect.bottom = b.rect.top
                        bm.vely = 0
                        bm.velx = -4
                        temp2 = 0
                elif bm.vely < 0:
                    if bm.rect.top < b.rect.bottom:
                        bm.rect.top = b.rect.bottom
                        bm.vely = 0
                        bm.velx = 4
                        temp2 = 0

        #Coliciones EnemigosA contra Muros
        for bm in enemigosA:
            ls_co = pygame.sprite.spritecollide(bm,muros, False)
            for b in ls_co:
                if bm.velx > 0:
                    if bm.rect.right > b.rect.left:
                        bm.rect.right = b.rect.left
                        bm.velx = 0
                        bm.vely = 4
                        temp2 = 0
                elif bm.velx < 0:
                    if bm.rect.left < b.rect.right:
                        bm.rect.left = b.rect.right
                        bm.velx = 0
                        bm.vely = -4
                        temp2 = 0
                elif bm.vely > 0:
                    if bm.rect.bottom > b.rect.top:
                        bm.rect.bottom = b.rect.top
                        bm.velx = -4
                        bm.vely = 0
                        temp2 = 0
                elif bm.vely < 0:
                    if bm.rect.top < b.rect.bottom:
                        bm.rect.top = b.rect.bottom
                        bm.velx = 4
                        bm.vely = 0
                        temp2 = 0

        #Coliciones enemigosA contra Bombas
        for bm in enemigosA:
            ls_col = pygame.sprite.spritecollide(bm,bombas, False)
            for b in ls_col:
                if bm.velx > 0:
                    if bm.rect.right > b.rect.left:
                        bm.rect.right = b.rect.left
                        bm.velx = 0
                        bm.vely = 4
                        temp2 = 0
                elif bm.velx < 0:
                    if bm.rect.left < b.rect.right:
                        bm.rect.left = b.rect.right
                        bm.velx = 0
                        bm.vely = -4
                        temp2 = 0
                elif bm.vely > 0:
                    if bm.rect.bottom > b.rect.top:
                        bm.rect.bottom = b.rect.top
                        bm.vely = 0
                        bm.velx = -4
                        temp2 = 0
                elif bm.vely < 0:
                    if bm.rect.top < b.rect.bottom:
                        bm.rect.top = b.rect.bottom
                        bm.vely = 0
                        bm.velx = 4
                        temp2 = 0

        #Colision Rayos contra EnemigosA
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,enemigosA,False)
            for eee in ls:
                eee.vivo = False
                eee.m = mEA
                eee.con = 0
                eee.limite = 4
                eee.velx = 0
                eee.vely = 0

        #Colision EnemigosA contra jugador
        for bm in enemigosA:
            ls = pygame.sprite.spritecollide(bm,jugadores,False)
            for e in ls:
                e.vivo = False

#GESTION ENEMIGOS B
        enemigosB.update()
        for dm in enemigosB:
            if dm.con == 4:
                enemigosB.remove(dm)
        #Creacion de enemigosB automaticamente
        if temp3 == 150:
            temp3 = 0
            temp4 = 0
            if len(enemigosB) < limiteEnemigosB and pospawner2 != [0,0]:
                dmd = enemigoB(enemigoBaa,pospawner2)
                enemigosB.add(dmd)
        else:
            temp3 += 1
            temp4 += 1

        for dm in enemigosB:
            if temp4 == random.randrange(0,50):
                if dm.velx > 0:
                    dm.velx = 0
                    dm.vely = 4
                elif dm.velx < 0:
                    dm.velx = 0
                    dm.vely = -4
                elif dm.vely > 0:
                    dm.velx = 4
                    dm.vely = 0
                elif dm.vely < 0:
                    dm.velx = -4
                    dm.vely = 0

        #Coliciones EnemigosB contra Bordes pantalla
        for dm in enemigosB:
            if dm.rect.x > (ancho - dm.rect.width):
                dm.rect.x = ancho - dm.rect.width
                dm.velx = -4
                temp4 = 0
            if dm.rect.x < 0:
                dm.rect.x = 0
                dm.velx = 4
                temp4 = 0
            if dm.rect.y > (alto - dm.rect.height):
                dm.rect.y = alto - dm.rect.height
                dm.vely = 0
                dm.velx = -4
                temp4 = 0
            if dm.rect.y < 0:
                dm.rect.y = 0
                dm.vely = 0
                dm.velx = 4
                temp4 = 0
        #Coliciones EnemigosB contra Bloques
        for dm in enemigosB:
            ls_col = pygame.sprite.spritecollide(dm,bloques, False)
            for b in ls_col:
                if bm.velx > 0:
                    if dm.rect.right > b.rect.left:
                        dm.rect.right = b.rect.left
                        dm.velx = 0
                        dm.vely = 4
                        temp4 = 0
                elif dm.velx < 0:
                    if dm.rect.left < b.rect.right:
                        dm.rect.left = b.rect.right
                        dm.velx = 0
                        dm.vely = -4
                        temp4 = 0
                elif dm.vely > 0:
                    if dm.rect.bottom > b.rect.top:
                        dm.rect.bottom = b.rect.top
                        dm.vely = 0
                        dm.velx = -4
                        temp4 = 0
                elif dm.vely < 0:
                    if dm.rect.top < b.rect.bottom:
                        dm.rect.top = b.rect.bottom
                        dm.vely = 0
                        dm.velx = 4
                        temp4 = 0

        #Coliciones enemigosB contra Bombas
        for dm in enemigosB:
            ls_col = pygame.sprite.spritecollide(dm,bombas, False)
            for b in ls_col:
                if dm.velx > 0:
                    if dm.rect.right > b.rect.left:
                        dm.rect.right = b.rect.left
                        dm.velx = 0
                        dm.vely = 4
                        temp4 = 0
                elif dm.velx < 0:
                    if dm.rect.left < b.rect.right:
                        dm.rect.left = b.rect.right
                        dm.velx = 0
                        dm.vely = -4
                        temp4 = 0
                elif dm.vely > 0:
                    if dm.rect.bottom > b.rect.top:
                        dm.rect.bottom = b.rect.top
                        dm.vely = 0
                        dm.velx = -4
                        temp4 = 0
                elif dm.vely < 0:
                    if dm.rect.top < b.rect.bottom:
                        dm.rect.top = b.rect.bottom
                        dm.vely = 0
                        dm.velx = 4
                        temp4 = 0
        #Colision Rayos contra EnemigosB
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,enemigosB,False)
            for e in ls:
                e.vivo = False
                e.m = mEB
                e.con = 0
                e.limite = 4
                e.velx = 0
                e.vely = 0
        #Colision EnemigosB contra jugador
        for dm in enemigosB:
            ls = pygame.sprite.spritecollide(dm,jugadores,False)
            for e in ls:
                e.con = 0
                e.vivo = False

#GESTION DE CONTROL
    #Control de limites de bordes de pantalla
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


    #Eliminacion Bombas Automatica y Creacion de Rayos
        for b in bombas:
            if controlador:
                if estallar:
                    estallar = False
                    if b.time == tiempo:
                        explosionSonido.play()
                        if longrayo == 1:
                            ray = printrayo(rayoimage,ry,[b.rect.x - 64,b.rect.y-64],raio)
                        elif longrayo == 2:
                            ray = printrayo2(rayoimage,ryc,[b.rect.x - 96,b.rect.y-96],raioc)
                        rayos = ray[0]
                        rayoj = ray[1]
                        puntaj = ray[2]
                        bombas.remove(b)
                        break
                elif b.estallada:
                    explosionSonido.play()
                    if longrayo == 1:
                        ray = printrayo(rayoimage,ry,[b.rect.x - 64,b.rect.y-64],raio)
                    elif longrayo == 2:
                        ray = printrayo2(rayoimage,ryc,[b.rect.x - 96,b.rect.y-96],raioc)
                    rayos = ray[0]
                    rayoj = ray[1]
                    puntaj = ray[2]
                    bombas.remove(b)
                    break
            elif b.remover:
                explosionSonido.play()
                if longrayo == 1:
                    ray = printrayo(rayoimage,ry,[b.rect.x - 64,b.rect.y-64],raio)
                elif longrayo == 2:
                    ray = printrayo2(rayoimage,ryc,[b.rect.x - 96,b.rect.y-96],raioc)
                rayos = ray[0]
                rayoj = ray[1]
                puntaj = ray[2]
                bombas.remove(b)
                break
    #Eliminacion de Rayos automatica
        for r in rayos:
            if r.remover:
                rayos.remove(r)
    #Eliminacion de Muros automatica
        for m in muros:
            if m.con == 4:
                muros.remove(m)

#GESTION DE COLISIONES

        jugadores.update()#Cambio de sitio la actualizacion del jugador para evitar problemas de movimiento

        #Coliciones Jugador contra Bloques
        ls_col = pygame.sprite.spritecollide(j,bloques, False)
        for b in ls_col:
            if j.velx > 0:
                if j.rect.right > b.rect.left:
                    j.rect.right = b.rect.left
                    j.velx = 0
            elif j.velx < 0:
                if j.rect.left < b.rect.right:
                    j.rect.left = b.rect.right
                    j.velx = 0
            elif j.vely > 0:
                if j.rect.bottom > b.rect.top:
                    j.rect.bottom = b.rect.top
                    j.vely = 0
            elif j.vely < 0:
                if j.rect.top < b.rect.bottom:
                    j.rect.top = b.rect.bottom
                    j.vely = 0

        #Coliciones Jugador contra Muros
        ls_co = pygame.sprite.spritecollide(j,muros, False)
        for b in ls_co:
            if j.velx > 0:
                if j.rect.right > b.rect.left:
                    j.rect.right = b.rect.left
                    j.velx = 0
            elif j.velx < 0:
                if j.rect.left < b.rect.right:
                    j.rect.left = b.rect.right
                    j.velx = 0
            elif j.vely > 0:
                if j.rect.bottom > b.rect.top:
                    j.rect.bottom = b.rect.top
                    j.vely = 0
            elif j.vely < 0:
                if j.rect.top < b.rect.bottom:
                    j.rect.top = b.rect.bottom
                    j.vely = 0

        #Coliciones Rayos contra Bloques
        tip = []
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,bloques,False)

            for e in ls:
                tip.append(b.typesig)
                rayos.remove(b)

        for i in tip:
            for e in rayos:
                if e.type == i:
                    rayos.remove(e)

        #Coliciones Rayos contra Muros
        tip = []
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,muros,False)

            for e in ls:
                tip.append(b.typesig)

        for i in tip:
            for e in rayos:
                if e.type == i:
                    tip.append(e.typesig)
                    rayos.remove(e)

        for b in rayos:
            ls = pygame.sprite.spritecollide(b,muros,False)
            for e in ls:
                e.con = 0
                e.animacion = True
            if ls != []:
                rayos.remove(b)


        #Colision Rayos contra Jugador
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,jugadores,False)
            for e in ls:
                j.con = 0
                j.vivo = False

        #Colision Bombas contra Rayos
        tip = []
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,bombas,False)

            for e in ls:
                tip.append(b.typesig)

        for e in rayos:
            for i in tip:
                if e.type == i:
                    rayos.remove(e)
        for b in bombas:
            ls = pygame.sprite.spritecollide(b,rayos,False)
            for e in ls:
                b.remover = True
                b.estallada = True

        #Colision jugador contra ventajas
        if len(ventajas) != 0:
            lscv = pygame.sprite.spritecollide(j,ventajas,True)
            for vn in lscv:
                poder.play()
                musica = pygame.mixer.music.load('find_the_door.mp3')
                pygame.mixer.music.play(-1)
                if vn.type == 0:
                    cantBomb = cantBomb + 1
                elif vn.type == 1:
                    controlador = True
                elif vn.type == 2:
                    longrayo = longrayo + 1
        #Colision Rayos contra Generador
        for b in rayos:
            ls = pygame.sprite.spritecollide(b,generadores,False)
            for e in ls:
                if e.tipo == 1:
                    pospawner = [0,0]
                elif e.tipo == 2:
                    pospawner2 = [0,0]
                generadores.remove(e)
                if len(generadores) == 0:
                    spawner = False
#GESTION DE PANTALLA

        fondos.draw(pantalla)
        fondos.update()
        ventajas.draw(pantalla)
        bloques.draw(pantalla)
        muros.draw(pantalla)
        bombas.draw(pantalla)
        bombas.update()
        rayos.draw(pantalla)
        generadores.draw(pantalla)
        enemigosA.draw(pantalla)
        enemigosB.draw(pantalla)
        rayos.update()
        jugadores.draw(pantalla)
        muros.update()
        bloques.update()
        ventajas.update()
        generadores.update()
        jefes.update()
        jefes.draw(pantalla)

        segundo=lim-((seg*4)//tasa)
        tiempo = ((seg*4)//tasa)
        seg+=1

        pantalla.blit(fondgris,[0,alto])
        if segundo == 0:
            j.vivo = False
        if len(jefes) > 0:
            imprimir([300,alto + 33],[0,0,0],'Jefe: '+str(vidaJefe),20)
        elif vidaJefe == 0:
            pantalla.blit(bmuerto,hh)
        imprimir([220,alto + 33],[0,0,0],'Vidas: '+str(vidasJugador),20)

        if controlador:
            cuadroCon = pygame.transform.scale(ventajaDetonador,(20, 20))
            pantalla.blit(cuadroCon,[588,alto + 33])
        if cantBomb > 1:
            cuadroBom = pygame.transform.scale(ventajaBomba,(20, 20))
            pantalla.blit(cuadroBom,[568,alto + 33])
        if longrayo > 1:
            cuadroRay = pygame.transform.scale(ventajaFuego,(20, 20))
            pantalla.blit(cuadroRay,[548,alto + 33])
        imprimir([35,alto + 33],[0,0,0],'Tiempo: '+str(segundo),20)
        imprimir([150,alto + 33],[0,0,0],'Nivel '+str(nivelActual),20)

        reloj.tick(20)
        pygame.display.flip()
        gc.collect()
