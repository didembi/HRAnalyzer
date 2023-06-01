from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self,ad,soyad,sektor,tecrube,maas,yipranma_payi):
        super().__init__(ad,soyad,sektor,tecrube,maas)
        self.__yipranma_payi = yipranma_payi
    
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                yeni_maas = self.get_maas() + self.get_yipranma_payi() * 10
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                yeni_maas = self.get_maas() + (self.get_maas() % self.get_tecrube()) / 2 + self.get_yipranma_payi() * 10
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                yeni_maas = self.get_maas() + (self.get_maas() % self.get_tecrube()) / 3 + self.get_yipranma_payi() * 10
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
        return f"{ad_soyad}\nSektor: {self.get_sektor()}\nTecrube: {self.get_tecrube()} ay\nYeni Maaş: {self.zam_hakki()} TL"
