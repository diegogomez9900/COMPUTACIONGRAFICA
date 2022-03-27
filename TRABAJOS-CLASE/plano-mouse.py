import pygame
#from grafica import *   #importa las funciones de el archivo libreria


ancho = 600
alto = 400

origeny = ancho/2
origenx = alto/2


#pygame.draw.circle(pantalla,[255,255,255],[300,200],5)#pocion o, o
#se comentan las funciones por que estan importadas de grafica.py

def ubicar(p, posx, posy):
    pygame.draw.circle(p,[255,255,255],[posy,posx],2)
    return (transformar([posy,posx]))

def transformar(pos):#convierte un punto de la pantalla en un punto del plano cartesiano
    posy = pos[0] + origeny
    posx = -1*pos[1] + origenx
    return ([posy-ancho,posx])

def ubicar_mouse(p,pos):
    pygame.draw.circle(p,[255,255,255],pos,2)

def ubicar_plano(pos):#ubica el origen del un plano cartesiano en la posicion pos
    pygame.draw.line(pantalla,[255,255,255],[0,pos[1]],[ancho,pos[1]])#eje x
    pygame.draw.line(pantalla,[255,255,255],[pos[0],0],[pos[0],alto])#eje y


if __name__ == '__main__':
    ancho = 600
    alto = 400

    origeny = ancho/2
    origenx = alto/2

    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])#cambia resolucion de ventana y define una ventana llamada pantalla



    pygame.display.flip()


    fin = False
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(event.pos)
                pantalla.fill([0,0,0])
                ubicar_mouse(pantalla,event.pos)
                ubicar_plano(event.pos)
                print(transformar(event.pos))
                pygame.display.flip()
