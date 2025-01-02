# Bismillah
"""
Created on Sun Jun 30 16:39:33 2024

@author: Faxriddin
"""

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print("Bu son juft emas")
# else:
#     print("Rahmat")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh >=60:
#     narh = "bepul"
# elif yosh<= 18:
#     narh = 10000
# else:
#     narh = 20000

# print(f"Sizga kirish {narh}")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# birinchi_son = float(input('Birinchi sonni kiriting: '))
# ikkinchi_son = float(input("Ikkinchi sonni kiriting: "))
# if birinchi_son > ikkinchi_son:
#     print(birinchi_son, ">", ikkinchi_son)
# elif birinchi_son < ikkinchi_son:
#     print(birinchi_son, ">", ikkinchi_son)
# else:
#     print("Sonlar teng!")
    
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va 
# foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan 
# solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan 
# xabarlarni chiqaring.
# mahsulotlar = ['anor', 'olma', 'nok', 'limon', 'pista', 'tuz', 'non', 'bodom', 'mosh', 'guruch']
# savat = []
# for n in range(4):
#     savat.append(input(f"{n+1} chi mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va 
# do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga 
# qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['anor', 'olma', 'nok', 'limon', 'pista', 'tuz', 'non', 'bodom', 'mosh', 'guruch']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f"{n+1} chi mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:", mavjud_emas)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor" )

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va 
# foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login 
# mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ["polvon", 'kachok', 'olim', 'aqlli', 'kamtar']
# ask = input ("Loginni kiriting:")
# if ask in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")


# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
# son = int(input("Iltimos son kiriting: "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n}ga qoldiqsiz bo'linadi")



























