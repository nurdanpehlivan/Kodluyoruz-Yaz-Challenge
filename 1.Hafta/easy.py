# Kullanıcının doğum tarihini alarak kaç yaşında olduğunu bulan bir algoritma yazmanızı istiyorum.
import datetime

# Şu anki tarihi alma
today = datetime.datetime.now()

# Kullanıcıdan doğum tarihi
birth_year = int(input("Doğum yılınızı girin: "))
birth_month = int(input("Doğum ayınızı girin: "))
birth_day = int(input("Doğum gününüzü girin: "))

# Doğum tarihini datetime nesnesine dönüştürme
birth_date = datetime.datetime(birth_year, birth_month, birth_day)

# Yaşı hesaplama
age = today.year - birth_date.year

# Doğum günü bu yıl geçtiyse yaşı bir azaltma
if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
    age -= 1

# Sonucu yazdırma
print("Yaşınız:", age)

