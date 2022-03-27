import pygame
import random


if __name__ == '__main__':

    pygame.init()
    pantalla = pygame.display.set_mode([620,620])#cambia resolucion de ventana y define una ventana llamada pantalla
    pygame.display.flip() #flip, refresca la pantalla

    #pygame.draw.circle(pantalla,[255,255,255],[50,60],2)
    #pygame.draw.circle(pantalla,[255,255,255],[50,560],2)
    pygame.draw.line(pantalla,[255,255,255],[50,60],[50,460],4)#linea del cabezal
    pygame.draw.circle(pantalla,[255,255,255],[65, 260], 10)#cabezal

    a = 2

#CREACION DE LA LISTA DE SECTORES Y PINTANDO PANORAMA INICIAL
    Lista = []
    cont = 0
    #INGRESANDO NUMEROS ALEATORIOS
    while cont != 20:
        Lista.append(random.randrange(200))
        cont = cont + 1

    print(Lista)
    cont = 0
    aux = 0
    num = 0
    #MODIFICANDO NUMEROS REPETIDOS, NO  DEBE HABER NINGUNO REPETIDO
    while(cont != 20):
        num = Lista[cont]
        aux = cont
        cont = cont + 1
        while(cont != 20):
            if(num == Lista[cont]):
                Lista[cont] = Lista[cont] + 1
            cont = cont + 1
        cont = aux + 1
    print(Lista)
    cont = 0
    #ASIGNANDO COLORES ALEATORIOS Y POSICIONES A CADA PISTA
    while cont != 20:
        pygame.draw.circle(pantalla,[cont*10 + random.randrange(50),cont*10 + random.randrange(50),cont*10 + random.randrange(50)],[cont*10 + 400, Lista[cont]*2 + 60], 3)
        cont = cont + 1
    print(Lista[0])
    fin = False

    while not fin:
        for event in pygame.event.get():#lista de eventos, tambien event=pygame.event.get(), cambiando el for asi: for e(cualquier variable) in event: siendo event la lista de eventos anterior
            if event.type == pygame.QUIT:
                fin=True
        pygame.display.flip()
