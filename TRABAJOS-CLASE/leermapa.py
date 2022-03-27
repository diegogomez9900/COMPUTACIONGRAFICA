import pygame
import ConfigParser

mapa = ConfigParser.ConfigParser()
mapa.read('mapa.map')
#print mapa.sections()
#print mapa.items('info')
#print mapa.get('info','mapa')

for s in mapa.sections():
    #print s
    if s == 'info':
        #print mapa.get(s,'mapa')
        mp = mapa.get(s,'mapa')
    else:
        print mapa.get(s,'tipo'), mapa.get(s,'fil'), mapa.get(s,'col')

print mp, type(mp)
