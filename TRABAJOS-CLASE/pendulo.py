import pygame
import math

ancho = 600
alto = 400
#origen cartesiano
origenx = ancho/2
origeny = alto/2

def punto_plano(pos):#convierte un punto de la pantalla en un punto del plano cartesiano, si se grafica el punto, queda como quedaria en el plano cartesiano
    posx = pos[0] + origenx
    posy = -1*pos[1]
    return ([posx,posy])


def punto(pto):
    pygame.draw.circle(pantalla,[255,255,255],pto,2)


def polar(r,angulo):
    x = r*math.cos(math.radians(angulo))
    y = r*math.sin(math.radians(angulo))
    x = int(x)
    y = int(y)
    return ([x,y])

def polares(r,angulo):
    pos = []
    pos = polar(r,angulo)
    po = punto_plano(pos)
    print(pos)
    pygame.draw.line(pantalla,[255,0,255],[300,0],po)
    punto(pos)

if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla
    a = [300,200]
    b = [400,200]

    pygame.display.flip() #flip, refresca la pantalla


    fin = False
    angulo1 = 300
    angulo2 = 240
    #r = math.sin(2*(math.radians(angulo)))
    reloj = pygame.time.Clock()

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            else:
                if(angulo1 <= 300):
                    polares(100,angulo1)
                    angulo1 -= 1
                    pygame.display.flip()
                    reloj.tick(60)
                    if (angulo1 == 240):
                        polares(100,angulo2)
                        pygame.display.flip()
                        reloj.tick(60)

                pantalla.fill([0,0,0])
                pygame.display.flip()
                reloj.tick(60)
