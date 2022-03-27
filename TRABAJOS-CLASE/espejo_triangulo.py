import pygame

#dimensiones de la pantalla
ancho = 600
alto = 400
#origen cartesiano
origenx = ancho/2
origeny = alto/2

origen=[origenx,origeny]

def escalar_punto(punto, escalar):
    x = punto[0]*escalar
    y = punto[1]*escalar
    x = int(x)
    y = int(y)
    return ([x,y])

def dibujar_triangulo(pos1,pos2,pos3,color):
    pygame.draw.line(pantalla,color,pos1,pos2)
    pygame.draw.line(pantalla,color,pos2,pos3)
    pygame.draw.line(pantalla,color,pos3,pos1)

def punto_plano(pos):#convierte un punto de la pantalla en un punto del plano cartesiano, si se grafica el punto, queda como quedaria en el plano cartesiano
    posx = pos[0] + origenx
    posy = -1*pos[1] + origeny
    return ([posx,posy])

def punto(pto):#dibuja un punto en la pantalla de color blanco
    pygame.draw.circle(pantalla,[255,255,255],pto,2)

def ubicar_plano(pos):#ubica el origen del un plano cartesiano en la posicion pos
    pygame.draw.line(pantalla,[255,255,255],[0,pos[1]],[ancho,pos[1]])#eje x
    pygame.draw.line(pantalla,[255,255,255],[pos[0],0],[pos[0],alto])#eje y

def punto_menor(punto1,punto2):#retorna el punto menor entre dos puntos
    if(punto1[0] >= punto2[0]):
        x = punto2[0]
    else:
        x = punto1[0]

    if(punto1[1] >= punto2[1]):
        y = punto2[1]
    else:
        y = punto1[1]
    return ([x,y])

def trasladar(punto,t):
    x = punto[0]+t[0]
    y = punto[1]+t[1]
    return ([x,y])

def mover(pos1,pos2,pos3):
    p = punto_menor(pos1,pos2)
    pos1 = punto_plano(pos1)
    pos2 = punto_plano(pos2)
    pos3 = punto_plano(pos3)

    if (p==pos1):
        p = punto_menor(pos1,pos3)
    else:
        p = punto_menor(pos2,pos3)

    pp = escalar_punto(p,-2)

    ae = [pos1[0],(pos1[1]-pp[1])]
    be = [pos2[0],(pos2[1]-pp[1])]
    ce = [pos3[0],(pos3[1]-pp[1])]

    print(ae,be,ce)
    dibujar_triangulo((ae),(be),(ce),[0,255,255])


if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    pygame.display.flip() #flip, refresca la pantalla
    a=[100,50]
    b=[50,100]
    c=[100,100]
    d=[200,300]
    ubicar_plano(origen)
    ae = escalar_punto(a,-1)#si escalo el punto por -1, sale en cuadrante opuesto y rotado
    be = escalar_punto(b,-1)
    ce = escalar_punto(c,-1)
    dibujar_triangulo(punto_plano(a),punto_plano(b),punto_plano(c),[0,255,255])
    #dibujar_triangulo(punto_plano(ae),punto_plano(be),punto_plano(ce),[0,255,255])
    mover(a,b,c)

    pygame.display.flip()

    fin = False

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print(punto_plano(event.pos))
