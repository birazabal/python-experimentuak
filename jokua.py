# Jokutxoa 1.0
# Pygame liburutegia frogatzen
# https://stackoverflow.com/questions/10389487/spawning-multiple-of-the-same-sprite#10418347 >hainbat etsai
#https://stackoverflow.com/questions/8303685/how-would-i-display-the-score-in-this-simple-game> markagailu sinplea
#falta > ertzak kontrolatu, boss-en mugimentua ziklikoa bihurtu pantailatik irten gabe
#ahatearen disparoa hobetu / beste disparomota bat?
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
    #musikafitx = 'pum.wav'
    pygame.init()
    #pygame.mixer.init()
    #pygame.mixer.music.load(musikafitx)
    #pygame.mixer.music.play()
    #******************************************
    #3.1.- Nagusirako aldagai eta objetuen hasieratzeak
    # bi kontagailu, denbora ordez zikloak kontrolatzeko... + pantailaren hasieratzea
    kontm = 0
    nirekont = 0
    screen = pygame.display.set_mode((640, 480))

    #gure jokalaria izango dena eta fondoaren instantziak
    jokalaria = ahatetxoa()
    f = fondoa()
    # hainbat etsai batera maneiatzeko, taldeak = group
    enemies = pygame.sprite.Group()
    enemies2 = pygame.sprite.Group()
    #fondoaren abiadurarentzat aldagaia
    mugituab = -2
    #boss-a sortu den edo ez kontrolatzeko aldagaia
    sb = 0
    jokajota3 = False
    jokajota4 = False

    #3.1.- JOKU programa nagusiko BEGIZTA nagusia, jokalariak bizitzak galdu arte edo eta  X sakatu arte ez da amaituko

    while True:

        #markagailua erakusteko + bizitzak
        font = pygame.font.Font(None, 24)
        text = font.render("| Puntuak: " + str(jokalaria.emanpuntuak()) + " || Bizitzak: " + str(jokalaria.emanbizitzak() + "|"), 1, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width() / 2)
        if jokalaria.bizitzak > 0:
            nirekont += 1
            #hobeto mugitzeko funtzioa
            jokalaria.mugitub()
            # Ekintzaren bat egon ote den konprobatu > horren araberako aldaketak
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Agur, eta eskerrik asko jolasteagatik ;)")
                    sys.exit()
                # FROGATU ERABILTZAILEAREN KONTROLA, begiratu EBENTUAK + KOORDENATU MUGAK JARRI
                # BUKATZEKO BALDINTZA EZARRI > BIZITZAK, PANTAILAK ETB. > ORAINGOZ KONTROLAK "TXAPU"
                else:
                    jokalaria.mugitua(event)
            #tiroa mejoratzeko...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #print ("tiroo")
                    if not jokalaria.botata:
                        jokalaria.tiro(screen, enemies, enemies2)

            # HASI PANTAILEN LOGIKA: 2 PANTAILA, bakoitzak 2 FONDO, FONDO BAKOITZA nirekont-en arabera 4 ALDIZ IKUSI
            # PANTAILAREN ARABERAKO MALTZURRAK SORTU (ENEMY KLASEAK)
            # KASU HONETAN DENA NIRE KONTAGAILUAREN ARABERA... :( kutretxo, baina hastekooo
            # maltzurrak 9 aldiz sortu...

            #hasierako maltzurrak SORTU (enemy 1)
            if f.fziklo == 1 or f.fziklo == 2:
                if kontm < 3:
                    for x in range(0, 2):
                        enemies.add(Enemy(screen, 1))
                        kontm = kontm + 1
                if nirekont in (200, 400, 500, 800, 900, 1000, 1100):
                    kontm = 0
                mugituab = -2
                #f.update(screen)
            elif f.fziklo == 3:
                if (kontm < 4):
                    for x in range(0, 1):
                        # 1, 2  etsai motak, horizontalean mugitu
                        enemies.add(Enemy(screen, 1))
                    enemies.add(Enemy(screen, 2))
                    kontm = kontm + 1
                if nirekont in (100, 250, 500, 800, 900, 1000, 1100):
                    kontm = 0
                mugituab = -2
            elif f.fziklo == 4:
                if f.zein == 2:#hau zuzendu >> 1 jarri gero
                    if kontm < 5:
                        for x in range(0, 1):
                            #1,2 eta 3
                            enemies.add(Enemy(screen, 1))
                            enemies.add(Enemy(screen, 2))
                            enemies2.add(Enemy2(screen, 1))
                            kontm = kontm + 1
                    if nirekont in (100, 250, 500, 800, 900, 1000, 1100):
                        kontm = 0
                    mugituab = -2
                    #f.aldatu()

                else:
                    #2.zein 4.zikloan > Boss agertu
                    if sb == 0:
                        nireboss = Boss(screen, jokalaria)
                        sb = 1
                    mugituab = 0
                    if nireboss.rect.colliderect(jokalaria) == 1:
                        jokajota3 = True
            #inre kontagailua hasieratu
            if nirekont == 1280:
                nirekont = 0
            #etsaien egoera eguneratu
            enemies.update()
            enemies2.update()
            #zikloaren arabera  fondoaren kolorea  aldatzeko aukera
            if f.zein == 1:
                if f.fziklo == 1:
                    screen.fill((0, 100, 140))
                elif f.fziklo == 2:
                    screen.fill((0, 100, 160))
                elif f.fziklo == 3:
                    screen.fill((0, 100, 220))
                else:
                    screen.fill((0, 100, 255))
            else:
                if f.fziklo == 1:
                    screen.fill((100, 100, 140))
                elif f.fziklo == 2:
                    screen.fill((100, 100, 160))
                elif f.fziklo == 3:
                    screen.fill((0, 50, 0))
                else:
                    screen.fill((0, 100, 0))

            jokajota = pygame.sprite.spritecollide(jokalaria, enemies, True)
            jokajota2 = pygame.sprite.spritecollide(jokalaria, enemies2, True)

            if jokajota or jokajota2 or jokajota3 or jokajota4:
                jokalaria.image.fill((255, 0, 0))
                jokalaria.bizitzak = jokalaria.bizitzak - 1
                print("JOKALARIAREN BIZITZAK:" + str(jokalaria.bizitzak))
                botata = False
                jokalaria.hasierarara()
            f.move(mugituab)
            f.update(screen)
            jokalaria.update(screen)
            enemies.draw(screen)
            enemies2.draw(screen)
            #boss kontrolatzeko zatia /
            if sb == 1:
                nireboss.update(screen)
            # markagailua inprimatu
            screen.blit(text, textpos)
            # jokalaria.update(screen)

            pygame.display.update()
            erlojua.tick(60)
        else:
            if jokalaria.puntuak >100:
                print("ZORIONAK,OSO PARTIDA ONA JOKATU DUZU !!! ;) ;) ;) ")
                print("**************************************************")
                #fitxategira pasatu
                #izena = raw_input("sartu zure izena mesedez:")
            print("jokoa amaitu da!!! Puntuak = " + str(jokalaria.puntuak))
            #print("jokalaria: " + izena)
            exit()

#***********************************************************************************************
#4.- Klaseak eta funtzioak **********************************************************************
#***********************************************************************************************


#********************************
# 4.2.- ENEMY KLASEA(k)
#********************************

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, klasea):
        pygame.sprite.Sprite.__init__(self)
        #self.zein bi irudiak ezberdintzeko
        self.klasea = klasea
        self.bizizikloak = 500
        if self.klasea == 1:
            self.image = pygame.image.load("maltzurra1.png")
        else:
            self.image = pygame.image.load("supermaltzurra1.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randint(screen.get_width()-20, screen.get_width()+120), random.randint(0, screen.get_height()))
        self.zein = 1
    def update(self):
        if self.bizizikloak > 0:
            if self.klasea == 1:
                self.rect.move_ip(-3, 0)
            else:
                self.rect.move_ip(-4, 0)
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
            self.bizizikloak -= 1
        else:
            self.kill()
class Enemy2(pygame.sprite.Sprite):

            def __init__(self, screen, klasea):
                pygame.sprite.Sprite.__init__(self)
                # print "created a new sprite:", id(self)
                self.klasea = klasea
                if self.klasea == 1:
                    self.image = pygame.image.load("planeta.png")
                else:
                    self.image = pygame.image.load("planeta.png")
                self.rect = self.image.get_rect()
                self.rect.move_ip(random.randint(screen.get_width() - 100, screen.get_width() + 20),
                                  random.randint(-300, screen.get_height()))
                self.nora = "be"
                self.zein = 1
                self.bizizikloak = 500

            def update(self):
                if self.bizizikloak > 0:
                    self.rect.move_ip(-8, 0)
                    if (self.nora == "be"):
                        self.rect.move_ip(14, 8)
                        self.nora = "ez"
                        self.image = pygame.image. load("planeta2.png")
                        #print("behera")
                    elif (self.nora == "ez"):
                        self.rect.move_ip(-6, 2)
                        self.nora = "go"
                        self.image = pygame.image.load("planeta.png")
                        #print("ezkerrera")
                    elif (self.nora == "go"):
                        self.rect.move_ip(2, -5)
                        self.nora = "esk"
                        self.image = pygame.image.load("planeta2.png")
                    elif (self.nora == "esk"):
                        self.rect.move_ip(2, 2)
                        #print ("eskuinera")
                        self.nora = "be"
                    if self.zein == 1:
                        self.image = pygame.image.load("planeta.png")
                        self.zein = 2
                    else:
                        self.image = pygame.image.load("planeta2.png")
                        self.zein = 1

                    self.bizizikloak -= 1
                else:
                    self.kill()

class Boss(pygame.sprite.Sprite):

    def __init__(self, screen, jokalaria):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("superboss.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(screen.get_width(), screen.get_height()/2)
        self.zein = 1
        self.mugi = 0
        self.mugiblok = 0
        self.btiro = 100
        self.bbmugitzen = False
        self.balaboss = proiektila
        self.kolpeak = 5
        self.jokalaria = jokalaria
        self.balakjotzen = False

    def update(self, screen):
        font2 = pygame.font.Font(None, 24)
        text2 = font2.render("Kolpeak: " + str(self.inprimatukolpeak()), 1, (10, 10, 10))
        textpos2 = text2.get_rect(centerx=550, centery=420)
        if self.kolpeak > 0:
            if self.mugi == 0:
                if self.mugiblok < 35:
                    self.mugiblok = self.mugiblok + 1
                    self.rect.move_ip(-3, -1)
                    #-5 ezkerrera -2 gora
                else:
                    self.mugi = 1
                    self.mugiblok = 0
            elif self.mugi == 1:
                if self.mugiblok < 20:
                    self.mugiblok = self.mugiblok + 1
                    self.rect.move_ip(0, -2)
                else:
                    self.mugi = 2
                    self.mugiblok = 0
            elif self.mugi == 2:
                if self.mugiblok <20:
                    self.mugiblok = self.mugiblok + 1
                    self.rect.move_ip(0, 3)
                else:
                    self.mugi = 3
                    self.mugiblok = 0
            elif self.mugi == 3:
                if self.mugiblok < 20:
                    self.mugiblok = self.mugiblok + 1
                    self.rect.move_ip(3, 0)
                else:
                    self.mugi = 0
                    self.mugiblok = 0
            if self.zein == 1:
                self.image = pygame.image.load("superboss.png")
                self.zein = 2
            else:
                self.image = pygame.image.load("superboss2.png")
                self.zein = 1
            if self.balakjotzen == False:
                if self.rect.colliderect(self.jokalaria.bala) == 1:
                    # print ("jokalariaren balak jo du boss")
                    self.jokalaria.bala.suntsitu()
                    self.kolpeak -= 1
                    self.balakjotzen = True
                    if self.zein == 1:
                        self.image = pygame.image.load("superboss3.png")
                    self.jokalaria.puntuak = self.jokalaria.puntuak + 10
            else:
                if self.zein == 1:
                    self.image = pygame.image.load("superboss3.png")
            self.btiro = self.btiro - 1
            if (self.btiro == 0):
                self.bbmugitzen = True
                self.balaboss = self.tiro(screen)
                self.btiro = self.btiro + 90
            else:
                if self.btiro > 30 and self.bbmugitzen:
                    # balen abiadura
                    self.balaboss.move(screen, -9)
                    self.balaboss.update(screen)
                    # balek jokalaria jotzen ote duten frogatu
                    if self.jokalaria.rect.colliderect(self.balaboss) == 1:
                        self.jokalaria.hasierarara()
                        self.jokalaria.bizitzak -= 1
                elif self.bbmugitzen and self.btiro == 30:
                    self.bbmugitzen = False
                    self.bbtiro = 1
                    self.balakjotzen = False
            screen.blit(self.image, self.rect)
            screen.blit(text2,textpos2)
            pygame.display.update(self.rect)
        else:
            textpuntuak = font2.render("Puntuak: " + str(self.jokalaria.puntuak), 1, (10, 10, 10))
            textzorionak = font2.render("ZORIONAK, JOKOA AMAITU DUZU", 1, (10, 10, 10))
            textpospuntuak = textpuntuak.get_rect(centerx=300, centery=240)
            textposzorionak = textzorionak.get_rect(centerx=300, centery=200)
            print("ZORIONAK, JOKOA AMAITU DUZU!!!")
            print("Egindako puntoak: " + str(self.jokalaria.puntuak))
            print("*********GAME OVER************")
            print("*******************************")
            #i = 0
            #while (i<10000):
            #    screen.blit(textpuntuak, textpospuntuak)
            #    screen.blit(textzorionak, textposzorionak)
            #    i += 1
            self.kill()

            exit()

    def tiro(self, screen):
        bss = proiektila(self.rect.left + 20, self.rect.top + 55)
        return bss


    def inprimatukolpeak(self):

        kolpeak_graf = ""
        for x in range(0, self.kolpeak):
            kolpeak_graf = kolpeak_graf + " * "
        return kolpeak_graf

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
        self.botata = False
        self.tiroluzera = 200
        self.bala = proiektila
        self.atiro = 60
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

    def mugitua(self,event):

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
            #if event.key == pygame.K_SPACE:
                #print("kaixo karapaixo")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.move(0, 3)
            if event.key == pygame.K_DOWN:
                self.move(0, 3)
            if event.key == pygame.K_RIGHT:
                self.move(3, 0)
            if event.key == pygame.K_LEFT:
                self.move(-3, 0)

    def mugitub(self):
        #if self.rect.left
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.move(-2, 0)
        if pressed[K_RIGHT]:
            self.move(2, 0)
        if pressed[K_UP]:
            self.move(0, -2)
        if pressed[K_DOWN]:
            self.move(0, 2)

    def tiro(self, screen, maltzurrak,maltzurrak2):
        #ahatearen muturretik "proiektila bota"
        #pygame.mixer.music.play()
        self.botata = True
        self.bala = proiektila(self.rect.left + 65, self.rect.top + 22)
        i = 0

        while self.atiro > 30 and self.botata:
            # balen abiadura
            self.bala.move(screen, 15)
            screen.blit(self.bala.image, self.bala.rect)
            self.bala.update(screen)
            maltzurjota = pygame.sprite.spritecollide(self.bala, maltzurrak, True)
            maltzurjota2 = pygame.sprite.spritecollide(self.bala, maltzurrak2, True)
            if maltzurjota or maltzurjota2:
                self.puntuak = self.puntuak + 1
                self.atiro = 60
                self.botata = False
                self.bala.suntsitu()
            self.atiro -= 1
        self.botata = False
        self.atiro = 60
        screen.blit(self.bala.image, self.bala.rect)
        #pygame.display.update(self.bala.rect)


    def hasierarara(self):
        self.rect.top = 100
        self.rect.left = 80
    def emanbizitzak(self):
        bizitzak_graf = ""
        for x in range(0,self.bizitzak):
            bizitzak_graf = bizitzak_graf + " # "
        return bizitzak_graf

    def emanpuntuak(self):
        return self.puntuak
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
    def ikutzen(self,zein):
        return self.rect.colliderect(zein)

    # ********************************
    # 4.5.- FONDOA KLASEA
    # ********************************
class fondoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hiperkuakfondua1.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0
        self.zein = 1
        self.fziklo = 1

    def aldatu(self):
        print ("aldatu deituta " + str(self.zein))
        self.zein = self.zein + 1
        if self.zein == 2:
            self.image = pygame.image.load("hiperkuakfondua2.png")




    def move(self, abiadura):
        # fondoen logika koordenatuen arabera.
        # fondoa 4 aldiz mugituko da (zikloak) eta hauek egitean,fondoa aldatuko da
        # 2. fondoaren 4.zikloan pantaila geratu egindo da, mugitu gabe.
        if (self.rect.left > -1280):
            self.rect.move_ip(abiadura, self.rect.top)
        else:
            if self.fziklo == 4:
                if self.zein == 1:
                    self.fziklo = 0
                    self.aldatu()
                else:
                    self.geratu()
            else:
                self.fziklo = self.fziklo + 1
                print(self.fziklo)
                self.rect.move_ip(1280, self.rect.top)

    def geratu(self):
            # guztiz geratzeko self.rect.move_ip(0, 0)
            self.rect.move_ip(0, 0)
    def update(self, screen):
        screen.blit(self.image, self.rect)


#************ class MENUA etb ******************#
class menua():
    def __init__(self):
        self.aukera = self.erakutsiMenua()
    def erakutsiMenua(self):
        print ("******************************************")
        print ("****Ongi etorri super-ahatetxoa jokora****")
        print ("******************************************")
        print ("1.- Jolastu")
        print("2.-Puntuazio taula ikusi") #inplementatu gabe
        print("3.-Irten")
        self.aukera = raw_input("sartu zure aukera >> ")
        if int(self.aukera) == 1:
            print("jolastu")
        elif int(self.aukera) == 3:
            print("Eskerrik asko aplikazioa probatzeagatik ;)")
            exit
        else:
            print("beste aukerak")
        return self.aukera
    def itzuliAukera(self):
        return self.aukera
# X.- PROGRAMA NAGUSIA HASIERATZEKO!
if __name__ == "__main__":
    m = menua()
    a = m.itzuliAukera()
    print a
    if int(a) == 1:
        main()

