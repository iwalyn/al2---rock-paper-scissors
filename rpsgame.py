import random

while True:
    rakipsecim = random.choice(["🪨", "✂", "📝"])

    secim = input("tas (t), kagit (k), makas (m)?  ").lower()

    if secim == "t":
        secim = "🪨"
    elif secim == "k":
        secim = "📝"
    elif secim == "m":
        secim = "✂"
    else:
        print("Geçersiz seçim!")
        continue

    # Kazanma durumlarını kontrol et
    if secim == rakipsecim:
        print(f"{rakipsecim}'e karşı {secim} yaptınız. Berabere!")
    elif (secim == "🪨" and rakipsecim == "✂") or \
         (secim == "✂" and rakipsecim == "📝") or \
         (secim == "📝" and rakipsecim == "🪨"):
        print(f"{rakipsecim}'e karşı {secim} yaptınız. Kazandınız!")
    else:
        print(f"{rakipsecim}'e karşı {secim} yaptınız. Kaybettiniz!")

    devam_istegi = input("Tekrar oynamak ister misiniz? (y/n) ").lower()
    if devam_istegi == "y":
        print("Yeniden Baslaniyor...")
        continue
    else:
        break