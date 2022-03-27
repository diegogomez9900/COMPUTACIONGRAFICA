import pygame

ancho = 1000
alto = 800

origeny = ancho/2
origenx = alto/2

puntos = [[50,50],[75,25],[25,75],[100,100]]

def ubicar(pos,origen):#convierte un punto de la pantalla en un punto del plano cartesiano
    posy = pos[0] + origen[0]
    posx = -1*pos[1] + origen[1]
    pygame.draw.circle(pantalla,[255,255,255],[posy,posx],2)


def ubicar_plano(p, pos):
    pygame.draw.line(p,[255,255,255],[0,pos[1]],[ancho,pos[1]])#eje x
    pygame.draw.line(p,[255,255,255],[pos[0],0],[pos[0],alto])#eje y

if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])#cambia resolucion de ventana y define una ventana llamada pantalla

    pygame.draw.line(pantalla,[255,255,255],[0,origenx],[ancho,origenx])#eje x
    pygame.draw.line(pantalla,[255,255,255],[origeny,0],[origeny,alto])#eje y

    for punto in puntos:
        ubicar(punto,[origeny,origenx])

    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(event.pos)
                pantalla.fill([0,0,0])#pinta la pantalla de un color, negro en este caso
                ubicar_plano(pantalla,event.pos)
                for punto in puntos:
                    ubicar(punto,event.pos)
                #print(transformar(event.pos))
                pygame.display.flip()
