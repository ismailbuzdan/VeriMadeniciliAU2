# -*- coding: utf-8 -*-
# Bu script iki farklı veri seti için keşifsel veri analizi (EDA) sürecini tek dosyada göstermektedir.
# Veri Seti 1: Python ile yapay olarak üretilen öğrenci performans verisi
# Veri Seti 2: Diskten okunan CSV formatındaki satış verisi
# Amaç: Veri yapısını anlamak, eksik veri kontrolü yapmak, özet istatistikler üretmek
# ve temel görselleştirmeler ile veriyi yorumlamaktır.

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Script ortamında grafiklerin sorunsuz üretilmesi için
import matplotlib.pyplot as plt

# Grafiklerin Türkçe karakter sorunu yaşamaması için temel ayar
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.unicode_minus"] = False

# -----------------------------------------------------------------------------
# 1) VERI SETI 1 - YAPAY VERI URETIMI
# -----------------------------------------------------------------------------
# Bu bölümde öğrenci performansı ile ilgili yapay bir veri seti oluşturulmaktadır.
# Değişkenler:
# - Yas: öğrencinin yaşı
# - CalismaSaati: haftalık çalışma süresi
# - Devamsizlik: dönem içindeki devamsızlık sayısı
# - InternetKullanimi: günlük sosyal/internet kullanım süresi
# - FinalNotu: yukarıdaki değişkenlerden etkilenerek oluşturulan final notu

np.random.seed(42)
ogrenci_sayisi = 200

yas = np.random.randint(18, 26, ogrenci_sayisi)
calisma_saati = np.random.randint(1, 25, ogrenci_sayisi)
devamsizlik = np.random.randint(0, 16, ogrenci_sayisi)
internet_kullanimi = np.random.randint(1, 9, ogrenci_sayisi)

# Final notu kontrollü bir formülle oluşturuldu.
# Çalışma saati arttıkça not artsın, devamsızlık ve aşırı internet kullanımı arttıkça düşsün istiyoruz.
final_notu = (
    45
    + (calisma_saati * 2.1)
    - (devamsizlik * 1.7)
    - (internet_kullanimi * 1.2)
    + np.random.normal(0, 6, ogrenci_sayisi)
)

# Notları 0-100 aralığında sınırlandırıyoruz.
final_notu = np.clip(final_notu, 0, 100)

df_yapay = pd.DataFrame({
    "Yas": yas,
    "CalismaSaati": calisma_saati,
    "Devamsizlik": devamsizlik,
    "InternetKullanimi": internet_kullanimi,
    "FinalNotu": np.round(final_notu, 2)
})

# Gerçek hayattaki veri problemlerini gösterebilmek için birkaç eksik değer ekliyoruz.
df_yapay.loc[[5, 41, 77], "CalismaSaati"] = np.nan
df_yapay.loc[[12, 90], "FinalNotu"] = np.nan

# -----------------------------------------------------------------------------
# 2) VERI SETI 1 - ILK INCELEME
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("VERI SETI 1 - YAPAY OGRENCI VERISI")
print("=" * 70)

# İlk 5 satır görüntülenir.
print("\nİlk 5 gözlem:")
print(df_yapay.head())

# Veri tipi ve gözlem sayısı incelenir.
print("\nVeri seti bilgisi:")
print(df_yapay.info())

# Boyut bilgisi alınır.
print("\nBoyut bilgisi (satır, sütun):", df_yapay.shape)

# -----------------------------------------------------------------------------
# 3) VERI SETI 1 - EKSIK VERI KONTROLU
# -----------------------------------------------------------------------------
# Hangi sütunda kaç eksik değer olduğu kontrol edilir.
print("\nEksik veri sayıları:")
print(df_yapay.isnull().sum())

# Eksik değerleri medyan ile dolduruyoruz.
# EDA'de farklı yaklaşımlar uygulanabilir, burada basit ve öğretici bir yöntem seçildi.
df_yapay["CalismaSaati"] = df_yapay["CalismaSaati"].fillna(df_yapay["CalismaSaati"].median())
df_yapay["FinalNotu"] = df_yapay["FinalNotu"].fillna(df_yapay["FinalNotu"].median())

print("\nEksik veri doldurma sonrası kontrol:")
print(df_yapay.isnull().sum())

# -----------------------------------------------------------------------------
# 4) VERI SETI 1 - OZET ISTATISTIKLER
# -----------------------------------------------------------------------------
print("\nÖzet istatistikler:")
print(df_yapay.describe())

# Korelasyon matrisi sayısal değişkenler arası ilişkiyi anlamak için kullanılır.
print("\nKorelasyon matrisi:")
print(df_yapay.corr(numeric_only=True))

# -----------------------------------------------------------------------------
# 5) VERI SETI 1 - GORSELLESTIRME
# -----------------------------------------------------------------------------
# Histogram: Final notlarının dağılımını gösterir.
plt.figure()
df_yapay["FinalNotu"].hist(bins=15)
plt.title("Yapay Veri - Final Notu Dağılımı")
plt.xlabel("Final Notu")
plt.ylabel("Frekans")
plt.tight_layout()
plt.savefig("grafik.png")
plt.close()

# Scatter plot: Çalışma saati ile final notu arasındaki ilişki incelenir.
plt.figure()
plt.scatter(df_yapay["CalismaSaati"], df_yapay["FinalNotu"])
plt.title("Yapay Veri - Çalışma Saati ve Final Notu İlişkisi")
plt.xlabel("Çalışma Saati")
plt.ylabel("Final Notu")
plt.tight_layout()
plt.savefig("grafik_2.png")
plt.close()

# Boxplot: Devamsızlığın dağılımını ve aykırı değer olup olmadığını gösterir.
plt.figure()
plt.boxplot(df_yapay["Devamsizlik"])
plt.title("Yapay Veri - Devamsızlık Boxplot")
plt.ylabel("Devamsızlık")
plt.tight_layout()
plt.savefig("grafik_3.png")
plt.close()

# -----------------------------------------------------------------------------
# 6) VERI SETI 2 - DISKTEN VERI CEKME (CSV DOSYASI)
# -----------------------------------------------------------------------------
# Bu bölümde harici bir dosyadan veri okunmaktadır.
# Dosya adı: eda_satis_verisi.csv
# Not: Bu dosya script ile aynı klasörde bulunmalıdır.

df_satis = pd.read_csv("eda_satis_verisi.csv", encoding="utf-8-sig")

print("\n" + "=" * 70)
print("VERI SETI 2 - SATIS VERISI (CSV'DEN OKUNDU)")
print("=" * 70)

# Tarih sütununu tarih tipine çeviriyoruz.
df_satis["Tarih"] = pd.to_datetime(df_satis["Tarih"])

# -----------------------------------------------------------------------------
# 7) VERI SETI 2 - ILK INCELEME
# -----------------------------------------------------------------------------
print("\nİlk 5 gözlem:")
print(df_satis.head())

print("\nVeri seti bilgisi:")
print(df_satis.info())

print("\nBoyut bilgisi (satır, sütun):", df_satis.shape)

# -----------------------------------------------------------------------------
# 8) VERI SETI 2 - EKSIK VERI KONTROLU
# -----------------------------------------------------------------------------
print("\nEksik veri sayıları:")
print(df_satis.isnull().sum())

# Sayısal değişkenlerde eksik değerleri medyan ile dolduruyoruz.
df_satis["Müşteri_Yaşı"] = df_satis["Müşteri_Yaşı"].fillna(df_satis["Müşteri_Yaşı"].median())
df_satis["Satış_Tutarı"] = df_satis["Satış_Tutarı"].fillna(df_satis["Satış_Tutarı"].median())

print("\nEksik veri doldurma sonrası kontrol:")
print(df_satis.isnull().sum())

# -----------------------------------------------------------------------------
# 9) VERI SETI 2 - OZET ISTATISTIKLER VE GRUPLAMALAR
# -----------------------------------------------------------------------------
print("\nÖzet istatistikler:")
print(df_satis.describe(include="all"))

# Bölgelere göre ortalama satış tutarı
print("\nBölgelere göre ortalama satış tutarı:")
print(df_satis.groupby("Bölge")["Satış_Tutarı"].mean().sort_values(ascending=False))

# Kategorilere göre toplam satış
print("\nKategorilere göre toplam satış tutarı:")
print(df_satis.groupby("Kategori")["Satış_Tutarı"].sum().sort_values(ascending=False))

# -----------------------------------------------------------------------------
# 10) VERI SETI 2 - GORSELLESTIRME
# -----------------------------------------------------------------------------
# Bölgelere göre ortalama satış tutarını sütun grafik ile gösteriyoruz.
plt.figure()
df_satis.groupby("Bölge")["Satış_Tutarı"].mean().sort_values().plot(kind="bar")
plt.title("Satış Verisi - Bölgelere Göre Ortalama Satış Tutarı")
plt.xlabel("Bölge")
plt.ylabel("Ortalama Satış Tutarı")
plt.tight_layout()
plt.savefig("grafik_4.png")
plt.close()

# Kategorilere göre toplam satış tutarını pasta grafiği ile gösteriyoruz.
plt.figure()
df_satis.groupby("Kategori")["Satış_Tutarı"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Satış Verisi - Kategorilere Göre Toplam Satış Payı")
plt.ylabel("")
plt.tight_layout()
plt.savefig("grafik_5.png")
plt.close()

# Müşteri yaşı ile satış tutarı arasındaki ilişkiyi scatter plot ile inceliyoruz.
plt.figure()
plt.scatter(df_satis["Müşteri_Yaşı"], df_satis["Satış_Tutarı"])
plt.title("Satış Verisi - Müşteri Yaşı ve Satış Tutarı")
plt.xlabel("Müşteri Yaşı")
plt.ylabel("Satış Tutarı")
plt.tight_layout()
plt.savefig("grafik_6.png")
plt.close()

# -----------------------------------------------------------------------------
# 11) GENEL DEGERLENDIRME
# -----------------------------------------------------------------------------
# Bu script ile iki farklı veri seti üzerinde temel keşifsel veri analizi uygulanmıştır.
# Birinci veri seti yapay olarak üretilmiş, ikinci veri seti ise dış dosyadan okunmuştur.
# EDA sürecinde uygulanan başlıca adımlar:
# - Veri oluşturma / veri okuma
# - İlk gözlem ve veri tipi kontrolü
# - Eksik veri analizi ve doldurma
# - Özet istatistikler
# - Korelasyon ve gruplama
# - Temel görselleştirmeler
print("\nAnaliz tamamlandı.")
