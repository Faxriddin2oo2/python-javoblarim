#Bismillah
"""
Created on Sun Jun 30 15:46:25 2024

@author: Faxriddin
"""
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=='gm':
#         print(car.upper())
#     else:
#         print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# login = input("Loginingizni kiriting: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# birinchi_son = input("1-chi sonni kiriting: ")
# ikkinchi_son = input("2-chi sonni kiriting: ")
# if birinchi_son == ikkinchi_son:
#     print("Sonlar teng ekan!")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = int(input("Son kiriting: "))
# print("Son musbat!") if son >= 0 else print("Son manfiy!")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
number = int(input("Son kiriting: "))
if number >= 0:
    print(f"{number} ning ildizi {int(number**(1/2))}")
else:
    print("Musbat son kiriting!")


