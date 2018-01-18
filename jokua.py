# Jokutxoa 1.0
# Pygame liburutegia frogatzen
# https://stackoverflow.com/questions/10389487/spawning-multiple-of-the-same-sprite#10418347 >hainbat etsai
#https://stackoverflow.com/questions/8303685/how-would-i-display-the-score-in-this-simple-game> markagailu sinplea

# *********************************************************************************************
#1.-liburutegiak inportatu ********************************************************************
# *********************************************************************************************
import sys
import random
import pygame
from pygame.locals import *

# *********************************************************************************************
#2.- Aldagaien hasieratzea *********************************************************************
# *********************************************************************************************
erlojua = pygame.time.Clock()
pantaila = 1
bizitzak = 3

#*****************************************************************************************************************
#****************************************************************************************************************
#3.- Programa nagusirako funtzioa: main***************************************************************************
#***********************************************************************************************

def main():
    #musika gehitu **** hh instrumental bat ***
    #musikafitx = 'musika.mp3'
    pygame.init()
    #pygame.mixer.init()
    #pygame.mixer.music.load(musikafitx)
    #pygame.mixer.music.play()
    #******************************************
    #3.1.- Nagusirako aldagai eta objetuen hasieratzeak
    super = 0
    zenbatfondo = 0
    kontm = 0
    haizea = 0
    abiadura = 2
    nirekont = 0
    puntuak = 0

    #pygame.init()
    screen = pygame.display.set_mode((640, 480))
    #markagailua?

    #gure jokalaria izango dena eta fondoaren instantziak


    jokalaria = ahatetxoa()
    f = fondoa()
    # hainbat etsai batera maneiatzeko, taldea = group
    enemies = pygame.sprite.Group()

    #3.1.- JOKU programa nagusiko BEGIZTA nagusia > X sakatu arte ez da amaituko

    while True:
        font = pygame.font.Font(None, 24)
        text = font.render("[*]Puntuak: " + str(puntuak) + " [*]Bizitzak: " + str(jokalaria.bizitzak), 1, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width() / 2)
        if jokalaria.bizitzak > 0:
            nirekont = nirekont +1
            # Ekintzaren bat egon ote den konprobatu > horren araberako aldaketak
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Agur, eta eskerrik asko jolasteagatik ;)")
                    sys.exit()
                # FROGATU ERABILTZAILEAREN KONTROLA, begiratu EBENTUAK + KOORDENATU MUGAK JARRI
                # BUKATZEKO BALDINTZA EZARRI > BIZITZAK, PANTAILAK ETB. > ORAINGOZ KONTROLAK "TXAPU"
                else:
                    jokalaria.mugitu(event)
                    #print("tekla bat jo du : edozein")
            pressed = pygame.key.get_pressed()
            if pressed[K_LEFT]:
                jokalaria.move(-2, 0)
            if pressed[K_RIGHT]:
                jokalaria.move(2, 0)
            if pressed[K_UP]:
                jokalaria.move(0, -2)
            if pressed[K_DOWN]:
                jokalaria.move(0, 2)
            if pressed[K_SPACE]:
                print ("tiroo")
                tiratuta = False
                bala = jokalaria.tiro(screen, enemies)
                i = 0
                while (i < 20):
                    bala.update(screen)
                    maltzurjota = pygame.sprite.spritecollide(bala, enemies, True)
                    if maltzurjota:
                       puntuak = puntuak + 1
                       i = 20
                       bala.suntsitu()
                    else:
                        i += 1
                        bala.move(screen, 15)
            # HASI PANTAILEN LOGIKA: 2 PANTAILA, bakoitzak 2 FONDO, FONDO BAKOITZA 4 ALDIZ IKUSI
            # PANTAILAREN ARABERAKO MALTZURRAK SORTU (ENEMY KLASEAK)

            if (pantaila == 1 and kontm < 9):
                for x in range(0, 2):
                    enemies.add(Enemy(screen, 1))
                    kontm = kontm + 1
            #beste maltzurrak...#
            if (super == 1):
                for x in range(0, 2):
                    enemies.add(Enemy(screen, 2))
                    kontm = kontm + 1

            if (nirekont < 1000):
                if (nirekont == 200 or nirekont == 400 or nirekont == 500 or nirekont == 800):
                    kontm = 0
            #beste maltzurrak+++
            if (nirekont == 100 or nirekont == 200 or nirekont == 300 or nirekont == 1000 or nirekont == 1200):
                super = 1
            else:
                super = 0

            enemies.update()
            f.move(-2)
            f.update(screen)
            jokalaria.update(screen)
            enemies.draw(screen)
            # markagailua inprimatu
            screen.blit(text, textpos)
            # jokalaria.update(screen)
            jokajota = pygame.sprite.spritecollide(jokalaria, enemies, True)
            if jokajota:
                jokalaria.image.fill((255, 255, 255))
                jokalaria.bizitzak = jokalaria.bizitzak - 1
                print("JOKALARIAREN BIZITZAK:" + str(jokalaria.bizitzak))
                jokalaria.hasierarara()
            pygame.display.update()
            erlojua.tick(60)
        else:
            print("jokoa amaitu da!!! Puntuak = " + str(jokalaria.puntuak))
            exit()

#***********************************************************************************************
#4.- Klaseak eta funtzioak **********************************************************************
#***********************************************************************************************


#********************************
# 4.2.- ENEMY KLASEA
#********************************

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, klasea):
        pygame.sprite.Sprite.__init__(self)
        #print "created a new sprite:", id(self)
        self.klasea = klasea
        if self.klasea == 1:
            self.image = pygame.image.load("maltzurra1.png")
        else:
            self.image = pygame.image.load("supermaltzurra1.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randint(screen.get_width()-20, screen.get_width()+120), random.randint(0, screen.get_height()))
        self.nora = "gora"
        self.zein = 1
    def update(self):
        if self.klasea == 1:
            self.rect.move_ip(-3, 0)
        else:
            #self.rect.move_ip(-3, 0)
            if (self.nora == "gora"):
                self.rect.move_ip(-2, 0)
                self.nora == "behera"
            else:
                self.rect.move_ip(-2, -2)
                self.nora == "gora"
        if self.zein == 1:
            if self.klasea == 1:
                self.image = pygame.image.load("maltzurra2.png")
            else:
                self.image = pygame.image.load("supermaltzurra2.png")
            self.zein = 2
        else:
            if self.klasea == 1:
                self.image = pygame.image.load("maltzurra1.png")
            else:
                self.image = pygame.image.load("supermaltzurra1.png")
            self.zein = 1



#********************************
# 4.3.- AHATETXOA KLASEA
#********************************
class ahatetxoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hiperkuak.png")
        self.rect = self.image.get_rect()
        self.rect.top = 100
        self.rect.left = 80
        self.zein = 1
        self.bizitzak = 3
        self.puntuak = 0
    def move(self, vx, vy):
        self.rect.move_ip(vx, vy)
        if self.zein == 1:
            self.image = pygame.image.load("hiperkuak2.png")
            self.zein = 2
        else:
            self.image = pygame.image.load("hiperkuak.png")
            self.zein = 1
    def update(self, screen):
        screen.blit(self.image, self.rect)

    def mugitu(self,event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move(0, -4)
                self.move(0, -4)
            if event.key == pygame.K_DOWN:
                self.move(0, 4)
                self.move(0, 4)
            if event.key == pygame.K_RIGHT:
                self.move(5, 0)
            if event.key == pygame.K_LEFT:
                self.move(-4, 0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.move(0, 3)
            if event.key == pygame.K_DOWN:
                self.move(0, 3)
            if event.key == pygame.K_RIGHT:
                self.move(3, 0)
            if event.key == pygame.K_LEFT:
                self.move(-3, 0)

    def tiro(self, screen, maltzurrak):

        #ahatearen muturretik "proiektila bota"
        proiek = proiektila(self.rect.left + 65, self.rect.top + 22)
        #i= 0
        return proiek
        #while (i < 20):
        #    jota = pygame.sprite.spritecollide(proiek, maltzurrak, True)
            #proiek.move(screen, 12)
        #    if jota:
        #        i = 20
        #        self.puntuak = self.puntuak + 1
        #        print("puntuak :" + str(self.puntuak))
                #print("maltzurra jotaaa > puntuak + 1")
        #    else:
        #        i = i + 1
        #        #proiek.update(screen)
        #        pygame.display.update(proiek)
    def hasierarara(self):
        self.rect.top = 100
        self.rect.left = 80

#********************************
# 4.4.- PROIEKTILA KLASEA
#********************************
class proiektila(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bala.png")
        self.rect = self.image.get_rect()
        self.rect.left = posx
        self.rect.top = posy
        self.zein = 1

    def move(self, screen, abiadura):
        self.rect.move_ip(abiadura, 0)
        if self.zein == 1:
            #self.image = pygame.image.load("bala.png")
            #screen.blit(screen, self.rect)
            self.zein = 2
        else:
            self.zein = 1
            #screen.blit(screen, self.rect)
        screen.blit(self.image, self.rect)
    def update(self, screen):
        pygame.display.update(self.rect)

    def suntsitu(self):
        self.image.fill((255, 255, 255))
    # ********************************
    # 4.4.- FONDOA KLASEA
    # ********************************
class fondoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hiperkuakfondua2.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0
        self.zein = 1

    def aldatu(self):
        if self.zein == 1:
            self.image = pygame.image.load("hiperkuakfondua2.png")
        elif self.zein == 2:
            self.image = pygame.image.load("hiperkuakfondua22.png")
            #fondoa aldatzen joateko ???
        self.zein = self.zein + 1
        print self.zein

    def move(self, abiadura):
        if (self.rect.left > -1280):
            self.rect.move_ip(abiadura, self.rect.top)
        else:
            self.rect.move_ip(1280, self.rect.top)
            self.zein = 2
            #fondo aldatu !!! ;)
            self.aldatu()
    def geratu(self):
            # guztiz geratzeko self.rect.move_ip(0, 0)
            self.rect.move_ip(0, 0)
    def update(self, screen):
        screen.blit(self.image, self.rect)


# X.- PROGRAMA NAGUSIA HASIERATZEKO!
if __name__ == "__main__":
    main()

