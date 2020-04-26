import random
i=0
sayac = 0
hak = int(input("Kaç hakkınız olsun ?"))
rand = random.randint(1,100)


while (i<hak):
     i += 1
     sayac += 1
     sayi = int(input("Bir sayı giriniz: "))
     if (sayi<rand):
         print(f'Çık.')
     elif (sayi>rand):
         print(f'İn.') 
     else:
         print(f'Tebrikler {sayac}. denemede bildiniz. Toplam puanınız: {100-(100/hak)*(sayac-1)}')    
         break
     if (i==hak):
         print(f'Hakkınız bitti tekrar deneyin. Tutulan sayı: {rand}')   
