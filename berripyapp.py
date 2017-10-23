# Feedparser: Python en RSS jarioak probatzen
# gakoa https://stackoverflow.com/questions/2244836/rss-feed-parser-library-in-python
import feedparser

class berria:

    izenburua = ""
    deskribapena = ""
    esteka = ""

    def __init__(self, izenburua, deskribapena, esteka):
        self.izenburua = izenburua
        self.deskribapena = deskribapena
        self.esteka = esteka

class berriZerrenda:
    zerrenda = []

    #eraikitzailea
    def __init__(self):
        zerrenda = []

    #berria zerrendara gehitzeko funtzioa
    def gehitu_berria_zerrendara(self, berria):
        self.zerrenda.append(berria)

    #zerrendako berriak ikusteko funtzioa
    def ikusi_berriak(self):
        for ber in self.zerrenda:
            print("*************")
            print(ber.izenburua)
            print(ber.esteka)
            print("*************")
class berripyapp:

    zerrenda = []
    bz = berriZerrenda()
    def __init__(self):
        self.kargatu_iturriak()
        self.irakurri_iturriak()
        self.bz = berriZerrenda()
        self.bz.ikusi_berriak()
    #filtroren bat jartzeko aukera... 
    def topatu_interesko_hitzak_bakarrik(self,hitza):
        #intereseko hitza topatu RSS jarioen artean?
        h_zerrenda = ["informatika", "python", "programazioa", "feedparser"]
        print(hitza)
    #Iturrien RSS helbideak zerrendan kargatzeaz arduratzen da
    def kargatu_iturriak(self):
        #self.zerrenda.append(helbideberriak)
        print("helbideak kargatzen")
        self.zerrenda = ["http://www.naiz.eus/rss/news.rss", "https://www.berria.eus//rss/gizartea.xml", "https://goiena.eus/aktualitatea/feed-rss", "http://hitza.eus/feed/", "http://www.noticiasdegipuzkoa.com/rss/general.xml", "http://www.diariovasco.com/rss/2.0/?section=ultima-hora","https://tokikom.eus/feed/"]
    # Iturriak irakurtzeaz, berriak sortu eta berrizerrendan sartzeaz arduratzen da
    def irakurri_iturria(self,helbidea):
        print("******************************")
        print(helbidea + " iturria irakurtzen")
        print("******************************")
        feed = feedparser.parse(helbidea)
        #print(feed["items"])
        for item in feed["items"]:
            #print("data: " + item["pubDate"])
            #if intereseko hitza in title or summary >> gehitu zerrendan
            b = berria(item["title"], item["summary"], item["link"])
            self.bz.gehitu_berria_zerrendara(b)
            #print("izenburua: " + item["title"])
            #print(item["summary"])
            #print("esteka: " + item["link"])
            #print("-------------------")

    def irakurri_iturriak(self):
        for iturria in self.zerrenda:
            self.irakurri_iturria(iturria)



b = berripyapp()

