# Kullanıcıdan bir metin almanızı istiyorum. Bu metnin içindeki en çok tekrar eden harfi bulmalı ve  kaç kere tekrar ettiğini göstermeli.
metin = input("Bir metin giriniz: ")

harfSayilari = {}
for harf in metin:
    harfSayilari[harf] = metin.count(harf)

enCokTekrarEdenHarf = max(harfSayilari, key=harfSayilari.get)
enCokTekrar = harfSayilari[enCokTekrarEdenHarf]

print(f"Girilen '{metin}' metninde en çok tekrar eden harf: {enCokTekrarEdenHarf}\nTekrar sayısı: {enCokTekrar}")
