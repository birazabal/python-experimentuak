#krr4m4rr0 2017-10-20

#testu kate bilatzaile froga xumea... ubuntu 16.04an frogatua
#usr/bin/python
#pathlib eta subprocess erabiltzea hobe legoke... python
#formatu ezberdinak aztertu...
import os

class bilatzailea():
    bilaketaKatea =""
    bilaketaKokap =""
    def __init__(self):
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
            print("\n")
            print("[+] adi-> " + fitxategia + " fitxategian [" + bilaketakatea + "] ageri da")
        else:
            print("bilaketa hitza ez da aurkitu dokumentu honetan")

        print ("\n")

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
        #for fitx in os.listdir(karpeta):
        #    self.bilatu_fitxategian(bilaketaKatea, fitx)

        #print(sententzia2)
b = bilatzailea()
