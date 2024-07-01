# Bismillah
"""
Created on Sun Jun 30 15:16:00 2024

@author: Faxriddin
"""

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['ali', 'vali', 'hasan', 'husan', 'olim']
# for ism in ismlar:
#     print('Assalomu alaykum', ism.title())
    
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# print("Kod", len(ismlar), "marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11,50,2))
# for son in sonlar:
#     print(f"{son**3}\n")

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# print("Sevimli kinolaringizni kiriting:")
# for n in range(5):
#     kinolar.append(input(f"{n+1} chi kino: "))
# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odamlar = []
n = int(input("Bugun nechi kishi bilan ko`rishdingiz>>>"))
m= list(range(n))
for k in m:
    odamlar.append(input(f"{k+1} chi odamning ismi: "))
print("Siz uchrashgan odamlar:",odamlar)