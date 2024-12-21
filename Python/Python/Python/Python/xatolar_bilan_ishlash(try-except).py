# Bismillah
"""
Created on Tue Jul 23 13:36:08 2024

@author: Faxriddin
"""


# yosh = input ("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")
# except:
#     print("Butun son kiritmadingiz")
    
# print("Dastur Tugadi!")

# MA'LUM TURDAGI XATOLARNI USHLASH
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")


# ZeroDivisionError
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# try:
#     z = y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print("Natija = " , z)
    

# IndexError 
# mevalar = ['olma', 'anor', 'anjir', 'uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda  {len(mevalar)} ta meva bor xolos")


# KeyError
# user = {"username" : "faxriddin",
#         "status" : "admin",
#         "email" : "admin@faxriddin.dev",
#         "phone" : "998945535332"}
# key = 'tel'
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")


# FileNotFoundError
# filename = 'data.txt' # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Boshqa fayl tanlang.")
    


# BIR NECHTA XATOLARNI USHLASH  
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n 
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadiz.")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")



# XATOLARNING OLDINI OLISH
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break        

# print(f"Siz {2021-yosh} yilda tug'ilgansiz")        
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    