# Bismillah
"""
Created on Fri Jul 26 17:21:57 2024

@author: Faxriddin
"""

#FROM LESSON
# import datetime as dt

# hozir = dt.datetime.now()
# print(hozir)

# # sanani ajratib olish
# print(hozir.date())

# #vaqtni ajratib olish
# print(hozir.hour)

# # minutni ajratib olish
# print(hozir.minute)

# # sekundni ajratib olish
# print(hozir.second)


# date ()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga = dt.date(2024, 7, 27)
# print(f"Ertangi sana: {ertaga}")

# # time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23, 45, 30)
# print(vaqtKeyin)

# Sanalar orasidagi farq
# bugun = dt.date.today()
# tugilgan_kunim = dt.date(2024, 9, 4)
# farq = tugilgan_kunim - bugun
# print(farq)
# print(f"Tug'ilgan kuningizgacha {farq.days} kun qoldi")

# Soatlar orasida farq
# hozir = dt.datetime.now()
# futbol = dt.datetime(2024, 7, 27, 23, 45, 00)
# farq = futbol - hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar / 60)
# soatlar = int(minutlar / 60)
# print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi")

# Vaqtni formatlash
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")

# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")

# sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)



# math —MATEMATIK FUNKSIYALAR
# import math

# PI = math.pi
# print(f"PI ning qiymati: {PI}")
# E = math.e
# print(f"e ning qiymati: {E}")


# #Trigonometriya
# print(math.sin(math.pi / 6))
# print(math.cos(0))
# print(math.tan(PI))


# # Radianlar va burchaklar o'rtasida konvertatsiya
# print(math.degrees(math.pi/2))
# print(math.radians(90))


# # logarifmlar
# #natural logarifm
# print(math.log(5))
# # 10 asosli logarifm
# print(math.log10(100))


# Sonlarni yaxlitlash
# x = 4.6
# print(math.ceil(x))
# print(math.floor(x))


# # Kvadrat ildiz
# x = 81
# math.sqrt(x)

# # Darajaga oshirish
# math.pow(x, 3) # x ning kubi
# math.pow(x, 5) # x ning 5 - darajasi
# math.pow(x, 1/3) # x ning kub ildizi



# pprint - CHIROYLI PRINT
# pprint(r.json())
# from pprint import pprint
# import json

# filename = "bemor.json"
# with open(filename) as f:
#     bemor = json.load(f)
    
# pprint(bemor)

# import requests
# r = requests.get("https://api.github.com")

# pprint(r.json())



# RegEx - ANDOZA YORDAMIDA MATN IZLASH
# import re
# from uzwords import words

# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...р$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))


# andoza = "^а...й$"
# matches = []
# for word in words:
#     if re.match(andoza, word):
#         matches.append(word)
        
# print(matches)
## Emailni ajratib olish
# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.findall(andoza, matn)
# print(email)

# # Kuchli parolni tekshirish
# andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
# msg = "Yangi parol kiriting"
# msg += "(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
# msg += "1 ta son va 1 ta maxsus belgi boʻlishi kerak): "

# while True:
#     password = input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermadi")
        
        

# PRACTICE