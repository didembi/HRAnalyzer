from Insan import Insan   # Insan sinifindan insan modülünü ice aktarma

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube   #Issizin tecrube degerini atama

    def get_tecrube(self):
        return self.__tecrube   # Issizin tecrube degerini getirme

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube      #Tecrube degerini guncelleme

    def statu_bul(self):     # İssizi uygun statuye atama islemi için fonksiyon olusturma
        try:
            etki_oranlari = {
                "mavi yaka": 0.2,
                "beyaz yaka": 0.35,
                "yönetici": 0.45
            }

            max_etki = 0
            en_uygun_statu = ""

            for statu, yil in self.__tecrube.items():    # Issizin  tecrube degeri ve statusunun etki orani ile carpma islemi
                etki = {}
                etki["mavi yaka"] = yil * etki_oranlari["mavi yaka"]
                etki["beyaz yaka"] = yil * etki_oranlari["beyaz yaka"]
                etki["yönetici"] = yil * etki_oranlari["yönetici"]

                if etki[statu] == max_etki :    # Eşitlik durumunda yönetici statüsünü atayalım
                    en_uygun_statu = "yönetici"
                if etki[statu] > max_etki:
                    max_etki = etki[statu]
                    en_uygun_statu = statu
                
            return en_uygun_statu    # Uygun statu degerini döndürme
        except Exception as e:
            return f"Hata: {str(e)}"

    def __str__(self):     # Gerekli degiskenleri yazdirma
        en_uygun_statu = self.statu_bul()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nEn Uygun Statü: {en_uygun_statu}"

