import pygame

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

#def escalarPFlinea(a,b,escalar):

if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([800,700])#cambia resolucion de ventana y define una ventana llamada pantalla


    a = [50,25]
    b = [100,25]
    c = [100,100]

    escalarPF(a,b,3)#primer punto es el punto fijo

    pygame.display.flip()
    fin = False

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
