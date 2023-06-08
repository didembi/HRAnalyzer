from Calisan import Calisan       # Calisan sinifindan calisan modlülünü ice aktarma
class BeyazYaka(Calisan):        # Ust sinifin init metodunu cagirarak tamel degerleri alma
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas,tesvik_primi):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas)
        self.__tesvik_primi = tesvik_primi 
  
#Tesvik primi degerini getirme ve guncelleme
    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
  
    def zam_hakki(self):   #Zam hakki metodunu oluşturma ve zammi hesaplama
        try:  
            tecrube = self.get_tecrube()
            maas = self.get_maas()
            tesvik_primi = self.get_tesvik_primi()
    #Tecrube , maas , tesvik primi degerlerini al

            if tecrube < 24:   # Tecrubeye gore maasın ne kadar artacagını hesaplama
                yeni_maas = maas + tesvik_primi
            elif 24 <= tecrube <= 48 and maas < 15000:
                yeni_maas = maas+((maas %tecrube)*5 + tesvik_primi)
            elif tecrube > 48 and maas < 25000:
                yeni_maas = maas+((maas % tecrube)*4 + tesvik_primi)
            else:
                yeni_maas= maas
    
            return yeni_maas
        
        except Exception as e:
            return f"Hata: {str(e)}"   #Hata durumunda mesaji yazdirma

    def __str__(self):   # Gerekli degiskenleri yazdirma
        ad_soyad = f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}"
        return f"{ad_soyad}\nTecrube: {self.get_tecrube()} ay\nYeni Maas: {self.zam_hakki():.2f} TL"