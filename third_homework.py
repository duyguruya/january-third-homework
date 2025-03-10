sayi = int(input("Bir sayı girin: "))

# for döngüsü ile toplam hesaplama
toplam_for = 0
for i in range(1, sayi + 1):
    toplam_for += i
print(f"For döngüsü ile toplam: {toplam_for}")

# while döngüsü ile toplam hesaplama
toplam_while = 0
i = 1
while i <= sayi:
    toplam_while += i
    i += 1
print(f"While döngüsü ile toplam: {toplam_while}")