# Bismillah
"""
Created on Tue Jul  2 17:23:20 2024

@author: Faxriddin
"""
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
# python_izohli_lugati = {
#     'int' : 'butun son',
#     'float' : 'xar qanday son',
#     'string' : 'matn',
#     'if' : 'agar',
#     'else' : 'shuningdek',
#     'list' : "ro'yxat",
#     'length' : 'uzunlig',
#     'max' : 'katta qiymat',
#     'min' : 'kichik qiymat',
#     'sum' : "yig'indi"
#     }

# for k,q in sorted(python_izohli_lugati.items()):
#     print(f"{k} ning ma'nosi - {q.capitalize()}")

# Davlatlar va ularning poytaxtlari lug'atini tuzing. 
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
poytaxtlar = {
    'Uzbekiston' : 'Toshkent',
    'Kazahkstan' : "Astana",
    'Afghanistan' : "Qobul",
    'Kirgizistan' : "Bishkek",
    'Turkmaniston' : "Ashxobod",
    'Tojikiston' : "Dushanbe"
    }
# print("O'rta Osiyo davlatlari:")
# for k in poytaxtlar.keys():
#     print(k)
# print("Davlatlaring poytaxtlari: ")
# for q in sorted(poytaxtlar.values()):
#     print(q)

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'
    }

# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

    
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.   
menu = {
        'osh': 23000,
        'manti' : 6000,
        'baliq' : 50000,
        "lag'mon" : 25000,
        "uyg'ur lag'mon" : 26000,   
        'shashlik' : 12000,
        'qaynatma' : 28000,
        "qovurma go'sht" : 80000,
        "sho'rva" : 20000,
        "qozon kabob": 75000
        }    
buyurtmalar = []
print("3 ta taom buyurtma qiling:")
for n in range(0,3):
    buyurtmalar.append(input(f"{n+1}chi taomni kiriting: "))
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    