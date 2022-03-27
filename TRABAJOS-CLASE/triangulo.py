import pygame

ancho = 600
alto = 400

origeny = ancho/2
origenx = alto/2

def ubicar(p, posx, posy):
    pygame.draw.circle(p,[255,255,255],[posy,posx],2)
    return (transformar([posy,posx]))

def transformar(pos):#convierte un punto de la pantalla en un punto del plano cartesiano
    posy = pos[0] + origeny
    posx = -1*pos[1] + origenx
    return ([posy-ancho,posx])

def ubicar_mouse(p,pos):
    pygame.draw.circle(p,[255,255,255],pos,2)


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])#cambia resolucion de ventana y define una ventana llamada pantalla

    pygame.display.flip()

    fin = False
    ls = []
    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                ls.append(event.pos)
                ubicar_mouse(pantalla,event.pos)
                #print(destransformar(event.pos))
                print(transformar(event.pos))
                i = len(ls)
                if (i == 3):
                    pygame.draw.line(pantalla,[255,0,0],ls[0],ls[1])
                    pygame.draw.line(pantalla,[255,0,0],ls[1],ls[2])
                    pygame.draw.line(pantalla,[255,0,0],ls[0],ls[2])
                    ls = []
                pygame.display.flip()
