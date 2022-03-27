import pygame
#dimensiones de la pantalla
ancho = 600
alto = 400
#origen cartesiano
origenx = ancho/2
origeny = alto/2

def punto_plano(pos):#convierte un punto de la pantalla en un punto del plano cartesiano, si se grafica el punto, queda como quedaria en el plano cartesiano
    posx = pos[0] + origenx
    posy = -1*pos[1] + origeny
    return ([posx,posy])


def ubicar(p, posx, posy):#ubica un punto en coordenadas de pantalla y lo retorna en coordenadas cartesianas
    pygame.draw.circle(p,[255,255,255],[posy,posx],2)
    return (punto_plano([posy,posx]))

def ubicar_plano(pos):#ubica el origen del un plano cartesiano en la posicion pos
    pygame.draw.line(pantalla,[255,255,255],[0,pos[1]],[ancho,pos[1]])#eje x
    pygame.draw.line(pantalla,[255,255,255],[pos[0],0],[pos[0],alto])#eje y

def ubicar_mouse(p,pos):#recibe un punto en coordenadas de pantalla y lo ubica
    pygame.draw.circle(p,[255,255,255],pos,2)

def escalar_punto(punto, escalar):#multiplica un punto por un escalar y lo retorna
    x = punto[0]*escalar
    y = punto[1]*escalar
    x = int(x)
    y = int(y)
    return ([x,y])

def trasladar(punto,t):#traslada un punto, t es lo que el punto se movera en x y en y
    x = punto[0]+t[0]
    y = punto[1]+t[1]
    return ([x,y])

def punto(pto):#dibuja un punto en la pantalla de color blanco
    pygame.draw.circle(pantalla,[255,255,255],pto,2)

def escalar_lineaPF(punto1,punto2, escalar):#escala una linea, con el primer punto recibido como punto fijo
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

def voltear_horario(pos, angulo):# devuelve un punto girado un angulo en sentido horario
    x = pos[0]*math.cos(angulo) - pos[1]*math.sin(angulo)
    y = pos[0]*math.sin(angulo) + pos[1]*math.cos(angulo)
    x1 = int(x)
    y1 = int(y)
    return ([x1,y1])

def voltear_antihorario(pos, angulo):#devuelve un punto girado un angulo en sentido antihorario
    x = pos[0]*math.cos(angulo) + pos[1]*math.sin(angulo)
    y = -1*pos[0]*math.sin(angulo) + pos[1]*math.cos(angulo)
    x1 = int(x)
    y1 = int(y)
    return ([x1,y1])

def rotarH(pos2,angulo):#rota un punto en sentido horario y lo devuelve, convierte un angulo en grados a radianes
    angulo = math.radians(angulo)
    pos2 = voltear_horario(pos2,angulo)
    return (pos2)

def rotarAH(pos2,angulo):#rota un punto en sentido antihorario y lo devuelve, convierte un angulo en grados a radianes
    angulo = math.radians(angulo)
    pos2 = voltear_antihorario(pos2,angulo)
    return (pos2)

def rotarPFH(punto1,punto2,angulo):#rota una linea en sentido con punto fijo en sentido horario
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

def rotarPFAH(punto1,punto2,angulo):#rota una linea en sentido con punto fijo en sentido antihorario
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

def dibujar_triangulo(pos1,pos2,pos3,color):
    pygame.draw.line(pantalla,color,pos1,pos2)
    pygame.draw.line(pantalla,color,pos2,pos3)
    pygame.draw.line(pantalla,color,pos3,pos1)

def rotar_poligonoH(posiciones,angulo):#rota un poligono en sentido horario
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

def rotar_poligonoAH(posiciones,angulo):#rota un poligono en sentido antihorario
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
