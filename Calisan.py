from Insan import Insan
class Calisan(Insan):
    def __init__(self,ad,soyad,sektor,tecrube,maas):
        super().__init__( ad, soyad,)
        self.__sektor = self.validate_sektor(sektor)
        self.__tecrube = tecrube
        self.__maas = maas
        
    def get_sektor(self):
        return self.__sektor
    def set_sektor(self,sektor):
        self.__sektor = self.validate_sektor(sektor)

    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,tecrube):
        self.__tecrube = tecrube
    
    def get_maas(self):
        return self.__maas
    def set_maas(self,yeni_maas):
        self.__maas = yeni_maas

    def validate_sektor(self, sektor):
        valid_sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor in valid_sektorler:
            return sektor
        else:
            raise ValueError("Sektor degeri gecersiz!")    
        
    def zam_hakki(self):
        try:
            if self.__tecrube < 2:
                return 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                yeni_maas = self.__maas * self.__tecrube / 100
            elif self.__tecrube > 4 and self.__maas < 25000:
                yeni_maas = (self.__maas * self.__tecrube) / 200
            else:
                yeni_maas = self.__maas

            if yeni_maas == self.__maas:
                self.__maas = yeni_maas

            return yeni_maas

        except Exception as e:
            return f"Hata: {str(e)}"

        
    def __str__(self):
        ad_soyad = f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}"
        
        tecrube = f"Tecrube: {self.__tecrube} ay"
        yeni_maas = f"Yeni Maaş: {self.zam_hakki()} TL"
        return f"{ad_soyad}\\n{tecrube}\n{yeni_maas}"
