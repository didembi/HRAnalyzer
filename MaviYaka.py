from Calisan import Calisan   # Calisan sinifindan calisan modlülünü ice aktarma
class MaviYaka(Calisan):   # Ust sinifin init metodunu cagirarak tamel degerleri alma
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas,yipranma_payi):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas) 
        self.__yipranma_payi = yipranma_payi

#Yipranma payi degerini getirme ve guncelleme
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):    #Zam hakki metodunu oluşturma ve zam oranini hesaplama
        try:
            tecrube = self.get_tecrube()
            maas =self.get_maas()
            yipranma_payi = self.get_yipranma_payi()
            zam_orani = 0
    #Tecrube , maas , yipranma payi degerlerini al 

            if tecrube < 24:    # Tecrube ve maasa göre zam oranini hesapla 
                zam_orani = yipranma_payi * 10
            elif 24 <= tecrube <= 48 and maas < 15000:
                zam_orani = (maas % tecrube) / 2 + (yipranma_payi * 10)
            elif tecrube > 48 and maas < 25000:
                zam_orani = (maas % tecrube) / 3 + (yipranma_payi * 10)

            yeni_maas = maas + (maas * zam_orani / 100)  # Zam oranini yüzde olarak hesapla
            yeni_maas = round(yeni_maas, 2)  # Yeni maas degerini 2 ondalık basamaga yuvarlama

            return yeni_maas

        except Exception as e:
            return f"Hata: {str(e)}"   # Hata mesaji yazdirma

    def __str__(self):     # Gerekli degiskenleri yazdirma
        ad_soyad = f"Ad: {self.get_ad()} \nSoyad: {self.get_soyad()}"
        return f"{ad_soyad}\nTecrube: {self.get_tecrube()} ay\nYeni Maas: {self.zam_hakki():.2f} TL"
