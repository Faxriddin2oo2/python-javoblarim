# Bismillah
"""
Created on Sat Jul  6 17:17:09 2024

@author: Faxriddin
"""
# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# def kupaytmani_top(*sonlar):
#     """Sonlarning ko'paytmasini qaytaruvchi funksiya"""
#     kupaytma = 1
#     for son in sonlar:
#         kupaytma *= son
#     return kupaytma

# print(kupaytmani_top(1,2,3,4))
        

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, 
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def info(ism,familiya,**malumotlar):
    """Talaba haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar    

print(info('Faxriddin', 'Teshaboyev', t_yil = 2002, t_joy = 'Jarqorgan'))