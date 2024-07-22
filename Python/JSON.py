# Bismillah 
"""
Created on Mon Jul 22 15:00:37 2024

@author: Faxriddin
"""

# From lesson
import json

# x = 10
# x_json = json.dumps(x)

# ism = 'faxriddin'
# ism_json = json.dumps(ism)

# sonlar = [12, 32, 65, 78]
# sonlar_json = json.dumps(sonlar)


# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# bemor_json = json.dumps(bemor)
# bemor = {
#     "ism" : "Alijon Valiyev",
#     "yosh" : 30,
#     "oila" : True,
#     "farzandlar" : ("ahmad", "bonu"),
#     "allergiya" : None,
#     "dorilar" : [
#         {"nomi" : "Analgin", "midqori" : 0.5},
#         {"nomi" : "Panadol", "miqdori": 1.2}
#         ]
# }

# bemor_json = json.dumps(bemor, indent= 4)

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

with open('data/bemor.json','w') as f:
    json.dump(bemor,f)

# PRACTICE
# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)

with open('data/avto.json', 'w') as a:
    json.dump(data, a)



# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
talaba = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba_json = json.dumps(talaba)
talaba2 = json.loads(talaba_json)
print(talaba2['ism'], talaba2['familiya'])

with open('data/talaba.json', 'w') as t:
    json.dump(talaba,t)



# Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. Ularning har birini alohida qatordan 
# "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.
# FAYLNI QATORMA-QATOR OʻQISH
# filename = 'talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)

filename = 'data/students.json'
with open(filename) as file:
    for line in file:
        print(line)
with open(filename) as file:
    talabalar = file.readlines()






















