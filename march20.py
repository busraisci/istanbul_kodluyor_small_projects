#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Lütfen boyunuzu giriniz: "))
kilo =float(input("Lütfen kilonuzu giriniz: "))
vki = kilo / (boy * boy)
print(vki)

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("Lütfen maaşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranını giriniz: "))
zamliMaas = maas + (maas * (zamOrani / 100))
print(zamliMaas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program 

number1 = int(input("Lütfen ilk sayiyi giriniz: "))
number2 = int(input("Lütfen ikinci sayıyıyı giriniz: "))
number3 = int(input("Lütfen üçüncü sayıyı giriniz: " ))
bigNumber =0
if number1 > number2:
    bigNumber = number1
else:
    bigNumber = number2
if number3 > bigNumber:
    bigNumber = number3
else:
    bigNumber = bigNumber 
    print(bigNumber)    

   
#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını 

#Alanı: 3.14*(r*r) Çevresi: 2*3.14*r

yaricap = float(input("Yarıçap giriniz: "))

alan = 3.14 * (yaricap * yaricap)
print(f"Alan: {alan}")

cevre = 2 * 3.14 * yaricap
print(f"Çevre : {cevre} ")


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

number = int(input("Lütfen palindrom bir sayı giriniz: "))

numberStr = str(number)

print(numberStr)


def palindrom_mu(sayi) :
    #Sayıyı string olarak dönüştürelim
    sayi_str = str(sayi)
    #Sayının tersini alalım
    ters_sayi_str = sayi_str[: :-1]
    #Ters çevrilmiş  sayı. aslında giriş sayısıyla eşit mi kontrol edelim
    return sayi_str == ters_sayi_str

# Kullanıcılardan bir sayı girişi alalım
sayi = int(input("Bir sayı girin: ")) 

# Palindrom olup olmadığını kontrol edelim
if palindrom_mu(sayi):
    print("Girdiğiniz sayı bir palindromdur. ")
else:
    print("Girdiğiniz sayı bir palindrom değildir. ")    




