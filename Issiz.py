from Insan import Insan
class Issiz(Insan):
    def __init__(self, ad, soyad, tecrube):
        super().__init__(ad, soyad)
        self.__tecrube = tecrube
    
    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,yeni_tecrube):
        self.__tecrube = yeni_tecrube
    
    def statu_bul(self):
        try:
            max_deger = 0
            uygun_statu = ""

            for statu,yil in self.__tecrube.items():
                if statu == "mavi yaka":
                    etki = yil*0.2
                elif statu == "beyaz yaka":
                    etki = yil*0.35
                elif statu == "yonetici":
                    etki = yil*0.45
                else:
                    raise ValueError("Geçerli olmayan statu:"+statu)
                
                if etki > max_deger:
                    max_deger= etki
                    uygun_statu = statu
            return uygun_statu
        except Exception as e:
            print("Hata:",e)
    
    def __str__(self):
        ad_soyad = f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}"
        try:
            uygun_statu = self.statu_bul()
            return f"{ad_soyad}\nEn Uygun Statü: {uygun_statu}"
        except Exception as e:
            return ad_soyad + "\nHata: " + str(e)
