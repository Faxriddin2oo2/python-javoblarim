# Bismillah
"""
Created on Fri Jul  5 18:35:30 2024

@author: Faxriddin
"""
# def salom_ber():
#         """Salom beruvchi funksiya"""
#         print("Assalomu alaykum!")     
        
# salom_ber()


# # Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def t_yilni_hisobla():
#     """Tug'ilgan yilini hisoblaydigan funksiya"""
#     ism = input("Ismingizni kiriting: ")
#     yosh = int (input("Yoshingizni kiriting: "))
#     print(f"{ism.title()} sizning tug'ilgan yilingiz: {2024 - yosh} ")
    
# t_yilni_hisobla()


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kvadrat_kubni_hisobla():
#     """Sonning kvadrati va kubini hisoblovchi funksiya"""
#     son = int(input("Son kiriting : "))
#     print(f"{son}ning kvadrati = {son**2}, kubi esa = {son**3}")

# kvadrat_kubni_hisobla()


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def toq_juftligini_hisobla():
#     """son juft yoki toqligini aniqlovchi funksiya"""
#     son = int(input("Iltimos, son kiriting: "))
#     if son%2 == 0:
#         print("Siz kiritgan son juft!")
#     else:
#         print("Siz kiritgan son toq!")
        
# toq_juftligini_hisobla()   


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def kattani_aniqla():
#     """Sonlarni kattasini chiqaruvchi funksiya"""
#     son1 = int(input("Birinchi sonni kiriting: "))
#     son2 = int(input("Ikkinchi sonni kiriting: "))
#     if son1 > son2:
#         print(f"Bu sonlarning kattasi: {son1}")
#     elif son1 < son2:
#         print(f"Bu sonlarning kattasi: {son2}")
#     else:
#         print("Sonlar teng!")

# kattani_aniqla()
        
        
# Foydalanuvchidan x va y sonlarini olib, x darajasida y ni konsolga chiqaruvchi funksiya yozing.
# def darajaga_chiqar(y=2):
#     """Bir sonni ikinchisining darajasiga chiqaruvchi funksiya"""
#     x = int(input("X ga qiymat bering: "))
#     print(f"x darajasida y = {x**y}")
      
# darajaga_chiqar()

# def bolinish_alomatlari(son):
#    """Qanaqa sonlarga bo'linishini tekshiradigan funksiya"""
#     n = 2
#     while son>= n:
#         if son%n == 0:
#             print(f"{son} {n}ga qoldiqsiz bo'linadi")
#         n+=1

# bolinish_alomatlari(2520)
        
        
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 
# Natijalarni konsolga chiqaring.
def bolinish_alomatlari(son):
    """Bo'linish alomatlarini tekshiruvchi funksiya"""
    for n in range(2,11) :
        if son%n == 0:
            print(f"{son} {n}ga qolqisiz bo'linadi")
            
bolinish_alomatlari(2520)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        