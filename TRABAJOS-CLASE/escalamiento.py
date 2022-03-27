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

def ubicar2(pos, escalar):#convierte un punto de la pantalla en un punto del plano cartesiano
    x = pos[0]
    y = pos[1]
    pos[0] = x*escalar
    pos[1] = y*escalar
    posy = pos[0] + origeny
    posx = -1*pos[1] + origenx
    pygame.draw.circle(pantalla,[255,255,255],[posy,posx],2)


#def escalamiento(pos1, pos2, escalar):
#    pos1 = transformar(pos1)
#    pos2 = transformar(pos2)
#    pygame.draw.line(pantalla, [255,255,255], pos1, [pos1*escalar,pos2x*escalar],1)

def transformar(pos):#convierte un punto de la pantalla en un punto del plano cartesiano
    posy = pos[0] + origeny
    posx = -1*pos[1] + origenx
    return ([posy-ancho,posx])

def destransformar(pos):#convierte un punto de la pantalla en un punto del plano cartesiano
    posy = pos[0] - origeny
    posx = -1*pos[1] - origenx
    return ([posy,posx])

def ubicar_mouse(p,pos):
    pygame.draw.circle(p,[255,255,255],pos,2)

if __name__ == '__main__':
    ancho = 600
    alto = 400

    origeny = ancho/2
    origenx = alto/2

    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])#cambia resolucion de ventana y define una ventana llamada pantalla

    pygame.draw.line(pantalla,[255,255,255],[0,origenx],[ancho,origenx])#eje x
    pygame.draw.line(pantalla,[255,255,255],[origeny,0],[origeny,alto])#eje y
    ubicar2([5,5],5)
    ubicar2([10,10],5)
    ubicar2([50,100],2)
    #escalamiento([5,5], [10,10], 3)

    pygame.display.flip()


    fin = False
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                ubicar_mouse(pantalla,event.pos)
                #print(destransformar(event.pos))
                print(transformar(event.pos))
                pygame.display.flip()
