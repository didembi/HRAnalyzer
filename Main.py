from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

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
    
    calisan1 = Calisan("15632478645","Deniz","Kara","33","Erkek","İngiliz","muhasebe","25")
    calisan2 = Calisan("78645865214","Merve","Yilmaz","36","Kadin","Türk","diğer","9")
    calisan3 = Calisan("78645898542","Rumeysa","Yilmaz","36","Kadin","Türk","teknoloji","12")
    print(calisan1)
    print(calisan2)
    print(calisan3)

    maviyaka1 = MaviYaka("84286235415","Furkan","Ermemiş","30","Erkek","Türk""4","12000","0.2")
    maviyaka2 = MaviYaka("45875325841","Thomas","Enderson","27","Erkek","Ingiliz","2","10000","0.1")
    maviyaka3 = MaviYaka("34675414852","Yigit","Akkan","27","Erkek","Türk","5","17000","0.5")
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)

    beyazyaka1= BeyazYaka("12378965414","Kerem","Saglam","23","Erkek","Türk","0","10000","1000")
    beyazyaka2 = BeyazYaka("12475395145","Osman","Pinar","27","Erkek","Türk","3","12000","2000")
    beyazyaka3 = BeyazYaka("145563258265","Ilkim","Dirgin","27","Kadin","Ingiliz","5","20000","2500")
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
except Exception as e:
    print(f"Hata: {str(e)}")

