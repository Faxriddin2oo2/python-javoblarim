# Bismillah
"""
Created on Sat Jul  6 15:24:19 2024

@author: Faxriddin
"""

# range() funksiyasiga o'xshagan funksiyani qadam degan o'zgaruvchi qo'shib yozish 
# def oraliq(min,max,qadam = ''):
#     sonlar = []
#     if qadam:
#         while min<max:
#             sonlar.append(min)
#             min += int(qadam)
#     else:
#         while min<max:
#             sonlar.append(min)
#             min += 1
#     return sonlar

# print(oraliq(1, 10))
# print(oraliq(1, 10, 2))



# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
def malumot_ber(ismi,familiyasi,t_yil,t_joy,email = '',raqami=''):
    malumotlar = {
        "ism" : ismi,
        "familiya": familiyasi,
        "t_yil" : t_yil,
        "t_joy" : t_joy,
        "email" : email,
        "raqam" : raqami
        }
    return malumotlar
# talaba = malumot_ber("Faxriddin", "Teshaboyev", 2002, "Jarqo'rg'on", "teshaboyevfaxriddin1@gmail.com",90000000)

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. 
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# mijozlar = []
# while True:
#     print("\nQuyidagi malumotlarni kiriting: ")
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting:")
#     t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     t_joy = input("Tug'ilgan joyingizni kiriting: ")
#     email = input("Emailingizni kiriting: ")
#     raqam = int(input("Raqamingizni kiriting: "))
#     mijozlar.append(malumot_ber(ism,familiya,t_yil,t_joy,email,raqam))
#     savol = input("Yana malumot kiritasizmi? (yes/no)")
#     if savol != 'yes':
#         break
# print("Bizning mijozlarimiz: ")
# for mijoz in mijozlar:
#     print(f"{mijoz['familiya'].title()} {mijoz['ism'].title()} {mijoz['t_yil']} yilda {mijoz['t_joy'].title()} tumanida tug'ilgan")


# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def kattasini_top(son1,son2,son3):
#     if son1 > son2 and son1>son3:
#         return son1
#     elif son2 > son1 and son2>son3:
#         return son2
#     else:
#         return son3

# print(kattasini_top(3, 6, 5))

# tepadagi funksiyani boshqacha yechimi:
# def kattasini_top(x,y,z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# print(kattasini_top(4, 5, 8))



# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida 
# qaytaruvchi funksiya yozing
# def parametrlar_qaytar(radius, pi=3.14):
#     parametrlar = {
#         "radius": radius,
#         "diametr": radius*2,
#         "perimetr": 2*radius*pi,
#         "yuzi" : pi*radius**2
#         }
#     return parametrlar
    
# print(parametrlar_qaytar(3))




# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 
# 1 dan katta musbat sonlar)
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# print(tub_sonlar_top(1, 10))


# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. 
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
# unda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
def fibonacci(n):    
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(10))















