# Bismillah
"""
Created on Wed Jul 31 17:29:21 2024

@author: Faxriddin
"""

# Username Generator

# Username generatsiya qiluvchi user_name nomli funksiyani yozing.

# Funksiya foydalanuvchidan ismini so’rashi kerak.

# Keyin funksiya kiritilgan ismni teskari o’girib, uning oxiriga 0 dan 9 gacha bo’lgan ixtiyoriy sonni qo’shsin.

# Oxirida funksiya foydalanuvchiga usernameni qaytarsin.
# import random as r

# def user_name():
#     ism = input("Ismingizni kiriting: ")
#     for i in reversed(ism.lower()):
#         print(i, end="")
#     print(r.randint(0, 10))
        

# user_name()




# String to Integers.

# Convert_add degan funksiya yasang, u orqali kiritilgan stringlar listini ([‘1’, ‘3’, ‘5’])  integerga o’tkazib ([1, 3, 5]), 
# summasi hisoblansin (9).
def convert_add(lst):
    sonlar = [int(son) for son in lst]
    print(sum(sonlar))
        
convert_add(["1", '2', "4"])

# def Сonvert_add(lst):
#     sonlar= [int(son) for son in lst]
#     yigindi = sum(sonlar)
#     return yigindi

# result = convert_add(['6', '7', '2'])
# print(result)  
