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
    pos2 = punto_plano(pos2)
    pygame.draw.line(pantalla,[255,255,255],[300,200],pos2)

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([600,400])#cambia resolucion de ventana y define una ventana llamada pantalla

    pygame.display.flip() #flip, refresca la pantalla

    con = 5
    reloj = pygame.time.Clock()
    fin = False

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True

        rotarH([50,50],con)
        reloj.tick(10)#cada 10 ticks aumenta el contador
        con+=5
        pygame.display.flip()
