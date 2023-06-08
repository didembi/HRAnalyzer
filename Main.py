from Insan import Insan    #Butun modulleri ice aktarma
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd      # Pandas kutuphanesini cagırma

try:
#Insan nesnelerini olusturma
    insan1 = Insan(12378965456,"Yüksel","Demir","36","Erkek","Türk")
    insan2 = Insan(45672318942,"Buket","Sergen","33","Kadin","Türk")
    print("Insan sinifi")
    print(insan1)
    print(insan2)
    
#Issiz nesnelerini olusturma
    issiz1 = Issiz(14563287496,"Maria","Garcia","48","Kadin","Alman",{ "mavi yaka": 14, "beyaz yaka": 9, "yönetici": 7 })
    issiz2 = Issiz(96385214714,"Abidin","Güclü","33","Erkek","Türk",{ "mavi yaka": 7, "beyaz yaka": 4, "yönetici": 0 })
    issiz3 = Issiz(75315984256,"Berke","Uzak","30","Erkek","Türk",{ "mavi yaka": 7, "beyaz yaka": 0, "yönetici": 0})
    print("\nIssiz sinifi")
    print(issiz1)
    print(issiz2)
    print(issiz3)
    
 #Calisan nesnelerini olusturma   
    calisan1 = Calisan(15632478645,"Deniz","Kara","33","Erkek","İngiliz","muhasebe",48,13000)
    calisan2= Calisan(78645865214,"Merve","Yilmaz","36","Kadin","Türk","diğer",12,12200)
    calisan3 = Calisan(78645898542,"Rumeysa","Yilmaz","36","Kadin","Türk","teknoloji",60,23000)
    print("\nCalisan sinifi")
    print(calisan1)
    print(calisan2)
    print(calisan3)
    
#Mavi yaka nesnelerini olusturma
    maviyaka1 = MaviYaka(84286235415,"Furkan","Ermemiş","30","Erkek","Türk","inşaat",48,13000,0.8)
    maviyaka2 = MaviYaka(45875325841,"Thomas","Enderson","27","Erkek","Ingiliz","teknoloji",24,10000,0.5)
    maviyaka3 = MaviYaka(34675414852,"Yigit","Akkan","34","Erkek","Türk","muhasebe",60,16000,0.6)
    print("\nMavi yaka sinifi")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)
    
#Beyaz yaka nesnelerini olusturma
    beyazyaka1= BeyazYaka(12378965414,"Kerem","Saglam","23","Erkek","Türk","diğer",0,10000,1000)
    beyazyaka2 = BeyazYaka(12475395145,"Pinar","Osman","27","Kadin","Türk","diğer",36,12000,2000)
    beyazyaka3 = BeyazYaka(74563258265,"Ilkim","Dirgin","30","Kadin","Fransiz","teknoloji",60,20000,2500)
    print("\nBeyaz yaka sinifi")
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
    print("\n")
    

    data = {
        "Nesne": ["Calisan", "Calisan", "Calisan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
        "TC_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
                   maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(),
                   beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
                maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), 
                beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
                   maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), 
                   beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
        "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), 
                maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), 
                beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
        "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), 
                     maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), 
                     beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
        "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), 
                  maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), 
                  beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
        "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), 
                   maviyaka1.get_sektor(), maviyaka2.get_sektor(), maviyaka3.get_sektor(),
                   beyazyaka1.get_sektor(), beyazyaka2.get_sektor(), beyazyaka3.get_sektor()],
        "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), 
                    maviyaka1.get_tecrube(), maviyaka2.get_tecrube(), maviyaka3.get_tecrube(), 
                    beyazyaka1.get_tecrube(), beyazyaka2.get_tecrube(), beyazyaka3.get_tecrube()],
        "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), 
                 maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(), 
                 beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],
        "Yipranma Payi": [0,0,0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(), 0,0,0],
        "Teşvik Prim": [0,0,0,0,0,0, beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(), beyazyaka3.get_tesvik_primi()],
        "Yeni Maaş": [calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki(), maviyaka1.zam_hakki(), maviyaka2.zam_hakki(), maviyaka3.zam_hakki(), beyazyaka1.zam_hakki(), beyazyaka2.zam_hakki(), beyazyaka3.zam_hakki()]
    }

    # DataFrame'i olusturma
    df = pd.DataFrame(data)

    # Tecrübe degerini yıla cevirme
    df["Tecrübe"] = df["Tecrübe"] // 12
    print(df)

    # Bos degerlere 0 atama
    df.fillna(0, inplace=True)

    # Calisan, mavi yaka ve beyaz yaka için gruplandırarak tecrube ve yeni maaş ortalamalarini hesaplama
    ortalama_df = df.groupby("Nesne").agg({"Tecrübe": "mean", "Yeni Maaş": "mean"})
    print("Tecrübe(yila göre) ve yeni maaşlarin ortalamasi:")
    print(ortalama_df)
    print("\n")

    # Maaşı 15000TL üzerinde olanlarin toplam sayisini bulma
    maas_ustundeki_sayi = df[df["Maaş"] > 15000].shape[0]
    print("Maaşı 15000TL üzerinde olanların toplam sayısı:", maas_ustundeki_sayi)
    print("\n")

    # Yeni maasa göre DataFrame'i kucukten buyuge siralama
    df_sirali = df.sort_values("Yeni Maaş")
    print("Yeni maaşa göre siralanmiş DataFrame:")
    print(df_sirali)
    print("\n")

    # Tecrubesi 3 seneden fazla olan Beyaz yakalilari bulma
    beyazyaka_tecrube = df[(df["Nesne"] == "Beyaz Yaka") & (df["Tecrübe"] > 3)]
    if not beyazyaka_tecrube.empty:
        print("Tecrübesi 3 seneden fazla olan Beyaz yakalılar:")
        print(beyazyaka_tecrube)
    else:
        print("Tecrübesi 3 seneden fazla olan Beyaz yakalı bulunmamaktadır.")

    # Yeni maasi 10000 TL uzerinde olanlarin 2-5 satir arasındaki tc_no ve yeni_maaş sütunlarini secme
    yuksek_maasli = df[df["Yeni Maaş"] > 10000].iloc[1:5, [1, 12]]
    yuksek_maasli.columns = ["TC_no", "Yeni Maaş"]
    print("Yeni maaşi 10000 TL üzerinde olanlarin 2-5 satir arasindaki tc_no ve yeni_maaş sütunlari:")
    print(yuksek_maasli)
    print("\n")


    # Ad, soyad, sektör ve yeni maasi iceren yeni bir DataFrame olusturma
    yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
    print("Yeni DataFrame:")
    print(yeni_df)

except Exception as e:
    print(f"Hata: {str(e)}")
