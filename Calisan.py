from Insan import Insan    # Insan sinifindan insan modülünü ice aktarma
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.kontrol_Sektor(sektor)  # Calisanin sektorunu kontrol için fonksiyonu kullanaarak sektor atama
        self.__tecrube = tecrube
        self.__maas = maas       #Calisanin tecrube ve maasini atama
    
    def get_sektor(self):
        return self.__sektor    # Calisanin sektorunu getirme
    def set_sektor(self, sektor):
        self.__sektor = self.kontrol_Sektor(sektor)   # Calisanin sektorunu kontrol etmek icin sektoru guncelleme

    def get_tecrube(self):
        return self.__tecrube    # Calisanin tecrube degerini getirme
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube     #Tecrube degerini guncelleme

    def get_maas(self):
        return self.__maas    #Calisanin maasini getirme

    def kontrol_Sektor(self, sektor):
        kontrol_sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor in kontrol_sektorler:
            return sektor    # Gecerli sektor degerini döndürme
        else:
            raise ValueError("Sektor gecersiz!")       # Gecersiz sektor ise hata yazisini yazdirma

    def zam_hakki(self):          #Zam hakki metodunu oluşturma ve zam oranini hesaplama
        try:
            tecrube = self.get_tecrube()
            maas = self.get_maas()
            zam_orani = 0  # Baslangıc değeri
    #Tecrube , maas  degerlerini al

            if tecrube < 24:
                zam_orani =0
            elif 24 <= tecrube <= 48 and maas < 15000:
                zam_orani = maas % tecrube
            elif tecrube > 48 and maas < 25000:
                zam_orani = (maas % tecrube) / 2

            if zam_orani == 0:
                yeni_maas = maas
            else:
                yeni_maas = maas + ((zam_orani * maas) / 100)  # Zam oranini maasa ekleyerek yeni maas degerini olusturma

            yeni_maas = round(yeni_maas, 2)   # Yeni maas degerini 2 ondalık basamaga yuvarlama
            return yeni_maas

        except Exception as e:
            return f"Hata: {str(e)}"   #Hata durumunda mesaji yazdirma

    def __str__(self):       # Gerekli degiskenleri yazdirma
        ad_soyad = f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}"
        return f"{ad_soyad}\nTecrube: {self.get_tecrube()} ay\nYeni Maas: {self.zam_hakki():.2f} TL"
