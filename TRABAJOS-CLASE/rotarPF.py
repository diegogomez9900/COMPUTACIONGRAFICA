import pygame
import math

def voltear_horario(pos, angulo):
    x = pos[0]*math.cos(angulo) - pos[1]*math.sin(angulo)
    y = pos[0]*math.sin(angulo) + pos[1]*math.cos(angulo)
    x1 = int(x)
    y1 = int(y)
    return ([x1,y1])

def voltear_antihorario(pos, angulo):
    x = pos[0]*math.cos(angulo) + pos[1]*math.sin(angulo)
    y = -1*pos[0]*math.sin(angulo) + pos[1]*math.cos(angulo)
    x1 = int(x)
    y1 = int(y)
    return ([x1,y1])

def punto_plano(pos):
    x = pos[0] + 300
    y = -1*pos[1] + 200
    return ([x,y])

def rotarH(pos2,angulo):
    angulo = math.radians(angulo)
    pos2 = voltear_horario(pos2,angulo)
    return (pos2)

def rotarAH(pos2,angulo):
    angulo = math.radians(angulo)
    pos2 = voltear_antihorario(pos2,angulo)
    return (pos2)
#________________________________________________________________________________
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

def punto(pto):
    pygame.draw.circle(pantalla,[255,255,255],pto,2)

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

    pygame.draw.line(pantalla,[255,0,255],af,bf)
    pygame.draw.line(pantalla,[255,255,255],a,b)
#________________________________________________________________

def rotarPFH(punto1,punto2,angulo):
    punto(punto1)
    punto(punto2)

    pygame.draw.line(pantalla,[255,255,255],punto1,punto2)

    p1=escalar_punto(punto1,-1)
    p2=escalar_punto(punto2,-1)

    pf = punto1
    t = p1

    ap = trasladar(punto1,t)
    bp = trasladar(punto2,t)

    be = rotarH(bp,angulo)

    af = trasladar(ap,pf)
    bf = trasladar(be,pf)

    punto(af)
    punto(bf)
    pygame.draw.line(pantalla,[255,255,255],af,bf)

def rotarPFAH(punto1,punto2,angulo):
    punto(punto1)
    punto(punto2)

    pygame.draw.line(pantalla,[255,255,255],punto1,punto2)

    p1=escalar_punto(punto1,-1)
    p2=escalar_punto(punto2,-1)

    pf = punto1
    t = p1

    ap = trasladar(punto1,t)
    bp = trasladar(punto2,t)

    be = rotarAH(bp,angulo)

    af = trasladar(ap,pf)
    bf = trasladar(be,pf)

    punto(af)
    punto(bf)
    pygame.draw.line(pantalla,[255,255,255],af,bf)


def dibujar_poligono(posiciones,color):
    i = 0
    for pos in posiciones:
        if(i==0):
            p = pos
            i = 1
        else:
            pygame.draw.line(pantalla,color,p,pos)
            p=pos
    pygame.draw.line(pantalla,color,posiciones[0],posiciones[len(posiciones) - 1])

def rotar_poligonoH(posiciones,angulo):
        ls = []
        for punto in posiciones:
            p1=escalar_punto(punto,-1)
            ls.append(p1)

        pf = posiciones[0]
        t = ls[0]

        ls_p = []
        for punto in posiciones:
            ap = trasladar(punto,t)
            ls_p.append(ap)

        ls_e = []
        for punto in ls_p:
            be = rotarH(punto,angulo)
            ls_e.append(be)

        ls_f = []
        for punto in ls_e:
            af = trasladar(punto,pf)
            ls_f.append(af)

        for pto in ls_f:
            pygame.draw.circle(pantalla,[255,0,0],pto,2)

        dibujar_poligono(ls_f,[255,255,0])

def rotar_poligonoAH(posiciones,angulo):
        ls = []
        for punto in posiciones:
            p1=escalar_punto(punto,-1)
            ls.append(p1)

        pf = posiciones[0]
        t = ls[0]

        ls_p = []
        for punto in posiciones:
            ap = trasladar(punto,t)
            ls_p.append(ap)

        ls_e = []
        for punto in ls_p:
            be = rotarAH(punto,angulo)
            ls_e.append(be)

        ls_f = []
        for punto in ls_e:
            af = trasladar(punto,pf)
            ls_f.append(af)

        for pto in ls_f:
            pygame.draw.circle(pantalla,[255,0,255],pto,2)

        dibujar_poligono(ls_f,[255,0,0])

def punto_menor(punto1,punto2):
    if(punto1[0] >= punto2[0]):
        x = punto2[0]
    else:
        x = punto1[0]

    if(punto1[1] >= punto2[1]):
        y = punto2[1]
    else:
        y = punto1[1]
    return ([x,y])


if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    a = [50,50]
    b = [100,50]
    c = [50,100]
    d = [100,100]
    e = [150,50]
    f = [300,200]
    g = [300,100]
    h = [150,100]
    i = [150,200]
    j = [150, 250]
    #rotarPFH(a,c,90)
    #dibuja un pentagono
    #los puntos se deben enviar de manera que el primero y el segundo se junten
    #dibujar_poligono([a,b,c])
    #rotar_poligono([a,b,c],90)
    pygame.display.flip() #flip, refresca la pantalla



    fin = False
    angulo = 0
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                angulo += 5
                print(event.button)#imprime en consola el numero correspondiente al boton del mouse oprimido
                b = event.button#guarda en b, el numero del evento del boton
                pantalla.fill([0,0,0])
                if (b == 4):
                    rotar_poligonoH([f,g,h,i,j],angulo)

                if (b == 5):
                    rotar_poligonoAH([f,g,h,i,j],angulo)
            pygame.display.flip()
