# Proje Gereksinimleri

## 1) apt search çıktısını ayrıştırma
- Kullanıcı bir paket adı yazar.
- Program `apt search <paket>` çalıştırır.
- Çıktıdan paket adlarını ve temel bilgiyi ayrıştırır.

## 2) Snap ve Flatpak araması (aynı anda)
- Program snap yüklüyse `snap find <paket>` ile arama yapar.
- Program flatpak yüklüyse `flatpak search <paket>` ile arama yapar.
- Sonuçları tek ekranda ayrı başlıklar altında gösterir.

## 3) Paket detayları
- apt için: versiyon, boyut (Installed-Size), bağımlılıklar (Depends)
- snap/flatpak için: temel sürüm/bilgi (araçların sağladığı kadarıyla)
