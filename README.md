# Keşifsel Veri Analizi Ödevi

Bu repo, keşifsel veri analizi (EDA) ödevi kapsamında hazırlanmıştır. Çalışmada iki farklı veri seti üzerinde aşama aşama analiz gerçekleştirilmiştir.

## Çalışmanın Kapsamı

Bu ödevde iki farklı veri seti kullanılmıştır:

1. **Yapay olarak üretilen veri seti**
   - Python kullanılarak oluşturulmuştur.
   - Örnek değişkenler üzerinden veri üretimi yapılmış ve temel keşifsel veri analizi adımları uygulanmıştır.

2. **Dosyadan okunan veri seti**
   - CSV formatındaki veri dosyası kullanılmıştır.
   - Veri içe aktarıldıktan sonra özet istatistikler, eksik veri kontrolü, dağılım incelemeleri ve görselleştirmeler yapılmıştır.

## Kullanılan Dosyalar

- `kesifsel_veri_analizi_odev.py` → Tek script dosyası
- `eda_satis_verisi.csv` → İkinci veri seti
- `kisa_rapor_eda_odev_guncel2.docx` → Kısa açıklayıcı rapor

## Uygulanan Adımlar

Script içerisinde aşağıdaki işlemler yer almaktadır:

- Gerekli kütüphanelerin yüklenmesi
- Yapay veri setinin oluşturulması
- İlk veri incelemesi
- Veri tiplerinin kontrol edilmesi
- Eksik veri analizi
- Tanımlayıcı istatistiklerin incelenmesi
- Aykırı değerlerin gözlemlenmesi
- Görselleştirme işlemleri
- Dosyadan veri okuma ve ikinci veri seti üzerinde aynı EDA sürecinin uygulanması
- Genel sonuç ve değerlendirme

## Not

Script tek dosya olarak hazırlanmıştır ve her işlem `#` yorum satırları ile açıklanmıştır.

## GitHub Repo Linki

GitHub bağlantısı:

[https://github.com/ismailbuzdan/VeriMadeniciliAU2](https://github.com/ismailbuzdan/VeriMadeniciliAU2)

## Çalıştırma

Aşağıdaki temel kütüphaneler gereklidir:

```bash
pip install pandas numpy matplotlib seaborn
```

Ardından script çalıştırılabilir:

```bash
python kesifsel_veri_analizi_odev.py
```

## Hazırlayan

İsmail Buzdan

