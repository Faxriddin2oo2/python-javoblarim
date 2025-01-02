# Bismillah
"""
Created on Tue Jul 23 15:31:05 2024

@author: Faxriddin
"""

# From lesson
# FUNKSIYANI TEKSHIRISH
# def get_full_name(ism, familiya):
#     return f"{ism} {familiya}".title()

# get_full_name('faxriddin', 'teshaboyev')



# SONLARNI TEKSHIRISH
# def getArea(r, pi = 3.14159):
#     """Doiraning yuzini qaytaruvchi funksiya"""
#     return pi*(r**2)

# def getPerimetr(r, pi = 3.14159):
#     """Doiraning perimetirini qaytaruvchi funksiya"""
#     return 2*pi*r

# getArea(10)
# getPerimetr(10)
# getPerimetr(4)



# MANTIQIY QIYMATLARNI TEKSHIRISH
# def tubSonmi(n):
#     if n == 2 or n == 3: return True
#     if n%2 == 0 or n<2: return False
#     for i in range (3, int(n**0.5)+1, 2): #faqat toq sonlarni tekshiramiz
#         if n%i == 0:
#             return False
#     return True



# PRACTICE
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
# def maxSon(x,y,z):
#     max = x
#     if x<y:
#         max = y
#     if z>y:
#         max = z
#     return max 

# print(maxSon(14, 11, 9))



# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
# def kattaXarf():
#     sozlar = ['olma', 'nok', 'taxta', 'kocha', 'noutbook', 'issiq']
#     kattaSozlar = []
#     for soz in sozlar:
#          kattaSozlar.append(soz.title())
         
#     return kattaSozlar

# print(kattaXarf())



# Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
def juftSon(m):
    if m %2 == 0: return True
    else: return False

# print(juftSon(4))
        

 

























