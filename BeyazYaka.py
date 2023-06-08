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

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                yeni_maas = self.get_maas() + self.get_tesvik_primi()
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                yeni_maas = (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                yeni_maas = (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
            else:
                yeni_maas = self.get_maas()
            
            if yeni_maas == self.get_maas():
                return self.get_maas()
            else:
                self.set_maas(yeni_maas)
                return yeni_maas
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def __str__(self):
        ad_soyad = f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}"
        return f"{ad_soyad}\nTecrube: {self.get_tecrube()} ay\nYeni Maas: {self.zam_hakki()} TL"