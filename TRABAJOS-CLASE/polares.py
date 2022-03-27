import pygame
import math

ancho = 600
alto = 400
#origen cartesiano
origenx = ancho/2
origeny = alto/2

def punto_plano(pos):#convierte un punto de la pantalla en un punto del plano cartesiano, si se grafica el punto, queda como quedaria en el plano cartesiano
    posx = pos[0] + origenx
    posy = -1*pos[1] + origeny
    return ([posx,posy])

def voltear_antihorario(pos, angulo):
    x = pos[0]*math.cos(angulo) + pos[1]*math.sin(angulo)
    y = -1*pos[0]*math.sin(angulo) + pos[1]*math.cos(angulo)
    x1 = int(x)
    y1 = int(y)
    return ([x1,y1])

def rotarAH(pos2,angulo):
    angulo = math.radians(angulo)
    pos2 = voltear_antihorario(pos2,angulo)
    return (pos2)

def punto(pto):
    pygame.draw.circle(pantalla,[255,255,255],pto,2)

def escalar_punto(punto, escalar):
    x = punto[0]*escalar
    y = punto[1]*escalar
    x = int(x)
    y = int(y)
    return ([x,y])

def trasladar(punto,t):
    x = punto[0]+t[0]
    y = punto[1]+t[1]
    return ([x,y])

def escalarPF(punto1,punto2, escalar):
    punto(punto1)
    punto(punto2)

    p1=escalar_punto(punto1,-1)
    p2=escalar_punto(punto2,-1)

    pf = punto1
    t = p1

    ap = trasladar(punto1,t)
    bp = trasladar(punto2,t)

    ae = escalar_punto(ap,escalar)
    be = escalar_punto(bp,escalar)

    af = trasladar(ae,pf)
    bf = trasladar(be,pf)

    punto(af)
    punto(bf)

    #pygame.draw.line(pantalla,[255,0,255],af,bf)
    #pygame.draw.line(pantalla,[255,255,255],a,b)

    return ([af,bf])

def rotarPFAH(punto1,punto2,angulo):
    #punto(punto1)
    #punto(punto2)

    #pygame.draw.line(pantalla,[255,255,255],punto1,punto2)

    p1=escalar_punto(punto1,-1)
    p2=escalar_punto(punto2,-1)

    pf = punto1
    t = p1

    ap = trasladar(punto1,t)
    bp = trasladar(punto2,t)

    be = rotarAH(bp,angulo)

    af = trasladar(ap,pf)
    bf = trasladar(be,pf)

    #punto(af)
    #punto(bf)
    #pygame.draw.line(pantalla,[255,255,255],af,bf)

    return ([af,bf])

def polar(r,angulo):
    x = r*math.cos(math.radians(angulo))
    y = r*math.sin(math.radians(angulo))
    x = int(x)
    y = int(y)
    return ([x,y])

def polares(r,angulo):
    pos = []
    pos = polar(r,angulo)
    pos = punto_plano(pos)
    punto(pos)

def dibujar_poligono(posiciones,color):#dibuja un poligono creando lineas desde el punto 1 hasta el punto 2, y asi, de la list de puntos posiciones
    i = 0
    for pos in posiciones:
        if(i==0):
            p = pos
            i = 1
        else:
            pygame.draw.line(pantalla,color,p,pos)
            p=pos
    pygame.draw.line(pantalla,color,posiciones[0],posiciones[len(posiciones) - 1])

def dibujar_po_re(lados, r):
    cambio = 360/lados
    i = 0
    angulo = 0
    ls = []
    pos=[]
    while (i != lados):
        pos = polar(r,angulo)
        pos = punto_plano(pos)
        punto(pos)
        ls.append(pos)
        if (i == lados):
            flag = 1
        else:
            angulo = angulo + cambio
            i = i + 1

    print(ls)
    dibujar_poligono(ls,[255,0,255])

if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    a = [300,200]
    b = [400,200]

    #polares(10,350)
    dibujar_po_re(10,100)
    pygame.display.flip() #flip, refresca la pantalla


    fin = False
    angulo = 90
    r = math.sin(2*(math.radians(angulo)))
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #    polares(r,angulo)
        #        angulo += 1
        #        r = 2*math.sin(3*math.radians(angulo))*50
        #    pygame.display.flip()
