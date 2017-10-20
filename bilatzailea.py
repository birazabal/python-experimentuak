
#krr4m4rr0 2017-10-20

#testu kate bilatzaile froga xumea...
#usr/bin/python
#pathlib eta subprocess erabiltzea hobe legoke... python
#formatu ezberdinak aztertu...
#docx > https://stackoverflow.com/questions/116139/how-can-i-search-a-word-in-a-word-2007-docx-file#1979864
import os
#from docx import *

class bilatzailea():
    bilaketaKatea = ""
    bilaketaKokap = ""
    zenbat = 0
    topatuak = []
    def __init__(self):

        zenbat = 0
        topatuak = []
        self.aurkezpena()
        self.eskatu_bilaketa_katalogoan()

    def aurkezpena(self):
        print("*********************************************")
        print("***Testu kate bilatzailea 1.o****************")
        print("*********************************************")
        print("************************************2017*****")
    #fitxategi batean bilatzeko funtzioa
    def eskatu_bilaketa_fitxategian(self):
        bilaketaKatea = input("1) ZER BILATU: sartu bilatu nahi den testu katea: ")
        bilaketaKokap = input("2) NON BILATU: zein fitxategitan bilatu nahi duzu?")
        self.bilatu_fitxategian(bilaketaKatea, bilaketaKokap)

    #hainbat fitxategitan bilatzeko funtzioa
    def eskatu_bilaketa_katalogoan(self):
        bilaketaKatea = input("1) ZER BILATU: sartu bilatu nahi den testu katea: ")
        bilaketaKokap = input("2) NON BILATU: zein karpetatan bilatu nahi duzu?")
        self.bilatu_katalogoan(bilaketaKatea, bilaketaKokap)

    def bilatu_fitxategian(self, bilaketakatea, fitxategia):
        print("*****************************************")
        print(">> " + fitxategia + " fitxategian bilatzen")
        sententzia = "grep " + bilaketakatea + " " + fitxategia
        emaitza = os.system(sententzia)
        if (emaitza == 0):
            self.zenbat = self.zenbat + 1
            self.topatuak.append(fitxategia)
            print("\n")
            print("[+] adi-> " + fitxategia + " fitxategian [" + bilaketakatea + "] ageri da")
        else:
            print("bilaketa hitza ez da aurkitu dokumentu honetan")

        print ("\n")

    def bilatu_docx_fitxategian(self, bilaketakatea, fitxategia):
            print("*****************************************")
            print(">> " + fitxategia + " fitxategian bilatzen")
            print("oraindik probatu gabe")
            emaitza = false
            #dokumentua = opendocx(fitxategia)
            #emaitza = search(dokumentua, bilaketakatea)
            if (emaitza == true):
                print("\n")
                print("[+] adi-> " + fitxategia + " fitxategian [" + bilaketakatea + "] ageri da")
                self.zenbat = self.zenbat + 1
            else:
                print("bilaketa hitza ez da aurkitu dokumentu honetan")

            print("\n")

    def bilatu_katalogoan(self,bilaketaKatea, karpeta):
        os.chdir(karpeta)
        sententzia = "ls -p | grep -v /"
        #emaitza = os.system(sententzia)
        for fitxategia in os.scandir(karpeta):
            if fitxategia.is_file():
                #oraingoz .py eta .txt fitxategiak soilik...
                if (".py" in fitxategia.name) or (".txt" in fitxategia.name):
                    # eta PDF, eta .DOC, eta .DOCX?
                    print(fitxategia.name)
                    self.bilatu_fitxategian(bilaketaKatea, fitxategia.name)
                #.docx proba
                elif ".docx" in fitxategia.name:
                    self.bilatu_docx_fitxategian(bilaketaKatea, fitxategia.name)
        #for fitx in os.listdir(karpeta):
        #    self.bilatu_fitxategian(bilaketaKatea, fitx)
        print("*************************************")
        print("[" + str(self.zenbat) + "] fitxategitan topatu da katea")
        for i in self.topatuak:
            print(i)

        #print(sententzia2)
b = bilatzailea()
