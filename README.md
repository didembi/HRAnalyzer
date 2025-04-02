📌 Proje Adı: HRAnalyzer
Açıklama:
Bu proje, çalışanların maaş hesaplamalarını, tecrübe analizlerini ve kategori bazlı değerlendirmelerini yapan bir insan kaynakları yönetim sistemidir. Çalışanlar İşsiz, Çalışan, Mavi Yaka, Beyaz Yaka olarak sınıflandırılır ve maaşlarına zam oranları belirlenir.

🚀 Özellikler
✅ Çalışanların temel bilgilerini kaydetme
✅ Mavi yaka, beyaz yaka gibi kategorilere ayırma
✅ Tecrübe, sektör ve maaş bazlı analizler yapma
✅ Yeni maaş hesaplama ve zam oranı belirleme
✅ Çalışan verilerini pandas kullanarak tablo halinde görüntüleme

📂 Proje Yapısı

📦 HRAnalyzer
 ┣ 📜 main.py               # Ana çalışma dosyası
 ┣ 📜 Insan.py              # Temel insan sınıfı
 ┣ 📜 Issiz.py              # İşsiz sınıfı
 ┣ 📜 Calisan.py            # Çalışan sınıfı
 ┣ 📜 MaviYaka.py           # Mavi yaka sınıfı
 ┣ 📜 BeyazYaka.py          # Beyaz yaka sınıfı
 ┣ 📜 README.md             # Proje açıklamaları (bu dosya)
🛠 Kullanılan Teknolojiler
🔹 Python
🔹 Pandas (veri analizi için)

💻 Kurulum & Çalıştırma
Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsin:
1️⃣ Projeyi klonla
git clone https://github.com/kullaniciadi/HRAnalyzer.git
cd HRAnalyzer
2️⃣ Gerekli bağımlılıkları yükle
pip install pandas
3️⃣ Projeyi çalıştır
python main.py

📊 Örnek Çıktılar
Projeyi çalıştırdığında aşağıdaki gibi bir çıktı alabilirsin:

Calisan sinifi
Ad: Deniz, Soyad: Kara, Maaş: 13000, Yeni Maaş: 14200
Ad: Merve, Soyad: Yilmaz, Maaş: 12200, Yeni Maaş: 12800
...
Maaşı 15000TL üzerinde olan çalışan sayısı: 3
 
