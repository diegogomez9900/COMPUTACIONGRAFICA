import pygame

#dimensiones de la pantalla
ancho = 600
alto = 400
#origen cartesiano
origenx = ancho/2
origeny = alto/2

def punto(pto):#dibuja un punto en la pantalla de color blanco
    pygame.draw.circle(pantalla,[255,255,255],pto,2)

def punto_plano(pos):#convierte un punto de la pantalla en un punto del plano cartesiano, si se grafica el punto, queda como quedaria en el plano cartesiano
    posx = pos[0] + origenx
    posy = -1*pos[1] + origeny
    return ([posx-ancho,posy])

def ubicar_plano(pos):#ubica el origen del un plano cartesiano en la posicion pos
    pygame.draw.line(pantalla,[255,255,255],[0,pos[1]],[ancho,pos[1]])#eje x
    pygame.draw.line(pantalla,[255,255,255],[pos[0],0],[pos[0],alto])#eje y

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

def trasladar(punto,t):#traslada un punto, t es lo que el punto se movera en x y en y
    x = punto[0]+t[0]
    y = punto[1]+t[1]
    return ([x,y])

def escalar_punto(punto, escalar):#multiplica un punto por un escalar y lo retorna
    x = punto[0]/3
    y = punto[1]/3
    x = int(x)
    y = int(y)
    return ([x,y])

def escalar_poligono(posiciones, escalar):#escala una linea, con el primer punto recibido como punto fijo
    ls=[]
    for punto in posiciones:
        p1=escalar_punto(punto,-1)
        ls.append(p1)

    pf = posiciones[0]
    t = ls[0]
    ls_p=[]
    for punto in posiciones:
        ap = trasladar(punto,t)
        ls_p.append(ap)

    ls_e = []
    for punto in posiciones:
        ae = escalar_punto(punto,1)
        ls_e.append(ae)

    ls_f=[]
    for punto in ls_e:
        af = trasladar(punto,pf)
        ls_f.append(af)

    for pto in ls_f:
        pygame.draw.circle(pantalla,[255,0,0],pto,2)

    dibujar_poligono(ls_f,[255,255,0])


def escalar5(p,escalar):

    p[0] = escalar_punto(p[0],1)
    p[1] = escalar_punto(p[1],1)
    p[2] = escalar_punto(p[2],1)
    p[3] = escalar_punto(p[3],1)
    p[4] = escalar_punto(p[4],1)


    dibujar_poligono(p,[200,2,255])

if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])#cambia resolucion de ventana y define una ventana llamada pantalla
    ubicar_plano([origenx,origeny])

    pygame.display.flip() #flip, refresca la pantalla





    fin = False
    p=[]
    poss=[]
    i = 0
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                p = punto_plano(event.pos)
                print(p)
                if(p[0] >= 0):
                    if(p[1] <= 0):
                        punto(event.pos)
                        i += 1
                        poss.append(event.pos)

                if (i == 5):
                    dibujar_poligono(poss,[0,255,255])
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if(i==5):
                    escalar5(poss,0.3)
                    poss=[]
                    i=0
        pygame.display.flip()
