# Starbucks Ürün Analizi

Bu proje, *Starbucks ürünleri* üzerinde veri analizi ve görselleştirme yaparak içgörüler elde etmeyi amaçlamaktadır. Kullanılan veri kümesi, Starbucks'ta bulunan farklı kategorilere ait yiyecek ve içeceklerin besin değerlerini içermektedir. Proje kapsamında *veri analizi, görselleştirme ve karar ağacı modeli oluşturma* adımları gerçekleştirilmiştir.

## 📌 Projede Kullanılan Yöntemler

1. *Veri Keşfi ve Ön İşleme*
   - Veri setinin yüklenmesi ve temel istatistiklerinin incelenmesi
   - Eksik verilerin doldurulması
   - Kategorik değişkenlerin sayısal hale getirilmesi

2. *Veri Görselleştirme*
   - *Pasta Grafiği:* Ürün kategorilerinin dağılımı
   - *Sütun Grafiği:* Her bir ürün kategorisinin frekansı
   - *Histogram:* Kalori dağılımı
   - *Saçılım Grafiği:* Kalori ve karbonhidrat arasındaki ilişki
   - *Korelasyon Matrisi:* Değişkenler arasındaki ilişkileri gösteren ısı haritası

3. *Makine Öğrenmesi ile Karar Ağacı Modeli*
   - Bağımsız değişkenler: Kalori, yağ, karbonhidrat, lif ve protein değerleri
   - Bağımlı değişken: Ürün kategorisi
   - Veri setinin eğitim ve test olarak ayrılması
   - Karar ağacı modeli oluşturulması ve doğruluk oranının hesaplanması
   - Karar ağacının görselleştirilmesi

---

## 📂 Dosya Yapısı

- **starbucks.csv** → Starbucks ürünlerinin besin değerlerini içeren veri seti
- **starbucks_analysis.py** → Veri analizi ve makine öğrenmesi kodları

## 📊 Veri Görselleştirme

Projede kullanılan görselleştirme yöntemleri ile Starbucks ürünlerine dair önemli bilgiler elde edilmiştir. Aşağıda bazı görselleştirmeler hakkında açıklamalar yer almaktadır:

### 🎯 Ürün Kategorilerine Göre Dağılım

Ürün kategorilerinin yüzdelik dağılımını görmek için *pasta grafiği* kullanılmıştır. Her kategoriye özel bir renk atanarak görselleştirme yapılmıştır.

### 📈 Kalori Dağılımı

Ürünlerin kalori dağılımını analiz etmek için *histogram grafiği* oluşturulmuştur. Böylece hangi aralıktaki ürünlerin daha fazla olduğu gözlemlenmiştir.

### 🔍 Kalori & Karbonhidrat İlişkisi

Ürünlerin kalori ve karbonhidrat değerleri arasındaki ilişki *scatter plot (saçılım grafiği)* ile incelenmiştir. Böylece, yüksek karbonhidrat içeren ürünlerin genellikle daha yüksek kalori değerine sahip olduğu görülmüştür.

### 🔥 Korelasyon Analizi

Besin değerleri arasındaki ilişkileri daha iyi anlamak için *korelasyon matrisi* oluşturulmuştur. Bu sayede, hangi besin değerlerinin birbirleriyle doğrudan ilişkili olduğu analiz edilmiştir.

---

## 🧠 Karar Ağacı Modeli

Proje kapsamında, Starbucks ürünlerini besin değerlerine göre sınıflandıran bir *karar ağacı modeli* oluşturulmuştur. Modelin doğruluk oranı hesaplanmış ve karar ağacının görselleştirilmesi gerçekleştirilmiştir.

*Öne çıkan noktalar:*
- Veri seti eğitim (%80) ve test (%20) olarak ayrılmıştır.
- *DecisionTreeClassifier* kullanılarak model eğitilmiştir.
- Modelin doğruluk oranı hesaplanmış ve değerlendirilmiştir.

---

## Starbucks Ürün Dağılımı 
![WhatsApp Image 2025-02-10 at 00 40 30_9e43a3e8](https://github.com/user-attachments/assets/dc709e0f-641f-4270-a026-8fbea515ef78)
## Ürün Türlerine Göre Dağılım
![WhatsApp Image 2025-02-10 at 00 38 13_6d3ae473](https://github.com/user-attachments/assets/3af37684-1350-4563-be01-0fc8a43d89ab)
## Kalori Dağılımı 
![WhatsApp Image 2025-02-10 at 00 41 15_8d24dcf3](https://github.com/user-attachments/assets/737ab01f-8a33-424c-bbb7-d9845d971cb0)
## Kalori ve Karbonhidrat İlişkisi
![WhatsApp Image 2025-02-10 at 00 38 44_1ac31abf](https://github.com/user-attachments/assets/cf2bc9cf-a783-4f70-9b2a-aa6e8f4969b3)
## Değişkenler arasındaki Korelasyon
![WhatsApp Image 2025-02-10 at 00 39 43_dc0bbee3](https://github.com/user-attachments/assets/74b70843-4eb5-4445-ba5c-3188c0c82a9f)
## Decision tree figure
![WhatsApp Image 2025-02-10 at 00 41 51_2197af77](https://github.com/user-attachments/assets/c059ca57-22a6-4bd6-a41c-038459723d0b)
## Doğruluk Oranı 
![WhatsApp Image 2025-02-10 at 00 09 33_9cee2095](https://github.com/user-attachments/assets/2e88d70c-9731-49ce-a505-6f5615c9bcf1)








