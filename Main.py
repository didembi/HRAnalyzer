from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

try:
    insan1 = Insan("12378965456","Yüksel","Demir","36","Erkek","Türk")
    insan2 = Insan("45672318942","Buket","Sergen","33","Kadin","Türk")

    print(insan1)
    print(insan2)
except Exception as e:
    print(f"Hata olustu: {str(e)}")

try:
    issiz1 = Issiz("14563287496","Maria","Garcia","28","Kadin","Alman","4")
    issiz2 = Issiz("96385214714","Abidin","Güclü","25","Erkek","Türk","1")
    issiz3 = Issiz("75315984256","Berke","Uzak","27","Erkek","Türk","3")
    print(issiz1)
    print(issiz2)
    print(issiz3)
    
    calisan1 = Calisan("15632478645","Deniz","Kara","33","Erkek","İngiliz","muhasebe","25","15000")
    calisan2 = Calisan("78645865214","Merve","Yilmaz","36","Kadin","Türk","diğer","9","12000")
    calisan3 = Calisan("78645898542","Rumeysa","Yilmaz","36","Kadin","Türk","teknoloji","12","15000")
    print(calisan1)
    print(calisan2)
    print(calisan3)

    maviyaka1 = MaviYaka("84286235415","Furkan","Ermemiş","30","Erkek","Türk","inşaat","48","12000","0.2")
    maviyaka2 = MaviYaka("45875325841","Thomas","Enderson","27","Erkek","Ingiliz","teknoloji","24","10000","0.1")
    maviyaka3 = MaviYaka("34675414852","Yigit","Akkan","34","Erkek","Türk","muhasebe","60","17000","0.5")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)

    beyazyaka1= BeyazYaka("12378965414","Kerem","Saglam","23","Erkek","Türk","diğer","0","10000","1000")
    beyazyaka2 = BeyazYaka("12475395145","Pinar","Osman","27","Kadin","Türk","diğer","36","12000","2000")
    beyazyaka3 = BeyazYaka("145563258265","Ilkim","Dirgin","30","Kadin","Fransiz","teknoloji","60","20000","2500")
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
except Exception as e:
    print(f"Hata: {str(e)}")

data = {
    "Nesne": ["Calisan","Calisan","Calisan","MaviYaka","MaviYaka","MaviYaka","BeyazYaka","BeyazYaka","BeyazYaka"],
    "TC_no" : ["15632478645","78645865214","78645898542","84286235415","45875325841","34675414852","12378965414","12475395145","145563258265"],
    "Ad" : ["Deniz","Merve","Rumeysa","Furkan","Thomas","Yigit","Kerem","Pinar","Ilkim"],
    "Soyad" : ["Kara","Yilmaz","Yilmaz","Ermemiş","Enderson","Akkan","Saglam","Osman","Dirgin"],
    "Yaş" : [33,36,36,30,27,34,23,27,30],
    "Cinsiyet": ["Erkek", "Kadin", "Kadin", "Erkek", "Erkek", "Erkek", "Erkek", "Kadin", "Kadin"],
    "Uyruk": ["İngiliz", "Türk", "Türk", "Türk", "İngiliz", "Türk", "Türk", "Türk", "Fransiz"],
    "Sektör": ["muhasabe", "diger", "teknoloji", "inşaat", "teknoloji", "muhasebe", "diğer", "diğer", "teknoloji"],
    "Tecrübe": [25,9,12,48,24,60,0,36,60],
    "Maaş": [15000,12000,15000,12000,10000,17000,10000,12000,20000],        
    "Yipranma Payi": [0,0,0.2,0.1,0.5,0,0,0],
    "Teşvik Prim": [0,0,0,0,0,0,1000,2000,2500],
    "Yeni Maaş": [0,0,0,0,0,0,0,0,0]
    }
df = pd.DataFrame(data)

    # Boş değerleri 0 atama 
df.fillna(0, inplace=True)
df["tecrube"] = df["tecrube"] * 12 

# Gruplandırarak tecrübe ve yeni maaş ortalamalarını hesaplama
gruplanmis_df = df.groupby("nesne_degeri").agg({"tecrube": "mean", "yeni_maas": "mean"})
print(gruplanmis_df)

# Maaşı 15000 TL üzerinde olanların toplam sayısını bulma
maas_ust_limit = 15000
toplam_sayi = df[df["maas"] > maas_ust_limit].shape[0]
print("Maaşi {} TL üzerinde olanların toplam sayısı: {}".format(maas_ust_limit, toplam_sayi))

# Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
siralama_df = df.sort_values("yeni_maas")
print(siralama_df)

# Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
tecrube_limit = 3
beyaz_yaka_df = df[(df["nesne_degeri"] == "beyaz yaka") & (df["tecrube"] > tecrube_limit)]
print(beyaz_yaka_df)

# Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır arasındakileri seçme
yeni_maas_limit = 10000
secilen_df = df[df["yeni_maas"] > yeni_maas_limit].iloc[2:5, ["tc_no", "yeni_maas"]]
print(secilen_df)

# Yeni bir DataFrame oluşturma sadece ad, soyad, sektör ve yeni maaşı içeren
yeni_df = df[["ad", "soyad", "sektor", "yeni_maas"]]
print(yeni_df)
