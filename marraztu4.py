#Marraztuz abestu 1.0 
#2017-10-01 krr4m4rr0 + k4t
#Kanbas bat marrazteko. Marraztutako koordenatuen arabera, soinua erreproduzitu.
#dependentziak: Pygame, fludisynth, mingus
#wav era pasatzeko, etorkizunean midito2audio? https://pypi.python.org/pypi/midi2audio/0.1.1
#https://stackoverflow.com/questions/40439367/how-to-draw-cursor-with-pygame
import sys
import pygame 
import time
import mingus
#import json
import threading
from mingus.midi import fluidsynth
from mingus.containers.note import Note

#hasieraketa

pygame.init()

#*******************konstante eta aldagaien deklarazioa*******************
# koloreak RGB formatuan
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
white = [255,255,255]
#leihoaren tamaina
size = [960,540]
zerrenda = []
zerrendaBase = []
nirekatea = "{"
#beharrezko irudien karga
Cursor = pygame.image.load('/home/galtzagorri/Mahaigaina/cursor.png')
Cursor_Clicked = pygame.image.load('/home/galtzagorri/Mahaigaina/cursor_clicked.png')
ikono_garbitu = pygame.image.load('/home/galtzagorri/Mahaigaina/garbitu.png')
ikono_erreproduzitu = pygame.image.load('/home/galtzagorri/Mahaigaina/media-playback-start.png')
fondorako = pygame.image.load('/home/galtzagorri/Mahaigaina/musikapp.png')

#***********************pantaila eta erlojuaren hasieraketa***************
screen=pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption("Marraztuz abestu")
pygame.mouse.set_visible(0)
done = False
mouse_down = False
clock = pygame.time.Clock()
screen.blit(fondorako,(0,0)) 

#koordenatua klasea, puntu guztiak objetu moduan errejistratzeko
class Koordenatua():
    posx = 0
    posy = 0
    kolorea = "gorria"
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

#Marrazkiaren koordenatuak pantailatik bistaratzeko funtzioa ( y koordenatua ) 
def erreproduzitu_sekuentzia():
    for i in range(0,len(zerrenda)):
        print zerrenda[i].posy


#Marrazkiko koordenatuak fluidsynth bitartez erreproduzitzeko funtzioa ( koordenatuaren arabera)

def erreproduzitu_marrazkia(screen):
    fluidsynth.init('/home/galtzagorri/Mahaigaina/Arachno SoundFont - Version 1.0.sf2',"alsa")
    for i in range(0,len(zerrenda)):
        print zerrenda[i].posy
        nota = (zerrenda[i].posy) % 127
        fluidsynth.play_Note(nota,1,100)
        time.sleep(0.5)
   

def erreproduzitu_marrazkia2(screen):
    fluidsynth.init('/home/galtzagorri/Mahaigaina/Arachno SoundFont - Version 1.0.sf2',"alsa")
    #fluidsynth.init('/home/galtzagorri/Mahaigaina/grand-piano-YDP-20160804.sf2',"alsa")
    for i in range(0,len(zerrenda)):
        print zerrenda[i].posy
        print zerrendaBase[i].posy
        nota = (zerrenda[i].posy) % 127
        nota2 = (zerrendaBase[i].posy) % 126
        t = threading.Thread(target=fluidsynth.play_Note(nota,1,100))
        t2 = threading.Thread(target=fluidsynth.play_Note(nota2,1,100))
        #t.start()
        #t2.start()
        #fluidsynth.play_Note(nota,1,100)
        #fluidsynth.play_Note(nota2,2,100)
        time.sleep(0.5)

# menua marrazeko funtzioa
def menua_marraztu(screen):
    #menu posible bat horizontalean, garrantzitsuena: PLAY botoia, hemen klik egitean, koordenatuen araberako musika.
    # STOP-ek geratu egingo du musika
    # GARBITUk, garbitu egingo du.
    # GORDE-k konposizioa gordeko du PROGRAMAN berriro entzuteko
    # KARGATU-k fitxategiak kargatuko ditu.
    # ETORKIZUNEAN , SOINU MENUA ? 
    pygame.draw.rect(screen, GREEN, pygame.Rect(10, 10, 100, 70))
    screen.blit(ikono_garbitu,(10,0)) 
    pygame.draw.rect(screen, BLUE, pygame.Rect(120, 10, 100, 70))
    screen.blit(ikono_erreproduzitu,(120,0))
    pygame.draw.rect(screen, RED, pygame.Rect(230, 10, 100, 70))

#datuak gordetzeko, koordenatu objetuak zerrenda-n gehitu
def datuak_gorde(x,y):
    
    k = Koordenatua(x,y)
    zerrenda.append(k)
    zerrendaBase.append(k)
    print 'gordetako balioak' + str(x) + ':>' + str(y)
  
    


def marraztu_kurtsorea(screen,x,y):
    LINE_COLOR = (240,0,0)
    #image1 = pygame.Surface((50, 50))
    #image1.set_colorkey((0, 0, 0))
    #pygame.draw.line(screen, LINE_COLOR, (0, 0), (49, 49))
    #image1.convert()
    #pygame.display.flip()
    if mouse_down:
        #screen.blit(Cursor_Clicked,(x,y-48)) honekin marrazten dira objetuak!!--->
	datuak_gorde(x,y)
        #fitxategi batean gorde balioak? Hobe datu egitura batean? JSON? (x,y) koordenatuak dira. kontuz irekiera eta itxieraz "a" append
        #sys.stdout=open("/home/galtzagorri/Mahaigaina/fitxa.txt","a")
        #print(x,y)
        #sys.stdout.close()
     
        #koordenatu zehatzak erabili, aurrez kanbasa ondo erabaki EKINTZA EZBERDINAK EGIKARITZEKO
        if ((960>x>100) and (540>y>100)):
            #print "baldintza bete da"
            pygame.draw.circle(screen,(255,0,0),(x,y),10,0)
            #pygame.display.flip()
        elif ((x<100) and (y<150)):
            #garbitu!
            screen.fill(white)
            menua_marraztu(screen)
            zerrenda = []
            zerrendaBase = []
        elif (((x>120) and (x<300)) and ((y>0) and (y<150))):
            erreproduzitu_marrazkia2(screen)
            erreproduzitu_sekuentzia()
       
	
     
    else:
        #print "klik egin gabe"
        LINE_COLOR = (240,0,0)

#*****************ziklo, programa nagusia ************************
menua_marraztu(screen)
datuak = ""
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    #screen.fill(white)
    pos = pygame.mouse.get_pos()
    x=pos[0]
    y=pos[1]
    #pygame.display.flip()
    marraztu_kurtsorea(screen,x,y)
    pygame.display.flip()
    clock.tick(60)

