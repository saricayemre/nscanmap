# Gelişmiş Ağ Tarama Aracı: NScanMap
# NScanMap Nedir?

![resim](https://github.com/saricayemre/nscanmap/blob/main/resimler/resim.png?raw=true)

NScanMap, nmap tabanlı ağ keşif programıdır. python dili ile kodlanmıştır. Nmap aracının içinde bulunan tüm ramaları tek komutile kullanamya yarar ve tarama sonuçlarını raporlar. Bu araç ile NMap'ın komutlarını tek tek girmenize gerek yoktur. Sadece programı çalıştırarak Nmap içerisinde bulunan en popler ve işe yarar taramaların sonuçlarını kullanıcıya gösterir. 

## İçerisindeki Tarama Çeşitleri ve Açıklamaları

### İşletim Sistemi Tespiti

Sızılan sunucuların işletim sistemini bilmek oldukça faydalı bir senaryo hazırlamamıza olanak sağlar. NScanMap aracı, ilk olarak hedefin işletim sistemini tespit etme işlemini gerçekleştirir. Raporlama kısmında işletim sistemini, kernek(çekirdek) sürümünü gösterir.

### TCP Bağlantı Taraması

Bu tarama hedefe paketler göndererek hedefin yanıt vermesi beklenir. Açık durumda ise hedef RST-ACK paketlerigönderir ve ana makine karşılık olarak ACK bayraklı paketler göndererek raporlama işlemi sunulur. 

### UDP Taraması

Hedeffe UDP paketleri göndererek hedefin yanıt vermesi beklenir. Eğer hedef yanıt verirse portlar açık demektir.

### FIN Taraması

Hedefe FIN bayraklı paketler gönderir. Sonucunda portların durumu hakkında bilgi verir.

### Ping Taraması

Hedefe tek bir ping göndererek  ve hedefin ICMP Echo yanıtını vermesi beklenir. Bu raporlama sonucunda port durumu hakkında bilgi verir.

### ARP Keşfi

Hedefe paket gönderek host adı domain adı gibi bilgileri listelemeye yarar.

### IP Protokol Taraması

Hedefe IP paketleri göndererek alınan yanıtta portların hangi servisi kullandığını, durumlarını ve protokollarını gösterir.

### No Port Taraması

Portların bağlantı noktası taraması yapmamızı sağlayan taramadır ve sonucunda portların bağlantı durumlarını rapor eder.

# Kullanımı

![indexgif](https://github.com/saricayemre/nscanmap/blob/main/resimler/index.gif?raw=true)

```
cd NScanMap/
chmod +x nscanmap.py
sudo pip3 install -r requirement.txt
python3 nscanmap.py

```

